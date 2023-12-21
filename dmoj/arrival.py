hours, minutes = input().split(":")
mins = int(minutes)
hours = int(hours)
t=hours*60 + mins
time = 0

# Start in Rush Hour
if (t >= 420 and t < 600):
    perc = ((600- t) / 240)
    time2 = (1 - perc) * 60 * 2
    time += perc * 240
    time += time2
elif (t >= 900 and t < 1140):
    perc = ((1140 - t) / 240)
    time2 = (1 - perc) * 60 * 2
    time += perc * 240
    time += time2
    
# Doesn't start in rush hour but overlaps into first rush hour
elif (t > 300 and t < 420):
    perc = ((420 - t) / 240)
    time2 = (1 - perc) * 60 * 2
    time += perc * 240
    time += time2
elif (t > 780 and t < 900):
    perc = ((900 - t) / 240)
    time2 = (1 - perc) * 60 * 2
    time += perc * 240
    time += time2
else:
    time = 120
    
hours = int((hours + (time // 60)) % 24)
mins = int((mins + (time % 60))) % 60
hour_str = ""
mins_str = ""
if hours <= 9:
    hour_str += "0"
    hour_str += str(hours)
else:
    hour_str = str(hours)
    
if mins <= 9:
    mins_str += "0"
    mins_str += str(mins)
else:
    mins_str = str(mins)   
print(hour_str+":"+mins_str)