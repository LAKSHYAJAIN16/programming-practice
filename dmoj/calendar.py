start, days = list(map(int, input().split(" ")))

print("Sun Mon Tue Wed Thr Fri Sat".rstrip())

# Some $#!7 for the first week
current_day = start
date = 1
cur_line = " " * 4 * (start - 1)

while date <= days:
    if current_day > 7:
        current_day = 1
        print(cur_line.rstrip())
        cur_line = ""
        
    if date < 10:
        cur_line += "  "
        cur_line += str(date)
    else:
        cur_line += " "
        cur_line += str(date)
        
    cur_line += " "
    current_day += 1
    date += 1
    
if cur_line != "":
    print(cur_line.rstrip())