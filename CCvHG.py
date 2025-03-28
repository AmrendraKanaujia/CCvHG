# Cursor Movement by Hand Gesture by Amrendra Kumar Kanaujia @amrendrakanaujia

# Gesture Info:
# Always start with neutral pose ie all 4 fingers and thumb is up and open ie show full palm.
# Cursor: Cursor will move according to thumb tip.
# Left click: When index finger is down than thumb.
# Right click: When mid finger is down than thumb.
# Scroll up: When thumb tip and ring finger tip is touched.
# Scroll down: When thumb tip and little finger tip is touched.
# No two or more finger should down at same time.
# One needs some practice to use cursor control correctly and precisely.
# Thanks to Python and it's various libraries and tutorials for this project.

# Importing Files
import cv2 # For camera and recording
import mediapipe as mp # Hand recognition and landmarks drawing
import pyautogui as pag # Automation
import os # Checking file path
import pygame # For playing sound
import tkinter as tk # GUI
from tkinter import messagebox # For quit dialog box
import threading # For threading
import webbrowser # For opening web link

# Main Class
class MainApp:

    # GUI using tkinter (Main) (Constructor)
    # Main GUI Constructor
    def __init__(self):

        self.running = False

        self.root = tk.Tk()
        self.root.title("Cursor Control via Hand Gesture App")
        # self.root.geometry("1200x850")
        self.root.configure(bg="#d4f1f4")

        # Add an icon for the application
        # icon_path = "ccvhgicon.ico" # For Exe.
        icon_path = r"Source_Code\ccvhgicon.ico"
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)
        else:
            print(f"Icon file not found: {icon_path}. Using default icon.")

        # For heading inside window and at top
        self.heading = tk.Label(self.root, text="Cursor Control via Hand Gesture", font=("Arial", 18, "bold"), bg="#d4f1f4", fg="black")
        self.heading.pack(padx=10, pady=10)

        # Start Button
        self.start_button = tk.Button(self.root, width=20, height=2, text=("Start"), font=("Arial", 18), bg="#189ab4", fg="white", command=self.start_cursor_control_program)
        self.start_button.pack(padx=10, pady=10)

        # On clicking start button then this text will be displayed
        self.start_button_text = tk.Text(self.root, font=("Arial", 14, "bold"), bg="#f8ea8c", fg="black", width=28, height=3)
        self.start_button_text.pack_forget()

        # When application is running/started then:
        self.running_text = tk.Text(self.root, font=("Arial", 14, "bold"), bg="#b4f8c8", fg="black", width=28, height=3)
        self.running_text.pack_forget()

        # Stop Button
        self.stop_button = tk.Button(self.root, width=20, height=2, text=("Stop"), font=("Arial", 18), bg="#189ab4", fg="white", command=self.stop_cursor_control_program)
        self.stop_button.pack(padx=10, pady=10)

        # On clicking stop button then this text will be displayed
        self.stop_button_text = tk.Text(self.root, font=("Arial", 14, "bold"), bg="#ffaebc", fg="black", width=28, height=3)
        self.stop_button_text.pack_forget()

        # Connect to Dev Button
        self.connect_to_dev = tk.Button(self.root, width=20, height=2, text=("Connect to Dev"), font=("Arial", 18),bg="#189ab4", fg="white", command=self.connect_func)
        self.connect_to_dev.pack(padx=10, pady=10)

        # Instruction Button
        self.instructions_button = tk.Button(self.root, width=20, height=2, text="Read Instructions", font=("Arial", 18), bg="#05445e", fg="white", command = self.toggle_instructions)
        self.instructions_button.pack(padx=10, pady=10)

        # Text inside instruction box
        self.instructions_text1 = tk.Text(self.root, font=("Calibri", 14, "bold"), bg="#05445e", fg="white", height=10, width=85)
        self.instructions_text1.insert(tk.END, "Cursor movement by hand gesture by Amrendra Kumar Kanaujia @amrendrakanaujia\n\n")

        self.instructions_text1.insert(tk.END, "Gesture Instructions/How to use:\n")
        self.instructions_text1.insert(tk.END, "1. Always start with neutral pose i.e all 4 fingers and thumb is up and open i.e show full palm.\n")
        self.instructions_text1.insert(tk.END, "2. Cursor: Cursor will move according to thumb tip.\n" )
        self.instructions_text1.insert(tk.END, "3. Left Click: When index fingertip is more down than thumb tip.\n")
        self.instructions_text1.insert(tk.END, "4. Right Click: When mid fingertip is more down than thumb tip.\n")
        self.instructions_text1.insert(tk.END, "5. Scroll Up: When ring fingertip and thumb tip is touched.\n")
        self.instructions_text1.insert(tk.END, "6. Scroll Down: When little finger and thumb tip is touched.\n")
        self.instructions_text1.insert(tk.END, "7. No two or more finger must down at same time or touched to thumb simulatenously.")
        self.instructions_text1.pack_forget()

        # Error Box
        self.error_text = tk.Text(self.root, font=("Arial", 14, "bold"), bg="red", fg="black", width=42, height=3)
        self.error_text.pack_forget()

        # For calling closing dialog box
        self.root.protocol("WM_DELETE_WINDOW", self.closing_box) # closing dialogbox
        self.root.mainloop()

    # GUI Button Command Functions:
    # Read Instructions Button Fuction
    def toggle_instructions(self):
        if not self.instructions_text1.winfo_viewable():

            # self.start_button_text.pack_forget()
            # self.running_text.pack_forget()
            # self.stop_button_text.pack_forget()
            # self.error_text.pack_forget()

            self.instructions_text1.pack(padx=10, pady=10)
            self.instructions_button.config(text="Hide Instructions")
        else:
            self.instructions_text1.pack_forget()
            self.instructions_button.config(text="Show Instructions")

    # Start Button Function
    # GUI and Threading: Using thread to run GUI and main cursor control logic simultaneously
    def start_cursor_control_program(self):
        if not self.running:
            self.running_text.pack_forget()
            self.stop_button_text.pack_forget()
            self.error_text.pack_forget()
            # self.instructions_text1.pack_forget()

            self.start_button_text.delete("1.0", tk.END)
            self.start_button_text.insert(tk.END, "\n Application starting...\n")
            self.start_button_text.pack(padx=10, pady=10)

            self.running = True
            self.second_thread = threading.Thread(target=self.main_cursor_control_logic)
            self.second_thread.start()
           
    # Main Program Logic
    def main_cursor_control_logic(self):
        
        # Initialize pygame mixer
        pygame.mixer.init()

        #sound file
        # r = Raw String: treats \ as normal character not as escape character.
        # file_path = r"C:\Users\amren\Documents\BCA Minor Project\Sound_Files\mouse_click_sound.mp3"

        # file_path = "ccvhg_sound.mp3" # For Exe.
        file_path = r"Source_Code\ccvhg_sound.mp3"
        if not os.path.exists(file_path):
            self.running = False
            self.start_button_text.pack_forget()
            self.running_text.pack_forget()
            self.stop_button_text.pack_forget()
            # self.instructions_text1.pack_forget()

            self.error_text.delete("1.0", tk.END)
            self.error_text.insert(tk.END, "\n Error Occured! Application coudn't be started.\n")
            self.error_text.pack(padx=10, pady=10)
            raise FileNotFoundError(f"File not found: {file_path}")

        
        # click_sound = pygame.mixer.Sound("ccvhg_sound.mp3") # For Exe.
        click_sound = pygame.mixer.Sound(r"Source_Code\ccvhg_sound.mp3")

        mp_hands = mp.solutions.hands  # Hands detection module
        mp_drawing = mp.solutions.drawing_utils  # Drawing utilities to overlay landmarks

        #accesing screen cordinates
        screen_w, screen_h = pag.size()
        #printing coordinates
        print('The Screen width:', screen_w)
        print('The Screen height:', screen_h)

        cap = cv2.VideoCapture(0)  # Start video capture from 
        if not cap.isOpened():
            self.running = False
            self.start_button_text.pack_forget()
            self.running_text.pack_forget()
            self.stop_button_text.pack_forget()
            # self.instructions_text1.pack_forget()

            self.error_text.delete("1.0", tk.END)
            self.error_text.insert(tk.END, "\n Error Occured! Application coudn't be started.\n")
            self.error_text.pack(padx=10, pady=10)

        with mp_hands.Hands(
                static_image_mode=False,       # Set to False for video input
                max_num_hands=1,               # Maximum number of hands to detect
                min_detection_confidence=0.5,  # Detection confidence threshold
                min_tracking_confidence=0.5) as hands:
            
            # self.running = True
            while self.running and cap.isOpened():
                ret, flip_frame = cap.read()  # Capture a single frame
                frame = cv2.flip(flip_frame, 1)
                if not ret:
                    # print("Failed to grab frame")
                    self.running = False
                    self.start_button_text.pack_forget()
                    self.running_text.pack_forget()
                    self.stop_button_text.pack_forget()
                    # self.instructions_text1.pack_forget()

                    self.error_text.delete("1.0", tk.END)
                    self.error_text.insert(tk.END, "\n Error Occured! Application coudn't be started.\n")
                    self.error_text.pack(padx=10, pady=10)
                    break

                # Convert the image to RGB as MediaPipe requires it
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Process the frame and detect hands
                results = hands.process(rgb_frame)

                # Check if hands are detected
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        # Draw landmarks on each detected hand
                        mp_drawing.draw_landmarks(
                            image=frame,
                            landmark_list=hand_landmarks,
                            connections=mp_hands.HAND_CONNECTIONS,
                            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 255), circle_radius=2 ),
                            connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=1 )
                            )
                        
                        #accesing thumb tip's coordinates: 4
                        thumb_tip = hand_landmarks.landmark[4]

                        #converting to screen coordinates
                        # Set a margin for the camera frame
                        margin_ratio = 0.1  # Maps 80% of camera view to full screen
                        # x_margin = screen_w * margin_ratio
                        # y_margin = screen_h * margin_ratio

                        # Scale hand position within these margins
                        thumb_tip_x = ((thumb_tip.x - margin_ratio) / (1 - 2 * margin_ratio)) * screen_w
                        thumb_tip_y = ((thumb_tip.y - margin_ratio) / (1 - 2 * margin_ratio)) * screen_h

                        
                        #move cursor acc to 4
                        pag.moveTo(thumb_tip_x, thumb_tip_y, duration=0.05)

                        #accesing indexfin_tip's coordinate: 8
                        indexfin_tip = hand_landmarks.landmark[8]
                        #converting to screen coordinates
                        indexfin_tip_y = ((indexfin_tip.y - margin_ratio) / (1 - 2 * margin_ratio)) * screen_h
                        # indexfin_tip_y = (indexfin_tip.y * screen_h)

                        #condition for left click
                        left_click_diff = abs(thumb_tip_y - indexfin_tip_y)
                        print("left diff:", left_click_diff)
                        if left_click_diff < 60:
                            pag.click(x=thumb_tip_x, y=thumb_tip_y, clicks=1, interval=0.5, button='left', duration=0.0)
                            print('Diff:', left_click_diff, "Left Key Clicked")
                            click_sound.play()

                        #accesing midfin_tip's coordinate: 12
                        midfin_tip = hand_landmarks.landmark[12]
                        #converting to screen coordinates
                        midfin_tip_y = ((midfin_tip.y - margin_ratio) / (1 - 2 * margin_ratio)) * screen_h
                        # midfin_tip_y = (midfin_tip.y * screen_h)

                        #condition for left click
                        right_click_diff = abs(thumb_tip_y - midfin_tip_y)
                        print('Right Diff:', right_click_diff)
                        if right_click_diff < 40:
                            pag.click(x=thumb_tip_x, y=thumb_tip_y, clicks=1, interval=0.5, button='right', duration=0.0)
                            print('Diff:', right_click_diff, "Right Key Clicked")
                            click_sound.play()

                        #accesing ringfin_tip's coordinate: 16
                        ringfin_tip = hand_landmarks.landmark[16]
                        #converting to screen coordinates
                        ringfin_tip_y = ((ringfin_tip.y - margin_ratio) / (1 - 2 * margin_ratio)) * screen_h
                        # ringfin_tip_y = (ringfin_tip.y * screen_h)

                        #condition for scroll up
                        ringfin_diff = abs(thumb_tip_y - ringfin_tip_y)
                        print('Ring fingure Diff:', ringfin_diff)
                        if ringfin_diff < 40:
                            pag.scroll(100)
                            print('Diff:', ringfin_diff, "Scroll Up")
                            click_sound.play()

                        #accesing pinkfin_tip's coordinate: 20
                        pinkfin_tip = hand_landmarks.landmark[20]
                        #converting to screen coordinates
                        pinkfin_tip_y = ((pinkfin_tip.y - margin_ratio) / (1 - 2 * margin_ratio)) * screen_h
                        # pinkfin_tip_y = (pinkfin_tip.y * screen_h)

                        #condition for scroll down
                        pinkfin_diff = abs(thumb_tip_y - pinkfin_tip_y)
                        print('Pinky fingure Diff:', pinkfin_diff)
                        if pinkfin_diff < 40:
                            pag.scroll(-100)
                            print('Diff:', pinkfin_diff, "Scroll down")
                            click_sound.play()
                        
                        if left_click_diff < 60 and right_click_diff < 40:
                            print("Use Error: Both Index finger and Mid finger can't be closed to thumb at same time. ")
                        

                # Display the output frame with hand landmarks
                cv2.imshow('Hand Detection', frame)

                if self.running:
                    self.start_button_text.pack_forget()
                    self.stop_button_text.pack_forget()
                    self.error_text.pack_forget()
                    # self.instructions_text1.pack_forget()

                    self.running_text.delete("1.0", tk.END)
                    self.running_text.insert(tk.END, "\n Application running.\n")
                    self.running_text.pack(padx=10, pady=10)

                # Break the loop if 'q' key is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                   break

        # Release resources
        cap.release()
        cv2.destroyAllWindows()


    # GUI
    def stop_cursor_control_program(self):
        if self.running:
            self.running = False

            self.start_button_text.pack_forget()
            self.running_text.pack_forget()
            self.error_text.pack_forget()
            # self.instructions_text1.pack_forget()

            self.stop_button_text.delete("1.0", tk.END)
            self.stop_button_text.insert(tk.END, "\n Application stopped.\n")
            self.stop_button_text.pack(padx=10, pady=10)

    # GUI
    def connect_func(self):
        webbrowser.open("https://linktr.ee/amrendrakanaujia")

    # GUI
    def closing_box(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"): #yes is presses = true
            self.running = False
            self.root.destroy()
        
# Object Creation
app = MainApp()

# PyInstaller CMD command
# pyinstaller --noconfirm --noconsole --icon="ccvhgicon.ico" --add-data "ccvhg_sound.mp3;." CCvHG.py


