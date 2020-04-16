import os
from twython import Twython
from src.model import engine, Answered
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from src.storage import open_image

"""
loads environment variables of .env
"""
load_dotenv()

"""
ORM configurations
"""
Session = sessionmaker(bind=engine)
session = Session()

"""
Config access to Twitter API
"""
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')
images_path = os.getenv('images_path')
conn = engine.connect()

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


def post_in_twitter(tweet_id, text='', ):
    """
    Create a new tweet
    :param tweet_id: id string of Tweet to answer
    :param text: text to include in the Tweet
    """
    response = twitter.upload_media(media=open_image())
    twitter.update_status(
        status=text, in_reply_to_status_id=tweet_id, media_ids=[response['media_id']])


def salve_answer(id_tweet):
    """
    Save id of tweet answered
    :param id_tweet: string id of tweet
    """
    answered = Answered(id_tweet=id_tweet)
    session.add(answered)
    session.commit()


def tweet_answered(id_tweet):
    """
    checks if the tweet has been answered
    :param id_tweet: string id of tweet
    :return: bool
    """
    query = session.query(Answered).filter_by(id_tweet=id_tweet)
    if query.count() > 0:
        return True
    return False


def search():
    """
    Find the last 20 tweets which the bot was mentioned
    and answers those that have not been answered
    :return:
    """
    results = twitter.get_mentions_timeline()

    for result in results:
        id_post = result['id_str']

        if tweet_answered(id_post):
            continue

        post_in_twitter(id_post)
        salve_answer(id_post)
