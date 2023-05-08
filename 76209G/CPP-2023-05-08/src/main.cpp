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
  float mFL = (  1,  1, -1);
  float mBL = ( -1,  1,  1);
  float mFR = ( -1,  1, -1);
  float mBR = (  1,  1,  1) ;  
  while (true) {
    float fb = Controller1.Axis3.position(percent);
    float lr = Controller1.Axis1.position(percent);
    float jaw = Controller1.Axis4.position(percent);

  }
}
