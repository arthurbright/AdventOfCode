


with open("in", "r") as file:

    total = 0
    
    for line in file:
        arr = line.split()
        s = arr[0]

        nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

        done = False
        for i in range(len(s)):
            c = s[i]
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                total += 10 * (ord(c) - ord('0'))
                break
            else:
                for ss in nums:
                    if s[i:].startswith(ss):
                        total += 10 * (nums.index(ss) + 1)
                        done = True
                        break
                if done:
                    break

        
        s = s[::-1]
        for i in range(9):
            nums[i] = nums[i][::-1]

        # print(nums)
        # print(s)
        done = False
        for i in range(len(s)):
            c = s[i]
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                total += (ord(c) - ord('0'))
                break
            else:
                for ss in nums:
                    if s[i:].startswith(ss):
                        total += (nums.index(ss) + 1)
                        done = True
                        break
                if done:
                    break
    
    print(total)