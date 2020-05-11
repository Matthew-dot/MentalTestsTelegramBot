from sqlalchemy import create_engine, MetaData, Table, Column, Integer


engine = create_engine("sqlite:///data.db")
meta = MetaData(bind=engine)

users = Table(
    "users",
    meta,
    Column("id", Integer),
    Column("how_many_state", Integer, default=0),
    Column("how_many_result", Integer, default=0),
    Column("uncertainty_state", Integer, default=0),
    Column("uncertainty_result", Integer, default=0)
)
meta.create_all()
conn = engine.connect()

def create_new_user(id):
    s = users.select().where(users.c.id == id)
    r = conn.execute(s)
    if not r.first():
        ins = users.insert().values(id = id)
        conn.execute(ins)


def get_test_state(id, test_name):
    s = users.select().where(users.c.id == id)
    r = conn.execute(s)
    return r.first()[test_name + "_state"]


def get_test_result(id, test_name):
    s = users.select().where(users.c.id == id)
    r = conn.execute(s)
    return r.first()[test_name + "_result"]


def update_test(id, test_name, plus_result):
    u = users.update().where(users.c.id == id).values({test_name + "_state": get_test_state(id, test_name) + 1,
                                               test_name + "_result": get_test_result(id, test_name) + plus_result})
    conn.execute(u)


def reset_test(id, test_name):
    u = users.update().where(users.c.id == id).values({test_name + "_state": 0,
                                                       test_name + "_result": 0})
    conn.execute(u)