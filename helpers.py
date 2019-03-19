import sqlite3
from typing import List
import os


def retrieve_for_id(identifier: int, table: str) -> List[int]:
    conn = sqlite3.connect(f"dbs/{table}.db")
    c = conn.cursor()
    data = c.execute(f'SELECT * FROM {table} where id = {identifier}')
    data = data.fetchone()
    return data[1].split(':')


if __name__ == '__main__':
    print(retrieve_for_id(300, 'wild_gangster'))
