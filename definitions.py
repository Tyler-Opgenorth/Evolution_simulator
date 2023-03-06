import random
import math


def age_and_move(name, WIDTH, HEIGHT):
    name['age'] += .1
    name['fertility'] += .1
    if abs(name['x_speed']) > name['speed'] - (name['size'] / 10):
        name['x_speed'] = name['speed'] - (name['size'] / 10)
    if abs(name['y_speed']) > name['speed'] - (name['size'] / 10):
        name['y_speed'] = name['speed'] - (name['size'] / 10)
    name['y_speed'] += random.randint(-1, 1) / 10
    name['x_speed'] += random.randint(-1, 1) / 10
    name['x'] += name['x_speed']
    name['y'] += name['y_speed']

    if name['x'] >= WIDTH:
        name['x'] = WIDTH-1
        name['x_speed'] = -name['x_speed']
    if name['y'] >= HEIGHT:
        name['y'] = HEIGHT-1
        name['y_speed'] = -name['y_speed']
    if name['x'] <= 0:
        name['x'] = 1
        name['x_speed'] = -name['x_speed']
    if name['y'] <= 0:
        name['y'] = 1
        name['y_speed'] = -name['y_speed']
    name['hunger'] -= .1


def eat(eater, eaten, eatens):
    if math.dist((eater['x'], eater['y']), (eaten['x'], eaten['y'])) <= eaten['size'] + eater['size']:
        eater['hunger'] += eaten['size']
        eatens.remove(eaten)


def breed(name, names):
    for name2 in names:
        if math.dist((name['x'],
                      name['y']),
                     (name2['x'],
                      name2['y'])) <= (name2['size'] + name['size']) and \
                name['hunger'] >= 50 and \
                name2 != name and \
                name2['hunger'] >= 50 and \
                name['fertility'] >= 100 and \
                name2['fertility'] >= 100:
            name['hunger'] -= 50
            name2['hunger'] -= 50
            name['fertility'] = 0
            name2['fertility'] = 0
            name3 = {'size': (name['size'] + name2['size']) / 2 + (random.randint(-10, 10) / 10),
                     'x': name['x'],
                     'y': name['y'],
                     'x_speed': random.randint(-1, 1),
                     'y_speed': random.randint(-1, 1),
                     'hunger': 100,
                     'age': 0,
                     'speed': (name['speed'] + name2['speed']) / 2 + (random.randint(-10, 10) / 10),
                     'color': (
                         (name['color'][0] + name2['color'][0]) / 2, (name['color'][1] + name2['color'][1]) / 2,
                         (name['color'][2] + name2['color'][2]) / 2),
                     'generation': name['generation'] + 1,
                     'fertility': 0}
            name['hunger'] = name['size'] * 10
            names.append(name3)
