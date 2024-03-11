from datetime import datetime
#vvodim dati
date1str = input("Введите 1 дату в формате (гггг-мм-дд чч:мм:сс): ")  
date2str = input("Введите 2 дату в формате (гггг-мм-дд чч:мм:сс): ")
#iz str v datu
date1 = datetime.strptime(date1str, '%Y-%m-%d %H:%M:%S')
date2 = datetime.strptime(date2str, '%Y-%m-%d %H:%M:%S')

# Конвертация в секунды
sec1= date1.timestamp()
sec2= date2.timestamp()

# Вывод raznici v секундax
print(sec2 - sec1)