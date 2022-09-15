myVariable = 0

def when_started1():
    global myVariable
    drivetrain.turn_for(RIGHT, 150, DEGREES, wait=True)
    drivetrain.drive_for(REVERSE, 1900, MM, wait=True)
    intake_motor_group.set_velocity(100, PERCENT)
    intake_motor_group.spin(REVERSE)
    wait(1, SECONDS)
    drivetrain.drive_for(FORWARD, 500, MM, wait=True)
    wait(1, SECONDS)
    drivetrain.turn_for(RIGHT, 50, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 250, MM, wait=True)
    drivetrain.turn_for(LEFT, 45, DEGREES, wait=True)

vr_thread(when_started1)
