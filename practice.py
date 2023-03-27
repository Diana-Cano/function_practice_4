def max_num(int1,int2,int3):
    list = [int1, int2, int3]
    print(max(list))


def mult_list(list):
    result = 1
    for x in list:
        result = result * x
    print(result)

myList = [1,2,3]

mult_list(myList)

def rev_string(string):
    print string[::-1]

rev_string("hai")

def num_within(x,a,b):
  return x in range(a,b+1)


triangle = [[1],[1,1]]
def pascal(n):
    if n<1:
        print("invalid number of rows")
    elif n ==1:
        print(triangle[0])
    else:
        row_number = 2

        whilelen(triangle) < n:
            row = []
            row_prev = triangle[row_number-1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i>0 abd i< length-1:
                    row.append(triangle[row_number-1][i-1]=triangle[row_number-1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        for row in triangle:
            print(row)



    #had to use solution code for pascal function, coulnt wrap my head around it.
    
    
    