import sqlite3


def write_data_to_db(connection, query, data):
    for i in data:
        try:
            with connection:
                connection.execute(query, i)
        except sqlite3.IntegrityError as e:
            print(f'{i}: ошибка записи', e)
            continue
        else:
            print(f'{i}: запись данных прошла успешно')
            continue    


def get_all_from_db(connection, query):
    result = [row for row in connection.execute(query)]
    return result



if __name__ == '__main__':
    conn = sqlite3.connect('air.db')

##    conn.execute('''create table if not exists aircrafts
##                        (aircraft_code char(3) NOT NULL PRIMARY KEY,
##                         model text NOT NULL,
##                         range integer NOT NULL CHECK (range > 0));''')

##    data = [('SU9', 'Sukhoi SuperJet-100', 3000),
##            ('ND8', 'Samolet', 1200),
##            ('KN3', 'IL-120', 5300),
##            ('OR1', 'Boieng', 6500)]
##    query_insert = 'INSERT into aircrafts values (?, ?, ?)'
##    write_data_to_db(conn, query_insert, data)

##    conn.execute('''CREATE TABLE if not exists seats
##                        (aircraft_code char(3) NOT NULL,
##                         seat_no varchar(4) NOT NULL,
##                         fare_conditions varchar(10) NOT NULL,
##                         FOREIGN KEY (aircraft_code) REFERENCES aircrafts (aircraft_code) ON DELETE CASCADE
##                         PRIMARY KEY(aircraft_code, seat_no));''')

##    data = [( 'SU9', '4A', 'Business' ),
##            ( 'ND8', '4B', 'Business' ),
##            ( 'ND8', '40A', 'Economy' ),
##            ( 'KN3', '40B', 'Economy' ),
##            ( 'KN3', '40F', 'Economy' ),
##            ( 'OR1', '43F', 'Economy' )]
##    query_insert = 'INSERT into seats values (?, ?, ?)'
##    write_data_to_db(conn, query_insert, data)
    
    query_get_all = 'SELECT * from aircrafts'
    print(get_all_from_db(conn, query_get_all))
    
    query_get_all = 'SELECT * from seats'
    print(get_all_from_db(conn, query_get_all))
    
    conn.commit()
##    conn.close()
