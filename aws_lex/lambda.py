import json
from botocore.vendored import requests
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



def lambda_handler(event, context):

    apikey = '012848aba81de7c33562d2d7c29577d6'
    cityName = event['currentIntent']['slots']['cityName']
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apikey}&mode=json&units=metric'
    data = requests.get(url).json()
    logger.debug(data)
    n = '\n'
    response = f"The weather in {data['name']} is mainly {data['weather'][0]['main']} with {n} Min Temp: {data['main']['temp_min']} {n} Max Temp: {data['main']['temp_max']} {n} Pressure: {data['main']['pressure']} {n} Humidity: {data['main']['humidity']} {n} Visibility: {data['visibility']}"
    
    # TODO implement
    return {
    "sessionAttributes": {},
 
      "dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
        "message": {
          "contentType": "PlainText",
          "content": response,
      }
    }
}
