
with open("in", "r") as file:

    total = 0
    

    id = 0
    for line in file:
        id += 1
        arr = line.split(":")
        string = arr[1]

        arr = string.split(";")
        good = True
        
        maxred = 0
        maxblue = 0
        maxgreen = 0
        for pick in arr:
            arr2 = pick.split()
            ll = len(arr2)
            blue = 0
            red = 0
            green = 0
            #print(arr2)
            for i in range(0, ll, 2):
                if arr2[i + 1] == "blue":
                    blue = int(arr2[i])
                elif arr2[i + 1] == "green":
                    green = int(arr2[i])
                else:
                    #print(arr2[i])
                    red = int(arr2[i])
            maxred = max(maxred, red)
            maxblue = max(maxblue, blue)
            maxgreen = max(maxgreen, green)
            
        total += maxred * maxblue * maxgreen




    print(total)