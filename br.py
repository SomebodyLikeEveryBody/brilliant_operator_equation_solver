import itertools

#########################
def get_combinations(p_array_nbs, p_array_operations):
    """
    Returns a list of all combinations of the given operations, like
    ['+', '+', '+', '+'] ['+', '+', '+', '-'] ['+', '-', '+', '+'] ['+', '*', '-', '/']
    etc

    Of course, if we have n given numbers, there will be n-1 operators to put between each
    side-by-side numbers

    :param: p_array_nbs: list containing all numbers to compose with, as int, float or strings, for example, [0.5, 1, 2, 3.5], or [0.5, 0.5, 0.5, 0.5]
    :type: p_array_nbs: list
    :param: p_array_operations: list containing all possible operations we can use, as strings. For example, ['+', '-', '*']
    :type: p_array_operations: list
    :return: a list of all combinations of the given operations
    :rtype: list
    """
    return (list(itertools.product(p_array_operations, repeat=len(p_array_nbs) - 1)))


def generate_expression(p_array_nbs, p_list_operations):
    """
    Takes a list of numbers, a list of operations and returns a string of the
    corresponding operations.

    For example, takes [1, 2, 3, 4] and ['+', '-', '-']
    and returns '1 + 2 - 3 - 4'

    Of course, it works if len(p_array_nb) = p_list_operarations) + 1
    to put each operator between each side-by-side numbers

    :param: p_array_nbs: list containing all the numbers of the expression (like [1, 2, 3])
    :type: list
    :param: p_list_operations: array containing all the operators of the expression (like ['+', '*'])
    :type: list
    :return: a string of the generated expression (like "1 + 2 * 3")
    :rtype: string
    """

    ret_expression = ''

    for i in range(0, len(p_array_nbs) - 1):
        ret_expression += p_array_nbs[i] + ' ' + p_list_operations[i] + ' '

    ret_expression += p_array_nbs[-1]

    return ret_expression


def find_expressions(p_nb_target, p_array_nbs, p_array_operations):
    """
    Takes a list of numbers and a list of possibles operations
    test all possibilities and returns the matching possibilities

    :param: p_nb_target: the result of the operation to obtain with the expression
    :type: int
    :param: p_array_nbs:  list containing all the numbers of the operation
    :type: list
    :param: p_array_operations: list containing all the operations we can use in the expression
    :type: list
    :rtype: None
    """

    lists_operations = get_combinations(p_array_nbs, p_array_operations)
    list_results = []

    for list_operations in lists_operations:
        temp_expression = generate_expression(p_array_nbs, list_operations)
        temp_result = eval(temp_expression)

        print('[+] Trying: ' + temp_expression)

        if temp_result == p_nb_target:
            print('==> RESULT FOUND')
            list_results.append(temp_expression + ' = ' + str(p_nb_target))

    print('\n\n--> ' + str(len(list_results)) + ' results found for equation (' + generate_expression(p_array_nbs, ['[?]' for el in p_array_nbs]) + ' =  {0}) with operators {1}:\n\n{2}'.format(p_nb_target, p_array_operations, '\n'.join(list_results)))

if __name__ == "__main__":
    find_expressions(2, ['0.5', '0.5', '0.5', '0.5', '0.5'], ['+', '-', '*', '/'])
