from collections import deque

from psl.PSL_constants import P3, P2, P5, P7

results = []
formatted_results = []
with open('./build_groups_by_concatenation.txt', 'w+') as formatted_output_file:
    for p7_el_idx, p7_el in enumerate(P7):
        p7_el_deq = deque(p7_el)
        for p7_el_deq_i in xrange(0, len(p7_el_deq)):
            p7_rotated_el_deq = deque(p7_el_deq)
            p7_rotated_el_deq.rotate(p7_el_deq_i)
            for p3_el_idx, p3_el in enumerate(P3):
                p3_el_deq = deque(p3_el)
                for p3_el_deq_i in xrange(0, len(p3_el_deq)):
                    p3_rotated_el_deq = deque(p3_el_deq)
                    p3_rotated_el_deq.rotate(p3_el_deq_i)
                    for p2_el_idx, p2_el in enumerate(P2):
                        p2_el_deq = deque(p2_el)
                        for p2_el_deq_i in xrange(0, len(p2_el_deq)):
                            p2_rotated_el_deq = deque(p2_el_deq)
                            p2_rotated_el_deq.rotate(p2_el_deq_i)
                            for p5_el_idx, p5_el in enumerate(P5):
                                p5_el_deq = deque(p5_el)
                                for p5_el_deq_i in xrange(0, len(p5_el_deq)):
                                    p5_rotated_el_deq = deque(p5_el_deq)
                                    p5_rotated_el_deq.rotate(p5_el_deq_i)
                                    result = [tuple(p7_rotated_el_deq), tuple(p3_rotated_el_deq), tuple(p2_rotated_el_deq), tuple(p5_rotated_el_deq)]
                                    results.append(result)
                                    iteration_text = u'P7_%d(%d)P3_%d(%d)P2_%d(%d)P5_%d(%d)' % (
                                        p7_el_idx, p7_el_deq_i, p3_el_idx, p3_el_deq_i, p2_el_idx, p2_el_deq_i, p5_el_idx, p5_el_deq_i)
                                    formatted_result = {"iteration": iteration_text, "result": result}
                                    formatted_output = iteration_text + " - " + str(result) + "\n"
                                    formatted_output_file.writelines(formatted_output)
                                    formatted_results.append(formatted_result)
print(u'Elements processed=%d' % (len(results)))
