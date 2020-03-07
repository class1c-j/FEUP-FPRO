"""
Write a script that given an hour and minutes by user input, prints at what time the alarm clock will ring, knowing that the current hour is hour and the current minutes are minutes. The clock goes off after 6 hour and 51 minutes.
"""
hour = int(input())
minutes = int(input())

minutes += (51 + 6 * 60)
minutes_alarm = minutes % 60

hours_alarm = hour + (minutes // 60)
hours_alarm %= 24

print(f'{hours_alarm:02}', end = '')
print(':', end = '')
print(f'{minutes_alarm:02}')
