#region VEXcode Generated Robot Configuration
import math
import random
from vexcode_vrc import *
from vexcode_vrc.events import get_Task_func
  
# constructors

drivetrain = Drivetrain()
brain = Brain()
bottom_distance = Distance("BottomDistance", 18)
roller_optical = Optical("RollerOptical", 2)
gps = GPS("GPS", 3)
intake_motor_group = Motor("IntakeMotorGroup", 10)
bottom_line_tracker = LineTracker("BottomLineTracker", 22)
middle_line_tracker = LineTracker("MiddleLineTracker", 23)
top_line_tracker = LineTracker("TopLineTracker", 24)
#endregion VEXcode Generated Robot Configuration

# -------------------------------------------------
# 
# 	Project:            VEXcode Project 2023
#	  Author:             Matthias Kreier
#	  Created:            2023/03/27
#	  Description:        VEXcode V5 Python Project
#   Starting Position:  A
#   Preload:            2 disks
# 
# -------------------------------------------------

from math import sqrt

path = [[-920,  920, 0],[-920,-1450, 0],[750, -1400, 0],[ 500,-1150, 1],[-600, -710, 0],
        [ 400, -250, 1],[   0,    0, 0],[-600,  200, 0],[ 400,  400, 1],[   0,  950, 0],
        [-600,  950, 0],[ 920,  950, 1],[ 920, 1500, 0],[-600, 1320, 0],[ 600,  600, 1],
        [ 600, -600, 1],[1400,-1350, 1],[1500, -900, 0]]

def goto(target_x, target_y, reverse):
    x1 = gps.x_position(MM)
    y1 = gps.y_position(MM)
    delta_x = target_x - x1
    delta_y = target_y - y1
    distance = math.sqrt(delta_x**2 + delta_y**2)     # pythagorean theorem
    if ( delta_x == 0 ):
        if ( delta_y < 0):
            direction = 90
        else:
            direction = 270
    else:
        direction = - math.atan(delta_y / delta_x) * 180 / math.pi
    if ( delta_x < 0 ):
        direction = direction + 180
    if ( reverse != 0 ):
        direction = direction + 180
    if ( direction > 360 ):
        direction = direction - 360
    drivetrain.turn_to_heading(direction, DEGREES, wait=True)
    if ( reverse != 0 ):
        drivetrain.drive_for(REVERSE, distance, MM, wait=True)
    else:
        drivetrain.drive_for(FORWARD, distance, MM, wait=True)

def main():
    drivetrain.set_drive_velocity(100,PERCENT)
    intake_motor_group.set_velocity(90, PERCENT)
    drivetrain.turn_for(LEFT, 73, DEGREES, wait=True)
    intake_motor_group.spin(REVERSE)
    # shoot first two disks into blue goal
    drivetrain.turn_for(LEFT, 20, DEGREES, wait=True)

    # get the third one
    drivetrain.drive_for(FORWARD, 340, MM, wait=True)
    # move the roller
    drivetrain.turn_for(RIGHT, 95,DEGREES,wait=True)
    intake_motor_group.stop()
    drivetrain.drive_for(REVERSE, 40, MM, wait=True)
    intake_motor_group.spin_for(FORWARD,40,DEGREES,wait=True)
    drivetrain.drive_for(FORWARD, 20, MM, wait=True)
    intake_motor_group.spin(REVERSE)
    drivetrain.drive_for(FORWARD, 200, MM, wait=True)
    drivetrain.turn_for(LEFT, 90, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 100, MM, wait=True)
    wait(0.4,SECONDS)
    drivetrain.turn_for(LEFT, 90, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 350, MM, wait=True)
    drivetrain.turn_for(LEFT, 90, DEGREES, wait=True)
    intake_motor_group.stop()
    drivetrain.drive_for(REVERSE, 120, MM, wait=True)
    intake_motor_group.spin_for(FORWARD,40,DEGREES,wait=True)
    # two rollers are red now


    drivetrain.drive_for(FORWARD, 350, MM, wait=True)
    intake_motor_group.spin(REVERSE)
    drivetrain.drive_for(FORWARD, 350, MM, wait=True)
    drivetrain.turn_for(RIGHT, 78, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 350, MM, wait=True)




    wait(10,SECONDS)
    drivetrain.drive_for(REVERSE, 500, MM, wait=True)
    drivetrain.drive_for(FORWARD, 200, MM, wait=True)
    drivetrain.drive_for(REVERSE, 1000, MM, wait=True)
    wait(1, SECONDS)
    drivetrain.turn_for(LEFT, 21, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 451, MM, wait=True)
    drivetrain.turn_for(RIGHT, 16, DEGREES, wait=True)
    wait(1, SECONDS)
    drivetrain.turn_for(LEFT, 26, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 499, MM, wait=True)
    drivetrain.turn_for(RIGHT, 21, DEGREES, wait=True)
    wait(1, SECONDS)
    drivetrain.turn_for(LEFT, 24, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 381, MM, wait=True)
    drivetrain.turn_for(RIGHT, 24, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 200, MM, wait=True)
    wait(2, SECONDS)
    drivetrain.turn_for(RIGHT, 9, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 900, MM, wait=True)
    drivetrain.turn_for(LEFT, 19, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 350, MM, wait=True)
    wait(3, SECONDS)
    intake_motor_group.stop()
    drivetrain.set_drive_velocity(100, PERCENT)
    fork_motor_group.spin_to_position(1800, DEGREES, wait=False)
    for x, y, r in path:            # loop for all coordinates in path array
        goto(x, y, r)
    pick_up() 
    goto( 1500,  100, 0)
    stop_project()


vr_thread(main)
