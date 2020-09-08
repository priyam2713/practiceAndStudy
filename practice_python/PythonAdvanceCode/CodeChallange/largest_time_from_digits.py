# Given an array of 4 digits, return the largest 24 hour time that can be made.
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger
# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

# function of getting all combination of digits in list except same index value combination
def getAllCombinations(digits = []):
    combinations_of_digits = []
    if not digits:
        combinations_of_digits.append(current)
    else:
        for index1, val1 in enumerate(digits):
            for index2 ,val2 in enumerate(digits):
                # restrict to make combination of value which are in the same position in list
                if index1 != index2:
                    combinations_of_digits.append(str(val1)+str(val2))
    return combinations_of_digits

# function of get Largest TIME
def findLargestTimeFromDigits(input_digits=[]):
    if not input_digits:
        return ""
    else:
        # get all valid digits combination
        combinations = getAllCombinations(input_digits)

        # Get all valid hours combinations 
        combinations_hrs = [x for x in combinations if int(x) <= 23]
        # Get all valid minutes combinations 
        if combinations_hrs:
            hours_str = max(combinations_hrs)
            unit_digit = int(hours_str) % 10 
            tens_digit = int(hours_str) // 10
            input_digits.remove(unit_digit)
            input_digits.remove(tens_digit)
            new_combinations = getAllCombinations(input_digits)
            minutes_str = max(new_combinations)
            return "{}:{}".format(str(hours_str), str(minutes_str))
            
        else:
            return ""

if __name__ == "__main__":
    input_digits = [1,5,0,5]
    result = findLargestTimeFromDigits(input_digits)
    print(result)