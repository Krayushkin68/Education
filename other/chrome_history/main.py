import datetime
import sqlite3

TIMEZONE = 3


def timestamp_to_date(timestamp):
    return datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=timestamp, hours=TIMEZONE)


def date_to_timestamp(date):
    epoch_start = datetime.datetime(1601, 1, 1)
    dif = date - epoch_start - datetime.timedelta(hours=TIMEZONE)
    return int(f'{dif.days * 60 * 60 * 24 + dif.seconds}{dif.microseconds:06d}')


def check_url(con, cursor, url, visit_time):
    cursor.execute("select id, visit_count, last_visit_time from urls where url = (?)", (url,))
    res = cursor.fetchone()
    print(res)
    if res:
        id = res[0]
        visit_count = int(res[1])
        last_visit_time = res[2]
        if timestamp_to_date(last_visit_time) < visit_time:
            cursor.execute("update urls set visit_count = (?), last_visit_time = (?) where id = (?)",
                           (visit_count + 1, date_to_timestamp(visit_time), id))
            con.commit()
        else:
            cursor.execute("update urls set visit_count = (?) where id = (?)",
                           (visit_count + 1, id))
            con.commit()
        return id
    else:
        return False


def add_history_row(url, visit_time):
    path_url = r'C:\Users\Krayu\AppData\Local\Google\Chrome\User Data\Default\History'
    # path_url = r'data/History'
    try:
        con = sqlite3.connect(path_url)
        con.execute("PRAGMA foreign_keys = 1")
        cursor = con.cursor()

        # Get url_id by url or create new
        url_id = check_url(con, cursor, url, visit_time)
        if url_id:
            query = 'insert into visits (url, visit_time, from_visit, transition, segment_id) values (?, ?, ?, ?, ?)'
            cursor.execute(query, (url_id, date_to_timestamp(visit_time), 0, 805306368, 0))
            con.commit()

        cursor.close()
        con.close()
    except sqlite3.Error as e:
        print('Error: ', e)
    finally:
        if con:
            con.close()


def show_visits():
    path_url = r'C:\Users\Krayu\AppData\Local\Google\Chrome\User Data\Default\History'
    try:
        con = sqlite3.connect(path_url)
        con.execute("PRAGMA foreign_keys = 1")
        cursor = con.cursor()
        cursor.execute('select * from visits')
        res = cursor.fetchall()
        [print(i) for i in res]
        cursor.close()
        con.close()
    except sqlite3.Error as e:
        print('Error: ', e)
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    date = datetime.datetime(2021, 10, 26, 13, 48, 13, 333)
    add_history_row('https://youtube.com/', date)
    # show_visits()
