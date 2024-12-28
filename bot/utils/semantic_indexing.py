from collections import OrderedDict


def first_value[V](ordered_dictionary: OrderedDict[object, V]) -> V:
    return next(iter(ordered_dictionary.values()))