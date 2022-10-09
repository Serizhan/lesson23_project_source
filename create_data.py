import functions


check_data = {
    'filter': functions.filter_query,
    'map': functions.map_query,
    'unique': functions.unique_query,
    'sort': functions.sort_query,
    'limit': functions.limit_query,
    'regex': functions.regex,
}


def build_query(cmd, param, data):
    if data is None:
        with open('data/apache_logs.txt') as file:
            prepared_data = list(map(lambda x: x.strip(), file))
    else:
        prepared_data = data

    return check_data[cmd](param=param, data=prepared_data)
