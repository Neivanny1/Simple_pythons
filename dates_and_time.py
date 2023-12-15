# working with dates and time
# Calculating days to your birthday
from datetime import datetime
def when_is_my_birthday():
    today = datetime.now().date()
    dob = "2002-04-20"
    dob_format = "%Y-%m-%d"
    ddob = datetime.strptime(dob, dob_format).date()
    print(ddob)
    sub = today - ddob
    print(sub)
when_is_my_birthday()