def only_diff_elements(set_1, set_2):
    value1 = set_1.difference(set_2)
    value2 = set_2.difference(set_1)
    combine = value1.union(value2)
    return combine
