array = []
for i in range(6):
    array.append(map(int, raw_input().strip().split()))
sum_max = -9 *7    
for i in range(4):
    for j in range(4):
        g_sum = sum(array[i][j:j+3]) + array[i+1][j+1] + sum(array[i+2][j:j+3])
        if g_sum > sum_max : sum_max = g_sum 
        
print sum_max
