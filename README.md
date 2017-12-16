Senior Design Dec1710 - Team VOLDEMORT
Sean Jellison, Alex Orman, Lixing Liu, Chris Kelley, Evan Lambert

This is our Senior Design project at Iowa State University.
Details about the project can be found here: http://dec1710.sd.ece.iastate.edu

**Introduction**
The goal of our project was to see if we could use a neural network on an
embedded system to perform object recognition using only images from an onboard
camera. The data gained would be used to aid in fully automating flight, landing,
and takeoff of a drone. Our primary target to identify were runways.

The software is written in Python 2.7 and uses openCV for camera interaction and
image manipulation and Tensorflow for the neural network. We used Google's Inception
network, a convolution neural network, as a base to give us better accuracy since
the network is pre-trained on common and simple shapes and objects. We only had to
train the last layer on whatever we were looking for.

**Hardware Used**
The project was pretty open ended for us. We started by researching microcontrollers
to use. Our client suggested we use an NVIDIA Jetson Tk1 or Tx1 since they already had
their own custom Tx1's they were using.

Board - NVIDIA Jetson Tx1
Camera - Logitech C270 Webcam

**Software Used**
One of the first things we looked into was what we wanted to develop our network in. We
chose Tensorflow largely because two of our members had previous experience with it, but
also because Tensorflow has Python libraries for quick and easy development. This
influenced the rest of our software decisions

Python 2.7
openCV 3.1.0
Tensorflow 1.2.1