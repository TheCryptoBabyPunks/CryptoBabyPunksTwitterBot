import os
import logging
import requests
import emoji
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from config import Config, create_api
from opensea import OpenSeaAPI


logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logging.getLogger('apscheduler.executors.default').propagate = False

    
class PostTweet:
    
    def __init__(self, api):
        self.api=api

    def read_template(self, name):
        with open(Config.TEMPLATES_PATH + f'/{name}.txt', 'r') as file:
            return file.read()
        
    def find_acc(self, q, key):
        try: 
            acc = q[key]['user']['username']
            return ':ghost:' if acc==None else acc
        except: return ':ghost:'   

    def asset_name(self, q):
        try: 
            name = q['asset']['name']
            return 'A bundle' if name==None else name
        except: return 'A bundle'  
                         
    def successful(self, q):
        template = self.read_template('successful')
        txt = emoji.emojize(
        template.format(
            asset_name=self.asset_name(q),
            acc=self.find_acc(q, 'winner_account'),
            seller=self.find_acc(q, 'seller'),
            price='{0:.2f}'.format(round(float(q['total_price']
                    )/(1000000000000000000), 2)), 
            symbol=q['payment_token']['symbol'],
            permalink=q["asset"]["permalink"],
            collection_slug=q["collection_slug"]
            ))
        self.update(txt, q['asset']['image_url'])
        
    def offer_entered(self, q): 
        template = self.read_template('offer_entered')                 
        txt = emoji.emojize(
        template.format(
            acc=self.find_acc(q, 'from_account'),
            asset_name=self.asset_name(q),
            price='{0:.2f}'.format(round(float(q['bid_amount']
                    )/(1000000000000000000), 2)), 
            symbol=q['payment_token']['symbol'],
            permalink=q["asset"]["permalink"],
            collection_slug=q["collection_slug"]
        ))        
        self.update(txt, q['asset']['image_url'])
   
    def created(self, q):  
        template = self.read_template('created')         
        txt = emoji.emojize(
        template.format(
            acc=self.find_acc(q, 'from_account'),
            asset_name=self.asset_name(q),
            price='{0:.2f}'.format(round(float(q['ending_price']
                    )/(1000000000000000000), 2)),                
            symbol=q['payment_token']['symbol'],
            permalink=q["asset"]["permalink"],
            collection_slug=q["collection_slug"]
        ))      
        self.update(txt, q['asset']['image_url'])

    def update(self, txt, img):
        filename = '/temp.jpg'
        path = Config.FILE_PATH + filename
        request = requests.get(img, stream=True)
        if request.status_code == 200:
            with open(path, 'wb') as image:
                for chunk in request:
                    image.write(chunk)
            self.api.update_with_media(path, status=txt)
            os.remove(path)
        else:
            logger.info(f"{datetime.utcnow()}:unable to download image") 

sched = BlockingScheduler(timezone='utc')
@sched.scheduled_job('interval', id='main', minutes=Config.lag)
def main():
    occurred_before = datetime.utcnow().replace(microsecond=0)
    occurred_after = occurred_before - timedelta(minutes=Config.lag)
    query = app.events(
        Config.collection_slug, 
        occurred_after=occurred_after, 
        occurred_before=occurred_before)
    if not query['asset_events']==[]: # We must have something to work on!
        for q in query['asset_events']: # Several events? No problem!
            if not q["asset"]==None: # We don't do bundles here!
                if q['event_type']=='successful': # We focus on sales only!
                    try:
                        post.successful(q)
                        logger.info(f'{occurred_after}:{occurred_before}:{q["asset"]["name"]}:{q["event_type"]}:tweeted') 
                    except Exception as e:
                        logger.info(f'{occurred_after}:{occurred_before}:OOOPS! An issue has occured', exc_info=True)
                        raise e
                        continue
                else:
                     logger.info(f'{occurred_after}:{occurred_before}:{q["asset"]["name"]}:{q["event_type"]}:not_tweeted') 
            else:
                 logger.info(f'{occurred_after}:{occurred_before}:bundle:{q["event_type"]}:not_tweeted') 
    else:
         logger.info(f'{occurred_after}:{occurred_before}:no_events_found') 
                 
    
if __name__ == "__main__":
    
    api = create_api()
    app = OpenSeaAPI()
    post = PostTweet(api)
    sched.start()


