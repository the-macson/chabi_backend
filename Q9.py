

from datetime import datetime
from datetime import timedelta
def date_diff(from_date, to_date, difference):
    from_date = datetime.strptime(from_date, '%y-%m-%d')
    to_date = datetime.strptime(to_date, '%y-%m-%d')
    if (to_date - from_date) < timedelta(days=difference):
        return True
    else:
        return False
    
print(date_diff('20-01-01', '20-01-02', 2))
print(date_diff('20-01-01', '20-01-03', 2))
print(date_diff('20-01-01', '20-01-04', 2))