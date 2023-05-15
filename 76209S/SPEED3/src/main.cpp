/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       mk                                                        */
/*    Created:      Mon May 15 2023                                           */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Controller1          controller                    
// MotorL               motor         1               
// MotorR               motor         10              
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"

using namespace vex;

int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();

  Brain.Screen.print("User control.");
  Controller1.Screen.clearScreen();
  Controller1.Screen.print("User control");
  float speed = 0;
  float jaw = 0;
  float speedL = 0;
  float speedR = 0;
  float k = 0.00001;
  while (true) {
    speed = Controller1.Axis3.position(percent);
    jaw = Controller1.Axis1.position(percent);
    speedL += (( 0.2 * speed - 0.05 * jaw) - speedL) * k;
    speedR += ((-0.2 * speed - 0.05 * jaw) - speedR) * k;
    MotorL.spin(forward,speedL,volt);
    MotorR.spin(forward,speedR,volt);
  }
}
