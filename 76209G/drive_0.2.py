#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
motor_FL = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_BL = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
motor_FR = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
motor_BR = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration
vexcode_brain_precision = 0
vexcode_console_precision = 0
vexcode_controller_1_precision = 0
myVariable = 0

def when_started1():
    global myVariable, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    controller_1.screen.set_cursor(1, 1)
    controller_1.screen.print("Regular")
    controller_1.screen.next_row()

def ondriver_drivercontrol_0():
    global myVariable, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    controller_1.screen.set_cursor(1, 1)
    controller_1.screen.print("Driver    ")
    controller_1.screen.next_row()
    M = ((  1,  1, -1),
         ( -1,  1,  1),
         ( -1,  1, -1),
         (  1,  1,  1))
    D = (0, 0, 0)
    S = (0, 0, 0, 0)
    while True:
        D[0] = controller_1.axis3.position() / 10.0 # forward/back
        D[1] = controller_1.axis4.position() / 10.0 # left/right
        D[2] = controller_1.axis1.position() / 10.0 # jaw
        S = M * D
        motor_FL.spin(FORWARD, S[0], VOLT)
        motor_BL.spin(FORWARD, S[1], VOLT)
        motor_FR.spin(FORWARD, S[2], VOLT)
        motor_BR.spin(FORWARD, S[3], VOLT)
        controller_1.screen.set_cursor(2, 1)
        controller_1.screen.print(D[0], D[1], D[2], "      ")
        controller_1.screen.next_row()
        controller_1.screen.print(S[0], S[1], S[2], S[3], "       ")
        wait(5, MSEC)

def onauton_autonomous_0():
    global myVariable, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    brain.screen.set_cursor(1, 1)
    controller_1.screen.print("Autonomous")
    controller_1.screen.next_row()
    motor_FL.spin_for(FORWARD, 180, DEGREES, wait=False)
    motor_FR.spin_for(REVERSE, 180, DEGREES, wait=False)

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

when_started1()
