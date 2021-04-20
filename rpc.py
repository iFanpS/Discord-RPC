from discord import client
from pypresence import Presence
import time, json
from pathlib import Path

banner = """
==============================
Discord RPC By iFanpS
Not 100% by Me
Credit Bearski11
=============================
"""
print(banner)

def awalan():
    try:
        path = "rpcsave.json"
        with open(path,"r") as f:
            j = json.load(f)
            id = str(j['client_id'])
            states = str(j['state'])
            detailss = str(j['detail'])
            limgs = str(j['largeimg'])
            simgs = str(j['smallimg'])
        RPC = Presence(id)
        RPC.connect()
        RPC.update(state=states, details=detailss, large_image=limgs, small_image=simgs, start=time.time())
        print('Your DiscordRichPresence is working now!')
    except FileNotFoundError:
        print('Please make rpcsave.json first!')

if __name__ == "__main__":
    awalan()
