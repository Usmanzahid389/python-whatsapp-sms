#import pywhatkit
import keyboard as k
import pyautogui
import time
import webbrowser as web
from flask import Flask, request, jsonify
from urllib.parse import quote

app = Flask(__name__)

def send_whatsapp(phone_number, message, x_cord=761, y_cord=884):
    msg = message.format("{name}")
    web.open(f"https://web.whatsapp.com/send?phone={phone_number}&text={quote(msg)}")
    time.sleep(15)  # adjust duration if required
    pyautogui.click(x_cord, y_cord)
    time.sleep(2)
    k.press_and_release('enter')
    time.sleep(2)
    k.press_and_release('ctrl+ w')
    time.sleep(1)
    print("Message sent..!!")


@app.route('/send_whatsapp_message', methods=['POST'])
def send_whatsapp_message():
    data = request.get_json()
    phone_number = data.get('phone_number')
    message = data.get('message')

    if not phone_number or not message:
        return jsonify({'error': 'Phone number and message are required.'}), 400

    send_whatsapp(phone_number, message)
    return jsonify({'message': 'Message sent successfully!'})


if __name__ == '__main__':
    app.run(debug=True)
