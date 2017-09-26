timenow = int(input("what is the time now? "))
hourswait = int(input("how many hours should we wait?"))

alarmtime = (hourswait % 24) + timenow
alarmtime = alarmtime % 24
if alarmtime > 12 :
    alarmtime = alarmtime % 12
    print("time will be" + str(alarmtime) + "PM")
else:
    print("time will be" + str(alarmtime) + "AM")
print(alarmtime)
