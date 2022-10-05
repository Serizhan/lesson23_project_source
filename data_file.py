
def open_file():
    with open('data/apache_logs.txt') as file:
        return list(map(lambda x: x.strip(' '), file))

def make_query(data, param):
    pass