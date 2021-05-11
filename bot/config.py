import os
import os.path as op
import tweepy
import logging

logger = logging.getLogger()

class Config:  
    # Twitter
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
        
    # local
    FILE_PATH = op.join(op.dirname(__file__), '../files')
    TEMPLATES_PATH = op.join(op.dirname(__file__), '../templates')
    
    # OpenSea (OS) params
    collection_slug = 'cryptobabypunks'
    
    # BlockingScheduler params
    lag = 15 # minutes
    

def create_api():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(Config.CONSUMER_KEY, Config.CONSUMER_SECRET)
    auth.set_access_token(Config.ACCESS_TOKEN, Config.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api