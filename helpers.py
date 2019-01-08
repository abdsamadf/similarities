from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""
    # before submitting again look at it

    matrix = []
    h = len(a) + 1
    w = len(b) + 1
    # matrix = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    # generating a empty 2d list
    for i in range(h):
        matrix.append([0 for i in range(w)])
        # 0 or (0, None)
    # for i in range(h):
    #     s = []
    #     for j in range(w):
    #         s.append((0, None))
    #     matrix.append(s)
    matrix[0][0] = (0, None)

    # base cases
    for i in range(1, h):
        matrix[i][0] = (i, Operation.DELETED)

    for i in range(1, w):
        matrix[0][i] = (i, Operation.INSERTED)

    # filling the other entries in the table
    for j in range(1, w):
        for i in range(1, h):
            cost_deleted = matrix[i - 1][j][0] + 1
            cost_inserted = matrix[i][j - 1][0] + 1
            if (a[i - 1] == b[j - 1]):
                # ith char of a is jth char of b
                cost_subsituted = matrix[i - 1][j - 1][0]
            else:
                cost_subsituted = matrix[i - 1][j - 1][0] + 1

            costs = [cost_deleted, cost_inserted, cost_subsituted]
            operations = [Operation.DELETED, Operation.INSERTED, Operation.SUBSTITUTED]

            # find min_index of min_value
            min_index, min_value = min(enumerate(costs), key=lambda x: x[1])

            # matrix store (cost, operation)
            matrix[i][j] = (min_value, operations[min_index])
    return matrix
