#include "move.hpp"
#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/twist.hpp>

#include <cmath>

using namespace std::chrono_literals;

Move::Move(const std::string &name) : Node(name)
{
    this->declare_parameter<std::string>("cmd_vel_topic", "/turtle1/cmd_vel");
    auto cmdVelTopic = this->get_parameter("cmd_vel_topic").as_string();
    
    this->publisher_ = this->create_publisher<geometry_msgs::msg::Twist>(cmdVelTopic, 10);
    
}

CircleMove::CircleMove(std::string &&name) : Move(std::move(name))
{
    this->timer_ = this->create_wall_timer(500ms, std::bind(&CircleMove::timerCallback, this));
    RCLCPP_INFO(this->get_logger(), "CircleMove node has been started.");
}

void CircleMove::timerCallback()
{   
    // create velocity message using move()
    move();
    this->publisher_->publish(this->msg_);
    RCLCPP_INFO(this->get_logger(), "Driving Turtle in a circle.");
}

void CircleMove::move()
{
    this->msg_.linear.x = 0.5;
    this->msg_.angular.z = 0.4;
}

SpiralMove::SpiralMove(std::string &&name) : Move(std::move(name))
{
    this->timer_ = this->create_wall_timer(500ms, std::bind(&SpiralMove::timerCallback, this));
    RCLCPP_INFO(this->get_logger(), "SpiralMove node has been started.");
}

void SpiralMove::timerCallback()
{
    // calculate the linear and angular velocities using move()
    // x = ..... , y = .....
    move();
    this->publisher_->publish(this->msg_);
    RCLCPP_INFO(this->get_logger(), "Driving Turtle in a spiral.");
}

void SpiralMove::move()
{
    double linearSpeed = 0.5;
    double spiralParam = 0.9;
    double timeUnit = 0.5; // 500ms
    
    // No!! we dont use odom. Instead we use x and y from our control update
    double radius = sqrt(this->x_*this->x_ + this->y_*this->y_) + 1e-5;
    auto angSpeed = linearSpeed / (spiralParam * radius);

    // update states
    this->theta_ += angSpeed*timeUnit;
    this->x_ += linearSpeed * cos(this->theta_)*timeUnit;
    this->y_ += linearSpeed * sin(this->theta_)*timeUnit;
    
    // binding message
    this->msg_.linear.x = linearSpeed;
    this->msg_.angular.z = angSpeed;
}
