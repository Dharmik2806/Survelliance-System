import cv2,time

#Create an object for external camera
video=cv2.VideoCapture(0)

a=0

while True:
    #This will check for milliseconds
    a=a+1

    #Create a frame object
    check,frame=video.read()

    # They both will give us matrix values of frames
    #print(check)
    #print(frame)

    #coverting to grayscale
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Showing the frame
    cv2.imshow("Capturing",frame)

    #Stopping the stream
    #cv2,waitKey(0)

    #For PLaying the camera
    key=cv2.waitKey(1)

    if key==ord('q'):
        break

print(a)

#Shutting down camera
video.release()

cv2.destroyAllWindows

