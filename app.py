from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# Set up a separate logger for user inputs
user_input_logger = logging.getLogger('user_input_logger')
user_input_logger.setLevel(logging.INFO)
handler = logging.FileHandler('user_input.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
user_input_logger.addHandler(handler)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    user_input_logger.info(user_input)
    return f'Thank you! You entered: {user_input}'

if __name__ == '__main__':
    app.run(debug=True)