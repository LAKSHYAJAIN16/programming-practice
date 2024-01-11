N = int(input())
dict_links = {}

for j in range(N):
    a = input()
    
    # Append it to the dictionary
    dict_links[a] = []
    
    # Now, browse the doc
    l_open = False
    while True:
        k = input()
        if k == "</HTML>":
            break
        
        # Loop through input
        for m in range(len(k)):
            try:
                if k[m + 3] == "H" and k[m + 4] == "R" and k[m + 5] == "E":
                    if k[m + 6] == "F" and k[m + 7] == " ":
                        if k[m + 8] == "=" and k[m + 9] == '"':
                            url = ""
                            for f in range(m + 10, len(k)):
                                if k[f] == '"':
                                    break
                                else:
                                    url += k[f]  
                            dict_links[a].append(url)
                            print("Link from " + a + " to " + url)
                            
            except:
                continue
 
def check(already, f, l2):
    if dict_links[f].includes(l2) and already.includes(l2) == False:
        return True
    if dict_links[f].includes(l2) == False and already.includes(l2) == True:
        return False
    else:
        already.append(l2)
        for q in range(0, len(dict_links[f])):   
            return check(already, dict_links[f][q], l2)
                                    
while True:
    l1 = input()
    l2 = input()
    print(check([],l1,l2))
    