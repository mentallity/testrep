def multiply_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result


def find_min(lst):
    return min(lst)


def count_even_numbers(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count


def remove_element(lst, element):
    count = lst.count(element)
    lst = [x for x in lst if x != element] # Удаляем все вхождения элемента из списка
    return count


def merge_lists(list1, list2):
    return list1 + list2


def calculate_power(lst, power):
    return [num**power for num in lst]




if __name__ == '__main__':
      #task1
      my_list = [1, 2, 3, 4]
      print(multiply_elements(my_list))

      #task2
      my_list = [5, 3, 8, 1]
      print(find_min(my_list))
      
      #task3
      my_list = [2, 5, 6, 7, 10]
      print(count_even_numbers(my_list))
      
      #task4
      my_list = [1, 2, 3, 2, 4, 5, 2]
      element_to_remove = 2
      print(remove_element(my_list, element_to_remove))
      
      #task5
      my_list1 = [1, 2, 3]
      my_list2 = [4, 5, 6]
      print(merge_lists(my_list1, my_list2))
      
      #task6
      my_list = [1, 2, 3, 4]
      power = 2
      print(calculate_power(my_list, power))