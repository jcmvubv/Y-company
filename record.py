import cv2
import numpy as np
#import pyautogui
import time
# libraries to add minimize feature the window
import win32gui
import win32con
#=========== use mkdir to make a directory
from os import mkdir
#============================make directory if not available
try:
    mkdir("recordings")
except FileExistsError:
    pass
#=============method to minimize window
def minimizeWindow():
    window = win32gui.FindWindow(None,"Screen recorder")
    win32gui.ShowWindow(window,win32con.SW_MINIMIZE)

# initialize screen resolution, get it from your OS settings
SCREEN_SIZE = (1366, 768)
# define the video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write object
output = cv2.VideoWriter("recordings/"+"SreenRecording "+time.strftime("%H-%M-%S %d-%m-%y")+".mp4",
                         fourcc, 20.0, (SCREEN_SIZE))
print("Recording started.... \nwindow minimized in taskbar.\npress q to exit.")

minimized = False
while True:
    # make a screenshot
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # show the frame
    cv2.imshow("Screen recorder", frame)
    if minimized== True:
        pass
    else:
        minimized = True
        minimizeWindow()
        
    # write the frame
    output.write(frame)
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        print("\rRecording Finished.")
        break

# make sure everything is closed when exited
output.release()
cv2.destroyAllWindows()