from ex3 import maximum

def happy():
    result = True
    if maximum ([]) == None:
        # "ailed to run maximum with empty list
        print("test 1 is ok")
    else:
        print("test 1 FAILED")
        result = False
    if maximum([0, 0, 0]) == 0:
        # Failed to run all zeroes
        print("test 2 is ok")
    else:
        print("test 2 FAILED")
        result = False
    if maximum([-3, -4, -35]) == -3:
        # Failed when maximum was negative
        print("test 3 ok")
    else:
        result = False
        print("test 3 FAILED")
    if maximum([100,100,1]) == 100:
        # Failed when 2 nums are the same next to each other
        print ("test 3 ok")
    else:
        result = False
        print("test 3 FAILED")
    if maximum([1,0,1]) == 1:
        # Failed when 2 nums equal max, not next to each other"
        result = True
        print("test 4 ok")
    else:
        result = False
        print("test 4 FAILED")
    if maximum([4,99,98]) == 99:
        # Failed when max is first
        print("test 5 ok")
    else:
        print("test 5 Failed ")
        result = False
    if maximum([1]) == 1:
        # Failed when list consists of one num"
        print("test 6 ok")
    else:
        print ("test 6 FAILED")
        result = False
    if maximum([2.56, 3.79, 1.002]) == 3.79:
        #"failed when arg were float"
        print("test 7 ok")
    else:
        print("test 7 FAILED")
        result = False
    return result



if __name__ == '__main__':
    (test())