import chardet as cd
import time


byte1 = b'abc'
time.sleep(10)
cs = cd.detect(byte1)