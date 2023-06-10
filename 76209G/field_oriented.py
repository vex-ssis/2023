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
motor_roller = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
motorIntake = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
gyro_h = Gyro(brain.three_wire_port.h)


# wait for rotation sensor to fully initialize
wait(30, MSEC)



# define variables used for controlling motors based on controller inputs
controller_1_right_shoulder_control_motors_stopped = True

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global controller_1_right_shoulder_control_motors_stopped, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            # check the buttonR1/buttonR2 status
            # to control motor_roller
            if controller_1.buttonR1.pressing():
                motor_roller.spin(FORWARD)
                controller_1_right_shoulder_control_motors_stopped = False
            elif controller_1.buttonR2.pressing():
                motor_roller.spin(REVERSE)
                controller_1_right_shoulder_control_motors_stopped = False
            elif not controller_1_right_shoulder_control_motors_stopped:
                motor_roller.stop()
                # set the toggle so that we don't constantly tell the motor to stop when
                # the buttons are released
                controller_1_right_shoulder_control_motors_stopped = True
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)
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
    gyro_h.set_heading(0, DEGREES)

def ondriver_drivercontrol_0():
    global myVariable, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    motor_roller.set_velocity(100, PERCENT)
    motorIntake.set_velocity(100, PERCENT)

    controller_1.screen.set_cursor(1, 1)
    controller_1.screen.print("User Control    ")
    controller_1.screen.next_row()
    while True:
        theta = (gyro_h.heading(DEGREES)*math.pi)/180
        c = math.cos(theta)**2
        s = -math.sin(theta)**2
        if theta > math.pi:
            s = -s
        if theta > math.pi / 2 and theta < math.pi * 3 / 2:
            c = -c
        mFL = (  c + s, c - s, -1)
        mBL = ( -c + s, c + s,  1)
        mFR = ( -c + s, c + s, -1)
        mBR = (  c + s, c - s,  1)    
        fb = controller_1.axis3.position()
        lr = controller_1.axis4.position()
        jaw = controller_1.axis1.position()
        speed_FL = mFL[0]*fb + mFL[1]*lr + mFL[2]*jaw
        speed_BL = mBL[0]*fb + mBL[1]*lr + mBL[2]*jaw
        speed_FR = mFR[0]*fb + mFR[1]*lr + mFR[2]*jaw
        speed_BR = mBR[0]*fb + mBR[1]*lr + mBR[2]*jaw
        motor_FL.spin(FORWARD, speed_FL, PERCENT)
        motor_BL.spin(FORWARD, speed_BL, PERCENT)
        motor_FR.spin(FORWARD, speed_FR, PERCENT)
        motor_BR.spin(FORWARD, speed_BR, PERCENT)
        controller_1.screen.set_cursor(2, 1)
        controller_1.screen.print(fb, lr, jaw, theta, "    ")
        controller_1.screen.next_row()
        controller_1.screen.print(speed_FL, speed_BL, speed_FR, speed_BR, "      ")
        if controller_1.buttonR1.pressing():
            motor_roller.spin(FORWARD)
        elif controller_1.buttonR2.pressing():
            motor_roller.spin(REVERSE)
        else:
            motor_roller.stop()
        if controller_1.buttonL1.pressing():
            motorIntake.spin(FORWARD)
        elif controller_1.buttonL2.pressing():
            motorIntake.spin(REVERSE)
        else:
            motorIntake.stop()

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
