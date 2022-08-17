from pyrogram.handlers import MessageHandler
import time
from pyrogram import Client,  filters
import logging
import requests
import download
import random
import os
import validation
logging.basicConfig(level=logging.INFO)
bot = Client(
    "ses1",
    api_id=348759, 
    api_hash="5dc6f4b54b1985199b42a069a5745306",
  workers = 5, 
  bot_token='1635563068:AAFBGsHY9b-ySQMLwedNrXUB7WrlGqpqoYk'
)