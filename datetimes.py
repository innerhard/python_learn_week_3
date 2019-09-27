from datetime import datetime, timedelta
dt_now = datetime.now()
delta_day = timedelta(1)
delta_mount = timedelta(31)
print(f"{dt_now - delta_day}")  # Вчера
print(f"{dt_now}")  # Сегодня
print(f"{dt_now - delta_mount}")  # Месяц назад

date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')

print(date_dt)
