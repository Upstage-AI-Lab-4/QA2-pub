from langchain_upstage import ChatUpstage
from langchain_upstage import UpstageEmbeddings
import requests

import config   # API_KEY, DATA_API_KEY

def embed_model_init():
    return UpstageEmbeddings(api_key=config.API_KEY, model='solar-embedding-1-large')

def llm_init():
    return ChatUpstage(api_key=config.API_KEY)