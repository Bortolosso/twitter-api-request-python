import requests


bearer_token = "AAAAAAAAAAAAAAAAAAAAAC%2BuiAEAAAAAEXHv%2FGRK8jhBtxhSHMDZG2%2Br6JE%3D5JzVX6Wtg71etvSr4DYHgHh9mKk9JDdIumNO2Avi2RWs33Qe1j"


def create_url(find):
    url = "https://api.twitter.com/1.1/search/tweets.json?q={0}&count=100&result_type=recent".format(find)
    
    return url


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
        
    return response.json()


def main(find):
    url = create_url(find)
    json_response = connect_to_endpoint(url)
    
    return json_response['search_metadata']