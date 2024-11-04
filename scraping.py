######################################################################################################################################
#  ____________________________    _____ __________.___ _______    ________  .___   _____  ________ __________   ____ ____  __.
# /   _____/\_   ___ \______   \  /  _  \\______   \   |\      \  /  _____/  |   | /     \ \______ \\______   \ /_   |    |/ _|
# \_____  \ /    \  \/|       _/ /  /_\  \|     ___/   |/   |   \/   \  ___  |   |/  \ /  \ |    |  \|    |  _/  |   |      <  
# /        \\     \___|    |   \/    |    \    |   |   /    |    \    \_\  \ |   /    Y    \|    `   \    |   \  |   |    |  \ 
#/_______  / \______  /____|_  /\____|__  /____|   |___\____|__  /\______  / |___\____|__  /_______  /______  /  |___|____|__ \
#        \/         \/       \/         \/                     \/        \/              \/        \/       \/               \/
#######################################################################################################################################
#@felzosqrt
################################################
#IDEA: Access the site for the top 1,000 movies. 
#Check the headers under the Fetch/XHR section.
#Identify the GET method (it retrieves the first 50 movies).
#Modify the request to fetch all 1,000 and send it to the backend URL.

import os 
from urllib.parse import urlunsplit, urlencode, quote
import json
import requests
import pandas as pd

### backendURL
### dictionary of parametres from IMDB, operation is being called, when open page 
### top 1000 IMDB https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc

### Can be found in "response"
request_params = {
    "operationName": "AdvancedTitleSearch",
    "variables": {
        "after": "eyJlc1Rva2VuIjpbIjguNSIsIjk5OSIsInR0MDExMDM1NyJdLCJmaWx0ZXIiOiJ7XCJjb25zdHJhaW50c1wiOntcInJhbmtlZFRpdGxlTGlzdENvbnN0cmFpbnRcIjp7XCJhbGxSYW5rZWRUaXRsZUxpc3RzXCI6W3tcInJhbmtlZFRpdGxlTGlzdFR5cGVcIjpcIlRPUF9SQVRFRF9NT1ZJRVNcIixcInJhbmtSYW5nZVwiOntcIm1heFwiOjEwMDB9fV0sXCJleGNsdWRlUmFua2VkVGl0bGVMaXN0c1wiOltdfX0sXCJsYW5ndWFnZVwiOlwiZGUtREVcIixcInNvcnRcIjp7XCJzb3J0QnlcIjpcIlVTRVJfUkFUSU5HXCIsXCJzb3J0T3JkZXJcIjpcIkRFU0NcIn0sXCJyZXN1bHRJbmRleFwiOjQ5fSJ9",
        "first": 50,
        "locale": "de-DE",
        "rankedTitleListConstraint": {
            "allRankedTitleLists": [
                {
                    "rankRange": {
                        "max": 1000
                    },
                    "rankedTitleListType": "TOP_RATED_MOVIES"
                }
            ],
            "excludeRankedTitleLists": []
        },
        "sortBy": "USER_RATING",
        "sortOrder": "DESC"
    },
    "extensions": {
        "persistedQuery": {
            "sha256Hash": "60a7b8470b01671336ffa535b21a0a6cdaf50267fa2ab55b3e3772578a8c1f00",
            "version": 1
        }
    }
}

# variables after delete, since we want all 1k 
# note that key/value "after" is used to mark which page u on, if u want to scrape f.E. from 400-500 or so 
# request params is kind of 
#############################################################################################################

request_params = {
    "operationName": "AdvancedTitleSearch",
    "variables": json.dumps({
         "first": 1000,
        "locale": "de-DE",
        "rankedTitleListConstraint": {
            "allRankedTitleLists": [
                {
                    "rankRange": {
                        "max": 1000
                    },
                    "rankedTitleListType": "TOP_RATED_MOVIES"
                }
            ],
            "excludeRankedTitleLists": []
        },
        "sortBy": "USER_RATING",
        "sortOrder": "DESC"
    },separators=(',',':'), indent=0).replace('\n',''),

    "extensions": json.dumps({
        "persistedQuery": {
            "sha256Hash": "60a7b8470b01671336ffa535b21a0a6cdaf50267fa2ab55b3e3772578a8c1f00",
            "version": 1
        }
    },separators=(',',':'), indent=0).replace('\n','')
}


url = 'https://caching.graphql.imdb.com/?'

#we need to urlencode
#{"first":1000,"locale":"de-DE","sortBy":"USER_RATING","sortOrder":"DESC"}
#to
#%7B%22first%22%3A1000%2C%22locale%22%3A%22de-DE%22%2C%22sortBy%22%3A%22USER_RATING%22%2C%22sortOrder%22%3A%22DESC%22%7D
#if we wouldnt separate above line 70, whitespace, /n etc. would be also convertet in URL and we had different
#string, and server would not accept!

params = urlencode(request_params)


#This header informs the server that the client expects the response to be in JSON format. 
# It is a way to specify the desired media type of the response.
#Without this header, the server might return data in a different format 
# (e.g., XML or plain text), which may not be what your application can handle.

headers = {'Accept': 'application/json',
           'Content-Type': 'application/json'}

### our modified URL
urlvar = url + urlencode(request_params)

### GetData as JSON
response = requests.get(url=urlvar, headers=headers)


movie_data = response.json()
#print(movie_data)

#print(url + urlencode(request_params))

#print(quote("{\""))   

with open("movie_data.json", "w") as json_file:
    json.dump(movie_data, json_file)

#print(movie_data.keys())







""" # Annahme: movie_data ist bereits geladen und enthält das JSON-Objekt
if 'advancedTitleSearch' in movie_data['data']:
    df = pd.json_normalize(movie_data['data']['advancedTitleSearch'])

# DataFrame in eine Excel-Datei speichern
file_path = 'MoviesData.xlsx'
df.to_excel(file_path, index=False, engine='openpyxl')
 """
