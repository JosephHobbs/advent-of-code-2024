################################################################################
# solution_01_1.py
################################################################################

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    # Initlaize two lists; one for each column.  Fill them and then sort
    # each list individually so values are in order.

    list1 = []
    list2 = []
    for input_line in input_data:
        value1, value2 = input_line.split()
        list1.append(int(value1))
        list2.append(int(value2))

    list1.sort()
    list2.sort()

    # Calculate the result by subtracting values between the lists. Since
    # there is no guarantee on which is higher, take the absolute value to
    # eliminate any negatives.

    result = 0
    for i in range(len(list1)):
        result += abs(list1[i] - list2[i])

    return result

################################################################################
# END
################################################################################