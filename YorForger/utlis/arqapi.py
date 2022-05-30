import json
import sys
from random import randint
from time import time

import aiohttp
from YorForger import aiohttpsession 
from aiohttp import ClientSession

from Python_ARQ import ARQ

from YorForger import BOT_ID, OWNER_ID, ARQ_API_URL, ARQ_API_KEY
from YorForger import pbot

ARQ_API = "WPLYQX-KLEHQY-AXINRQ-WNIPGO-ARQ"
ARQ_API_KEY = "WPLYQX-KLEHQY-AXINRQ-WNIPGO-ARQ"
SUDOERS = OWNER_ID
ARQ_API_URL = "https://arq.hamker.in"

# Aiohttp Client
print("[INFO]: INITIALZING AIOHTTP SESSION")
aiohttpsession = ClientSession()
# ARQ Client
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

app = pbot
import socket
