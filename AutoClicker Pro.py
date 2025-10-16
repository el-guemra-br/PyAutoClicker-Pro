import pyautogui
import time
import keyboard

 
timer = int(input("Enter the duration in seconds before starting the automatic click: "))

 
click_duration = float(input("Enter the duration of the click in milliseconds(1s=1000ms): "))/1000.0 

 
running = True

 
def click_mouse(duration):
	pyautogui.mouseDown()
	time.sleep(duration)
	pyautogui.mouseUp()

nClick = 1

 
def toggle_running():
	global running
	running = not running
	if running:
		print("Play")
	else:
		print("Pause")


def stop_program():
	print("Stopping the program")
	exit()




print(f"Waiting for {timer} seconds before starting the automatic click...")
time.sleep(timer)


while True:
	if running:
		click_mouse(click_duration)
		print('  CLICK n:', nClick )
		nClick=nClick+1


keyboard.add_hotkey('shift+p', toggle_running)


keyboard.add_hotkey('esc', stop_program)


time.sleep(click_duration) 



