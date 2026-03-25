import time
import os

hours = int(os.getenv('PROCESS_DURATION_HOURS', 5))
duration_seconds = hours * 3600

print(f"Starting {hours}-hour process...")
start = time.time()

while time.time() - start < duration_seconds:
    elapsed = time.time() - start
    print(f"Elapsed: {elapsed/3600:.1f} hours")
    time.sleep(300)  # Log every 5 minutes

print("Process completed!")
