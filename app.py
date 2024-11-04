from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    app.logger.info(f'User input: {user_input}')
    return f'Thank you! You entered: {user_input}'

if __name__ == '__main__':
    app.run(debug=True)