import time
from flask import Flask, render_template, request
import threading

app = Flask(__name__)

def cozy_glow():
    print("Starting Cozy Glow mood...")
    while True:
        print("Cozy Glow is active...")
        time.sleep(2)

def rainbow_wave():
    print("Starting Rainbow Wave mood...")
    while True:
        print("Cozy Rainbow Wave is active...")
        time.sleep(2)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/set_mood/<mood_name>')
def set_mood(mood_name):
    if mood_name == 'cozy':
        threading.Thread(target=cozy_glow).start()
        return "Cozy Glow selected!"
    elif mood_name == 'rainbow':
        threading.Thread(target=rainbow_wave).start()
        return "Rainbow Wave selected!"
    else:
        return "Mood not found"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)