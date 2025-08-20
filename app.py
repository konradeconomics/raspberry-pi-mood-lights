import time
from flask import Flask, render_template, request
import threading

app = Flask(__name__)

stop_event = threading.Event()

current_mood_thread = None

def kill_current_mood():
    global current_mood_thread, stop_event

    if current_mood_thread and current_mood_thread.is_alive():
        print("Signaling current mood to stop...")
        stop_event.set()
        current_mood_thread.join()
        print("Current mood thread stopped.")
    
    stop_event.clear()


def cozy_glow():
    print("Starting Cozy Glow mood...")
    while not stop_event.is_set():
        print("Cozy Glow is active...")
        time.sleep(1)

    print("Cozy Glow thread received stop signal. Exiting gracefully.")


def rainbow_wave():
    print("Starting Rainbow Wave mood...")
    while not stop_event.is_set():
        print(" Rainbow Wave is active...")
        time.sleep(1)

    print("Rainbow Wave thread received stop signal. Exiting gracefully.")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/set_mood/<mood_name>')
def set_mood(mood_name):
    global current_mood_thread

    kill_current_mood()

    if mood_name == 'cozy':
        current_mood_thread = threading.Thread(target=cozy_glow)
        current_mood_thread.start()
        return "Cozy Glow selected!"
    elif mood_name == 'rainbow':
        current_mood_thread = threading.Thread(target=rainbow_wave)
        current_mood_thread.start()
        return "Rainbow Wave selected!"
    elif mood_name == 'off':
        stop_event
        return "Turned off lights."
    else:
        return "Mood not found"
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

