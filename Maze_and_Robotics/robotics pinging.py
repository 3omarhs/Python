import os
import threading
import time

ara=["zuj.edu.jo", "google.com", "yahoo.com", "facebook.com", "youtube.com"]

def pinging(i):
    os.system("ping"+str(ara[i]))

r = time.time()

for h in range(0,5):
    pinging(h)

r = time.time()-r

for j in range (0,5):
    t=threading.Thread(target=pinging, args=(j,))
    t.start()

print(r)