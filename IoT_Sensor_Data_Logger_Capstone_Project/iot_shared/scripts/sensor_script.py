import time
import random
from datetime import datetime
while True:
     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     value = random.uniform(20.0, 30.0)
     log_entry = f"{timestamp}, {value:.2f}\n"
     print(log_entry, flush=True)
     time.sleep(0.001)
