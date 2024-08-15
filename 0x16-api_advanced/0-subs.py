#!/usr/bin/python3
"""Function to get the number of subscribers for a specified Reddit subreddit."""

import requests

def number_of_subscribers(subreddit):
    # Define the Reddit API URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set up custom headers to include a User-Agent
    headers = {
        'User-Agent': 'Custom User-Agent'
    }

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code is 200 OK
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the number of subscribers
            return data['data']['subscribers']
        else:
            # If not a successful response, return 0
            return 0
    except Exception as e:
        # Handle any exceptions that occur and return 0
        return 0
