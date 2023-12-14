map = {
    "0" : [
        "-1",
        "-2",
        "-3",
        "-7"
    ],
    "-1" : [
        "-5",
        "-6",
        "-7"
    ],
    "1" : [
        "-3",
        "-7"
    ],
    "2" : [
        "-3",
        "-7"
    ],
    "3" : [
        "-3",
        "-4",
        "-5",
        "-7"
    ],
    "4" : [
        "-5",
        "-7"
    ],
    "5" : [
        "-3",
        "-4",
        "-5",
        "-7"
    ],
    "6" : [
        "-3",
        "-7"
    ],
    "7" : [
        "-3",
        "-4",
        "-5",
        "-6",
        "-7"
    ]
}

pos = [
    -1,
    -5
]

while True:
    dir, m = input().split(" ")
    is_d = False
    
    if dir == "q":
        break
    
    if dir == "l":
        for i in range(int(m)):
            pos[0] -= 1
            
            if str(pos[0]) in map:
                if str(pos[1]) in map[str(pos[0])]:
                    is_d = True 
                      
                else:
                    map[str(pos[0])].append(str(pos[1]))
            else:
                map[str(pos[0])] = [str(pos[1])]
                
    if dir == "r":
        for i in range(int(m)):
            pos[0] += 1
            
            if str(pos[0]) in map:
                if str(pos[1]) in map[str(pos[0])]:
                    is_d = True 
                      
                else:  
                    map[str(pos[0])].append(str(pos[1]))
            else:
                map[str(pos[0])] = [str(pos[1])]
                
    if dir == "u":
        for i in range(int(m)):
            pos[1] += 1
            
            if str(pos[0]) in map:
                if str(pos[1]) in map[str(pos[0])]:
                    is_d = True   
                else:
                    map[str(pos[0])].append(str(pos[1]))
            else:
                map[str(pos[0])] = [str(pos[1])]
                
    if dir == "d":
        for i in range(int(m)):
            pos[1] -= 1
            
            if str(pos[0]) in map:
                if str(pos[1]) in map[str(pos[0])]:
                    is_d = True 
                      
                else:  
                    map[str(pos[0])].append(str(pos[1]))
            else:
                map[str(pos[0])] = [str(pos[1])]   
                   
    if is_d == True:
        print(pos[0], pos[1], "DANGER")
        break
    else:
        print(pos[0], pos[1], "safe")