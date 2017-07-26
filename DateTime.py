import datetime
now = datetime.datetime.now()
time = str(now.time())
print('The time in Portland is '+time[0:8]+'.')
hour = int(time[0:2])
if hour < 21 and hour > 8:
    print('The Portland branch is open.')
else:
    print('The Portland branch is closed')
print('The time in New York is '+str(hour+3)+time[2:8]+'.')
if hour > 11:
    print('The New York branch is open.')
else:
    print('The New York branch is closed.')
if hour < 16:
    print('The time in London is '+str(hour+8)+time[2:8]+'.')
else:
    print('The time in London is '+str(hour-16)+time[2:8]+'.')
if hour < 5 or hour > 16:
    print('The London branch is open.')
else:
    print('The London branch is closed')
