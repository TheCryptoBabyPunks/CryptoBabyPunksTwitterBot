import requests

class OpenSeaAPI:   
    
    def __init__(self):
        self.path = "https://api.opensea.io/api/v1/"
        
    def events(self, collection_slug, **kwargs):
        url = self.path + 'events'
        querystring = {
            "collection_slug":f"{collection_slug}",
            "offset":"0",
            "limit":"50"
        }
        querystring.update(kwargs)
        response = requests.request("GET", url, params=querystring)
        return response.json()   
    
    def assets(self, token_ids, **kwargs):
        url = self.path + 'assets'
        querystring = {
            "token_ids":f"{token_ids}",
            "order_direction":"desc",            
        }
        querystring.update(kwargs)
        response = requests.request("GET", url, params=querystring)
        return response.json()  