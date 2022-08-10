import sys, pygame
import math
pygame.init()


def rotate(surface, angle, car_position):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rectangle = rotated_surface.get_rect(center=car_position)
    return rotated_surface, rotated_rectangle


clock = pygame.time.Clock()
RED = (255, 0, 0)
BLUE = (0, 0, 120)
size = width, height = (600, 600)
carPos = [300, 300]
carAngle = 0
carSpeed = 0
carAcc = .2

screen = pygame.display.set_mode(size)
carSur = pygame.Surface((80, 30))
carSur.fill(RED)
carRect = carSur.get_rect(center=carPos)

turnLeft = False
turnRight = False
forward = False
backward = False

while True:
    # do stuff to the screen
    pygame.key.set_repeat(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # check key downs
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            turnLeft = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            turnRight = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            forward = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            backward = True

        # check key ups
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            turnLeft = False
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            turnRight = False
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            forward = False
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            backward = False

    # apply accelerations to angle and speed
    if turnLeft:
        carAngle = carAngle + 5 
    if turnRight:
        carAngle = carAngle - 5
    if forward:
        carSpeed += carAcc
    if backward:
        carSpeed -= carAcc

    # apply speed and angle to position
    carPos[0] += math.cos(carAngle * 2 * (math.pi / 360)) * carSpeed
    carPos[1] += -math.sin(carAngle * 2 * (math.pi / 360)) * carSpeed
    carSpeed = carSpeed * 0.95

    # handle collision
    if carPos[0] < 0 or carPos[0] > width or carPos[1] < 0 or carPos[1] > height:
        carSpeed *= -1

    # draw the screen
    screen.fill(BLUE)
    rotSur, rotRect = rotate(carSur, carAngle, carPos)
    screen.blit(rotSur, rotRect)
    pygame.display.update()
    clock.tick(60)
