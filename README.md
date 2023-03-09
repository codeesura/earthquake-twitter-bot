# Twitter Earthquake Bot

This is a Python script that retrieves the latest earthquake data from Kandilli Observatory and Earthquake Research Institute (KOERI) website and tweets the information using the Twitter API.

## Requirements

This script requires the following Python libraries:

- `tweepy`: To interact with the Twitter API.
- `requests`: To send HTTP requests and receive responses.
- `BeautifulSoup`: To parse HTML content.

You can install these libraries using pip:

```
pip install tweepy requests beautifulsoup4
```

## Setup

To use this script, you need to have a Twitter Developer Account and create an application to get the API keys and access tokens required for authentication.

You can follow these steps to get your Twitter API credentials:

1- Go to the Twitter [Developer Portal](https://developer.twitter.com/en/portal/dashboard).

2- Log in with your Twitter account.

3- Create a new Project and give it a name.

4- Create a new App inside the Project and give it a name.

5- Go to the "Keys and Tokens" tab and generate your Consumer Keys and Access Tokens.

6- Copy your Consumer Keys and Access Tokens and paste them in the script.

```Python
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Tweepy authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Tweepy API object
api = tweepy.API(auth)
```

## Usage

You can run the script by running the following command in your terminal:

```bash
python twitter_earthquake_bot.py
````

The script will retrieve the latest earthquake data from KOERI website, parse the HTML content, and tweet the information using the Twitter API.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the LICENSE file for details.
