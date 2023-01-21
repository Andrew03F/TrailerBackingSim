import pygame
import sys
import math
pygame.init()


def rotate(surface, angle, car_position):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rectangle = rotated_surface.get_rect(center=car_position)
    return rotated_surface, rotated_rectangle


def dot(v, u):
    return v[0] * u[0] + v[1] * u[1]


def find_angle_needed(trailer_position, hitch_position, distance):
    angle = math.acos((hitch_position[0] - trailer_position[0]) / distance)
    angle = angle * (180.0 / math.pi)
    if (hitch_position[1] - trailer_position[1]) < 0:
        return angle
    return - angle


def find_distance(point1, point2):
    distance = math.sqrt((point2[1] - point1[1]) ** 2 + (point2[0] - point1[0]) ** 2)
    return distance


def init_positions(level):
    if level == 1:
        carPos[0] = 150
        carPos[1] = 550
        trailPos[0] = 50
        trailPos[1] = 550
        # returns 3 zero values to be assigned to carAngle, trailAngle, and carSpeed
        return 0, 0, 0
    if level == 2:
        carPos[0] = 50
        carPos[1] = 550
        trailPos[0] = 150
        trailPos[1] = 550
        # returns values to be assigned to carAngle, trailAngle, and carSpeed
        return 180, 180, 0
    if level == 3:
        carPos[0] = 75
        carPos[1] = 550
        trailPos[0] = 75
        trailPos[1] = 450
        # returns values to be assigned to carAngle, trailAngle, and carSpeed
        return 270, 270, 0
    if level == 4:
        carPos[0] = 300
        carPos[1] = 280
        trailPos[0] = 300
        trailPos[1] = 400
        # returns values to be assigned to carAngle, trailAngle, and carSpeed
        return 90, 90, 0


def has_won(level, trail_angle, car_angle):
    rad = car_angle * (2 * (math.pi / 360))
    trailRad = trail_angle * (2 * (math.pi / 360))
    inter_point3 = [trailPos[0] + 20 * math.cos(trailRad) - 15 * math.sin(trailRad),
                    trailPos[1] - 20 * math.sin(trailRad) - 15 * math.sin(trailRad)]
    inter_point4 = [trailPos[0] + 20 * math.cos(trailRad) + 15 * math.sin(trailRad),
                    trailPos[1] - 20 * math.sin(trailRad) + 15 * math.sin(trailRad)]

    # back corners of trailer
    inter_point5 = [trailPos[0] - 40 * math.cos(trailRad) + 15 * math.sin(trailRad),
                    trailPos[1] + 40 * math.sin(trailRad) + 15 * math.sin(trailRad)]
    inter_point6 = [trailPos[0] - 40 * math.cos(trailRad) - 15 * math.sin(trailRad),
                    trailPos[1] + 40 * math.sin(trailRad) - 15 * math.sin(trailRad)]
    if level == 1:
        if inter_point3[0] > 500 \
                and inter_point4[0] > 500 \
                and inter_point5[0] > 500 \
                and inter_point6[0] > 500:
            return True
        return False
    if level == 2:
        if inter_point3[0] > 500 \
                and inter_point4[0] > 500 \
                and inter_point5[0] > 500 \
                and inter_point6[0] > 500:
            return True
        return False
    if level == 3:
        if inter_point3[0] > 500 \
                and inter_point4[0] > 500 \
                and inter_point5[0] > 500 \
                and inter_point6[0] > 500:
            return True
        return False
    if level == 4:
        if inter_point3[1] < 100 \
                and inter_point4[1] < 100 \
                and inter_point5[1] < 100 \
                and inter_point6[1] < 100:
            return True


