from datetime import datetime
from datetime import timedelta
def f(date, n):
    from_date = datetime.strptime(date, '%y-%m-%d')
    to_date = from_date - timedelta(days=n)
    return to_date.strftime('%y-%m-%d')

print(f('16-12-10', 11))