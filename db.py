import sqlite3 as sqlt

db_name = 'message_id_DB.db'


def start_db():
    base = sqlt.connect(db_name)
    base.execute('CREATE TABLE IF NOT EXISTS "pubId" ("id"	INTEGER NOT NULL UNIQUE,'
                 '"public_id"     BLOB,'
                 'PRIMARY KEY("id" AUTOINCREMENT))')
    base.commit()


def add_id(id):
    with sqlt.connect(db_name) as conn:
        cur = conn.cursor()
        data = cur.execute('SELECT public_id from pubId WHERE public_id = ?', (id,)).fetchall()
        if not data:
            cur.execute('INSERT INTO pubId VALUES (null, ?)', (id,))
            return True
        else:
            return False


def get_all_id():
    with sqlt.connect(db_name) as conn:
        cur = conn.cursor()
        text = cur.execute('SELECT public_id from pubId').fetchall()
    return text
