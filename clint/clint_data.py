import cv2
import time
print (cv2.__version__)
dispW=320
dispH=240                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
img_counter = 2800
flip = 2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(1)
print(f'this is the result {cam.read()}')
while True:
    delay = 0
    ret , frame = cam.read()
    cv2.imshow('picam',frame)
    cv2.moveWindow('picam',0,0)
    img_name = "Parking_data_{}.png".format(img_counter)
    cv2.imwrite(img_name,frame)
    img_counter+=1
    if cv2.waitKey(1)==ord('q'):
        break
    #for _ in range(10):
        time.sleep(1)

cam.release() 
cv2.destroyAllWindows()
