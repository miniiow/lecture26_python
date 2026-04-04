# 리스트와 반복구조 프로그래밍 연습
# 정수로 구성되어 있는 리스트를 파라미터로 입력받아 다음의 기능을 수행하는 함수 구현

def getIndex(num_list, target):
    for i in range(len(num_list)):
        if num_list[i] == target:
            return i

def getMax(num_list):
    max = num_list[0]
    for i in num_list:
        if max < i:
            max = i
    return max

def getMin(num_list):
    min = num_list[0]
    for i in num_list:
        if min > i:
            min = i
    return min

def countGT(num_list, target):
    count = 0
    for i in num_list:
        if i >= target:
            count += 1
    return count

def sumList(num_list):
    sum_list = 0
    for i in num_list:
        sum_list += i
    return sum_list

def swapList(num_list):
    index = len(num_list)-1
    for i in range(0, len(num_list)//2):
        num_list[i], num_list[index] = num_list[index], num_list[i]
        index -= 1
    return num_list


number_list = [23,45,27,11,25,65,78]
print(getIndex(number_list, 25))
print(getMax(number_list))
print(getMin(number_list))
print(countGT(number_list, 42))
print(sumList(number_list))
swapList(number_list)
print(number_list)