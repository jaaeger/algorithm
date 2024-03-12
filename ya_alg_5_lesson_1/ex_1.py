data_1 = list(map(int, input().split()))
data_2 = list(map(int, input().split()))

start_1 = data_1[0]-data_1[1]
finish_1 = data_1[0]+data_1[1]
start_2 = data_2[0]-data_2[1]
finish_2 = data_2[0]+data_2[1]
result = 0

# Если промежутки раздельны
if (finish_1 < start_2) or (finish_2 < start_1):
    result = finish_1-start_1+finish_2-start_2
# Если один промежуток сливается или внутри
elif (start_1 >= start_2) and (finish_1 <= finish_2):
    result = finish_2-start_2+1
elif (start_1 <= start_2) and (finish_1 >= finish_2):
    result = finish_1 - start_1+1
# Если промежутки пересекаются
elif finish_1>=start_2 and finish_1<finish_2:
    result = finish_2-start_1+1
elif finish_2>=start_1 and finish_2<finish_1:
    result = finish_1-start_2+1
print(result)
'''
#start_1 = data_1[0]-data_1[1]
#finish_1 = data_1[0]+data_1[1]+1
result = set()
for i in range(data_1[0]-data_1[1], data_1[0]+data_1[1]+1):
    result.add(i)
for i in range(data_2[0]-data_2[1], data_2[0]+data_2[1]+1):
    result.add(i)

print(len(result))

#def solve(start, finish):
#    for i in range(start, finish+1):
#        result.add(i)
'''