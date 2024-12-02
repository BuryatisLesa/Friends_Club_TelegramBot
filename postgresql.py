import psycopg2


# creating db in PostgreSQL
def create_database_postgresql(namedb):
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"CREATE DATABASE {namedb}")
        print(f"DB '{namedb}' success created!")
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Error at creating DB: {e}")


# # connection of DB
# with psycopg2.connect(
#     dbname="friendsclub",
#     user="postgres",
#     password="postgres",
#     host="localhost",
#     port="5432"
# ) as conn:
#     with conn.cursor() as cur:
#         # creating tabel animals
#         cur.execute('''
#             CREATE TABLE IF NOT EXISTS animals (
#                 animal_id SERIAL PRIMARY KEY,
#                 name VARCHAR(500) NOT NULL
#             );
#         ''')

#         # creating tabel questions
#         cur.execute('''
#             CREATE TABLE IF NOT EXISTS questions (
#                 id SERIAL PRIMARY KEY,
#                 question TEXT,
#                 animal_id INT,
#                 FOREIGN KEY (animal_id) REFERENCES animals(animal_id)
#             );
#         ''')

#         conn.commit()
