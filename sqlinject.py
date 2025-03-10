import hashlib
import datetime

start = datetime.datetime.now()
for i in range(10000000):
    hash = hashlib.sha256(str(i).encode()).digest()
    if b"'='" in hash:
        print("Found: %d => %s" % (i, hash))
        print(datetime.datetime.now() - start)