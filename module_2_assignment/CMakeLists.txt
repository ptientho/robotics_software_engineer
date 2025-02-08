cmake_minimum_required(VERSION 3.8)
project(module_2_assignment)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/CmdVel.srv"
)

set(AUTOGEN_TARGET_DEPENDS
  "rclcpp"
  "geometry_msgs"
  "std_msgs"
)

# ADD TASK 5 Executables here
include_directories(include)

add_executable(move_circle src/main1.cpp src/move.cpp)
add_executable(move_spiral src/main2.cpp src/move.cpp)
add_executable(turtle_move_service src/turtle_move_service.cpp)
add_executable(led_control src/led_publisher.cpp)
add_executable(led_receiver src/led_subscriber.cpp)
ament_target_dependencies(move_circle ${AUTOGEN_TARGET_DEPENDS})
ament_target_dependencies(move_spiral ${AUTOGEN_TARGET_DEPENDS})
ament_target_dependencies(turtle_move_service ${AUTOGEN_TARGET_DEPENDS})
ament_target_dependencies(led_control ${AUTOGEN_TARGET_DEPENDS})
ament_target_dependencies(led_receiver ${AUTOGEN_TARGET_DEPENDS})

rosidl_get_typesupport_target(cpp_typesupport_target ${PROJECT_NAME} rosidl_typesupport_cpp)
target_link_libraries(turtle_move_service "${cpp_typesupport_target}")


install(TARGETS
  move_circle
  move_spiral
  turtle_move_service
  led_control
  led_receiver
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

ament_export_dependencies(rosidl_default_runtime)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
