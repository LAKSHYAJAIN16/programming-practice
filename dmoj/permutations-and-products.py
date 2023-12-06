k = int(input())
facs = []

def factors(k):
    facs = set()
    for i in range(1, k // 2 + 1):
        if k % i == 0:
            if k // i == i + 1 and i!= 1:
                continue
            else:
                facs.add(i)
                facs.add(k // i)
    return facs

def predict(k1, k2):
    # Do the thing
    print(">>> ? " + str(k1) + " " + str(k2), end="\n") 
    
    # Get k1 * k2
    fax = factors(int(input()))
    facs.append(fax)
    print(facs)
    
    # Run it all of the times
    if k1 == 1 and k2 == 2:
        # Convert all of the $#!7
        neins = []
        for i in range(len(facs) - 1, 0, -1):
            s1 = facs[i]
            s2 = facs[i - 1]
            nums = []
            print(s1, s2)
            for val in s1:
                for val2 in s2:
                    if val == val2:
                        nums.append(val)
                        break    
                                                        
            neins.append(nums)
            
        print(neins)
                    
    else:
        predict(k1 - 1, k1)
        
predict(k - 1, k)