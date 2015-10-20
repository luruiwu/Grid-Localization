import rospy
import rosbag
from std_msgs.msg import String#Motion, Observation
#from tf.transformations import euler_from_quarternion
from tf.transformations import euler_from_quaternion

f = open("bag_content.txt","w")
bag = rosbag.Bag('../bag/grid.bag','r')
topics = []
topics.append('Motion')
topics.append('Observation')


try:
	for topic, msg, time_stamp in bag.read_messages(topics=['Movements', 'Observations']):
		f.write("--------------------------------------------------\n")
		f.write(str(topic) + "\n")
		if topic == 'Movements':
			print euler_from_quaternion((msg.rotation1.x,msg.rotation1.y,msg.rotation1.z,msg.rotation1.w))
		f.write(str(msg) + "\n")
		f.write(str(time_stamp) + "\n")
		f.write( "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
finally:
	bag.close()
	f.close()

