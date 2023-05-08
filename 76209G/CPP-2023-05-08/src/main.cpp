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
