list = [1,2,3,4,5,6,100]

# mean = 0

# for i in list:
#     mean += i
    
# mean = mean / len(list)

# print(mean)


def mean(arr):
    mean =0
    for i in arr:
        mean += i 
    return mean/len(arr)
  
print(mean(list))
print(mean([1,2,3,4,5,6,7,8,9,10]))