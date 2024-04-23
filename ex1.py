import time

nums= [3,2,1]

inf= True
i=0
while inf == True:
    a=0
    while a < len(nums):
        print(nums[i],end="\n")
        #i+=1       #old code
        #i= i % len(nums)
        i=(i+1) % len(nums)
        a+=1
        time.sleep(0.05)
    print(end="\n")
    time.sleep(1)