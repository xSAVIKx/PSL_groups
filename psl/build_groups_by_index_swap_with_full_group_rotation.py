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
    for i1, i2 in zip(indexes_to_swap, original_index):
        swappable_copy[i1 - 1] = swappable[i2 - 1]
    return swappable_copy


def swap_group(swappable, rotation_index, group):
    result = copy.copy(swappable)
    for element in group:
        deq = deque(element)
        deq.rotate(rotation_index)
        result = makeSwap(result, element, deq)
    return result


swappable = copy.copy(first_group_element)
rotated = swap_group(swappable, 0, P5)

with open('./build_groups_by_index_swap_with_full_group_rotation_unique.txt', 'w+') as formatted_unique_output_file:
    with open('./build_groups_by_index_swap_with_full_group_rotation.txt', 'w+') as formatted_output_file:
        for p7_el_idx in xrange(0, len(P7[0])):
            swappable = copy.copy(first_group_element)
            swappable = swap_group(swappable, p7_el_idx, P7)
            for p3_el_idx in xrange(0, len(P3[0])):
                swappable = swap_group(swappable, p3_el_idx, P3)
                for p2_el_idx in xrange(0, len(P2[0])):
                    swappable = swap_group(swappable, p2_el_idx, P2)
                    for p5_el_idx in xrange(0, len(P5[0])):
                        swappable = swap_group(swappable, p5_el_idx, P5)
                        result = list(swappable)
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
        if not comp(el, el_2):
            new_el = makeSwap(el, el, el_2)
            if unique_results.__contains__(new_el):
                print new_el
first_unique = unique_results[101]
print str(first_unique) + "\n"
second_unique = unique_results[101]
print str(second_unique) + "\n"
new_el = makeSwap(first_unique, first_unique, second_unique)
print str(new_el) + "\n"
