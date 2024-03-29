import requests
import streamlit as st
import time


def run_prediction(file, operation=None, parameters=None, test=False):
    """
    This function takes a file as input, sends it to the Truedocs API, and returns a prediction
    """
    if test:
        time.sleep(2)
        return {
            "prediction": {
                "documentType": "test",
                "entity": "The Testing Company",
                "confidence": 0.8246,
            }
        }

    api_endpoint = f"{st.secrets['truedocs_api_url']}/{operation}"
    headers = {"X-Api-Key": st.secrets["truedocs_api_key"]}

    files = [("document", file)]

    # Send the file to the API and get the response
    response = requests.post(
        api_endpoint, headers=headers, data=parameters, files=files
    )

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        return response.json()
    else:
        # If the request was not successful, raise an exception
        raise Exception(
            "Truedocs API request failed with status code " + str(response.status_code)
        )
