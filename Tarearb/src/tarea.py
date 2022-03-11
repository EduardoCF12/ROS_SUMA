#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import Int16


    
#Subscriber

class tarea():

    def __init__(self):
        self.a=0
        self.b=0
        self.sub=rospy.Subscriber("topicotarea",Int16,self.callbacksubs)
        self.sub2 = rospy.Subscriber("topicotarea1",Int16,self.callbacksubs2)

    def callbacksubs(self, data):
        self.a = data.data
        

    def callbacksubs2(self, data):
        self.b = data.data
        

    def suma(self):
        rospy.loginfo(rospy.get_caller_id()+ "Suma: "+str(self.a+self.b))

    def subscriber(self):
        #rospy.init_node("sub",anonymous=True)
        rospy.Subscriber("topicotarea",Int16, self.callbacksubs)
    
    #Publisher 

    def publisher(self):
        pub = rospy.Publisher("topicotarea",Int16,queue_size=1)
        pub1 = rospy.Publisher("topicotarea1",Int16,queue_size=1)
        rospy.init_node("nodtar")
        rate = rospy.Rate(10)
        a=5
        b=3
        rospy.loginfo("%d, %d",a,b)
        pub.publish(a)
        pub1.publish(b)
    
    
    






#main
if __name__ == "__main__":
    try:
        
        while not rospy.is_shutdown():
            tarea1 = tarea()
            tarea1.publisher()
            tarea1.suma()

    except rospy.ROSInterruptException:
        print("Fallo en el sistema")
