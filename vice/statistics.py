import psycopg2

def get_job_statistics(job_id):
    conn = _get_postgres_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * from jobs")
    print(cursor.fetchone())
    return {}

def _get_postgres_connection():
    return psycopg2.connect(host="postgres", port="5432", dbname="vice", user="vice", password="vice")