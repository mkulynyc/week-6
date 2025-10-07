# Imports
import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Setting up access to mk.env to get access token
load_dotenv(dotenv_path="mk.env")


# Genius API interaction class
class Genius:

    def __init__(self, access_token=None):
        '''
        Function to initialize the Genius API client.
        If no access_token is provided, it will look for ACCESS_CODE in environment variables.

        Parameters:
        access_token (str): The access token for the Genius API.

        Returns:
        None

        '''

        # Use token from env if not passed directly
        self.access_token = access_token or os.getenv("ACCESS_CODE")
        self.base_url = https://api.genius.com
        self.headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

    