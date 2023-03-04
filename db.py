import psycopg2
from psycopg2.extras import RealDictCursor


def select_all(query):
    conn = psycopg2.connect("dbname=project_two")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def select_all_pets(query,params):
    conn = psycopg2.connect("dbname=project_two")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query,params)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def select_one(query, params):
    conn = psycopg2.connect("dbname=project_two")
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(query, params)
    result = cur.fetchone()
    return result

def update(query, params):
    conn = psycopg2.connect("dbname=project_two")
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    conn.close()

def insert(query, params):
    conn = psycopg2.connect("dbname=project_two")
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    conn.close()

    
