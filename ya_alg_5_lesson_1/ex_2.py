data_1 = list(map(int, input().split(':')))
data_2 = list(map(int, input().split(':')))
data_3 = int(input())
result = 0

sum_1 = data_1[0] + data_2[0]
sum_2 = data_1[1] + data_2[1]


if sum_1 > sum_2:
    result = 0
elif sum_1 == sum_2 and data_3 == 2 and data_1[0] > data_1[1]:
    result = 0
else:
    if data_3==1 and sum_2-sum_1!=0:
        result = sum_2-sum_1
    else:
        result = sum_2-sum_1+1


print(result)
