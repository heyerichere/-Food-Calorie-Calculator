from flask import Flask, request, jsonify
import twilio.twiml.messaging_response

app = Flask(__name__)

# Create an empty dictionary to store user data
user_data_cache = {}

@app.route('/sms', methods=['POST'])
def receive_sms():
    # Get the incoming SMS message
    incoming_message = request.values.get('Body', '').strip()
    phone_number = request.values.get('From', '').strip()

    # Check if the user is already registered
    if phone_number in user_data_cache:
        # Check if we've already asked for the name
        if 'name' in user_data_cache[phone_number]:
            # Check if we've already asked for wage/salary
            if 'wage' in user_data_cache[phone_number]:
                response_message = "Your data is already recorded."
            else:
                response_message = "Great! Now, please provide your annual wage."
        else:
            # This is the initial prompt for new users
            response_message = "Welcome to Wellfare! Please provide your First and Last name to sign up."
    else:
        # This is the initial prompt for new users
        response_message = "Welcome to our website! Please provide your First and Last name to sign up."
        

    # Update or record user data based on the conversation flow
    if 'name' not in user_data_cache.get(phone_number, {}):
        user_data_cache.setdefault(phone_number, {})['name'] = incoming_message
    elif 'wage' not in user_data_cache.get(phone_number, {}):
        user_data_cache.setdefault(phone_number, {})['wage'] = incoming_message

    # Create a TwiML response
    response = twilio.twiml.messaging_response.MessagingResponse()
    response.message(response_message)

    return str(response)

@app.route('/user_data', methods=['GET'])
def get_user_data():
    # Return the user data stored in the dictionary as JSON
    return jsonify(user_data_cache)

if __name__ == '__main__':
    app.run(debug=True)
