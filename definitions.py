import random
import math


def age_and_move(name):
    name['age'] += .1
    name['fertility'] += .1
    if abs(name['x_speed']) > name['speed']-(name['size']/10):
        name['x_speed'] = name['speed']-(name['size']/10)
    if abs(name['y_speed']) > name['speed']-(name['size']/10):
        name['y_speed'] = name['speed']-(name['size']/10)
    name['y_speed'] += random.randint(-1, 1) / 10
    name['x_speed'] += random.randint(-1, 1) / 10
    name['x'] += name['x_speed']
    name['y'] += name['y_speed']

    if name['x'] >= 800:
        name['x'] = 799
        name['x_speed'] = -name['x_speed']
    if name['y'] >= 600:
        name['y'] = 599
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