def has_crashed(level, trail_angle, car_angle):
    rad = car_angle * (2 * (math.pi / 360))
    trailRad = trail_angle * (2 * (math.pi / 360))

    # front corners of the car
    inter_point1 = [carPos[0] + 35 * math.cos(rad) - 10 * math.sin(rad),
                    carPos[1] - 35 * math.sin(rad) - 10 * math.cos(rad)]
    inter_point2 = [carPos[0] + 35 * math.cos(rad) + 10 * math.sin(rad),
                    carPos[1] - 35 * math.sin(rad) + 10 * math.cos(rad)]
    # front corners of trailer
    inter_point3 = [trailPos[0] + 20 * math.cos(trailRad) - 15 * math.sin(trailRad),
                    trailPos[1] - 20 * math.sin(trailRad) - 15 * math.sin(trailRad)]
    inter_point4 = [trailPos[0] + 20 * math.cos(trailRad) + 15 * math.sin(trailRad),
                    trailPos[1] - 20 * math.sin(trailRad) + 15 * math.sin(trailRad)]

    # back corners of trailer
    inter_point5 = [trailPos[0] - 40 * math.cos(trailRad) + 15 * math.sin(trailRad),
                    trailPos[1] + 40 * math.sin(trailRad) + 15 * math.sin(trailRad)]
    inter_point6 = [trailPos[0] - 40 * math.cos(trailRad) - 15 * math.sin(trailRad),
                    trailPos[1] + 40 * math.sin(trailRad) - 15 * math.sin(trailRad)]

    # back corners of the car
    inter_point7 = [carPos[0] - 35 * math.cos(rad) + 10 * math.sin(rad),
                    carPos[1] + 35 * math.sin(rad) + 10 * math.cos(rad)]
    inter_point8 = [carPos[0] - 35 * math.cos(rad) - 10 * math.sin(rad),
                    carPos[1] + 35 * math.sin(rad) - 10 * math.cos(rad)]

    # check for jack knife
    car_v = [math.cos(rad ), math.sin(rad % 360)]
    trail_v = [math.cos(trailRad), math.sin(trailRad)]

    if dot(car_v, trail_v) < -0.5:
        return True

    if level == 1:
        x = 250
        y = 500
        if inter_point1[0] < x and inter_point1[1] < y\
                or inter_point2[0] < x and inter_point2[1] < y\
                or inter_point3[0] < x and inter_point3[1] < y\
                or inter_point4[0] < x and inter_point4[1] < y\
                or inter_point5[0] < x and inter_point5[1] < y\
                or inter_point6[0] < x and inter_point6[1] < y\
                or inter_point7[0] < x and inter_point7[1] < y\
                or inter_point8[0] < x and inter_point8[1] < y:
            return True
        x, y = 350, 350
        if inter_point1[0] > x and inter_point1[1] > y\
                or inter_point2[0] > x and inter_point2[1] > y\
                or inter_point3[0] > x and inter_point3[1] > y\
                or inter_point4[0] > x and inter_point4[1] > y\
                or inter_point5[0] > x and inter_point5[1] > y\
                or inter_point6[0] > x and inter_point6[1] > y\
                or inter_point7[0] > x and inter_point7[1] > y\
                or inter_point8[0] > x and inter_point8[1] > y:
            return True
        x, y = 350, 250
        if inter_point1[0] > x and inter_point1[1] < y\
                or inter_point2[0] > x and inter_point2[1] < y\
                or inter_point3[0] > x and inter_point3[1] < y\
                or inter_point4[0] > x and inter_point4[1] < y\
                or inter_point5[0] > x and inter_point5[1] < y\
                or inter_point6[0] > x and inter_point6[1] < y\
                or inter_point7[0] > x and inter_point7[1] < y\
                or inter_point8[0] > x and inter_point8[1] < y:
            return True
        if inter_point1[1] < 100\
                or inter_point2[1] < 100\
                or inter_point3[1] < 100\
                or inter_point4[1] < 100\
                or inter_point5[1] < 100\
                or inter_point6[1] < 100\
                or inter_point7[1] < 100\
                or inter_point8[1] < 100:
            return True
            # check if car is out of screen
        x, y = 0, 600
        if ((inter_point1[0] < x or inter_point1[1] < x) or (inter_point1[0] > y or inter_point1[1] > y))\
                or ((inter_point2[0] < x or inter_point2[1] < x) or (inter_point2[0] > y or inter_point2[1] > y)) \
                or ((inter_point3[0] < x or inter_point3[1] < x) or (inter_point3[0] > y or inter_point3[1] > y)) \
                or ((inter_point4[0] < x or inter_point4[1] < x) or (inter_point4[0] > y or inter_point4[1] > y)) \
                or ((inter_point5[0] < x or inter_point5[1] < x) or (inter_point5[0] > y or inter_point5[1] > y)) \
                or ((inter_point6[0] < x or inter_point6[1] < x) or (inter_point6[0] > y or inter_point6[1] > y)) \
                or ((inter_point7[0] < x or inter_point7[1] < x) or (inter_point7[0] > y or inter_point7[1] > y)) \
                or ((inter_point8[0] < x or inter_point8[1] < x) or (inter_point8[0] > y or inter_point8[1] > y)):
            return True
    if level == 2:
        x = 250
        y = 500
        if inter_point1[0] < x and inter_point1[1] < y \
                or inter_point2[0] < x and inter_point2[1] < y \
                or inter_point3[0] < x and inter_point3[1] < y \
                or inter_point4[0] < x and inter_point4[1] < y \
                or inter_point5[0] < x and inter_point5[1] < y \
                or inter_point6[0] < x and inter_point6[1] < y \
                or inter_point7[0] < x and inter_point7[1] < y \
                or inter_point8[0] < x and inter_point8[1] < y:
            return True
        x, y = 350, 350
        if inter_point1[0] > x and inter_point1[1] > y \
                or inter_point2[0] > x and inter_point2[1] > y \
                or inter_point3[0] > x and inter_point3[1] > y \
                or inter_point4[0] > x and inter_point4[1] > y \
                or inter_point5[0] > x and inter_point5[1] > y \
                or inter_point6[0] > x and inter_point6[1] > y \
                or inter_point7[0] > x and inter_point7[1] > y \
                or inter_point8[0] > x and inter_point8[1] > y:
            return True
        x, y = 350, 250
        if inter_point1[0] > x and inter_point1[1] < y \
                or inter_point2[0] > x and inter_point2[1] < y \
                or inter_point3[0] > x and inter_point3[1] < y \
                or inter_point4[0] > x and inter_point4[1] < y \
                or inter_point5[0] > x and inter_point5[1] < y \
                or inter_point6[0] > x and inter_point6[1] < y \
                or inter_point7[0] > x and inter_point7[1] < y \
                or inter_point8[0] > x and inter_point8[1] < y:
            return True
        if inter_point1[1] < 250 \
                or inter_point2[1] < 250 \
                or inter_point3[1] < 250 \
                or inter_point4[1] < 250 \
                or inter_point5[1] < 250 \
                or inter_point6[1] < 250 \
                or inter_point7[1] < 250 \
                or inter_point8[1] < 250:
            return True
            # check if car is out of screen
        x, y = 0, 600
        if ((inter_point1[0] < x or inter_point1[1] < x) or (inter_point1[0] > y or inter_point1[1] > y)) \
                or ((inter_point2[0] < x or inter_point2[1] < x) or (inter_point2[0] > y or inter_point2[1] > y)) \
                or ((inter_point3[0] < x or inter_point3[1] < x) or (inter_point3[0] > y or inter_point3[1] > y)) \
                or ((inter_point4[0] < x or inter_point4[1] < x) or (inter_point4[0] > y or inter_point4[1] > y)) \
                or ((inter_point5[0] < x or inter_point5[1] < x) or (inter_point5[0] > y or inter_point5[1] > y)) \
                or ((inter_point6[0] < x or inter_point6[1] < x) or (inter_point6[0] > y or inter_point6[1] > y)) \
                or ((inter_point7[0] < x or inter_point7[1] < x) or (inter_point7[0] > y or inter_point7[1] > y)) \
                or ((inter_point8[0] < x or inter_point8[1] < x) or (inter_point8[0] > y or inter_point8[1] > y)):
            return True
    if level == 3:
        # check if car is out of screen
        x, y = 0, 600
        if ((inter_point1[0] < x or inter_point1[1] < x) or (inter_point1[0] > y or inter_point1[1] > y)) \
                or ((inter_point2[0] < x or inter_point2[1] < x) or (inter_point2[0] > y or inter_point2[1] > y)) \
                or ((inter_point3[0] < x or inter_point3[1] < x) or (inter_point3[0] > y or inter_point3[1] > y)) \
                or ((inter_point4[0] < x or inter_point4[1] < x) or (inter_point4[0] > y or inter_point4[1] > y)) \
                or ((inter_point5[0] < x or inter_point5[1] < x) or (inter_point5[0] > y or inter_point5[1] > y)) \
                or ((inter_point6[0] < x or inter_point6[1] < x) or (inter_point6[0] > y or inter_point6[1] > y)) \
                or ((inter_point7[0] < x or inter_point7[1] < x) or (inter_point7[0] > y or inter_point7[1] > y)) \
                or ((inter_point8[0] < x or inter_point8[1] < x) or (inter_point8[0] > y or inter_point8[1] > y)):
            return True
        x, y = 155, 200
        if inter_point1[0] > x and inter_point1[1] > y \
                or inter_point2[0] > x and inter_point2[1] > y \
                or inter_point3[0] > x and inter_point3[1] > y \
                or inter_point4[0] > x and inter_point4[1] > y \
                or inter_point5[0] > x and inter_point5[1] > y \
                or inter_point6[0] > x and inter_point6[1] > y \
                or inter_point7[0] > x and inter_point7[1] > y \
                or inter_point8[0] > x and inter_point8[1] > y:
            return True
        x, y = 155, 150
        if inter_point1[0] > x and inter_point1[1] < y \
                or inter_point2[0] > x and inter_point2[1] < y \
                or inter_point3[0] > x and inter_point3[1] < y \
                or inter_point4[0] > x and inter_point4[1] < y \
                or inter_point5[0] > x and inter_point5[1] < y \
                or inter_point6[0] > x and inter_point6[1] < y \
                or inter_point7[0] > x and inter_point7[1] < y \
                or inter_point8[0] > x and inter_point8[1] < y:
            return True
        if inter_point1[1] < 50 \
                or inter_point2[1] < 50 \
                or inter_point3[1] < 50 \
                or inter_point4[1] < 50 \
                or inter_point5[1] < 50 \
                or inter_point6[1] < 50 \
                or inter_point7[1] < 50 \
                or inter_point8[1] < 50:
            return True
    if level == 4:
        # check if car is out of screen
        x, y = 0, 600
        if ((inter_point1[0] < x or inter_point1[1] < x) or (inter_point1[0] > y or inter_point1[1] > y)) \
                or ((inter_point2[0] < x or inter_point2[1] < x) or (inter_point2[0] > y or inter_point2[1] > y)) \
                or ((inter_point3[0] < x or inter_point3[1] < x) or (inter_point3[0] > y or inter_point3[1] > y)) \
                or ((inter_point4[0] < x or inter_point4[1] < x) or (inter_point4[0] > y or inter_point4[1] > y)) \
                or ((inter_point5[0] < x or inter_point5[1] < x) or (inter_point5[0] > y or inter_point5[1] > y)) \
                or ((inter_point6[0] < x or inter_point6[1] < x) or (inter_point6[0] > y or inter_point6[1] > y)) \
                or ((inter_point7[0] < x or inter_point7[1] < x) or (inter_point7[0] > y or inter_point7[1] > y)) \
                or ((inter_point8[0] < x or inter_point8[1] < x) or (inter_point8[0] > y or inter_point8[1] > y)):
            return True
        if inter_point1[1] > 450 \
                or inter_point2[1] > 450 \
                or inter_point3[1] > 450 \
                or inter_point4[1] > 450 \
                or inter_point5[1] > 450 \
                or inter_point6[1] > 450 \
                or inter_point7[1] > 450 \
                or inter_point8[1] > 450:
            return True
        if inter_point1[0] > 375 \
                or inter_point2[0] > 375 \
                or inter_point3[0] > 375 \
                or inter_point4[0] > 375 \
                or inter_point5[0] > 375 \
                or inter_point6[0] > 375 \
                or inter_point7[0] > 375 \
                or inter_point8[0] > 375:
            return True
        if inter_point1[0] < 225 \
                or inter_point2[0] < 225 \
                or inter_point3[0] < 225 \
                or inter_point4[0] < 225 \
                or inter_point5[0] < 225 \
                or inter_point6[0] < 225 \
                or inter_point7[0] < 225 \
                or inter_point8[0] < 225:
            return True
        x, y = 275, 200
        if inter_point1[0] < x and inter_point1[1] < y \
                or inter_point2[0] < x and inter_point2[1] < y \
                or inter_point3[0] < x and inter_point3[1] < y \
                or inter_point4[0] < x and inter_point4[1] < y \
                or inter_point5[0] < x and inter_point5[1] < y \
                or inter_point6[0] < x and inter_point6[1] < y \
                or inter_point7[0] < x and inter_point7[1] < y \
                or inter_point8[0] < x and inter_point8[1] < y:
            return True
        x, y = 325, 200
        if inter_point1[0] > x and inter_point1[1] < y\
                or inter_point2[0] > x and inter_point2[1] < y\
                or inter_point3[0] > x and inter_point3[1] < y\
                or inter_point4[0] > x and inter_point4[1] < y\
                or inter_point5[0] > x and inter_point5[1] < y\
                or inter_point6[0] > x and inter_point6[1] < y\
                or inter_point7[0] > x and inter_point7[1] < y\
                or inter_point8[0] > x and inter_point8[1] < y:
            return True
