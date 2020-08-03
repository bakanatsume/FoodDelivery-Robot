


# #!/usr/bin/env pybricks-micropython

# from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedRPM, MoveTank
# # # rightA = LargeMotor(OUTPUT_A)
# # # leftB = LargeMotor(OUTPUT_B)
# # # # portB = LargeMotor(OUTPUT_B)
# # # # portC = LargeMotor(OUTPUT_C)
# # # # portD = LargeMotor(OUTPUT_D)
# # # # on_for_degrees(speed=80, degrees=90)r
# # # STUD_MM = 8
# # # armSpeed = 30
# # # leftArm = -25
# # # rightArm = 25

# # # rightA.on_for_degrees(armSpeed, rightArm)
# # # leftB.on_for_degrees(armSpeed, rightArm)
# # # rightA.on_for_seconds(SpeedRPM(30), 5)
# # # leftB.on_for_seconds(SpeedRPM(30), 5)
# tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
# # # drive in a turn for 10 rotations of the outer motor

# from ev3dev2.sensor.lego import InfraredSensor
# #move = ''


# # def rotateLeftFar(speed, speed, rotation):
# #     tank_drive.on_for_rotations(speed, -speed, rotation)
# #     tank_drive.on_for_rotations(speed, speed, rotation)
# #     d = d+2


# # def rotateLeft(speed, state=True):
# #     tank_drive.on_for_rotations(speed, -speed, 2)
# #     tank_drive.on_for_rotations(speed, speed, 2)
# #     # d=d+2
# #     if state:
# #         move = 'far'
# #     else:
# #         move = 'near'
# #     if move == 'near'
# #         d = d+1
# #     else:
# #         d = d-1


# # def rotateLeftNear(speed, speed, rotation):
# #     tank_drive.on_for_rotations(speed, -speed, rotation)
# #     tank_drive.on_for_rotations(speed, speed, rotation)
# #     d = d-2
# # def rotateRight(lspeed, rspeed, deg):
# #     tank_drive.on_for_rotations(lspeed, rspeed, deg)


# i = 0
# d = 12


# def obstracleBypass(speed):
#     tank_drive.on_for_rotations(-speed, speed, 2)
#     tank_drive.on_for_rotations(speed, speed, 4)
#     tank_drive.on_for_rotations(speed, -speed, 2)
#     tank_drive.on_for_rotations(speed, speed, 4)
#     d=d-4
#     tank_drive.on_for_rotations(-speed, speed, 2)
#     tank_drive.on_for_rotations(speed, speed, 4)

# def stop():
#     tank_drive.on(0, 0)


# def moveForward(speed):
#     tank_drive.on_for_rotations(speed, speed, 4)

# # def moveBackward(speed, time):
# #     tank_drive.on_for_rotations(-speed, -speed, time)


# # # def move(lSpeed, rSpeed, time):
# # #     tank_drive.on_for_rotations(lSpeed, rSpeed, time)


# # moveForward(50, 5)
# # rotateLeft(0, 50, 4)
# # moveForward(50, 5)
# # rotateRight(50, 0, 4)
# # moveForward(50, 5)
# # rotateRight(50, 0, 4)
# # moveForward(50, 5)
# # rotateLeft(0, 50, 4)
# # moveForward(50, 5)
# # rotateLef(0, 50, 4)
# # moveForward(50, 5)
# # rotateRight(50, 0, 16)
# # moveForward(50, 5)


# # # move(50, 20, 5)  # right
# # # # (Left motor, right motor, rotation of speed / seconds)
# # # move(50, 50, 5)  # left
# # # move(-50, 50, 2)  # forward
# # # move(50, 50, 5)  # rotatae
# # # move(50, -50, 2)  # backward
# # # move(50, 50, 5)
# # # move(50, -50, 2)
# # # move(50, 50, 5)
# # # move(-50, 50, 2)
# # # move(50, 50, 15)
# # # move(-50, 50, 2)
# # # move(50, 50, 5)
# # # move(50, -50, 2)
# # # move(50, 50, 2)
# # # move(50, -50, 2)
# # # move(50, 50, 8)


# # so that script can be run from Brickman

# # Connect infrared and touch sensors to any sensor ports

# ir = InfraredSensor()

# # Put the infrared sensor into proximity mode.
# ir.mode = 'IR-PROX'

# while d != i:   # Stodebug p program by pressing touch sensor button
#     # Infrared sensor in proximity mode will measure distance to the closest
#     # object in front of it.
#     distance = ir.value()
#     moveForward(50)
#     d=d-4
#     print(distance)

#     if distance > 50:
#         obstracleBypass(50)

# print("Destination Reached")





