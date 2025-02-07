#include "move.hpp"
#include <rclcpp/rclcpp.hpp>


int main(int argc, char** argv) {
    // Create a new instance of the class
    rclcpp::init(argc, argv);
    auto circle_move_node = std::make_shared<CircleMove>("circle_move_node");

    rclcpp::executors::SingleThreadedExecutor exec;
    exec.add_node(circle_move_node);
    exec.spin();
    RCLCPP_INFO(circle_move_node->get_logger(), "Keyboard interrupt, shutting down.\n");

    rclcpp::shutdown();
    return 0;
}