RED = (255, 0, 0)
GREEN = (0, 125, 0)
BLUE = (80, 80, 80)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
curLevel = 1
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Times New Roman", 30)
timerSur = font.render("", True, WHITE)
isStarted = False
timeRestart = False

levelDisp = font.render("Level:" + str(curLevel), True, BLACK)
levelDispRect = levelDisp.get_rect(topleft=(0, 0))

endBannerSur = pygame.image.load("YOUWON.xcf")
endBannerRect = endBannerSur.get_rect(center=(300, 300))

# car attributes
carSize = (80, 30)
carSur = pygame.image.load("car.xcf")
carRect = carSur.get_rect(midleft=(300, 300))
carAngle = 0
carSpeed = 0
carAcc = 0.1
carPos = [carRect.centerx, carRect.centery]
rotCarRect = carRect

# trailer attributes
trailSize = (93, 35)
trailSur = pygame.image.load("trailer.xcf")
trailRect = trailSur.get_rect(midright=(290, 300))
trailAngle = 0
trailPos = [trailRect.centerx, trailRect.centery]

# off limits for level 1
wall11Sur = pygame.Surface((250, 495))
wall11Rect = wall11Sur.get_rect(topleft=(0, 0))

wall12Sur = pygame.Surface((250, 250))
wall12Rect = wall12Sur.get_rect(bottomright=(600, 600))

