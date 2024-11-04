# Flask User Input Logger

This is a simple Flask web application that allows users to enter text through a form. The entered text is then logged to a file on the server.

## Features

- A web form for user input
- Logs user input to a file (`user_input.log`)

## Requirements

- Python 3.x
- Flask

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd flask_project
   ```

2. **Create a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**
   ```sh
   pip install Flask
   ```

## Running the Application

1. **Start the Flask application:**
   ```sh
   python app.py
   ```

2. **Open your web browser and navigate to:**
   ```
   http://127.0.0.1:5000/
   ```

3. **Enter text in the form and submit it.**

## Logging

- User input is logged to a file named `user_input.log` in the same directory as `app.py`.

## File Structure

```
flask_project/
│
├── 

app.py


├── templates/
│   └── index.html
├── 

user_input.log


└── venv/
```

## app.py

This file contains the main Flask application. It sets up a route for the home page and a route to handle form submissions. User input is logged to `user_input.log`.

## templates/index.html

This file contains the HTML template for the home page. It includes a form where users can enter text.

## user_input.log

This file contains the logged user inputs.

## License

This project is licensed under the MIT License.