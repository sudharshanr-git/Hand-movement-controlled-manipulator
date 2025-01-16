import cv2
import time
import serial
import struct
import mediapipe as mp
import serial.tools.list_ports
mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
mphands=mp.solutions.hands

arduino=serial.Serial()
port="COM7"
arduino.baudrate = 9600
arduino.port = port
arduino.open()


cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 700)
hands=mphands.Hands()
while True:
    data,image=cap.read()
    #Flip the image
    image=cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB)
    width, height, _ = image.shape 
    #storing the results
    results=hands.process(image)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            center_keypoint = hand_landmarks.landmark[8]
            mp_drawing.draw_landmarks(image,hand_landmarks, mphands.HAND_CONNECTIONS)

            x_px = int(center_keypoint.x * 180)+30
            if x_px<0:
                x_px=0
            if x_px>180:
                x_px=180
            y_px = int(center_keypoint.y * 180)+30
            if y_px<0:
                y_px=0
            if y_px>180:
                y_px=180
            z_px = int(220+(center_keypoint.z * 700))
            if z_px<0:
                z_px=0
            if z_px>180:
                z_px=180
            
            z_px=int((z_px/200)*180)#not reliable
            z_px=int(z_px/10)*10
            arduino.write(struct.pack('>BBB', x_px, y_px, z_px))
            print(x_px,y_px,z_px)
            break
    image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    cv2.imshow('Handtracker',image)
    cv2.waitKey(1)