from datetime import datetime
import pytz

s=datetime.strptime("3:00","%H:%M").time()
e=datetime.strptime("4:00","%H:%M").time()

now = datetime.now(pytz.timezone('Asia/Kolkata')).time()
c=now.replace(second=0, microsecond=0)
if s<=c<= e:
    print("The time within the range")
else:
    print("The time outside the range")