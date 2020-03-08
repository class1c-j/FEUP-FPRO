"""
Use Spyder3 to write a program that determines what is the actual time (using now of class datetime from module datetime).

Given that an alarm is set up for 8 hours and 30 minutes later, the program prints the time on display at the time of the alarm, using the format "hh:mm" (hours and minutes).
"""
import datetime

time = datetime.datetime.now()

alarm_time = (time + datetime.timedelta(hours=8, minutes=30))

print(alarm_time.strftime("%H:%M"))