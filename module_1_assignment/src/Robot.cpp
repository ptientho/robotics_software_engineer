#include "Robot.h"
#include <iostream>

Robot::Robot(const std::string name, const double weight, const double size,
             const TemperatureSensor &temperatureSensor,
             const DistanceSensor &distanceSensor,
             const SensorTemplate<char> &sensorOther)
    : _name(name), _speed(0.0), _weight(weight),
      _size(size), _temperatureSensor(temperatureSensor),
      _distanceSensor(distanceSensor), _sensorOther(sensorOther) {
  std::cout << "Robot " << _name << " created." << std::endl;
}

void Robot::moveForward(double speed) {
  _speed = speed;
  std::cout << "Robot" << _name << ": " << "Moving Forward with speed: " << speed << " m/s" << std::endl;
}

void Robot::moveBackward(double speed) {
  _speed = -speed;
  std::cout << "Robot" << _name << ": " << "Moving Backward with speed: " << speed << " m/s" << std::endl;
}

void Robot::stop() {
  std::cout << "Robot" << _name << ": " << "Stopping" << std::endl;
  _speed = 0.0;
}

void Robot::readDistance() { _distanceSensor.readDistance(); }

void Robot::readTemperature() { _temperatureSensor.readTemperature(); }

void Robot::readOther() { _sensorOther.readValue('0'); }
