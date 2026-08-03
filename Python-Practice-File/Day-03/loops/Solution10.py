import time

wait_time = 1
maxx_retries = 2
attempts = 0

while attempts < maxx_retries:
    print("Attempt" , attempts+1 , "-Wait_time ", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1