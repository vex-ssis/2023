/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       mk                                                        */
/*    Created:      Mon May 08 2023                                           */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Controller1          controller                    
// Drivetrain           drivetrain    1, 10           
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"

using namespace vex;

int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();
  Brain.Screen.printAt(10,20,"Lets go!");
  Brain.Screen.printAt(10,40,"I'm ready for competition!");
  Controller1.Screen.clearScreen();
  Controller1.Screen.newLine();
  Controller1.Screen.print("Lets go!");
  Controller1.Screen.newLine();
  Controller1.Screen.print("I'm ready!");
}
