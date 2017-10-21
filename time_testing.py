import time
pos = 1,1
body = [pos]*100
start = time.perf_counter()
body.pop(0)
print((time.perf_counter()-start)*1000)