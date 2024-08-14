from langchain_upstage import ChatUpstage
from langchain_upstage import UpstageEmbeddings
import requests

import config   # API_KEY, DATA_API_KEY

def embed_model_init():
    return UpstageEmbeddings(api_key=config.API_KEY, model='solar-embedding-1-large')

def llm_init():
    return ChatUpstage(api_key=config.API_KEY)

def KAC_Departure_api():
    KAC_api_key = config.DATA_API_KEY
    flight_date = datetime.today().strftime('%Y%m%d')
    url = f'https://api.odcloud.kr/api/FlightStatusListDTL/v1/getFlightStatusListDetail?serviceKey={KAC_api_key}&cond%5BFLIGHT_DATE%3A%3AEQ%5D={flight_date}&cond%5BIO%3A%3AEQ%5D=o'
    return requests.get(url).json()

def KAC_Arrival_api():
    KAC_api_key = config.DATA_API_KEY
    flight_date = datetime.today().strftime('%Y%m%d')
    url = f'https://api.odcloud.kr/api/FlightStatusListDTL/v1/getFlightStatusListDetail?serviceKey={KAC_api_key}&cond%5BFLIGHT_DATE%3A%3AEQ%5D={flight_date}&cond%5BIO%3A%3AEQ%5D=i'
    return requests.get(url).json()

def IIAC_Arrival_api():
    IIAC_api_key = config.DATA_API_KEY
    url = 'http://apis.data.go.kr/B551177/StatusOfPassengerFlightsOdp/getPassengerArrivalsOdp'
    params ={
        'serviceKey' : IIAC_api_key,
        'from_time' : '0000',
        'to_time' : '2400',
        'airport' : '',
        'flight_id' : '',
        'airline' : 'KE',
        'lang' : 'E',
        'type' : 'json'
    }
    return requests.get(url=url, params=params).json()

def IIAC_Departure_api():
    IIAC_api_key = config.DATA_API_KEY
    url = 'http://apis.data.go.kr/B551177/StatusOfPassengerFlightsOdp/getPassengerDeparturesOdp'
    params ={
        'serviceKey' : IIAC_api_key,
        'from_time' : '0000',
        'to_time' : '2400',
        'airport' : '',
        'flight_id' : '',
        'airline' : 'KE',
        'lang' : 'E',
        'type' : 'json'
    }
    return requests.get(url=url, params=params).json()