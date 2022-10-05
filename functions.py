def filter_query(param, data):
    return list(filter(lambda x: param in x, data))


def map_query(param, data):
    return list(map(lambda x: x.split(' ')[int(param)], data))


def unique_query(data, *args, **kwargs):
    return list(set(data))


def sort_query(param, data):
    if param == 'asc':
        reverse = False
    else:
        reverse = True
    return sorted(data, reverse=reverse)


def limit_query(param, data):
    return list(data)[:int(param)]
