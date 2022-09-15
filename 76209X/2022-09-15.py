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

#----------------------------------------------------------------------
#   
#   Project:            SSIS Dragons X, Team 76209X
#   Description:        Initial Submission
#                       
#   Date:               15.09.2022
#   Maximum score:      24 points
#   Time left:          48 seconds
#
#----------------------------------------------------------------------

# Library imports

from vexcode_vrc import *
from math import sqrt

def main():
    drivetrain.set_drive_velocity(90,PERCENT)

    brain.screen.clear_screen()
    brain.screen.print("SSIS Dragon X starting.\n")
    drivetrain.turn_for(RIGHT, 150, DEGREES)
    drivetrain.drive_for(REVERSE, 1800, MM)

    intake_motor_group.set_velocity(100, PERCENT)
    intake_motor_group.spin(REVERSE)
    wait(3, SECONDS)

    brain.screen.print("\nGet top yellow")
    # drivetrain.turn_for(RIGHT, 40, DEGREES)
    drivetrain.drive_for(FORWARD, 350, MM)

vr_thread(main)
