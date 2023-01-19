import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone

# Use '0' for VideoCapture if it's default
webcam = cv2.VideoCapture(0)
webcam.set(3, 1280)
webcam.set(4, 720)
detector = HandDetector()
# Creating FPS
fps = cvzone.FPS()

while True:
    # Making the frame
    info, img = webcam.read()
    # Showing the FPS
    fps_, img = fps.update(img, pos=(50, 80), color=(255, 0, 255), scale=3, thickness=2)

    # Find the hands
    hands, img = detector.findHands(img)

    # Display the output
    cv2.imshow('Hands and Face', img)

    # Pressing 'Q' will exit the program
    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
