import math

def mergesort(query_list):
    n = len(query_list)
    if n > 1: # only run if size > 1
        array_One = query_list[0:n//2]
        array_Two = query_list[n//2:n]

        #recursion:
        mergesort(array_One)
        mergesort(array_Two)

        #merge:
        i = 0 # left array index
        j = 0 # right array index
        array_index = 0 # merge array index

        while (i < len(array_One)) and (j < len(array_Two)):
            if array_One[i] > array_Two[j]:
                query_list[array_index] = array_One[i]
                i += 1 #increment left array
            else:
                query_list[array_index] = array_Two[j]
                j += 1  # increment right array
            array_index += 1

        while i < len(array_One): # if array_one out of elements.
            query_list[array_index] = array_One[i]
            i += 1
            array_index += 1

        while j < len(array_Two): # if array_two out of elements.
            query_list[array_index] = array_Two[j]
            j += 1
            array_index += 1

        return query_list
#main = print(h(math.pow(10,7))- 1)

