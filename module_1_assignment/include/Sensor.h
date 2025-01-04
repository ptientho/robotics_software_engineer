#ifndef SENSOR_H
#define SENSOR_H

#include <string>
#include <iostream>

class Sensor {
public:
  Sensor(std::string name);
  auto getName() const -> std::string;

protected:
  std::string _name;
};

class DistanceSensor : public Sensor {
public:
  DistanceSensor(std::string name);
  void readDistance();
};

class TemperatureSensor : public Sensor {
public:
  TemperatureSensor(std::string name);
  void readTemperature();
};

template <typename T> class SensorTemplate : public Sensor {
public:
  SensorTemplate(std::string name) : Sensor(name) {}
  void readValue(T value) { std::cout << _name << ": " << "Read Value= " << value << std::endl; }
};

#endif // SENSOR_H