def max_list_element(list):
    max_elem = int(list[0])
    for elem in list:
        if int(elem) > max_elem:
            max_elem = int(elem)
    return int(max_elem)


first_list = input().split()
second_list = input().split()

print(max_list_element(first_list) * max_list_element(second_list))
