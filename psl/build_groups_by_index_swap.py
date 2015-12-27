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


with open('./build_groups_by_index_swap_unique.txt', 'w+') as formatted_unique_output_file:
    with open('./build_groups_by_index_swap.txt', 'w+') as formatted_output_file:
        for p7_el_idx, p7_el in enumerate(P7):
            swappable = copy.copy(first_group_element)
            for p7_el_deq_i in xrange(0, len(p7_el)):
                p7_rotated_el_deq = deque(p7_el)
                p7_rotated_el_deq.rotate(p7_el_deq_i)
                swapped_deque = makeSwap(swappable, p7_el, p7_rotated_el_deq)
                for p3_el_idx, p3_el in enumerate(P3):
                    for p3_el_deq_i in xrange(0, len(p3_el)):
                        p3_rotated_el_deq = deque(p3_el)
                        p3_rotated_el_deq.rotate(p3_el_deq_i)
                        swapped_deque = makeSwap(swapped_deque, p3_el, p3_rotated_el_deq)
                        for p2_el_idx, p2_el in enumerate(P2):
                            for p2_el_deq_i in xrange(0, len(p2_el)):
                                p2_rotated_el_deq = deque(p2_el)
                                p2_rotated_el_deq.rotate(p2_el_deq_i)
                                swapped_deque = makeSwap(swapped_deque, p2_el, p2_rotated_el_deq)
                                for p5_el_idx, p5_el in enumerate(P5):
                                    for p5_el_deq_i in xrange(0, len(p5_el)):
                                        p5_rotated_el_deq = deque(p5_el)
                                        p5_rotated_el_deq.rotate(p5_el_deq_i)
                                        swapped_deque = makeSwap(swapped_deque, p5_el, p5_rotated_el_deq)
                                        result = list(swapped_deque)
                                        results.append(result)
                                        iteration_text = u'P7_%d(%d)P3_%d(%d)P2_%d(%d)P5_%d(%d)' % (
                                            p7_el_idx, p7_el_deq_i, p3_el_idx, p3_el_deq_i, p2_el_idx, p2_el_deq_i, p5_el_idx, p5_el_deq_i)
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
