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

myVariable = 0

def when_started1():
    global myVariable
    drivetrain.turn_for(RIGHT, 149, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 1890, MM, wait=True)
    intake_motor_group.set_velocity(95, PERCENT)
    intake_motor_group.spin(REVERSE)
    wait(1, SECONDS)
    drivetrain.drive_for(FORWARD, 500, MM, wait=True)
    wait(1, SECONDS)
    drivetrain.turn_for(RIGHT, 50, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 250, MM, wait=True)
    drivetrain.turn_for(LEFT, 45, DEGREES, wait=True)
    wait(3, SECONDS)
    drivetrain.drive_for(FORWARD, 250, MM, wait=True)

vr_thread(when_started1)
