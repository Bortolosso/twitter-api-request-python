import pandas as pd
import psycopg2


def init_connection(data_lead):
    df = pd.DataFrame(data_lead)
    for col in df.columns:
        df[col] = df[col].apply(str)
        
    sql = 'DROP TABLE IF EXISTS public.twitter'
    create_db(sql)
    sql = '''CREATE TABLE public.twitter 
        (  
            id_file           character varying(300), 
            id_track          character varying(300), 
            track_name        character varying(300), 
            size_bytes        character varying(300), 
            prime_genre       character varying(300), 
            rating_count_tot  character varying(300), 
            n_citacoes        character varying(300)
        )'''
    create_db(sql)
    
    for i in df.index:
        values =  "VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}');".format(df['id_file'][i], df['id_track'][i], df['track_name'][i], df['size_bytes'][i], df['prime_genre'][i], df['rating_count_tot'][i], df['n_citacoes'][i])
        sql = "INSERT INTO public.twitter (id_file, id_track, track_name, size_bytes, prime_genre, rating_count_tot, n_citacoes) {0}".format(values)
        insert_db(sql)
    
    query_db('SELECT * FROM public.twitter')
    
    print('Dados inseridos no banco com sucesso !')


def connect_db():
    con = psycopg2.connect(
        host='localhost', 
        database='products',
        user='username',
        password='password'
    )
    
    return con


def create_db(sql):
    con = connect_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()
    
    
def insert_db(sql):
    con = connect_db()
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()
    
    
def query_db(sql):
    con = connect_db()
    cur = con.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    registros = []
    for rec in recset:
        registros.append(rec)
    con.close()
    return registros