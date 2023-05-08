using namespace vex;

extern brain Brain;

// VEXcode devices
extern controller Controller1;
extern motor MotorFL;
extern motor MotorBL;
extern motor MotorFR;
extern motor MotorBR;
extern motor MotorRoller;
extern motor MotorIntake;

/**
 * Used to initialize code/tasks/devices added using tools in VEXcode Pro.
 * 
 * This should be called at the start of your int main function.
 */
void  vexcodeInit( void );