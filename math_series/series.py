
def fibonacci(number):  # 0 1 1 2 3 5 8 ....
    """
    This function take number as an arg and return the nth value depend on fibonacci series
    """
    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


# -------------------------------------------------------------------------------------------------------


def lucas(number):  # 2, 1, 3, 4, 7, 11, 18, 29
    """
     This function take number as an arg and return the nth value depend on lucas series
    """
    if number == 0:
        return 2
    if number == 1:
        return 1

    return lucas(number - 1) + lucas(number - 2)

# ----------------------------------------------------------------------------------------------------------


def sum_series(number, first=0, second=1):  # 0 1 1 2 3 5 8 13 ...
    """
        This function uses the fibonacci and lucas, but it has custom  ,
        and it returns the index of the series bsed on the first and the second indexes

    """
    if number == 0:
        return first
    if number == 1:
        return second

    return sum_series(number - 1, first, second) + sum_series(number - 2, first, second)


# -------------------------------------------------------------------------------------------------