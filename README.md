# Smart-Car-safety
This project aims to improve driver safety by monitoring alertness through blink detection using a Raspberry Pi and a webcam. The system continuously tracks the driver's face and eyes using computer vision techniques.

### How it works:
The Raspberry Pi is connected to a webcam, capturing the driver's face in real-time.
It uses OpenCV and cvzone libraries to detect the eyes and calculate a blink ratio.
If the driver's eyes remain closed for too long (indicating drowsiness), the system triggers an alert.
The system also counts the total number of blinks and visualizes the blink ratio with live plotting.

### Hardware:
+ Raspberry Pi
+ Arduino
+ LED Bulbs
+ Buzzer
+ Motor
+ Webcam
+ SD card

### Libraries:
+ OpenCV
+ cvzone
+ FaceMeshDetector

### Features:
+ Real-time blink detection
+ Drowsiness alert system
+ Live plotting of blink ratio data
