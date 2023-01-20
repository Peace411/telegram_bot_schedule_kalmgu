
import pymssql

con = pymssql.connect(host="",
                      user="",
                      password="",
                      database="",
                      port=17160
                      )

def post_id(ct_id,group_id):
    cur = con.cursor()
    cur.execute(f'INSERT INTO specialization ("ct_id", "group_id") VALUES ({ct_id},{group_id})')
    con.commit()
    return 'ok'
def get_notification(ct_id):
    cur = con.cursor()
    cur.execute(f"SELECT * FROM specialization WHERE ct_id={int(ct_id)}")
    r= cur.fetchall()
    for row in r:
        return row[2]
def get_all_on_notifaction():
    cur = con.cursor()
    cur.execute(f"SELECT * FROM specialization WHERE notification={1}")
    r = cur.fetchall()
    print(r)
    return r
def post_notification(ct_id,switch):
    cur = con.cursor()
    cur.execute(f"UPDATE specialization SET notification={switch}  WHERE ct_id={int(ct_id)}")
    con.commit()
def reset(ct_id):
    cur = con.cursor()
    cur.execute(f'DELETE FROM specialization WHERE ct_id={int(ct_id)}')
    con.commit()
def get_id(ct_id):
    try:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM specialization WHERE ct_id={int(ct_id)}")
        r= cur.fetchall()
        for row in r:
            print(row)
            return row[1]

    except :
        return '0'
