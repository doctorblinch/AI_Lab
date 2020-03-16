from bucket_problem import *


if __name__ == '__main__':
    starting_node = Node(data=(0, 0))
    answers = [get_node_parent_history(answer, []) for answer in DLS(starting_node, check_optimum, 15)]
    answers.sort(key=lambda ans: len(ans))

    with open('answer.txt', 'w') as f:
        f.write('Program found {} solutions.\n\n'.format(len(answers)))
        for answer in answers:
            output = '\n\n\n{}\n\n'.format('#' * 100) + str(len(answer)) + ' ' + str(answer)
            f.write(output)
            print(output)
