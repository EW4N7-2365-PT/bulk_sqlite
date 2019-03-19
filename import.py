import sqlite3
import os
from base import BASE


def read_from_csv(filename: str) -> str:
    f = open(filename)
    while True:
        data = f.readline()
        if not data:
            break
        yield data


def prepare_db(db):
    db.execute('''CREATE TABLE wild_gangster
             (id integer primary key ,data text
             )''')
    db.commit()


def import_csv(filename: str) -> int:
    conn = sqlite3.connect(f"dbs/{filename[:-4]}.db")
    c = conn.cursor()
    prepare_db(conn)
    for line in read_from_csv(filename):
        identifier, *data = line.split(',')
        data = ':'.join(data).replace('\n', '')
        c.execute('''
            INSERT INTO wild_gangster(id,data)  VALUES (?,?)
            ''', (int(identifier) + 1, data))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    if not os.path.exists(os.path.join(BASE, 'dbs')):
        os.mkdir(os.path.join(BASE, 'data'))
    import_csv('wild_gangster.csv')
