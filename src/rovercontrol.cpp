#include <cinttypes>
#include <functional>
#include <memory>
#include <string>

#include <geometry_msgs/msg/twist.hpp>
#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/joy.hpp>


class RoverControl :public rclcpp::Node{
public:
    RoverControl() : Node("RoverControl_node"){
      //Publisher
      cmd_vel_pub = this->create_publisher<geometry_msgs::msg::Twist>("cmd_vel", 10);
      //Subscriber
      joy_sub = this->create_subscription<sensor_msgs::msg::Joy>("joy", rclcpp::QoS(10),[this](const sensor_msgs::msg::Joy::SharedPtr msg){joyCallback(msg);});
      enable_button = this->declare_parameter("enable_button", 5); //L1
      robot_l_x = this->declare_parameter("linear_x", 1); //LY
      robot_a_z = this->declare_parameter("angular_z", 3); //RX
      robot_l_x_scale = this->declare_parameter("scale_l_x", 1);
      robot_a_z_scale = this->declare_parameter("scale_a_z", 1.5);

  }
private:  
  void joyCallback(const sensor_msgs::msg::Joy::SharedPtr joy_msg){
    if (static_cast<int>(joy_msg->buttons.size()) > enable_button &&
           joy_msg->buttons[enable_button]){
      sendCmdVelMsg(joy_msg, "modename");
    }
    else{
    // When enable button is released, immediately send a single no-motion command
    // in order to stop the robot.
      if (!sent_disable_msg){
        // Initializes with zeros by default.
        auto cmd_vel_msg = std::make_unique<geometry_msgs::msg::Twist>();
        cmd_vel_pub->publish(std::move(cmd_vel_msg));
        sent_disable_msg = true;
      }
    }
  }
  void sendCmdVelMsg(const sensor_msgs::msg::Joy::SharedPtr joy_msg, const std::string& mode){
    // Initializes with zeros by default.
    auto cmd_vel_msg = std::make_unique<geometry_msgs::msg::Twist>();
    cmd_vel_msg->linear.x = getControllerVal(joy_msg, robot_l_x_scale, robot_l_x); //LY
    cmd_vel_msg->angular.z = getControllerVal(joy_msg, robot_a_z_scale, robot_a_z); //RX

    cmd_vel_pub->publish(std::move(cmd_vel_msg));
    sent_disable_msg = false;
  }
  double getControllerVal(const sensor_msgs::msg::Joy::SharedPtr joy_msg,double scale, const int& number){
    return joy_msg->axes[number] *scale;
  }
  int64_t enable_button;
  bool sent_disable_msg;
  int64_t robot_l_x;
  int64_t robot_a_z;
  int64_t robot_l_x_scale;
  int64_t robot_a_z_scale;
  rclcpp::Subscription<sensor_msgs::msg::Joy>::SharedPtr joy_sub;
  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr cmd_vel_pub;
};

int main(int argc, char * argv[])
  {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<RoverControl>());
    rclcpp::shutdown();
    return 0;
}
