################################################################################
# solution_01_2.py
################################################################################

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    # Initlaize two lists and fill them based on the values in each column.

    list1 = []
    list2 = []
    for input_line in input_data:
        value1, value2 = input_line.split()
        list1.append(int(value1))
        list2.append(int(value2))

    # For each value in the first list, count the number of times it occurs
    # within the second list. Multiply the value by the number of hits (in the)
    # 2nd list and add it to the result.

    result = 0

    for i in list1:
        hits = list2.count(i)
        result += (i * hits)

    return result

################################################################################
# END
################################################################################