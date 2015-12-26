import copy
import hashlib
from collections import deque

from psl.PSL_constants import P5, P7, P3, P2


class ResultHolder(object):
    def __init__(self, result_list):
        self.result_list = result_list

    def __hash__(self):
        return int(hashlib.md5(str(self.result_list)).hexdigest(), 16)

    def __str__(self):
        return str(self.result_list)


results = []
formatted_results = []
first_group_element = deque(range(1, 22))


def swap(swappable, i1, i2):
    swappable_copy = copy.copy(swappable)
    swappable_copy[i1] = swappable[i2]


def makeSwap(swappable, original_index, indexes_to_swap):
    swappable_copy = copy.copy(swappable)
    for i1, i2 in zip(original_index, indexes_to_swap):
        swappable_copy[i1 - 1] = swappable[i2 - 1]
    return swappable_copy


def comp(list1, list2):
    for val in list1:
        if val in list2:
            return True
    return False


swappable = copy.copy(first_group_element)
print swappable
p2_0 = copy.copy(P2[0])
p2_0_rotated_deque = deque(p2_0)
p2_0_rotated_deque.rotate(1)
swapped_deque = makeSwap(swappable, p2_0, p2_0_rotated_deque)

p5_0 = copy.copy(P5[0])
p5_0_rotated_deque = deque(p5_0)
p5_0_rotated_deque.rotate(1)
swapped_deque = makeSwap(swapped_deque, p5_0, p5_0_rotated_deque)
print swapped_deque

with open('./build_groups_by_index_swap.txt', 'w+') as formatted_output_file:
    for p7_el_idx, p7_el in enumerate(P7):
        swappable = copy.copy(first_group_element)
        p7_el_deq = deque(p7_el)
        for p7_el_deq_i in xrange(0, len(p7_el_deq)):
            p7_rotated_el_deq = deque(p7_el_deq)
            p7_rotated_el_deq.rotate(p7_el_deq_i)
            swapped_deque = makeSwap(swappable, p7_el_deq, p7_rotated_el_deq)
            for p3_el_idx, p3_el in enumerate(P3):
                p3_el_deq = deque(p3_el)
                for p3_el_deq_i in xrange(0, len(p3_el_deq)):
                    p3_rotated_el_deq = deque(p3_el_deq)
                    p3_rotated_el_deq.rotate(p3_el_deq_i)
                    swapped_deque = makeSwap(swapped_deque, p3_el_deq, p3_rotated_el_deq)
                    for p2_el_idx, p2_el in enumerate(P2):
                        p2_el_deq = deque(p2_el)
                        for p2_el_deq_i in xrange(0, len(p2_el_deq)):
                            p2_rotated_el_deq = deque(p2_el_deq)
                            p2_rotated_el_deq.rotate(p2_el_deq_i)
                            swapped_deque = makeSwap(swapped_deque, p2_el_deq, p2_rotated_el_deq)
                            for p5_el_idx, p5_el in enumerate(P5):
                                p5_el_deq = deque(p5_el)
                                for p5_el_deq_i in xrange(0, len(p5_el_deq)):
                                    p5_rotated_el_deq = deque(p5_el_deq)
                                    p5_rotated_el_deq.rotate(p5_el_deq_i)
                                    swapped_deque = makeSwap(swappable, p5_el_deq, p5_rotated_el_deq)
                                    result = ResultHolder(list(swapped_deque))
                                    results.append(result)
                                    iteration_text = u'P7_%d(%d)P3_%d(%d)P2_%d(%d)P5_%d(%d)' % (
                                        p7_el_idx, p7_el_deq_i, p3_el_idx, p3_el_deq_i, p2_el_idx, p2_el_deq_i, p5_el_idx, p5_el_deq_i)
                                    formatted_result = {"iteration": iteration_text, "result": result}
                                    formatted_output = iteration_text + " - " + str(result) + "\n"
                                    formatted_output_file.writelines(formatted_output)
                                    formatted_results.append(formatted_result)
print(u'Elements processed=%d\n' % (len(results)))
unique_results = dict()
for result in results:
    unique_results[result] = unique_results.get(result, 0) + 1

print(u'Unique results=%d\n') % (len(unique_results))
with open('./build_groups_by_index_swap_unique.txt', 'w+') as formatted_output_file:
    for result, amount in unique_results.items():
        formatted_output_file.writelines(str(result) + " - " + str(amount) + '\n')
