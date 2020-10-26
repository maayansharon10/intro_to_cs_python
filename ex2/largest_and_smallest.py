
def largest_and_smallest(num1, num2, num3):
    """this function receives 3 numbers and returns the largest number
        and the smallest number, in this order"""
    largest=0
    smallest=0
    #we define randomly largest and smallest so program could change them
    # later
    if num1 < num2:
        # will check which one is the largest/smallest once num1<num2
        if num1 < num3:
            # while (num1<num2) and (num1<num3)
            if num3 < num2:
                # while (num1<num2) and (num1<num3) and (num3<num2)
                largest = num2
                smallest = num1
            else:
                # while (num1<num2) and (num1<num3) and (num3<=num2)
                largest = num3
                smallest = num1
        else:
            # while nun1<num2 and num1>=num3
            largest = num2
            smallest = num3
    elif num1==num2==num3:
        return num1,num2
    else:
        # while num1 >= num2
        if num1 > num3:
            # while (num1 >= num2) and (num1>num3)
            if num3 > num2:
                # while (num1 >= num2) and (num1>num3) and (num3>num2)
                largest = num1
                smallest = num2
            else:
                # while (num1 >= num2) and (num1>num3) and (num3<=num2)
                largest = num1
                smallest = num3
        else:
            # while (num1 >= num2) and (num1<=num3)
            if num1 < num3:
                # while (num1 >= num2) and (num1<=num3) and num1<num3
                largest = num3
                smallest = num2
    # now that we looked at all cases possible,
    # we return largest and smallest
    return largest, smallest

