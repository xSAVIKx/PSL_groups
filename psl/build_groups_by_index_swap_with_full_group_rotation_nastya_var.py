import copy
from collections import deque

from psl.PSL_constants import P5, P7, P3, P2

results = []
formatted_results = []
unique_results = []
unique_formatted_results = []
first_group_element = deque(range(1, 22))


def makeSwap(swappable, original_index, indexes_to_swap):
    swappable_copy = copy.copy(swappable)
    for i1, i2 in zip(original_index, indexes_to_swap):
        swappable_copy[i1 - 1] = swappable[i2 - 1]
    return swappable_copy


def swap_group(rotation_index, group):
    result = copy.copy(first_group_element)
    if rotation_index == 0:
        return result
    for element in group:
        deq = deque(element)
        deq.rotate(rotation_index)
        result = makeSwap(result, element, deq)
    return result


def multiple_group_elements(swappable, first_group, second_group):
    swappable_copy = copy.copy(swappable)
    for i1, i2 in zip(first_group, second_group):
        swappable_copy[i2 - 1] = swappable[i1 - 1]
    return swappable_copy


def multiple_group(first_group, second_group):
    result = copy.copy(first_group_element)
    result = multiple_group_elements(result, first_group, second_group)
    return result


rotated_P5 = swap_group(1, P5)
mult_with_first = multiple_group(first_group_element, rotated_P5)

rotated_P3 = swap_group(1, P3)
rotated_P2 = swap_group(1, P2)
multiplicated_group_result = multiple_group(rotated_P3, rotated_P2)

with open('./build_groups_by_index_swap_with_full_group_rotation_unique_nastya.txt', 'w+') as formatted_unique_output_file:
    with open('./build_groups_by_index_swap_with_full_group_rotation_nastya.txt', 'w+') as formatted_output_file:
        for p7_el_idx in xrange(0, len(P7[0])):
            p7_swapped_group = swap_group(p7_el_idx, P7)
            for p3_el_idx in xrange(0, len(P3[0])):
                p3_swapped_group = swap_group(p3_el_idx, P3)
                p3_result = multiple_group(p7_swapped_group, p3_swapped_group)
                for p2_el_idx in xrange(0, len(P2[0])):
                    p2_swapped_group = swap_group(p2_el_idx, P2)
                    p2_result = multiple_group(p3_result, p2_swapped_group)
                    for p5_el_idx in xrange(0, len(P5[0])):
                        p5_swapped_group = swap_group(p5_el_idx, P5)
                        result = multiple_group(p2_result, p5_swapped_group)
                        result = list(result)
                        results.append(result)
                        iteration_text = u'P7(%d)P3(%d)P2(%d)P5(%d)' % (p7_el_idx, p3_el_idx, p2_el_idx, p5_el_idx)
                        formatted_result = {"iteration": iteration_text, "result": result}
                        formatted_output = iteration_text + " - " + str(result) + "\n"
                        formatted_output_file.writelines(formatted_output)
                        formatted_results.append(formatted_result)
                        if not unique_results.__contains__(result):
                            unique_results.append(result)
                            unique_formatted_results.append(formatted_result)
                            formatted_unique_output_file.writelines(formatted_output)

print(u'Elements processed=%d\n' % (len(results)))
print(u'Unique results=%d\n') % (len(unique_results))


def comp(list1, list2):
    for val in list1:
        if val in list2:
            return True
    return False


for el in unique_results:
    for el_2 in unique_results:
        new_el = multiple_group(el, el_2)
        if unique_results.__contains__(new_el):
            print new_el
first_unique = unique_results[1]
print str(first_unique) + "\n"
second_unique = unique_results[1]
print str(second_unique) + "\n"
new_el = multiple_group(first_unique, second_unique)
print str(new_el) + "\n"

first_unique = unique_results[15]
print str(first_unique) + "\n"
second_unique = unique_results[123]
print str(second_unique) + "\n"
new_el = multiple_group(first_unique, second_unique)
print str(new_el) + "\n"
