//base_scan->base_link로 변환을 broadcasting하는 작업을 수행하는 node
#include <ros/ros.h>
#include <tf/transform_broadcaster.h>

int main(int argc, char** argv){
	ros::init(argc, argv, "robot_tf_publisher");
	ros::NodeHandle n;

	ros::Rate r(100);

	tf::TransformBroadcaster broadcaster;

	while(n.ok()){
		broadcaster.sendTransform(
			tf::StampedTransform(
				tf::Transform(tf::Quaternion(0, 0, 0, 1), tf::Vector3(0.25, 0.0, 0.26595)),
				ros::Time::now(),"base_link", "laser")); //vector3 값은 base_link로부터 떨어져있는 base_scan의 거리 (m) x,y,z 값

		r.sleep();
	}
}
