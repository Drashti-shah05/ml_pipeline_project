from flask import Flask
from src.logger import logging 
from src.exception import CustomException
import os, sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception("Testing")
    except Exception as e:
        custom_error = CustomException(e, sys)
        logging.info(custom_error) 
        return "Hello world Welcome"

if __name__ == "__main__":
    app.run(debug=True)
