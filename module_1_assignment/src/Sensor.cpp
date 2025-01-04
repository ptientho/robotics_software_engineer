#include "Sensor.h"
#include <iostream>

Sensor::Sensor(std::string name) : _name(name) {}

auto Sensor::getName() const -> std::string { return _name; }

DistanceSensor::DistanceSensor(std::string name) : Sensor(name) {
  std::cout << "Distance Sensor " << _name << " created." << std::endl;
}

void DistanceSensor::readDistance() {
  std::cout << "Distance: " << "100cm" << std::endl;
}

TemperatureSensor::TemperatureSensor(std::string name) : Sensor(name) {
  std::cout << "Temperature Sensor " << _name << " created." << std::endl;
}

void TemperatureSensor::readTemperature() {
  std::cout << "Temperature: " << "20C" << std::endl;
}