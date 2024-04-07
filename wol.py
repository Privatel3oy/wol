from fastapi import FastAPI
from scapy.all import sendp
from scapy.layers.l2 import Ether

app = FastAPI()

def send_wol_layer2(mac_address):
    # clean up this mac address convert from string to byte
    mac_clean = mac_address.replace(":","").replace("-","")
    mac_byte = bytes.fromhex(mac_clean)
    

    # create the payload 0xFF(255) * 6 FF:FF:FF:FF:FF:FF + MAC address * 16
    payload = b'\xFF' * 6 + mac_byte * 16


    # create Ethernet frame destination = broadcast address  bind our payload (magic packet)
    magic_packet = Ether(dst="ff:ff:ff:ff:ff:ff") / payload
    
    
    # send the magic packet to the broadcast address
    sendp(magic_packet,"Ethernet")

@app.get("/")
async def root():
    return send_wol_layer2("08:BF:B8:3E:1B:04")
