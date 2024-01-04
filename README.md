# Demo app

A simple web app that allows users to upload a file and try out the Truedocs API.

## Running

1. Clone this repository to your local machine.
1. Navigate to the project directory in your terminal.
1. Create a python virtual environment and activate it with the following command `python -m venv .venv && source .venv/bin/activate`
1. Install the necessary Python packages by running `pip install -r requirements.txt`.
1. Copy the .streamlit/secrets_example.toml into .streamlit/secrets.toml and fill out the secret values.
1. Run the app by typing `streamlit run app.py` in your terminal.

## Usage

1. Once the app is running, navigate to the provided localhost URL in your web browser.
1. You will see a file uploader on the app's main page. Click on it to upload a file from your computer.
1. After you've selected a file, the app will automatically send it to the Truedocs API.
1. The app will display a loading spinner while it waits for the API to return the document class and metadata.
1. Once the API response is received, the app will display the prediction results on the page.
1. If there is an error during any part of this process, the app will display an error message.

## Notes

- The app is designed to handle one file upload at a time. If you want to analyze a different file, you will need to refresh the page and upload the new file.
- The app does not store any of the uploaded files or the results from the Document AI API. Once you refresh the page, the data is lost.
