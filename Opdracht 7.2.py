import time
import keyboard

regelnummer = 1

print("Druk op de ESC-toets om de loop te stoppen.")

while True:
    print(f"{regelnummer} Dit is mijn tweede Loop in Python.")
    time.sleep(0.5)
    regelnummer += 1

    if keyboard.is_pressed('esc'):
        print("gestopt!")`
        break
