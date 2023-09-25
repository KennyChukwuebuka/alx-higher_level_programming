def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            # Check if both lists are too short
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            # Attempt the division
            try:
                a = float(my_list_1[i])
                b = float(my_list_2[i])
                if b == 0:
                    raise ZeroDivisionError("division by 0")
                division_result = a / b
                result.append(division_result)
            except ValueError:
                result.append(0)
                print("wrong type")
            except ZeroDivisionError:
                result.append(0)
                print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        return result

# Example usage:
my_list_1 = [10, 20, 30]
my_list_2 = [2, 0, "40"]
list_length = 5

result = list_division(my_list_1, my_list_2, list_length)
print(result)
