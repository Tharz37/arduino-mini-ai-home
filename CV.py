import cv2
import mediapipe as mp
import serial
import time
import math

# Serial setup
ser = serial.Serial('COM3', 9600)  # Change COM port accordingly
time.sleep(2)

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Track device state
active_device = None

def calculate_distance(lm1, lm2):
    return math.hypot(lm2.x - lm1.x, lm2.y - lm1.y)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm = hand_landmarks.landmark

            # Get tip positions
            fingers = [lm[4], lm[8], lm[12], lm[16], lm[20]]

            # Gesture logic
            thumb_tip = lm[4]
            index_tip = lm[8]
            middle_tip = lm[12]

            # Open palm: LED ON
            if all(f.y < lm[0].y for f in fingers[1:]):
                ser.write(b'L_ON\n')
                active_device = 'LED'

            # Closed fist: LED OFF
            elif all(f.y > lm[0].y for f in fingers[1:]):
                ser.write(b'L_OFF\n')
                active_device = None

            # Thumbs up: Buzzer ON
            elif thumb_tip.y < lm[3].y and index_tip.y > lm[6].y:
                ser.write(b'B_ON\n')
                active_device = 'BUZZER'

            # Thumbs down: Buzzer OFF
            elif thumb_tip.y > lm[3].y and index_tip.y > lm[6].y:
                ser.write(b'B_OFF\n')
                active_device = None

            # Victory: Fan ON
            elif index_tip.y < lm[6].y and middle_tip.y < lm[10].y and lm[16].y > lm[14].y:
                ser.write(b'F_ON\n')
                active_device = 'FAN'

            # One finger up: Fan OFF
            elif index_tip.y < lm[6].y and middle_tip.y > lm[10].y:
                ser.write(b'F_OFF\n')
                active_device = None

            # Intensity control when device is active
            if active_device:
                pinch_dist = calculate_distance(index_tip, thumb_tip)
                intensity = int(min(max(pinch_dist * 200, 0), 255))
                cmd = f"{active_device[0]}_{intensity}\n"
                ser.write(cmd.encode())

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Mini AI Home", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
