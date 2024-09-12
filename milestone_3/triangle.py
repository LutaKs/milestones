import sys

def get_triangle(rows: int):
    pascal = []
    for i in range(rows):
        if i == 0:
            pascal.append([1])
        else:
            next_row = []
            prev_int = 0
            for j in pascal[i - 1]:
                next_row.append(j + prev_int)
                prev_int = j
            next_row.append(1)
            pascal.append(next_row)
    return pascal

def print_pascal(nums):
    result = ""
    low = ''
    for k in nums[-1]:
        low += str(k)+' '
    low = low.strip()     
    for row in nums[:-1]:
        align = ''
        for g in row:
            align += str(g)+" "
        align = align.strip()
        align = align.center(len(low), ' ')
        result += align
        result += '\n'    
    result += low    
    return result        

k = int(sys.argv[1])

print(print_pascal(get_triangle(k)))
