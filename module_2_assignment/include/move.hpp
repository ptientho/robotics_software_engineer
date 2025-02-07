#ifndef MOVE_HPP
#define MOVE_HPP

#include "rclcpp/rclcpp.hpp"
#include <geometry_msgs/msg/twist.hpp>

class Move : public rclcpp::Node
{

    public:
        Move(const std::string &name);
        virtual void move() = 0;
        
    protected:
        rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
        rclcpp::TimerBase::SharedPtr timer_;
        geometry_msgs::msg::Twist msg_;

        
};

class CircleMove : public Move
{
    public:
        CircleMove(std::string &&name);
        void move() override;
    private:
        void timerCallback();
};

class SpiralMove : public Move
{
    public:
        SpiralMove(std::string &&name);
        void move() override;
    private:
        void timerCallback();
        double x_ = 0.0;
        double y_ = 0.0;
        double theta_ = 0.0;
};


#endif  // MOVE_HPP