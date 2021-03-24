from pypresence import Presence
import time
import subprocess

banner = """
==============================
Discord RPC By iFanpS
Not 100%\\by Me
Credit Bearski11
=============================
"""
print(banner)

def awalan():
    pemilihan = input("Wanna customize the rpc? (y/n)\n==> ")
    if pemilihan == 'y':
        id = input("Put your client ID: ")
        state1 = input("Put your state rpc: ")
        details = input("Put your detail information rpc: ")
        limg = input("Large image name/number: ")
        simg = input("Small image name/number: ")
        client_id = id
        RPC = Presence(client_id) 
        RPC.connect() 
        print(RPC.update(state=f"{state1}", details=f"{details}", large_image=f"{limg}", small_image=f"{simg}", large_text="NAME", start=time.time()))
    if pemilihan == 'n':
        id1 = input("Put your client ID: ")
        client_id = id1
        RPC = Presence(client_id) 
        RPC.connect() 
        print(RPC.update(state=f"GOOD RPC :D", details=f"iFanpS RPC", large_image=f"no", small_image=f"no", large_text="NAME", start=time.time()))

def update():
    upt = input("Want to update the text? (y/n)")
    if upt == "y":
        subprocess.call('python3 rpc.py',shell=True)
    if upt == "n":
        print("Exiting program....")
        time.sleep(4)
        exit()

if __name__ == "__main__":
    awalan()
    time.sleep(5)
    update()
