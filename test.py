def minMoves(avg):
    count = 0 
    count1 = 0
    size = len[avg]

    ##count number of 1s
    for i in range(size):
        if (avg[i]==1):
            count1=count1+1

    ##count number of 1s in subarray
    for i in range(0,count1):
        if (avg[i]==1):
            count = count+1
    max1 = count

    for i in range(1,count1+1):
        if (avg[i-1]==1):
            count = count -1 

    minswap = count1 - max1

    return minswap