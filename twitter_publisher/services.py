import tweepy

def publish_tweet(api_key, api_secret, access_token, access_token_secret, message):
    try:
        auth = tweepy.OAuth1UserHandler(
            api_key, api_secret, access_token, access_token_secret
        )
        api = tweepy.API(auth)
        api.update_status(message)
        return True
    except Exception as e:
        print(f"Error al publicar: {e}")
        return False
