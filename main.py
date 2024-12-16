import cv2
import mediapipe as mp
import pyautogui

mp_solution =  mp.solutions.hands
hand_detector = mp_solution.Hands( max_num_hands=1)
drawing_util = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

landmarks_drawing = drawing_util.DrawingSpec(color=(0,255,0), thickness=2 , circle_radius=5)
connection_marks = drawing_util.DrawingSpec(color=(255,0,0), thickness=4)

screen_width, screenheight = pyautogui.size()

indexfinger_cordinate = None
thumb_cordinate = None

ismoving = True

while True:
    _,frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    hands = hand_detector.process(rgb_frame)
        
    if hands.multi_hand_landmarks:
        for hand in hands.multi_hand_landmarks:
            drawing_util.draw_landmarks(frame, hand,mp_solution.HAND_CONNECTIONS, landmark_drawing_spec=landmarks_drawing, connection_drawing_spec=connection_marks)

            indexfinger = hand.landmark[8]
            x = int(indexfinger.x * screen_width)
            y = int(indexfinger.y * screenheight) 
       
            if ismoving==True:
                pyautogui.moveTo(x,y)
                indexfinger_cordinate = y

            thumb = hand.landmark[4]
            thumbx = int(thumb.x * screen_width)
            thumby = int(thumb.y * screenheight)
            thumb_cordinate = thumby 

            if indexfinger_cordinate is not None and thumb_cordinate is not None:  
                    if abs(indexfinger_cordinate - thumb_cordinate) < 20:
                        ismoving=False
                        pyautogui.click()
                        ismoving=True 
           

    cv2.imshow("Hand detector", frame)
    cv2.waitKey(1)