
def bubble_sort(n):
    for l in range(len(n)-1, 0, -1):
        for i in range(l):
            print("index number {} and its value {}".format(i, n[i]))
            if n[i] > n[i+1]:
                temp = n[i+1]
                n[i+1] = n[i]
                n[i] = temp


def selection_sort(n):
    for l in range(len(n)-1, 0, -1):
        max_number_index = 0
        for i in range(1, l+1):
            if n[i] > n[max_number_index]:
                max_number_index = i
        print("max index number {} which value is {}".format(max_number_index, n[max_number_index]))
        temp = n[l]
        n[l] = n[max_number_index]
        n[max_number_index] = temp


def insertion_sort(n):
    for i in range(1, len(n)):
        current_position = i
        current_value = n[i]
        while current_position > 0 and current_value < n[i-1]:
            n[current_position] = n[current_position-1]
            current_position = current_position -1
        n[current_position] = current_value


arr = [26,54,93,17,77,31,44,55,20]

insertion_sort(arr)
print(arr)
# sqr function

def sqr(n):
    return n*n

def my_map(func,l):
    result = []
    for i in l:
        result.append(func(i))

    return result

a = my_map(sqr,[1,2,3,4,5])
print(a)