wall13Sur = pygame.Surface((250, 250))
wall13Rect = wall13Sur.get_rect(topright=(600, 0))

wall14Sur = pygame.Surface((350,5))
wall14Rect = wall14Sur.get_rect(bottomleft=(0,600))

wall16Sur = pygame.Surface((100, 100))
wall16Rect = wall16Sur.get_rect(topleft=(250, 0))

finishSur1 = pygame.image.load("finishLineVert.xcf")
finishRect1 = finishSur1.get_rect(topright=(500, 250))

# off limits for level 2
wall21Sur = pygame.Surface((250, 495))
wall21Rect = wall11Sur.get_rect(topleft=(0, 0))

wall22Sur = pygame.Surface((250, 250))
wall22Rect = wall12Sur.get_rect(bottomright=(600, 600))

wall23Sur = pygame.Surface((250, 250))
wall23Rect = wall13Sur.get_rect(topright=(600, 0))

wall24Sur = pygame.Surface((350, 5))
wall24Rect = wall14Sur.get_rect(bottomleft=(0,600))

wall26Sur = pygame.Surface((100, 250))
wall26Rect = wall16Sur.get_rect(topleft=(250, 0))

finishRect2 = finishSur1.get_rect(topright=(500, 250))

# off limits for level 3
wall31Sur = pygame.Surface((445, 400))
wall31Rect = wall31Sur.get_rect(bottomright=(600, 600))

