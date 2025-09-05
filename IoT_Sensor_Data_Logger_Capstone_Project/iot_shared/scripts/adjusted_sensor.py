import time
import random
from datetime import datetime
for i in range(1,1000):
     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     value = random.uniform(20.0, 30.0)
     log_entry = f"{timestamp}, {value:.2f}\n"
     print(log_entry, flush=True)
     
