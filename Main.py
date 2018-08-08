# the standard function calls
import tweepy

#learn more: https://python.org/pypi/tweepy
#tweepy setup
consumer_key = "# # # # #"
consumer_secret = '# # # # #'
access_token = '# # # # #'
access_token_secret = '# # # # #'

#more tweepy setup
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#function inputs a letter code and spits back out the following:
#WMATA Code (Ex. A01) - False - or "AC: Station (Code) or Station (Code)
def letterCodeTranslation(letterCode):
    if letterCod
# Main function to make wmata calls
def stationRequest(stationCode):
    import requests
    data = requests.get(
        'https://api.wmata.com/StationPrediction.svc/json/GetPrediction/%s?api_key=b01353b50cf94b9b91f5e03d96c974fc' % stationCode)
    #process json
    dataA = data.json()
    print(dataA)
    for Trains in dataA['Trains']:
        print(Trains['DestinationName'], Trains['Line'], Trains['Min'])

#manages the stream listner
myStreamListener = BotStreamer()
# Construct the Stream instance
stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=['@WmataBot'])

class BotStreamer(tweepy.StreamListener):
    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        print(status)
        username = status.user.screen_name
        print(username)
        print(status.text)
        statusText = status.text

myStreamListener = BotStreamer()
# Construct the Stream instance
stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=['@WmataBot'])
