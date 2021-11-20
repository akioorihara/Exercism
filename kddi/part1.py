#Given is a list of integers. You are required to compute the sum of the products 
#of the digits from each integer. For example, if the list consists of integers 25 
#and 15, you are to ouput 15 as 2 * 5 + 1+ 5 = 10 + 5 = 15. 
#List size is given in the first line of the input, and then each element in the list is give none per line 


def ComputeSum():

    calc = 1
    List = [] 
    size = input() 

    for i in range(int(size)):
        inputValue = input()
        for x in inputValue:
            calc *= int(x)
        List.append(calc)
        
        calc = 1
    
    return sum(List)


print(ComputeSum())