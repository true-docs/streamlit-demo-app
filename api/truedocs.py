import requests
import streamlit as st


def run_prediction(file, test=False):
    """
    This function takes a file as input, sends it to the Truedocs API, and returns a prediction
    """
    if test:
        return {
            "documentType": "test",
            "entity": "The Testing Company",
            "confidence": 0.8246
        }

    api_endpoint = f"{st.secrets['truedocs_api_url']}/classify"
    headers = {
        "X-Api-Key": st.secrets["truedocs_api_key"]
    }
    
    payload = {}
    files = [
        ('document', file)
    ]

    # Send the file to the API and get the response
    response = requests.post(api_endpoint, headers=headers, data=payload, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        response_json = response.json()
        p = response_json["prediction"]
        return p
    else:
        # If the request was not successful, raise an exception
        raise Exception("Truedocs API request failed with status code " + str(response.status_code))
