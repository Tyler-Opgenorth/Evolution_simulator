"""This is the main file for the evolution simulator.
It is a simple simulation of evolution.
created by: Tyler Opgenorth"""
import math
import pygame
import random
import definitions
import tkinter
pygame.init()
root = tkinter.Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

PYGAME = True
STARTING_HERBS = int(WIDTH * HEIGHT / 100000)
STARTING_CARNS = 0
STARTING_PLANTS = 0
speed = 60

font = pygame.font.Font('freesansbold.ttf', 32)

if PYGAME:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Evo test')
    clock = pygame.time.Clock()

herbs = []
for i in range(STARTING_HERBS):
    herb = {'size': random.randint(5, 15),
            'x': random.randint(0, WIDTH),
            'y': random.randint(0, HEIGHT),
            'x_speed': random.randint(-1, 1),
            'y_speed': random.randint(-1, 1),
            'hunger': 0,
            'age': 0,
            'speed': random.randint(1, 15),
            'color': (random.randint(25, 55), random.randint(25, 255), random.randint(125, 155)),
            'generation': 1,
            'fertility': 0}
    herb['hunger'] = herb['size'] * 10

    herbs.append(herb)

plants = []
for i in range(STARTING_PLANTS):
    plant = {'size': 1,
             'x': random.randint(0, WIDTH),
             'y': random.randint(0, HEIGHT), }
    plants.append(plant)

carns = []
for i in range(STARTING_CARNS):
    carn = {'size': random.randint(5, 10),
            'x': random.randint(0, WIDTH),
            'y': random.randint(0, HEIGHT),
            'x_speed': random.randint(-1, 1),
            'y_speed': random.randint(-1, 1),
            'hunger': 0,
            'age': 0,
            'speed': random.randint(1, 10),
            'color': (random.randint(155, 255), random.randint(25, 55), random.randint(25, 55)),
            'generation': 1,
            'fertility': 0}
    carn['hunger'] = carn['size'] * 10

    carns.append(carn)
max_generation = 0
herb_announcement = False
carn_announcement = False
running = True
while running:

    for herb in herbs:
        definitions.age_and_move(herb, WIDTH, HEIGHT)
        if herb['hunger'] <= 0 or herb['age'] >= 6000:
            herbs.remove(herb)
            break
        definitions.breed(herb, herbs)
        if herb['generation'] > max_generation:
            max_generation = herb['generation']

            print(" ----------------------------" +
                  "\n herbivore population " + str(len(herbs)) +
                  "\n carnivore population " + str(len(carns)) +
                  "\n This herbivore generations speed = " + str(math.trunc(herb['speed'])) +
                  "\n This herbivore generations size = " + str(math.trunc(herb['size'])) +
                  "\n This herbivore generation is number = " + str(herb['generation']))

        for plant in plants:
            definitions.eat(herb, plant, plants)

    for plant in plants:
        plant['size'] += .1

    plant = {'size': 1,
             'x': random.randint(1, WIDTH),
             'y': random.randint(1, HEIGHT), }
    plants.append(plant)

    for carn in carns:
        definitions.age_and_move(carn, WIDTH, HEIGHT)
        if carn['hunger'] <= 0 or carn['age'] >= 6000:
            carns.remove(carn)
            break
        definitions.breed(carn, carns)
        for herb in herbs:
            definitions.eat(carn, herb, herbs)

    if len(herbs) == 0 and not herb_announcement:
        print("herbivores extinct")
        herb_announcement = True
    if len(carns) == 0 and not carn_announcement:
        print("carnivores extinct")
        carn_announcement = True
    if len(herbs) == 0 and len(carns) == 0:
        running = False
        print("all animals extinct")
    # pygame setup
    # optional if you want to view the simulation
    if PYGAME:
        clock.tick(speed)
        screen.fill((0, 0, 0))
        text = font.render("herbivores: " + str(len(herbs)), True, (100, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    speed = 100000
                    print(" ----------------------------\n Running at max speed")
                if event.key == pygame.K_LEFT:
                    speed = 60
                    print(" ----------------------------\n Running at normal speed")

        for herb in herbs:
            pygame.draw.circle(screen, herb['color'], (int(herb['x']), int(herb['y'])), herb['size'])
        for plant in plants:
            pygame.draw.circle(screen, (0, 255, 0), (int(plant['x']), int(plant['y'])), plant['size'])
        for carn in carns:
            pygame.draw.circle(screen, carn['color'], (int(carn['x']), int(carn['y'])), carn['size'])
        screen.blit(text, (0, 10))
        pygame.display.flip()
        pygame.display.update()
