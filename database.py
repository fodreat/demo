import sqlite3
import hashlib
def connect_bd():
    conn=sqlite3.connect('shoes.db')
    conn.execute("PRAGMA foregion_keys = ON")
    return conn

def has_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_tables():
    conn=connect_bd()
    cur=conn.cursor()


    cur.execute("""
    CREATE TABLE IF NOT EXISTS roles(
        id integer primary key autoincrement,
        role_name varchar(20) not null
        )""")
    cur.execute("""
       CREATE TABLE IF NOT EXISTS users(
           id integer primary key autoincrement,
           Login varchar(50) not null,
           password_hash varchar(255),
           role_id integer not null,
           foreign key (role_id) references roles(id)
           )""")

    cur.execute("""
           CREATE TABLE IF NOT EXISTS products(
               id integer primary key autoincrement,
               name varchar(50) not null,
               article varchar,
               price integer not null,
               size integer not null,
               brent varchar(30),
               quanty integer
               )
              """)

    cur.execute("""
            CREATE TABLE IF NOT EXISTS orders(
                id integer primary key autoincrement,
                user_id integer not null,
                date varchar(25),
                status varchar(20) not null,
                total_amount integer not null,
                foreign key (user_id) references users(id)
                )
               """)


    cur.execute("""
                CREATE TABLE IF NOT EXISTS ordersItems(
                    id integer primary key autoincrement,
                    order_id integer not null,
                    product_id integer not null,
                    count varchar(250),
                    price_at_moment integer not null,
                    foreign key (order_id) references orders(id),
                    foreign key (product_id) references products(id)
                )
                   """)

    conn.commit()
    cur.execute("SELECT COUNT (*) FROM roles")
    if cur.fetchone()[0]==0:
        cur.executemany("INSERT INTO roles(role_name) VALUES(?)",
        [('guest',), ('client',), ('manager',), ('admin',)])
    cur.execute("SELECT COUNT (*) FROM users")
    if cur.fetchone()[0]==0:
        cur.executemany("INSERT INTO users(login,password_hash,role_id) VALUES(?,?,?)",
                        [
                            ('admin', has_password('admin'), 4),
                            ('manager', has_password('manager'), 3),
                            ('client', has_password('client'), 2),
                            ('client2', has_password('admin'), 2),
                        ]
                        )
    cur.execute("SELECT COUNT(*) FROM products")
    if cur.fetchone()[0] == 0:
        cur.executemany(
            "INSERT INTO products(name, article, price, size, brent, quanty) VALUES (?,?,?,?,?,?)",
            [
                ('Кроссовки Air Max', 'SH001', 8500, 42, 'Nike', 15),
                ('Кроссовки Ultraboost', 'SH002', 12000, 43, 'Adidas', 8),
                ('Ботинки зимние', 'SH003', 15000, 41, 'Timberland', 12),
                ('Туфли классические', 'SH004', 7000, 40, 'Geox', 20),
                ('Сандалии летние', 'SH005', 5500, 39, 'Birkenstock', 25),
                ('Кеды повседневные', 'SH006', 4500, 42, 'Converse', 30),
                ('Кроссовки беговые', 'SH007', 9500, 44, 'Asics', 10),
                ('Сапоги осенние', 'SH008', 13000, 38, 'Ecco', 7),
                ('Мокасины кожаные', 'SH009', 6500, 41, 'Clarks', 18),
                ('Кроссовки Stan Smith', 'SH010', 7500, 42, 'Adidas', 22),
            ])
    conn.commit()
create_tables()