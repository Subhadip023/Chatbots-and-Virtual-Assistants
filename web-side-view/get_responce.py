

# from sklearn.preprocessing import LabelEncoder

# import joblib

# label_encoder = LabelEncoder()

# classifier = joblib.load('model.pkl')
# def get_chatbot_response(user_input):
#     # Preprocess user input
#     user_input = [user_input]


#     # Predict intent using the trained model
#     predicted_class = classifier.predict(user_input)

#     # Convert the predicted class back to the original label
#     label_encoder.fit([key for key in responses.keys()])

#     predicted_intent = label_encoder.inverse_transform(predicted_class)

#     # Get the response based on the recognized intent
#     response = responses.get(predicted_intent[0], 'Sorry, I couldn\'t understand. Please try again.')

#     return response
import joblib
import tensorflow_hub as hub

def load_chatbot_model(model_path, encoder_model_url):
    # Load the trained model
    loaded_model = joblib.load(model_path)

    # Load Universal Sentence Encoder model
    encoder_model = hub.load(encoder_model_url)

    return loaded_model, encoder_model

def preprocess_input(encoder_model, text):
    encoded_text = encoder_model([text])[0]
    return encoded_text

def get_chatbot_response(user_input, loaded_model, encoder_model, response_mapping):
    # Preprocess user input
    preprocessed_input = preprocess_input(encoder_model, user_input)

    # Use the model to predict the intent
    predicted_intent = loaded_model.predict([preprocessed_input])

    # Map predicted intent to a response
    response = response_mapping.get(predicted_intent[0], "I'm sorry, I couldn't understand. Please try again.")

    return response

# Define paths and URLs
model_path = "model/model.pkl"
encoder_model_url = 'https://tfhub.dev/google/universal-sentence-encoder/4'

# Load the chatbot model and encoder
loaded_model, encoder_model = load_chatbot_model(model_path, encoder_model_url)




responses = {
    'cancel_order': 'Your order has been canceled successfully.',
    'complaint': 'We apologize for the inconvenience. Please provide more details, and we will assist you.',
    'contact_customer_service': 'You can contact our customer service at 1-800-XXX-XXXX.',
    'contact_human_agent': 'I am sorry, but I am just a virtual assistant. For more personalized assistance, please contact our customer service and ask to speak with a human agent.',
    'create_account': 'To create a new account, please visit our website and click on the \'Sign Up\' button. Follow the instructions to complete the registration process.',
    'change_order': 'If you need to make changes to your order, please contact our customer service as soon as possible. We\'ll do our best to accommodate your request.',
    'change_shipping_address': 'To update your shipping address, log in to your account and navigate to the \'My Account\' section. From there, you can edit your shipping information.',
    'check_cancellation_fee': 'To check the cancellation fee for your order, please refer to our website\'s cancellation policy or contact our customer service for more details.',
    'check_invoices': 'To view your invoices, log in to your account and go to the \'Invoices\' section. There, you can access and download your billing history.',
    'check_payment_methods': 'You can check the available payment methods during the checkout process on our website. We accept credit cards, debit cards, and PayPal.',
    'check_refund_policy': 'To understand our refund policy, please visit our website\'s refund policy page. If you have any specific questions, feel free to contact our customer service.',
    'delete_account': 'To delete your account, please contact our customer service and request an account deletion. We\'ll guide you through the process.',
    'delivery_options': 'We offer various delivery options, including standard shipping, express delivery, and same-day delivery. You can choose the one that best suits your needs during the checkout process.',
    'delivery_period': 'The delivery period depends on your location and the chosen delivery option. You will receive an estimated delivery date during the checkout process.',
    'edit_account': 'To edit your account information, log in to your account and navigate to the \'My Account\' section. From there, you can update your personal details.',
    'get_invoice': 'To get a copy of your invoice, log in to your account and visit the \'Invoices\' section. There, you can download and print your invoices.',
    'get_refund': 'To request a refund, please contact our customer service and provide the necessary order details. We\'ll process your refund as per our refund policy.',
    'newsletter_subscription': 'To subscribe to our newsletter, go to our website\'s newsletter subscription page and enter your email address. You will receive updates and promotions via email.',
    'payment_issue': 'If you are facing any issues with your payment, please check your payment method and billing details. If the problem persists, contact our customer service for assistance.',
    'place_order': 'To place an order, add the desired items to your cart and proceed to checkout. Follow the instructions to complete your purchase.',
    'recover_password': 'If you forgot your password, go to the login page and click on the \'Forgot Password\' link. Follow the instructions to reset your password.',
    'registration_problems': 'If you encounter any problems during the registration process, please contact our customer service for help.',
    'review': 'We value your feedback. You can leave a review for our products or services on our website or contact our customer service to share your feedback directly.',
    'set_up_shipping_address': 'To set up your shipping address, log in to your account and navigate to the \'Shipping Address\' section. There, you can add or update your shipping information.',
    'switch_account': 'To switch between multiple accounts, log out of the current account and log in using the credentials of the account you want to switch to.',
    'track_order': 'To track your order, log in to your account and go to the \'Order Tracking\' section. There, you can see the status and progress of your order.',
    'track_refund': 'To track the status of your refund, log in to your account and visit the \'Refunds\' section. There, you can see the details of your refund process.',
    # Add more responses for other intents
}

if __name__ == '__main__':
    # Example user input
    user_input = "How can I track my order?"
    
    # Get the chatbot response
    response = get_chatbot_response(user_input, loaded_model, encoder_model, responses)
    
    print("Chatbot Response:", response)