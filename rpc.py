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
    pemilihan = input("Wanna customize the rpc? (y/n)\n==> ")
    if pemilihan == 'y':
        idst = input("Put your client ID: ")
        state1 = input("Put your state rpc: ")
        details = input("Put your detail information rpc: ")
        limg = input("Large image name/number: ")
        simg = input("Small image name/number: ")
        path = 'rpcsave.json'
        data = {
            'client_id': idst,
            'state': state1,
            'detail': details,
            'largeimg': limg,
            'smallimg': simg,
        }
        with open(path, 'w+') as f:
            json.dump(data, f)
        path_two = 'rpcsave.json'
        with open(path_two, 'r') as f:
            j = json.load(f)
            ids = str(j['client_id'])
            states = str(j['state'])
            detailss = str(j['detail'])
            limgs = str(j['largeimg'])
            simgs = str(j['smallimg'])
        RPC = Presence(ids) 
        RPC.connect() 
        print(RPC.update(state=f"{states}", details=f"{detailss}", large_image=f"{limgs}", small_image=f"{simgs}", large_text="NAME", start=time.time()))
    if pemilihan == 'n':
        try:
            rpc_file = Path("rpcsave.json")
            if rpc_file.is_file():
                with open('rpcsave.json', 'r') as d:
                    je = json.load(d)
                    idt = str(je['client_id'])
        except FileNotFoundError:
            print('u should type y/yes i think')
            exit()
        RPC = Presence(idt)
        RPC.connect() 
        print(RPC.update(state=f"GOOD RPC :D", details=f"iFanpS RPC", large_image=f"no", small_image=f"no", large_text="NAME", start=time.time()))
        

if __name__ == "__main__":
    awalan()
