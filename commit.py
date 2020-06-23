from time import sleep
import os

def commit():
    delay = 9200

    os.system("git add .")
    os.system('git commit -m "Logs update"')
    os.system("git push")

    sleep(delay)
    commit()
commit()
