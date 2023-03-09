import tweepy
import requests
from bs4 import BeautifulSoup

# Enter your Twitter API keys
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Tweepy authentication process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create Tweepy API object
api = tweepy.API(auth)

# Scrape data from Kandilli website
response = requests.get('http://www.koeri.boun.edu.tr/scripts/lst8.asp')
html = response.text

# Parse HTML data
soup = BeautifulSoup(html, 'html.parser')
table = soup.find_all('table')[1]
rows = table.find_all('tr')

# Get latest earthquake information
earthquake = rows[2].find_all('td')
time = earthquake[0].text
lat = earthquake[1].text
lon = earthquake[2].text
depth = earthquake[3].text
mag = earthquake[4].text
place = earthquake[5].text

# Create tweet
tweet = f"Son deprem: {place}\nBüyüklük: {mag}\nDerinlik: {depth}\nKoordinatlar: {lat}, {lon}\nZaman: {time}"

# Send tweet
api.update_status(tweet)
