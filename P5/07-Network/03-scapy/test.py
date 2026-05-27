import os
import sys

a = "10.141.212."
for i in range(256):
    b = a + str(i)
    # with open(r"/Users/keivanjamali/Projects/Pure-Python/P5/07-Network/03-scapy/log.txt", "r+") as f:
        # f.writelines([f"####### {b} ######", str(os.system(f"ping {b} -t 3"))])
    print(f"####### {b} ######")
    os.system(f"ping {b} -t 3 -s 1")