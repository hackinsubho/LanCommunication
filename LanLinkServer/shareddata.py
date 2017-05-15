__author__ = 'RSVY'

import Queue
import threading
lst=[]
sendlst = []
clientmapdict = {}
q = Queue.Queue()
flag = 0
e = threading.Event()