wall32Sur = pygame.Surface((600, 50))
wall32Rect = wall32Sur.get_rect(topleft=(0, 0))

wall33Sur = pygame.Surface((445, 100))
wall33Rect = wall33Sur.get_rect(topright=(600, 50))

finishRect3 = finishSur1.get_rect(topright=(500, 150))

# off limits for level 4
wall41Sur = pygame.Surface((225, 400))
wall41Rect = wall41Sur.get_rect(bottomleft=(0, 600))

wall42Sur = pygame.Surface((225, 400))
wall42Rect = wall42Sur.get_rect(bottomright=(600, 600))

wall43Sur = pygame.Surface((275, 200))
wall43Rect = wall43Sur.get_rect(topleft=(0, 0))

wall44Sur = pygame.Surface((275, 200))
wall44Rect = wall44Sur.get_rect(topright=(600, 0))

wall45Sur = pygame.Surface((150, 150))
wall45Rect = wall45Sur.get_rect(midbottom=(300, 600))

finishSur2 = pygame.image.load("finishLineHorz.xcf")
finishRect4 = finishSur2.get_rect(topleft=(275, 100))

turnLeft = False
turnRight = False
forward = False
backward = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # check key downs
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
            turnLeft = True
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
            turnRight = True
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_w):
            forward = True
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
            backward = True

        #check for level change
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            carAngle, trailAngle, carSpeed = init_positions(1)
            curLevel = 1
            levelDisp = font.render("Level:" + str(curLevel), True, BLACK)
            levelDispRect = levelDisp.get_rect(topleft=(0, 0))
            timeRestart = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            carAngle, trailAngle, carSpeed = init_positions(2)
            curLevel = 2
            levelDisp = font.render("Level:" + str(curLevel), True, BLACK)
            levelDispRect = levelDisp.get_rect(topleft=(0, 0))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            carAngle, trailAngle, carSpeed = init_positions(3)
            curLevel = 3
            levelDisp = font.render("Level:" + str(curLevel), True, BLACK)
            levelDispRect = levelDisp.get_rect(topleft=(0, 0))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            carAngle, trailAngle, carSpeed = init_positions(4)
            curLevel = 4
            levelDisp = font.render("Level:" + str(curLevel), True, BLACK)
            levelDispRect = levelDisp.get_rect(topleft=(0, 0))

        # check key ups
        if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
            turnLeft = False
        if event.type == pygame.KEYUP and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
            turnRight = False
        if event.type == pygame.KEYUP and (event.key == pygame.K_UP or event.key == pygame.K_w):
            forward = False
        if event.type == pygame.KEYUP and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
            backward = False

    # alter the car and trailer's attributes
    if turnLeft:
        carAngle = carAngle + 5 * (carSpeed / 5)
        isStarted = True
    if turnRight:
        carAngle = carAngle - 5 * (carSpeed / 5)
        isStarted = True
    if forward:
        carSpeed = carSpeed + carAcc
        isStarted = True
    if backward:
        carSpeed -= carAcc
        isStarted = True

    # start the timer
    if not isStarted:
        timeStarted = pygame.time.get_ticks() / 1000
    if timeRestart:
        timeStarted = pygame.time.get_ticks() / 1000
        timeRestart = False
        isStarted = False
    timeSinceStartMin = str(int((pygame.time.get_ticks() / 1000 - timeStarted) / 60))
    timeSinceStart = timeSinceStartMin + ":" + format((pygame.time.get_ticks() / 1000 - timeStarted) % 60, '0.3f')
    timerSur = font.render(str(timeSinceStart), True, BLACK)
    timerRect = timerSur.get_rect(topright=(600, 0))

    # move car
    carPos[0] += math.cos(carAngle * 2 * (math.pi / 360)) * carSpeed
    carPos[1] += -math.sin(carAngle * 2 * (math.pi / 360)) * carSpeed
    carSpeed = carSpeed * 0.95

    # find new hitch point
    hitchPoint = (carPos[0] - 45 * math.cos(carAngle * 2 * (math.pi / 360)),
                  carPos[1] + 45 * math.sin(carAngle * 2 * (math.pi / 360)))

    # change trailer angle then move
    dist = find_distance(trailPos, hitchPoint)
    trailAngle = find_angle_needed(trailPos, hitchPoint, dist)

    if dist > 1:
        trailPos[0] += math.cos(trailAngle * 2 * (math.pi / 360)) * (dist - 45)
        trailPos[1] += -math.sin(trailAngle * 2 * (math.pi / 360)) * (dist - 45)

    if has_crashed(curLevel, trailAngle, carAngle):
        carAngle, trailAngle, carSpeed = init_positions(curLevel)

    if has_won(curLevel, trailAngle, carAngle):
        # check if the game has been beaten
        if curLevel <= 3:
            winBannerSur = font.render("  You beat level " + str(curLevel) + "!  ", True, BLACK, RED)
            winBannerRect= winBannerSur.get_rect(center=(300, 300))
            screen.blit(winBannerSur, winBannerRect)
            pygame.display.update()
            pygame.time.delay(1000)
            curLevel += 1
            levelDisp = font.render("Level:" + str(curLevel), True, BLACK)
            levelDispRect = levelDisp.get_rect(topleft=(0, 0))
            carAngle, trailAngle, carSpeed = init_positions(curLevel)
        else:
            screen.blit(endBannerSur, endBannerRect)
            pygame.display.update()
            while True:
                pygame.time.wait(100)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

    # draw the screen
    if curLevel == 1:
        # below car
        screen.fill(BLUE)
        wall11Sur.fill(GREEN)
        wall12Sur.fill(GREEN)
        wall13Sur.fill(GREEN)
        wall14Sur.fill(GREEN)
        wall16Sur.fill(GREEN)

        screen.blit(wall11Sur, wall11Rect)
        screen.blit(wall12Sur, wall12Rect)
        screen.blit(wall13Sur, wall13Rect)
        screen.blit(wall14Sur, wall14Rect)
        screen.blit(wall16Sur, wall16Rect)
        screen.blit(finishSur1, finishRect1)
        screen.blit(timerSur, timerRect)
        screen.blit(levelDisp, levelDispRect)

        rotCarSur, rotCarRect = rotate(carSur, carAngle, carPos)
        rotTrailSur, rotTrailRect = rotate(trailSur, trailAngle, trailPos)
        # on top of car
        screen.blit(rotCarSur, rotCarRect)
        screen.blit(rotTrailSur, rotTrailRect)
        pygame.display.update()
    if curLevel == 2:
        # below car
        screen.fill(BLUE)
        wall21Sur.fill(GREEN)
        wall22Sur.fill(GREEN)
        wall23Sur.fill(GREEN)
        wall24Sur.fill(GREEN)
        wall26Sur.fill(GREEN)

        screen.blit(wall21Sur, wall21Rect)
        screen.blit(wall22Sur, wall22Rect)
        screen.blit(wall23Sur, wall23Rect)
        screen.blit(wall24Sur, wall24Rect)
        screen.blit(wall26Sur, wall26Rect)
        screen.blit(finishSur1, finishRect2)
        screen.blit(timerSur, timerRect)
        screen.blit(levelDisp, levelDispRect)

        rotCarSur, rotCarRect = rotate(carSur, carAngle, carPos)
        rotTrailSur, rotTrailRect = rotate(trailSur, trailAngle, trailPos)
        # on top of car
        screen.blit(rotCarSur, rotCarRect)
        screen.blit(rotTrailSur, rotTrailRect)
        pygame.display.update()
    if curLevel == 3:
        screen.fill(BLUE)
        wall31Sur.fill(GREEN)
        wall32Sur.fill(GREEN)
        wall33Sur.fill(GREEN)

        screen.blit(finishSur1, finishRect3)
        screen.blit(wall31Sur, wall31Rect)
        screen.blit(wall32Sur, wall32Rect)
        screen.blit(wall33Sur, wall33Rect)

        # should not be covered
        screen.blit(timerSur, timerRect)
        screen.blit(levelDisp, levelDispRect)

        rotCarSur, rotCarRect = rotate(carSur, carAngle, carPos)
        rotTrailSur, rotTrailRect = rotate(trailSur, trailAngle, trailPos)
        # on top of car
        screen.blit(rotCarSur, rotCarRect)
        screen.blit(rotTrailSur, rotTrailRect)
        pygame.display.update()
    if curLevel == 4:
        screen.fill(BLUE)
        wall41Sur.fill(GREEN)
        wall42Sur.fill(GREEN)
        wall43Sur.fill(GREEN)
        wall44Sur.fill(GREEN)
        wall45Sur.fill(GREEN)

        screen.blit(finishSur2, finishRect4)
        screen.blit(wall41Sur, wall41Rect)
        screen.blit(wall42Sur, wall42Rect)
        screen.blit(wall43Sur, wall43Rect)
        screen.blit(wall44Sur, wall44Rect)
        screen.blit(wall45Sur, wall45Rect)

        # should not be covered
        screen.blit(timerSur, timerRect)
        screen.blit(levelDisp, levelDispRect)

        rotCarSur, rotCarRect = rotate(carSur, carAngle, carPos)
        rotTrailSur, rotTrailRect = rotate(trailSur, trailAngle, trailPos)
        # on top of car
        screen.blit(rotCarSur, rotCarRect)
        screen.blit(rotTrailSur, rotTrailRect)
        pygame.display.update()
    clock.tick(60)
