#use videoCaptureAT and record to record video of x seconds
# take input from user for x 
# and record video of x seconds
# save the video as sample.mp4
# import
from  videoCaptureAT import videoCaptureAT as vc

x = int(input("Enter the duration of the video in seconds: "))
vc.record(x,0)
print("Video has been recorded and saved as sample.mp4")
