import datetime
new_date = datetime.datetime.now()
date = new_date.strftime("%Y-%m-%d %H:%M:%S")
print(date)
#чтоб добавить микросекунды %f