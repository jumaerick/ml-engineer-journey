# A way of repeatedly executing some code
a = 10

while a > 0 : 
    print(a)
    if a < 5:
        break
    a-=1

# for i in range(2):
#     print(i, end = ' ')

squares = [n**2 for n in range(1, 5)]
# print(squares)
sq = [i**2 for i in range(5) if i > 1]
# print(sq)

def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    return len([neg for neg in nums if neg < 0])

# print(count_negatives([5, -1, -2, 0, 3]))

def has_lucky_numbers(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    is_lucky = False

    for num in nums:
        if (num > 0) & ((num % 7) == 0) :
            is_lucky = True

    return is_lucky

# def has_lucky_number(nums):
#     return any([num % 7 == 0 for num in nums])

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [i > thresh for i in L]

# print(elementwise_greater_than([1, 2, 3, 4], 2))

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(1, len(meals)):
        if(meals[i-1] == meals[i]):
            return True
    return False

# print(menu_is_boring(['rice', 'beans', 'beans']))