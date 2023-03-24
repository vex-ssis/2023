/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       mkreier                                                   */
/*    Created:      Thu Mar 23 2023                                           */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Motor1               motor         1               
// Controller1          controller                    
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"

using namespace vex;
double fb;
int counter;

int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();
  Motor1.setVelocity(40,percent);
  fb = Controller1.Axis3.position(percent);
  Motor1.spin(forward);
  Controller1.Screen.clearScreen();
  while(true) {
    fb = Controller1.Axis3.position(percent);
    if(fb < 0) {
      Motor1.spin(reverse);
    }
    else {
      Motor1.spin(reverse);
    }
    Motor1.setVelocity(fb, percent);
    Controller1.Screen.setCursor(0,0);
    Controller1.Screen.print("Input value: ");
    Controller1.Screen.print(fb);
    Controller1.Screen.print("  ");
    Controller1.Screen.newLine();
    Controller1.Screen.print("Counter: ");
    Controller1.Screen.print(counter);
    counter++;
  }
}
