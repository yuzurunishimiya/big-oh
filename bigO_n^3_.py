# Example of O(n^3)
def cubes(n):
    for i in range(n):
        for j in range (n):
            for k in range(n):
                print(i, j, k)

cubes(4)
