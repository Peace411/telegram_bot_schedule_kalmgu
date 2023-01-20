from mysql import client_mysql

group = dict(physics_3='26247', physics_2='26248', physics_4='26246', physics_1='26650', matem_1='26618',
             matem_2='26242', matem_3='0', matem_4='0',ib_1='26676',ib_2='0',ib_3='26249',ib_4='0')


def matem_group(call):
    if call.data == 'matem_3':
        client_mysql.post_id(call.from_user.id, group.get('matem_3'))

    elif call.data == 'matem_2':
        client_mysql.post_id(call.from_user.id, group.get('matem_2'))

    elif call.data == 'matem_1':
        client_mysql.post_id(call.from_user.id, group.get('matem_1'))

    elif call.data == 'matem_4':
        client_mysql.post_id(call.from_user.id, group.get('matem_4'))

def ib_group(call):
    if call.data == 'ib_3':
        client_mysql.post_id(call.from_user.id, group.get('ib_3'))

    elif call.data == 'ib_2':
        client_mysql.post_id(call.from_user.id, group.get('ib_2'))

    elif call.data == 'ib_1':
        client_mysql.post_id(call.from_user.id, group.get('ib_1'))

    elif call.data == 'ib_4':
        client_mysql.post_id(call.from_user.id, group.get('ib_4'))

def physics_group(call):
    if call.data == 'physics_3':
        client_mysql.post_id(call.from_user.id, group.get('physics_3'))
    elif call.data == 'physics_2':
        client_mysql.post_id(call.from_user.id, group.get('physics_2'))
    elif call.data == 'physics_1':
        client_mysql.post_id(call.from_user.id, group.get('physics_1'))
    elif call.data == 'physics_4':
        client_mysql.post_id(call.from_user.id, group.get('physics_4'))

