 import psycopg2


def get_parts():
    """ query parts from the parts table """
    conn = None
    try:
        conn = psycopg2.connect(host="127.0.0.1", user="postgres", password="subhashree10", dbname="codebinge", port="5432")
        cur = conn.cursor()
        cur.execute("SELECT city_name FROM cities ORDER BY city_name")
        rows = cur.fetchall()
        print("The number of cities: ", cur.rowcount)
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_parts()
