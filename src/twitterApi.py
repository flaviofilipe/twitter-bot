import os
import random
from twython import Twython
import datetime
import time
from model import engine, Aswered
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

Session = sessionmaker(bind=engine)
session = Session()

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

def post_in_twitter(text='', image=None, tweet_id=''):
    # This posts Tweets
    message = text if text else 'Mensagem Padrão 2!'
    message = f'{image} {message}'
    photo = open(get_random_image(), 'rb')
    response = twitter.upload_media(media=photo)
    twitter.update_status(
        status=message, in_reply_to_status_id=tweet_id, media_ids=[response['media_id']])
    print("Tweeted: %s" % message)
    # delay so that it doesn't look like the program is spamming Twitter


def get_random_image():

    for r, d, f in os.walk(images_path):
        images = f

    filename = f'{images_path}{random.choice(images)}'
    return filename


def search():

    # Default count=20
    results = twitter.get_mentions_timeline()
    now = datetime.date.today()
    now = str(now)
    now = now.replace("-", "")
    now = int(now)


    for result in results:
        id_post = result['id_str']
        name = result['user']
        creation_date = result['created_at']
        screen_name = name['screen_name']

        tweet_txt = result['text']
        if(tweet_aswered(id_post)):
            print(id_post)
            continue
        print('aquiii')
        salve_answer(id_post)
        # post_in_twitter(tweet_id=id_post)


def salve_answer(id_tweet):
    aswered = Aswered(id_tweet=id_tweet)
    session.add(aswered)
    session.commit()

def tweet_aswered(id_tweet):
    query = session.query(Aswered).filter_by(id_tweet=id_tweet)
    if(query.count() > 0): 
        return True
    return False

search()
