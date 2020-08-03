#!/usr/bin/env pybricks-micropython

from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedRPM, MoveTank
# # rightA = LargeMotor(OUTPUT_A)
# # leftB = LargeMotor(OUTPUT_B)
# # # portB = LargeMotor(OUTPUT_B)
# # # portC = LargeMotor(OUTPUT_C)
# # # portD = LargeMotor(OUTPUT_D)
# # # on_for_degrees(speed=80, degrees=90)r
# # STUD_MM = 8
# # armSpeed = 30
# # leftArm = -25
# # rightArm = 25

# # rightA.on_for_degrees(armSpeed, rightArm)
# # leftB.on_for_degrees(armSpeed, rightArm)
# # rightA.on_for_seconds(SpeedRPM(30), 5)
# # leftB.on_for_seconds(SpeedRPM(30), 5)
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
# # drive in a turn for 10 rotations of the outer motor


# def rotateLeft(lspeed, rspeed, deg):
#     tank_drive.on_for_rotations(lspeed, rspeed, deg)


# def rotateRight(lspeed, rspeed, deg):
#     tank_drive.on_for_rotations(lspeed, rspeed, deg)

i = 0
d = 30000


def moveForward(speed):
    tank_drive.on_for_rotations(speed, speed, 1)


def stop():
    tank_drive.on_for_rotations(0, 0, 0)


def obstracleBypass(speed):

    tank_drive.on_for_rotations(-speed, speed, 1.89)  # right
    tank_drive.on_for_rotations(speed, speed, 5)  # straight
    tank_drive.on_for_rotations(speed, -speed, 1.89)  # left
    tank_drive.on_for_rotations(speed, speed, 8)  # straight
    tank_drive.on_for_rotations(speed, -speed, 1.89)  # left
    tank_drive.on_for_rotations(speed, speed, 5)  # straight
    tank_drive.on_for_rotations(-speed, speed, 1.89)  # right

# def moveBackward(speed, time):
#     tank_drive.on_for_rotations(-speed, -speed, time)


# # def move(lSpeed, rSpeed, time):
# #     tank_drive.on_for_rotations(lSpeed, rSpeed, time)


# moveForward(50, 5)
# rotateLeft(0, 50, 4)
# moveForward(50, 5)
# rotateRight(50, 0, 4)
# moveForward(50, 5)
# rotateRight(50, 0, 4)
# moveForward(50, 5)
# rotateLeft(0, 50, 4)
# moveForward(50, 5)
# rotateLef(0, 50, 4)
# moveForward(50, 5)
# rotateRight(50, 0, 16)
# moveForward(50, 5)


# # move(50, 20, 5)  # right
# # # (Left motor, right motor, rotation of speed / seconds)
# # move(50, 50, 5)  # left
# # move(-50, 50, 2)  # forward
# # move(50, 50, 5)  # rotatae
# # move(50, -50, 2)  # backward
# # move(50, 50, 5)
# # move(50, -50, 2)
# # move(50, 50, 5)
# # move(-50, 50, 2)
# # move(50, 50, 15)
# # move(-50, 50, 2)
# # move(50, 50, 5)
# # move(50, -50, 2)
# # move(50, 50, 2)
# # move(50, -50, 2)
# # move(50, 50, 8)


# so that script can be run from Brickman

# Connect infrared and touch sensors to any sensor ports
ir = InfraredSensor()

# Put the infrared sensor into proximity mode.
ir.mode = 'IR-PROX'

while d != i:    # Stodebug p program by pressing touch sensor button
    # Infrared sensor in proximity mode will measure distance to the closest
    # object in front of it.
    distance = ir.value()
    print(distance)
    if(distance < 40):
        obstracleBypass(100)

    else:
        tank_drive.on(100, 100)


print('successful')
