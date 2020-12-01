import requests
from datetime import datetime
import time

write_wd_changes()



starttime = time.time()

while True:
    if (datetime.now().minute % 30) == 0:
        write_wd_changes()
    
    write_wp_changes()

    print(time.time())
    time.sleep(60.0 - ((time.time() - starttime % 60.0))
