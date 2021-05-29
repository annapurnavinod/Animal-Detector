# RCDS-Round The Clock Detection System

Problem Statement:
Animal attacks on crops in Kerala has been a cause of concern for a long time.

Introduction:
Munnar is a region in the Idukki high-range provinces of Kerala. The forest here is home to many wild animals such as tigers, elephants and wild boars. In the recent 10-15 years the destruction of crops by these creatures have been increasing and may reports of large scale plantation destructions  especially by wild boars and elephants were observed.


Solution:

The RCDS or Round The Clock Detection System is a product developed that has a 24-hour  animal detection set-up and surveillance for the farming vicinity.The surveillance for the farm can be done by a monitoring app installed in the farmer’s phone.

The hardware of the system has 2 controls for day and night .For Day time,  the presence of an external wild creature is detected with the help of an Ultrasonic sensor(HC -SR04) which on activation sets off a moderately low triggering alarm towards the animal. The simulation of the Ultrasonic sensor circuit is simulated [here.](https://www.tinkercad.com/things/4batVNO9OJZ-test/editel?sharecode=KnvPZKgdMqX2d_8PNaXX0Jo2ahHH1qfF4zlye5tGsnA)

![Animal Detector](https://user-images.githubusercontent.com/67196669/120081153-95e23c00-c0d9-11eb-9220-c26d52f7b1b7.png)

For night time detetcion we  install a 9t vision camera set up for detecting the object . The detection code developed using OpenCV library has been uploaded.The detected object is tracked using an  illuminant which gets immediately turned on.This can be used to set off the animal.In addition to the detection camera,another set of  cameras placed in the vicinity itself gets triggered and  navigates the animal away from the farm.

![pathway](https://user-images.githubusercontent.com/67196669/120081557-db076d80-c0db-11eb-8760-380e714783bb.jpeg)

This method is holistic in a way that it doesnt promote harming the animal but simply diverts them away from the farm to desirable location.


A web application installed on the farmer's phone helps to monitor the switching of modes from day to night, alert of intrusion etc.








