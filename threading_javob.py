import threading
import time

from threading_jins import*
from threading_ochst import*
from threading_ism import*
from threadingfam import*







t1 = threading.Thread(target=ism)
t2 = threading.Thread(target=fam)
t3 = threading.Thread(target=ochst)
t4 = threading.Thread(target=jins)

t1.start()
t2.start()
t3.start()
t4.start()