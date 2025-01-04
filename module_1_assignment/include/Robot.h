#ifndef ROBOT_H
#define ROBOT_H

#include "Sensor.h"
#include <string>

class Robot {
public:
  Robot(const std::string name, const double weight, const double size,
        const TemperatureSensor &temperatureSensor,
        const DistanceSensor &distanceSensor,
        const SensorTemplate<char> &sensorOther);
  void moveForward(double speed);
  void moveBackward(double speed);
  void stop();
  void readDistance();
  void readTemperature();
  void readOther();

private:
  std::string _name;
  double _speed;
  double _weight;
  double _size;
  TemperatureSensor _temperatureSensor;
  DistanceSensor _distanceSensor;
  SensorTemplate<char> _sensorOther;
};

#endif // ROBOT_H
