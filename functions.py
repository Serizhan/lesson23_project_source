import re


def filter_query(param: str, data):
    return list(filter(lambda x: param in x, data))


def map_query(param: str, data):
    return list(map(lambda x: x.split(' ')[int(param)], data))


def unique_query(data, *args, **kwargs):
    return list(set(data))


def sort_query(param: str, data):
    if param == 'asc':
        reverse = False
    else:
        reverse = True
    return sorted(data, reverse=reverse)


def limit_query(param: str, data):
    return list(data)[:int(param)]


def regex(param: str, data):
    result = []
    for i in data:
        pre_regex = re.compile(param)
        total = pre_regex.search(i)
        if total:
            result.append(i)
    return result
