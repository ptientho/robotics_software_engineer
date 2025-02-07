#include "move.hpp"
#include <rclcpp/rclcpp.hpp>


int main(int argc, char** argv) {
    // Create a new instance of the class
    rclcpp::init(argc, argv);
    auto spiral_move_node = std::make_shared<SpiralMove>("spiral_move_node");

    rclcpp::executors::MultiThreadedExecutor exec;
    exec.add_node(spiral_move_node);
    exec.spin();
    RCLCPP_INFO(spiral_move_node->get_logger(), "Keyboard interrupt, shutting down.\n");

    rclcpp::shutdown();
    return 0;
}