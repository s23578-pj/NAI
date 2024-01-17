"""
=================================================================
Computer Vision - OpenCV - Exercise nr 3 - Gesture Recognition
=================================================================

Authors:
Alicja Szczypior
Krzysztof Szczypior

+----------------------------------------------------------------------------+

To run the program, install the following Python packages (if required):
About version make sure you have at least
1. Python – 3.x (we used Python 3.8.8 in this project)
2. OpenCV – 4.5

Run “pip install opencv-python” to install OpenCV.
3. MediaPipe – 0.8.5

Run “pip install mediapipe” to install MediaPipe.
4. Tensorflow – 2.5.0

Run “pip install tensorflow” to install the tensorflow module.
5. Numpy – 1.19.3

If you are working on MAC just use pip3 command.

+----------------------------------------------------------------------------+

This program is used for hand gestures detection in real time including major packages: Hand Gesture Recognizer using
the MediaPipe framework and Tensorflow in OpenCV and Python. In this application we will detect:
okay, peace, thumbs up, thumbs down, call me, stop, rock, live long, fist and smile.

Mediapipe is used for detection - in our project we want to detect hands, but you can also detect face or any object.
This is developed by Google and is open-source and cross-platform framework. This library allows to recognize the hand
and the hand key points. MediaPipe returns a total of 21 key points for each detected hand. CHECK Hand Landmark Model:
https://www.analyticsvidhya.com/blog/2021/07/building-a-hand-tracking-system-using-opencv/

Tensorflow -> keras is used for machine learning, neural networks - open-source developed also by Google.
This app will use to pre-trained model gesture by load_model function.

NumPy is used to store and manipulate these coordinates because it allows for efficient matrix operations. Storing
landmark list -> landmarks = np.array(landmarks)


Gesture manual:
"call me" -> music: on
"stop" or "live long" -> music: stop
"okay": -> music: pause
"smile" -> music: unpause
"thumbs up" -> music: volume up
"thumbs down" -> music: volume down

"""
import cv2
import numpy as np
import mediapipe as mp
from keras.models import load_model

from controlSound import SoundController

# create sound controller instance
mySoundController = SoundController()

# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=2, min_detection_confidence=0.9)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
gesture_model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)

# Initialize the webcam
capture = cv2.VideoCapture(0)
sound_played = False

while True:
    # Read each frame from the webcam
    _, frame = capture.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(frame_rgb)

    # postprocess of the result
    if result.multi_hand_landmarks:
        gesture = ''
        for hands_landmarks in result.multi_hand_landmarks:
            landmarks = []
            for lm in hands_landmarks.landmark:
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)
                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, hands_landmarks, mpHands.HAND_CONNECTIONS)

            # Predict gesture
            prediction = gesture_model.predict([landmarks])
            classID = np.argmax(prediction)
            gesture = classNames[classID]

            # Get the position of the hand (assuming the first landmark is the wrist)
            hand_position = (landmarks[0][0], landmarks[0][1])

            # Adjust the position of the text (e.g., move it closer to the hand by subtracting from Y)
            text_offset_y = -500  # Adjust this value to move the text higher or lower
            hand_position_adjusted = (hand_position[0], hand_position[1] + text_offset_y)

            # show the prediction on the frame for each hand
            cv2.putText(frame, gesture, hand_position_adjusted, cv2.FONT_HERSHEY_SIMPLEX,
                        3, (0, 0, 255), 4, cv2.LINE_AA)

            if gesture == "call me" and not sound_played:
                mySoundController.play_sound()
                sound_played = True

            elif gesture == "stop" or gesture == "live long":
                mySoundController.stop_sound()
                sound_played = False
                
            elif gesture == "okay":
                mySoundController.pause_music()
                sound_played = False

            elif gesture == "smile" and not sound_played:
                mySoundController.unpause_music()
                sound_played = True

            elif gesture == "thumbs up":
                mySoundController.volume_up_music()

            elif gesture == "thumbs down":
                mySoundController.volume_down_music()

    cv2.imshow("Output", frame)

    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
capture.release()
cv2.destroyAllWindows()
