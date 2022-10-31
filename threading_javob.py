import threading
import time
from threading_ism import*
from threadingfam import*
from threading_ochst import*



t1 = threading.Thread(target=ism)
t2 = threading.Thread(target=fam)
t3 = threading.Thread(target=ochst)

t1.start()
t2.start()
t3.start()