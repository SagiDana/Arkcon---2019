#!/usr/bin/python
import time
from scapy.all import *
from threading import Thread, Event


# _IP = "13.56.195.185"
_IP = "54.193.121.32"


def worker(_event):
    while not _event.is_set():
        p = sniff(count=1,filter="ip src {}".format(_IP), timeout=1)    
        print(p.hexdump())

    

if __name__ == '__main__':
    
    _event = Event()
    t = Thread(target=worker, args=(_event,))
    t.start()

    # for i in [0,3,4,5,8,9,10,11,12,13,14,15,16,17,18]:
    #     print("Request type:{}".format(i))
    #     time.sleep(1)
    #     packet = IP(dst=_IP)/ICMP(type=i, code=0)/("A"*1)
    #     send(packet)
    
    packet = IP(dst=_IP)/ICMP(type=8, code=0)/("A"*9999)
    send(packet)
    # packet = IP(dst="54.193.121.32")/ICMP(type=3, code=0)/("A"*1)
    # send(packet)
    
    # time.sleep(2)

    _event.set()
    t.join()








