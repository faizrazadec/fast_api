import psycopg

with psycopg.connect("dbname=postgres user=faizrazadec") as conn:
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                    id serial primary key,
                    name varchar not null,
                    email varchar not null)
            """)
        users = [
            ('John Doe', 'johndoe@mail.com'),
            ('Sam Doe', 'samdoe@mail.com'),
            ('Doe John', 'doejohn@mail.com'),
            ('Smith Doe', 'smithdoe@mail.com'),
            ('John Bar', 'johnbar@mail.com'),
            ('Emily Chen', 'emilychen@mail.com'),
            ('Michael Davis', 'michaeldavis@mail.com'),
            ('Sophia Lee', 'sophialee@mail.com'),
            ('William Brown', 'williambrown@mail.com'),
            ('Olivia Taylor', 'oliviataylor@mail.com'),
            ('James Wilson', 'jameswilson@mail.com'),
            ('Ava Martin', 'avamartin@mail.com'),
            ('Robert Thompson', 'robertthompson@mail.com'),
            ('Isabella Garcia', 'isabellagarcia@mail.com'),
            ('Richard Harris', 'richardharris@mail.com'),
            ('Mia Rodriguez', 'miarodriguez@mail.com'),
            ('Charles Lewis', 'charleslewis@mail.com'),
            ('Charlotte Walker', 'charlottewalker@mail.com')
            ]
        
        for user in users:
            cur.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s)",
                user
            )

        cur.execute("SELECT * FROM users")
        cur.fetchall()

        for record in cur:
            print(record)

        conn.commit()