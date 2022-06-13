import cv2
dispW=320
dispH=240
dispW=320
dispH=240
flip = 2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
#vidcap = cv2.VideoCapture(0)
success,image = cam.read()
count = 0
while success:
    cv2.imwrite("data.jpg" % count ,image)
    img_name = "Parking_data_{}.png".format(img_counter)
    cv2.imwrite(img_name,frame)
    success,image = cam.read()
    print('frame',success)
    count+=1