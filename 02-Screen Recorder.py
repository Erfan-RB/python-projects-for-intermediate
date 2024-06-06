#Screen-Recorder
#import the required pakages
import pyautogui
import opencv as  cv2
import numpy as np

# Specify resolution
resolution = (1920, 1080)
# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")
# Specify name of Output file
filename =  "Recording.avi"
#specify frames rate
fps = 60.0
#create a videwriter object
out = cv2.VideWriter(filename, codec, fps, resolution)
# Create an Empty window
cv2.resizeWindow("Live", 480, 270)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    #BGR==>RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow('Live', frame)
    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cv2.destroyAllWindows()    
    
