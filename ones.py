def max_length(array):
    maxx = 0
    start = 0
    replace = 1  
    count = 0

    for i in range(len(array)):
        if array[i] == 0:
            count += 1

        while count > replace:
            if array[start] == 0:
                count -= 1
            start += 1

        if i - start + 1 > maxx:
            maxx = i - start + 1

    return maxx

print(max_length([1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1]))
 