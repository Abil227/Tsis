from datetime import datetime, timedelta
now = datetime.now()
yestrd = now - timedelta(days=1)
tmrrw = now + timedelta(days=1)
print(yestrd)
print(now)
print(tmrrw)