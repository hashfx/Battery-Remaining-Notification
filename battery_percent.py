"""
pip install psutil
pip install plyer
"""
import psutil
from plyer import notification
import time

battery = psutil.sensors_battery()

# From psutil we will import the sensors_battery class so we have the battery remaining stats
while (True):
    percent = battery.percent

    notification.notify(
        title="Battery Percentage",
        message=str(percent) + "% Battery remaining",
        timeout=10
    )

    # After every 60 mins it will show the battery percentage
    # time.sleep(Seconds)
    time.sleep(3600)
    continue
