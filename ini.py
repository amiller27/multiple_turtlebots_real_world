import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped, Quaternion
from sys import argv
import tf.transformations
rospy.init_node('pose_publisher')
pub = rospy.Publisher('/robot_0/initialpose', PoseWithCovarianceStamped)
pose = PoseWithCovarianceStamped()
pose.header.frame_id = '/map'
pose.pose.pose.orientation = Quaternion(*tf.transformations.quaternion_about_axis(float(argv[3]), (0, 0, 1)))
pose.pose.pose.position.x = float(argv[1])
pose.pose.pose.position.y = float(argv[2])
print repr(pose)
rate = rospy.Rate(1)
while not rospy.is_shutdown():
	pub.publish(pose)
	rate.sleep()
