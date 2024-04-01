import cv2
import numpy as np
import time
class videoCaptureAT:
    def record(seconds,index):
        cam = cv2.VideoCapture(index)

        # Get the frame dimensions
        ret, frame = cam.read()
        height, width = frame.shape[:2]
        shape = (width, height)

        # Create the video writer object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_write = cv2.VideoWriter('sampleee.mp4', fourcc, 20.0, shape)

        # Start the timer
        start_time = time.time()
        duration = seconds # Duration in seconds

        while time.time() - start_time < duration:
            ret, frame = cam.read()
            if not ret:
                print("Error: Failed to capture frame")
                break

            # Convert to grayscale (optional)
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Write the color frame to the video file
            video_write.write(frame)

            # Exit the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release resources
        cam.release()
        video_write.release()
        cv2.destroyAllWindows()