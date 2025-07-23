from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import json
from datetime import datetime

app = Flask(__name__)

sessions = {}  # Temporary state tracker per phone number

@app.route("/sms", methods=['POST'])
def sms_reply():
    from_number = request.form['From']
    message_body = request.form['Body'].strip()
    resp = MessagingResponse()

    if from_number in sessions:
        # We're expecting a to-do item from the user
        todo = message_body
        today = datetime.now().strftime("%Y-%m-%d")
        with open(f"todos_{from_number}.txt", "a") as f:
            f.write(f"{today}: {todo}\n")
        resp.message(f"Got it. Added to your list: {todo}")
        del sessions[from_number]

    elif message_body.upper().startswith("TODO:"):
        sessions[from_number] = True
        resp.message("What do you have to do tomorrow?")

    elif message_body.upper().startswith("SHOWTODO"):
        try:
            with open(f"todos_{from_number}.txt", "r") as f:
                items = f.read()
            resp.message(f"Your list:\n{items}")
        except FileNotFoundError:
            resp.message("You have no items yet.")
    else:
        resp.message("Send 'TODO:' to add a task or 'SHOWTODO' to view them.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
