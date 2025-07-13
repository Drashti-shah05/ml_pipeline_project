from flask import Flask
from src.logger import logging 
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
import os, sys

app = Flask(__name__)


def index():
    return "✅ Hello! Flask app is running."

@app.route('/', methods=['GET'])
def ingest_data():
    try:
        obj = DataIngestion()
        train_path, test_path = obj.initiate_data_ingestion()
        logging.info("Ingestion Successful: Train - %s, Test - %s", train_path, test_path)
        return f"✅ Data Ingestion Completed.<br>Train Path: {train_path}<br>Test Path: {test_path}"
    except Exception as e:
        custom_error = CustomException(e, sys)
        logging.error(custom_error)
        return f"❌ Error during ingestion:<br>{custom_error}"

if __name__ == "__main__":
    app.run(debug=True)
