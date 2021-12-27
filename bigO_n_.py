# big O(n)
def sum_in_range(n):
    sum = 0
    for x in range(0, n):
        sum += x # big O(1)
    return sum


sum = sum_in_range(10)
print("sum from 0 to 10 is:", sum)


# displaying array/list
# example of Big O(n)
def display_list(data: list):
    for datum in data:
        print(datum)

arr = [[1,2], [2,3], [3,4]]
display_list(arr)
