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
    id = int(input("Please put your Client ID: "))
    state1 = input("Put your state rpc: ")
    details = input("Put your Details rpc: ")
    limg = input("Put your large img name: ")
    simg = input("Put your small img name: ")
    client_id = f'{id}'
    RPC = Presence(client_id) 
    RPC.connect() 
    print(RPC.update(state=f"{state1}", details=f"{details}", large_image=f"{limg}", small_image=f"{simg}", large_text="NAME", start=time.time()))

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