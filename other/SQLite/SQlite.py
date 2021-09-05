import sqlite3


def write_data_to_db(connection, query, data):
    try:
        with connection:
            connection.executemany(query, data)
    except sqlite3.IntegrityError as e:
        print('Error occured: ', e)
        return False
    else:
        print('Запись данных прошла успешно')
        return True    


def get_all_from_db(connection, query):
    result = [row for row in connection.execute(query)]
    return result



if __name__ == '__main__':
    conn = sqlite3.connect('dhcp_snooping.db')

    conn.execute('''create table if not exists switch(mac text not NULL primary key,
    hostname text, model text,
    location text)''')

    data = [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
            ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
            ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
            ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]

    query_insert = 'INSERT into switch values (?, ?, ?, ?)'
    query_get_all = 'SELECT * from switch'

##    write_data_to_db(conn, query_insert, data)
    print(get_all_from_db(conn, query_get_all))
    
    
    conn.close()
