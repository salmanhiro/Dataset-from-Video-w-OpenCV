import cv2
import numpy as np

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('https://www.nasa.gov/downloadable/videos/arc-aav2718-krex-mvp2015-nasaweb.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

label = input('label: ')
# Read until video is completed
framecount = 0
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Display the resulting frame
    cv2.imshow('Frame',frame)
    
    if cv2.waitKey(25) & 0xFF == ord('s'): #take frame
        cv2.imwrite(f'{label}-{framecount}.jpg', frame)
        framecount += 1
        print(framecount)
    
    if cv2.waitKey(25) & 0xFF == ord('w'): # pause until any key pressed
        cv2.waitKey(-1)
        print('video paused')
    
    if cv2.waitKey(25) & 0xFF == ord('a'): # change label
        cv2.waitKey(-1)
        print('changing label...')
        label = input('label": ')

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

