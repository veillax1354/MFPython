import datetime, pytz
from options import load
load('options.json')
def timenow():
    try:
        tz = 'America/Denver'
        current_time = datetime.datetime.now(pytz.timezone(tz))
        monthcheck = int(current_time.month) - 9
        daycheck = int(current_time.day) - 9
        yearcheck = int(current_time.year) - 9
        hourcheck = int(current_time.hour) - 9
        mincheck = int(current_time.minute) - 9
        secondcheck = int(current_time.second) - 9
        # Time formatting for datetime
        if current_time.hour > 12:
            hour = int(current_time.hour) - 12
            ampm = 'PM'
            if hourcheck < 0:
                hour = '0' + str(hour)
            elif hourcheck > 0:
                hour = str(hour)
        elif current_time.hour < 12:
            hour = current_time.hour
            ampm = 'AM'
            if hourcheck < 0:
                hour = '0' + str(hour)
            elif hourcheck > 0:
                hour = str(hour)
        if monthcheck < 0:
            month = '0' + str(current_time.month)
        elif monthcheck > 0:
            month = str(current_time.month)
        if daycheck < 0:
            day = '0' + str(current_time.day)
        elif daycheck > 0:
            day = str(current_time.day)
        if yearcheck < 0:
            year = '0' + str(current_time.year)
        elif yearcheck > 0:
            year = str(current_time.year)
        if mincheck < 0:
            minute = '0' + str(current_time.minute)
        elif mincheck > 0:
            minute = str(current_time.minute)
        if secondcheck < 0:
            second = '0' + str(current_time.second)
        elif secondcheck > 0:
            second = str(current_time.second)
        ctime = str(month) + '/' + str(day) + '/' + str(year) + '\n' + str(
            hour) + ':' + str(minute) + str(ampm)
    # Handles date and time printing
    except:
        ctime = 'Sorry, an error occurred while trying to access the current date and time, please try again later.'
    # prints the date and time
    print(ctime)
