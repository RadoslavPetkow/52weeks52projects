import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

player1_name = input("Enter name for Player 1: ")
player2_name = input("Enter name for Player 2: ")

player1_score = 0
player2_score = 0

camera = cv2.VideoCapture(1, cv2.CAP_AVFOUNDATION)

if not camera.isOpened():
    print("Error: Could not access the camera.")
    exit()

print("Press 'q' to quit.")

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:
    round_active = False
    result_text = ""
    round_end_time = None

    while True:
        ret, frame = camera.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        gesture_player1 = None
        gesture_player2 = None

        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                landmarks = hand_landmarks.landmark
                wrist_x = landmarks[0].x

                if wrist_x < 0.5:
                    player = "Player 1"
                else:
                    player = "Player 2"

                fingertips = [4, 8, 12, 16, 20]
                finger_states = []
                for tip_id in fingertips:
                    if tip_id == 4:
                        finger_states.append(landmarks[tip_id].x < landmarks[tip_id - 1].x)
                    else:
                        finger_states.append(landmarks[tip_id].y < landmarks[tip_id - 2].y)

                gesture = "None"
                if all(state == False for state in finger_states):
                    gesture = "Rock"
                elif all(state == True for state in finger_states):
                    gesture = "Paper"
                elif finger_states[1] and not any(finger_states[2:]):
                    gesture = "Scissors"

                if player == "Player 1":
                    gesture_player1 = gesture
                else:
                    gesture_player2 = gesture

                wrist_x_pixel = int(landmarks[0].x * frame_width)
                wrist_y_pixel = int(landmarks[0].y * frame_height)

                cv2.putText(frame, f"{gesture}", (wrist_x_pixel, wrist_y_pixel - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        if gesture_player1 is not None and gesture_player2 is not None:
            if gesture_player1 != "None" and gesture_player2 != "None":
                if not round_active:
                    if gesture_player1 == gesture_player2:
                        result_text = "Tie!"
                    elif (gesture_player1 == "Rock" and gesture_player2 == "Scissors") or \
                         (gesture_player1 == "Paper" and gesture_player2 == "Rock") or \
                         (gesture_player1 == "Scissors" and gesture_player2 == "Paper"):
                        result_text = f"{player1_name} wins!"
                        player1_score += 1
                    else:
                        result_text = f"{player2_name} wins!"
                        player2_score += 1

                    round_active = True
                    round_end_time = time.time()
        if round_active:
            cv2.putText(frame, result_text, (int(frame_width / 2 - 200), 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

            if time.time() - round_end_time >= 5:
                round_active = False
                result_text = ""
                gesture_player1 = None
                gesture_player2 = None
                round_end_time = None

        cv2.putText(frame, f"{player1_name}: {player1_score}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Gesture: {gesture_player1}", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.putText(frame, f"{player2_name}: {player2_score}", (frame_width - 250, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Gesture: {gesture_player2}", (frame_width - 250, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Rock-Paper-Scissors Game", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()
