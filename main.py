import time
from datetime import datetime

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("\033[1;36m" + f"The time is now {current_time}" + "\033[0m", end="\r")
    time.sleep(1)
