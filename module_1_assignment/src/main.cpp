#include "Robot.h"
#include "Sensor.h"

auto main() -> int {
  // Sensors
  TemperatureSensor temperatureSensor("TXX");
  DistanceSensor distanceSensor("DYY");
  SensorTemplate<char> sensorOther("Prox");

  // Robots
  Robot robotA("Robot A", 10.0, 0.5, temperatureSensor, distanceSensor,
               sensorOther);

  robotA.moveForward(1.5);
  robotA.moveBackward(-1.5);
  robotA.stop();
  robotA.readDistance();
  robotA.readTemperature();
  robotA.readOther();

  Robot robotB("Robot B", 20.0, 1.0, temperatureSensor, distanceSensor,
               sensorOther);

  robotB.moveForward(2.0);
  robotB.moveBackward(-2.0);
  robotB.stop();
  robotB.readDistance();
  robotB.readTemperature();
  robotB.readOther();

  return 0;
}