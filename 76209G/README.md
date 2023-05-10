# Team G - The Honey Badgers with robot 'Natasha'

The Mecanum wheels are not easy to handle, but team G decided to give them a go: and worked tirelessly on them in the first semester.

Not to forget the virtual skills ...

## Example code for the mechanum drive

Unfortunately I can't use matrices with a drive vector and a motor vector. But we are close:

``` py
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
    mFL = (  1,  1, -1)
    mBL = ( -1,  1,  1)
    mFR = ( -1,  1, -1)
    mBR = (  1,  1,  1)    
    while True:
        fb = controller_1.axis3.position() / 10.0
        lr = controller_1.axis4.position() / 10.0
        jaw = controller_1.axis1.position() / 10.0
        speed_FL = mFL[0]*fb + mFL[1]*lr + mFL[2]*jaw
        speed_BL = mBL[0]*fb + mBL[1]*lr + mBL[2]*jaw
        speed_FR = mFR[0]*fb + mFR[1]*lr + mFR[2]*jaw
        speed_BR = mBR[0]*fb + mBR[1]*lr + mBR[2]*jaw
        motor_FL.spin(FORWARD, speed_FL, VOLT)
        motor_BL.spin(FORWARD, speed_BL, VOLT)
        motor_FR.spin(FORWARD, speed_FR, VOLT)
        motor_BR.spin(FORWARD, speed_BR, VOLT)
        controller_1.screen.set_cursor(2, 1)
        controller_1.screen.print(fb, lr, jaw, "    ")
        controller_1.screen.next_row()
        controller_1.screen.print(speed_FL, speed_BL, speed_FR, speed_BR, "      ")
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
```

If matrices would be supported, it would read like this

``` py
    M = ((  1,  1, -1),    # the matrix
         ( -1,  1,  1),
         ( -1,  1, -1),
         (  1,  1,  1))
    D = (0, 0, 0)          # drive input from controller (3 analog values)
    S = (0, 0, 0, 0)       # speed output to each of the 4 motors
    while True:
        D[0] = controller_1.axis3.position() / 10.0   # forward/back
        D[1] = controller_1.axis4.position() / 10.0   # left/right
        D[2] = controller_1.axis1.position() / 10.0   # jaw
        S = M * D
        motor_FL.spin(FORWARD, S[0], VOLT)
        motor_BL.spin(FORWARD, S[1], VOLT)
        motor_FR.spin(FORWARD, S[2], VOLT)
        motor_BR.spin(FORWARD, S[3], VOLT)        
```

## Converting code to C++

I actually did some copy and paste, and changed a few capitalized functions, but all in all very similar. Have a look:

``` cpp
/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       mk                                                        */
/*    Created:      Mon May 08 2023                                           */
/*    Description:  V5 project for 76209G with Mechanum wheels                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Controller1          controller                    
// MotorFL              motor         1               
// MotorBL              motor         11              
// MotorFR              motor         10              
// MotorBR              motor         20              
// MotorRoller          motor         8               
// MotorIntake          motor         19              
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"

using namespace vex;

int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();
  Brain.Screen.printAt(10,20,"Driver control 76209G started.");
  Controller1.Screen.setCursor(1, 1);
  Controller1.Screen.print("User control   ");
  Controller1.Screen.newLine();
  float mFL[] = {  1,  1, -1};
  float mBL[] = { -1,  1,  1};
  float mFR[] = { -1,  1, -1};
  float mBR[] = {  1,  1,  1};  
  while (true) {
    float fb = Controller1.Axis3.position(percent);
    float lr = Controller1.Axis1.position(percent);
    float jaw = Controller1.Axis4.position(percent);
    float speed_FL = mFL[0]*fb + mFL[1]*lr + mFL[2]*jaw;
    float speed_BL = mBL[0]*fb + mBL[1]*lr + mBL[2]*jaw;
    float speed_FR = mFR[0]*fb + mFR[1]*lr + mFR[2]*jaw;
    float speed_BR = mBR[0]*fb + mBR[1]*lr + mBR[2]*jaw;
    MotorFL.spin(forward, speed_FL, volt);
    MotorBL.spin(forward, speed_BL, volt);
    MotorFR.spin(forward, speed_FR, volt);
    MotorBR.spin(forward, speed_BR, volt);
    Controller1.Screen.setCursor(2, 1);
    Controller1.Screen.print(fb);
    Controller1.Screen.print(lr);
    Controller1.Screen.print(jaw);
    Controller1.Screen.print("    ");
    Controller1.Screen.newLine();
    Controller1.Screen.print(speed_FL);
    Controller1.Screen.print(speed_BL);
    Controller1.Screen.print(speed_FR);
    Controller1.Screen.print(speed_BR);
    Controller1.Screen.print("      ");
    if (Controller1.ButtonR1.pressing()) 
    {
      MotorRoller.spin(forward);
    }
    else if (Controller1.ButtonR2.pressing())
    {
      MotorRoller.spin(reverse);
    }
    else {
      MotorRoller.stop();
    }
    if (Controller1.ButtonL1.pressing())
    {
      MotorIntake.spin(forward);
    }
    else if (Controller1.ButtonL2.pressing())
    {
      MotorIntake.spin(reverse);
    }
    else
    {
        MotorIntake.stop();
    }
  }
}
```
