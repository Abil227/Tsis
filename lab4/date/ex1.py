from datetime import datetime, timedelta
now = datetime.now()
newdate = now - timedelta(days=5)
print(newdate)