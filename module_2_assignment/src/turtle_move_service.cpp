#include "rclcpp/rclcpp.hpp"
#include "module_2_assignment/srv/cmd_vel.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include <vector>

using namespace std::chrono_literals;
class CmdVelServiceServer : public rclcpp::Node {
public:
    CmdVelServiceServer() : Node("move_back_and_forth_server") {
        this->service_ = this->create_service<module_2_assignment::srv::CmdVel>(
            "cmd_vel_back_and_forth", std::bind(&CmdVelServiceServer::handle_cmd_vel, this, std::placeholders::_1, std::placeholders::_2));
        
    }

private:
    void handle_cmd_vel(const std::shared_ptr<module_2_assignment::srv::CmdVel::Request> request,
                        std::shared_ptr<module_2_assignment::srv::CmdVel::Response> response) {
        // handle the incorrect request
        auto robot_names = request->robot_names;
        std::vector<std::string> topic_names;
        for (const auto &robot_name : robot_names) {
            RCLCPP_INFO(this->get_logger(), "Received request: %s", robot_name.c_str());
            // create publisher according to requested name
            auto topic_name = "/"+ robot_name + "/cmd_vel";
            topic_names.push_back(topic_name);
        }
        
        for (const auto &topic_name : topic_names) {
            RCLCPP_INFO(this->get_logger(), "Publishing to topic: %s", topic_name.c_str());
            rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher = this->create_publisher<geometry_msgs::msg::Twist>(topic_name, 10);
            this->publishers_.push_back(publisher);
        }
        this->timer_ = this->create_wall_timer(3s, std::bind(&CmdVelServiceServer::timerCallback, this));
        
        response->success = true;
    }

    void timerCallback() {
        // create velocity message using move()
        if (this->counter_ % 2 == 0) {
            this->msg_.linear.x = 1.0;
            this->msg_.angular.z = 0.0;
        } else {
            this->msg_.linear.x = -1.0;
            this->msg_.angular.z = 0.0;
        }
        this->counter_++;
        for (auto& publisher : this->publishers_){
            publisher->publish(this->msg_);
        }
        RCLCPP_INFO(this->get_logger(), "Driving Turtle back and forth.");
    }

    rclcpp::Service<module_2_assignment::srv::CmdVel>::SharedPtr service_;
    std::vector<rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr> publishers_;
    rclcpp::TimerBase::SharedPtr timer_;
    geometry_msgs::msg::Twist msg_;
    int counter_ {0};
};


int main(int argc, char * argv[]){
    rclcpp::init(argc, argv);

    auto node = std::make_shared<CmdVelServiceServer>();

    RCLCPP_INFO(node->get_logger(), "Ready Move Any Turtlebot Back and Forth.");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}