def find(ordered_list, element_to_find):
    start_index = 0
    end_index = len(ordered_list)

    while True:
        middle_index = (end_index - start_index) // 2

        if start_index > end_index:
            return False

        middle_element = ordered_list[middle_index]

        if middle_element == element_to_find:
            return True

        elif middle_element < element_to_find:
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1
        

if __name__ == "__main__":
    list_numbers = [1, 3, 5, 30, 42, 43, 500]
    print(find(list_numbers, 30))
