from flask import Flask
import flask
import json
import pandas as pd
# from sqlalchemy.dialects.mysql import pymysql, mysqldb
import csv
import time
from sqlalchemy import create_engine
from sqlalchemy.types import CHAR,INT
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/index',methods=['POST'])
def index():
    print("connection done")
    print(flask.request.is_json)
    print('before is json')
    if flask.request.is_json:
        print('aaaaa')
        data = flask.request.get_json()
        print(data)
        print('print done')
        country = flask.request.json.get('country')
        year = flask.request.json.get('year')
        creature = flask.request.json.get('creature')
        print("connection done")
        print(country, year, creature)
        db = connect('root','pwd')
        query(creature,country,year,db)
        # time.sleep(5)
    return "done!"



def connect(user,pwd,host="127.0.0.1",port="3306",database="3170project"):
    conn = "mysql+pymysql://{}:{}@{}:{}/{}".format(user,pwd,host,port,database)
    engine = create_engine(conn)
    return engine

def query(creature_n,country_n,year_n,db):

    if len(creature_n) == 0: creature = ''
    else: creature = ' WHERE name="{}"'.format(creature_n)

    if len(country_n) == 0: 
        country = ';'
        country_ano = ''
    else:  
        country = ' WHERE ISO="{}";'.format(country_n)
        country_ano = ' WHERE ISO="{}"'.format(country_n)

    if len(year_n) == 0: year = ') '
    else: 
        if len(creature_n) == 0:year = ' WHERE year={})'.format(year_n)
        else: year = ' AND year={})'.format(year_n)

    command = '''SELECT year, country_and_area, name FROM (SELECT name, trade_ID, year FROM records NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country

    # print(command)
    # all_info = pd.read_sql(command,db)
    # all_info.to_csv('all_table.csv',index=False)

    creature_ = country_=year_ = ''

    if len(country_n) !=0 or len(year_n) != 0:
        creature_ = creature_n+','
    if len(year_n) != 0:
        country_ = country_n+','

    # command_2 = '''SELECT year, country_and_area, name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM creature NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' GROUP BY '''+creature_+country_+year_+" WITH ROLLUP;"

    # print(command_2)
    # count_table = pd.read_sql(command_2,db)
    # count_table.to_csv('count_table.csv',sep='\t',index=False)

    if len(year_n) != 0 and len(country_n) == 0 and len(creature_n) == 0:
        #2 is classfied by country, 3 is by creature
        # command_2 = '''SELECT year, country_and_area,  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM (SELECT trade_ID, year FROM records '''+creature+year+''' AS record NATURAL JOIN recorded_creature'''+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' GROUP BY country_and_area ORDER BY trade_count DESC; '''
        # command_3 = '''SELECT year,  name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM (SELECT trade_ID, year FROM crecords'''+creature+year+'''  AS record NATURAL JOIN recorded_creature AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' GROUP BY name ORDER BY trade_count DESC; '''
        command = '''SELECT year, name, country_and_area  FROM (SELECT name, trade_ID, country_and_area, year FROM (SELECT trade_ID, year FROM records  WHERE year={}) AS record NATURAL JOIN recorded_creature AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country) AS aaaa ;'''.format(
            year_n
        )#16s
        command_2 = '''SELECT year, country_and_area,  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, country_and_area, year FROM (SELECT trade_ID, year FROM records  WHERE year={}) AS record NATURAL JOIN recorded_creature AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country) AS aaaa GROUP BY country_and_area ORDER BY trade_count DESC;'''.format(
            year_n
        )#11.3s
        command_3 = '''SELECT year, name,  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, country_and_area, year FROM (SELECT trade_ID, year FROM records  WHERE year={}) AS record NATURAL JOIN recorded_creature AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country) AS aaaa GROUP BY name ORDER BY trade_count DESC;'''.format(
            year_n
        )#12s
        print(command)
        print(command_2)
        print(command_3)
        country_table = pd.read_sql(command_2,db)
        country_table.to_csv('/Users/endlessio/Downloads/CITESDB_web/public/query_data/country_table.csv',index=False)
        creature_table = pd.read_sql(command_3,db)
        creature_table.to_csv('/Users/endlessio/Downloads/CITESDB_web/public/query_data/creature_table.csv',index=False)
        fakeYear = csv.reader(open('/Users/endlessio/Downloads/CITESDB_web/public/query_data/year_table.csv',"w"))
        writer = csv.writer(fakeYear)
        writer.writerow(("hello", "k"))
        fakeYear.close()
    elif len(country_n) == 0 and len(creature_n) != 0 and len(year_n) == 0:
        #2 is classfied by year, 3 is country
        # command_2 =  '''SELECT year, name,  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM records NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' GROUP BY year ORDER BY trade_count DESC; '''
        # command_3 =  '''SELECT country_and_area, name,  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM records NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' GROUP BY country_and_area ORDER BY trade_count DESC; '''
        # command = '''SELECT year, name, country_and_area FROM (SELECT name, trade_ID, country_and_area, year FROM ((SELECT trade_ID, year FROM records) AS record NATURAL JOIN  (SELECT trade_ID, name FROM recorded_creature WHERE name ={}) AS sss) AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country) AS aaaa;'''.format(
        #     creature_n
        # )
        # command_2 = '''SELECT year, name,  COUNT(DISTINCT trade_ID) AS trade_count FROM ((SELECT name, trade_ID, country_and_area, year FROM (SELECT trade_ID, year FROM records ) AS record NATURAL JOIN  (SELECT trade_ID, name FROM recorded_creature WHERE name ={}) AS sss)AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country) AS aaaa GROUP BY year ORDER BY trade_count DESC;'''.format(
        #     creature_n
        # )
        # command_3 = '''SELECT country_and_area, name,  COUNT(DISTINCT trade_ID) AS trade_count FROM ((SELECT name, trade_ID, country_and_area, year FROM (SELECT trade_ID, year FROM records) AS record NATURAL JOIN (SELECT trade_ID, name FROM recorded_creature WHERE name ={}) AS sss)AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country) AS aaaa GROUP BY name ORDER BY trade_count DESC;'''.format(
        #     creature_n
        # )
        command = '''SELECT year, name, country_and_area 
FROM (SELECT name, trade_ID, country_and_area, year 
FROM (SELECT trade_ID, year,name, country_and_area FROM records AS record 
NATURAL JOIN (SELECT trade_ID, name FROM recorded_creature WHERE name ='{}') AS sss
NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country
NATURAL JOIN country) AS aaaa) AS woche;'''.format(creature_n) #3.7s
        command_2 = '''SELECT year, name, COUNT(DISTINCT trade_ID) AS trade_count 
FROM (SELECT name, trade_ID, country_and_area, year FROM (
SELECT trade_ID, year,name, country_and_area FROM records AS record NATURAL JOIN  
(SELECT trade_ID, name FROM recorded_creature WHERE name ='{}') AS sss NATURAL JOIN 
(SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country
NATURAL JOIN country) AS aaaa
) AS woche GROUP BY year ORDER BY year DESC;'''.format(creature_n)#5.3s
        command_3 = '''SELECT country_and_area, name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, country_and_area, year FROM (SELECT trade_ID, year,name, country_and_area FROM records AS record NATURAL JOIN  
(SELECT trade_ID, name FROM recorded_creature WHERE name ='{}') AS sss NATURAL JOIN 
(SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country
NATURAL JOIN country) AS aaaa) AS woche GROUP BY country_and_area ORDER BY trade_count DESC;'''.format(creature_n)#5.3s
        print(command)
        print(command_2)
        print(command_3)
        year_table = pd.read_sql(command_2,db)
        country_table = pd.read_sql(command_3,db)
        year_table.to_csv('/Users/endlessio/Downloads/CITESDB_web/public/query_data/year_table.csv',index=False)
        country_table.to_csv('/Users/endlessio/Downloads/CITESDB_web/public/query_data/country_table.csv',index=False)
        fakeYear = csv.reader(open('/Users/endlessio/Downloads/CITESDB_web/public/query_data/creature_table.csv',"w"))
        writer = csv.writer(fakeYear)
        writer.writerow(("hello", "k"))
        fakeYear.close()
    
    elif len(country_n) != 0  and len(creature_n) ==0 and len(year_n) == 0:#error
        #2 is creature, 3 is year
        # command_2 = '''SELECT  country_and_area, name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM records NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' GROUP BY name ORDER BY trade_count DESC;'''
        # command_3 = '''SELECT year, country_and_area, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM records NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' GROUP BY year ORDER BY trade_count DESC;'''
        command =  '''SELECT year, name, country_and_area FROM (SELECT name, trade_ID, country_and_area, year FROM (SELECT trade_ID, year FROM records) AS record NATURAL JOIN recorded_creature AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import WHERE ISO = '{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country NATURAL JOIN country) AS aaaa ;'''.format(
            country_n,country_n,country_n
        )#8.6
        # command_2 = '''SELECT country_and_area, name,  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, country_and_area, year FROM (SELECT trade_ID, year FROM records) AS record NATURAL JOIN recorded_creature AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import WHERE ISO = '{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country NATURAL JOIN country) AS aaaa GROUP BY name ORDER BY trade_count DESC;'''.format(
        #     country_n,country_n,country_n
        # )
        command_21 = '''SELECT country_and_area, name,  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, country_and_area, year FROM (SELECT trade_ID, year,ISO,name,country_and_area FROM records AS record NATURAL JOIN recorded_creature AS crecords	 NATURAL JOIN (SELECT trade_ID, ISO FROM import WHERE'''
        command_22 = ''' ISO = '{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country  NATURAL JOIN (SELECT ISO, country_and_area FROM country WHERE ISO='{}') AS aaaa ) AS uuuuu) AS wocao GROUP BY name ORDER BY trade_count DESC;'''.format(
            country_n,country_n,country_n,country_n
        )
        command_2 = command_21+command_22 #3.7

        # command_3 =  '''SELECT country_and_area, year,  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, country_and_area, year FROM (SELECT trade_ID, year FROM records) AS record NATURAL JOIN recorded_creature AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import WHERE ISO = '{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country NATURAL JOIN country) AS aaaa GROUP BY year ORDER BY trade_count DESC;'''.format(
        #     country_n,country_n,country_n
        # )
        command_31 = '''SELECT country_and_area, year,  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, country_and_area, year FROM (SELECT trade_ID, year,ISO,name,country_and_area FROM records AS record NATURAL JOIN recorded_creature AS crecords	 NATURAL JOIN (SELECT trade_ID, ISO FROM import WHERE'''
        command_32 = ''' ISO = '{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country  NATURAL JOIN (SELECT ISO, country_and_area FROM country WHERE ISO='{}') AS aaaa ) AS uuuuu) AS wocao GROUP BY year ORDER BY trade_count DESC;'''.format(
            country_n,country_n,country_n,country_n
        )
        command_3 = command_31+command_32 #3.7s
        print(command)
        print(command_2)
        print(command_3)
        creature_table = pd.read_sql(command_2,db)
        year_table = pd.read_sql(command_3,db)
        creature_table.to_csv("/Users/endlessio/Downloads/CITESDB_web/public/query_data/creature_table.csv",index=False)
        year_table.to_csv("/Users/endlessio/Downloads/CITESDB_web/public/query_data/year_table.csv",index=False)
        fakeYear = csv.reader(open('/Users/endlessio/Downloads/CITESDB_web/public/query_data/country_table.csv',"w"))
        writer = csv.writer(fakeYear)
        writer.writerow(("hello", "k"))
        fakeYear.close()


    elif len(year_n) !=0  and len(country_n) != 0 and len(creature_n) == 0:
        #  command_2 = '''SELECT year, country_and_area, name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM records NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' ORDER BY trade_count DESC;'''
        #  command = '''SELECT country_and_area, year, name  FROM (SELECT name, trade_ID, country_and_area, year FROM (SELECT trade_ID, year FROM records WHERE year = {}) AS record NATURAL JOIN recorded_creature AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import WHERE ISO = '{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country NATURAL JOIN country) AS aaaa;'''.format(
        #     year_n,country_n,country_n,country_n
        # )
        #  command_2 =   '''SELECT country_and_area, year, name,  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, country_and_area, year FROM (SELECT trade_ID, year FROM records WHERE year = {}) AS record NATURAL JOIN recorded_creature AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import WHERE ISO = '{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country NATURAL JOIN country) AS aaaa GROUP BY name ORDER BY trade_count DESC;'''.format(
        #     year_n,country_n,country_n,country_n
        # )
         command = '''SELECT  name,country_and_area,year
FROM((SELECT trade_ID, year FROM records WHERE year={}) AS record
NATURAL JOIN recorded_creature AS crecord
NATURAL JOIN (SELECT trade_ID,ISO FROM import WHERE ISO = '{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country
NATURAL JOIN (SELECT ISO, country_and_area FROM country WHERE ISO='{}') AS hhhh)'''.format(
    year_n,country_n,country_n,country_n,country_n
    )#3.9s
         command_2 = '''SELECT name,country_and_area,year, COUNT(DISTINCT trade_ID) AS trade_count
FROM((SELECT trade_ID, year FROM records WHERE year={}) AS record
NATURAL JOIN recorded_creature AS crecord
NATURAL JOIN (SELECT trade_ID,ISO FROM import WHERE ISO = '{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country
NATURAL JOIN (SELECT ISO, country_and_area FROM country WHERE ISO='{}') AS hhhh) GROUP BY name ORDER BY trade_count DESC;'''.format(
    year_n,country_n,country_n,country_n,country_n
)#4.2s

         print(command)
         print(command_2)
         creature_table = pd.read_sql(command_2,db)
         creature_table.to_csv("/Users/endlessio/Downloads/CITESDB_web/public/query_data/creature_table.csv",index=False)
         fakeYear = csv.reader(open('/Users/endlessio/Downloads/CITESDB_web/public/query_data/year_table.csv',"w"))
         writer = csv.writer(fakeYear)
         writer.writerow(("hello", "k"))
         fakeYear.close()
         fakeYearr = csv.reader(open('/Users/endlessio/Downloads/CITESDB_web/public/query_data/coutry_table.csv',"w"))
         writerr = csv.writer(fakeYearr)
         writerr.writerow(("hello", "k"))
         fakeYearr.close()

    elif len(year_n) !=0 and len(creature_n) != 0 and len(country_n) == 0:
        #command_2 = '''SELECT year, country_and_area, name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM records NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' ORDER BY trade_count DESC;'''
        # command = '''SELECT country_and_area, year, name FROM (SELECT name, trade_ID, country_and_area, year FROM ((SELECT trade_ID, year FROM records WHERE year = {}) AS record NATURAL JOIN (SELECT name, trade_ID FROM recorded_creature WHERE name={}) AS sss) AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import WHERE ISO = {} UNION SELECT trade_ID, ISO FROM export WHERE ISO={} UNION SELECT trade_ID, ISO FROM re_export WHERE ISO={}) AS all_country NATURAL JOIN country) AS aaaa;'''.format(
        #     year_n,creature_n
        # )
        # command_2 = '''SELECT country_and_area, year, name,  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, country_and_area, year FROM ((SELECT trade_ID, year FROM records WHERE year = {}) AS record NATURAL JOIN (SELECT name, trade_ID FROM recorded_creature WHERE name={}) AS sss) AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import WHERE ISO = {} UNION SELECT trade_ID, ISO FROM export WHERE ISO={} UNION SELECT trade_ID, ISO FROM re_export WHERE ISO={}) AS all_country NATURAL JOIN country) AS aaaa GROUP BY ISO ORDER BY trade_count DESC;'''.format(
        #     year_n,creature_n
        # )
        command = '''SELECT country_and_area,year,name,trade_ID FROM(
(SELECT trade_ID, year FROM records WHERE year={}) AS record
NATURAL JOIN (SELECT trade_ID, name FROM recorded_creature WHERE name = '{}') AS crecord
NATURAL JOIN (SELECT trade_ID,ISO FROM import  UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country
NATURAL JOIN (SELECT ISO, country_and_area FROM country ) AS hhhh
);'''.format(year_n,creature_n)#5.4s
        command_2 = '''SELECT country_and_area,year,name, COUNT(DISTINCT trade_ID) AS trade_count FROM(
(SELECT trade_ID, year FROM records WHERE year={}) AS record
NATURAL JOIN (SELECT trade_ID, name FROM recorded_creature WHERE name = '{}') AS crecord
NATURAL JOIN (SELECT trade_ID,ISO FROM import  UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country
NATURAL JOIN (SELECT ISO, country_and_area FROM country ) AS hhhh
) GROUP BY country_and_area ORDER BY trade_count;'''.format(
    year_n,creature_n
)#6.2s
        print(command)
        print(command_2)
        country_table = pd.read_sql(command_2,db)
        country_table.to_csv("/Users/endlessio/Downloads/CITESDB_web/public/query_data/country_table.csv",index=False)
        fakeYear = csv.reader(open('/Users/endlessio/Downloads/CITESDB_web/public/query_data/year_table.csv',"w"))
        writer = csv.writer(fakeYear)
        writer.writerow(("hello", "k"))
        fakeYear.close()
        fakeYearr = csv.reader(open('/Users/endlessio/Downloads/CITESDB_web/public/query_data/creature_table.csv',"w"))
        writerr = csv.writer(fakeYearr)
        writerr.writerow(("hello", "k"))
        fakeYearr.close()

    elif len(country_n) != 0 and len(creature_n) != 0 and len(year_n) == 0:
        #command_2 = '''SELECT year, country_and_area, name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM records NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' ORDER BY trade_count DESC;'''
        # command = '''SELECT country_and_area, year,name FROM (SELECT name, trade_ID, country_and_area, year FROM ((SELECT trade_ID, year FROM records) AS record NATURAL JOIN  (SELECT trade_ID, name FROM recorded_creature WHERE name ={}) AS sss) AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import WHERE ISO={} UNION SELECT trade_ID, ISO FROM export WHERE ISO={} UNION SELECT trade_ID, ISO FROM re_export WHERE ISO={}) AS all_country NATURAL JOIN country) AS aaaa ;'''.format(
        #     creature_n,country_n,country_n,country_n
        # )
        # command_2 = '''SELECT country_and_area, year,name,  COUNT(DISTINCT trade_ID) AS trade_count FROM ((SELECT name, trade_ID, country_and_area, year FROM (SELECT trade_ID, year FROM records  WHERE name={}) AS record NATURAL JOIN  (SELECT trade_ID, name FROM recorded_creature WHERE name ={}) AS sss) AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import WHERE ISO={} UNION SELECT trade_ID, ISO FROM export WHERE ISO={} UNION SELECT trade_ID, ISO FROM re_export WHERE ISO={}) AS all_country NATURAL JOIN country) AS aaaa GROUP BY year ORDER BY trade_count DESC;'''.format(
        #     creature_n,country_n,country_n,country_n
        # )
        command = '''SELECT country_and_area,year,name,trade_ID FROM(
(SELECT trade_ID, year FROM records ) AS record
NATURAL JOIN (SELECT trade_ID, name FROM recorded_creature WHERE name = '{}') AS crecord
NATURAL JOIN (SELECT trade_ID,ISO FROM import WHERE ISO = '{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country
NATURAL JOIN (SELECT ISO, country_and_area FROM country WHERE ISO='{}') AS hhhh
);'''.format(creature_n,country_n,country_n,country_n,country_n)
        command_2 = '''SELECT country_and_area,year,name,COUNT(DISTINCT trade_ID) AS trade_count FROM(
(SELECT trade_ID, year FROM records ) AS record
NATURAL JOIN (SELECT trade_ID, name FROM recorded_creature WHERE name = '{}') AS crecord
NATURAL JOIN (SELECT trade_ID,ISO FROM import WHERE ISO = '{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country
NATURAL JOIN (SELECT ISO, country_and_area FROM country WHERE ISO='{}') AS hhhh
)GROUP BY year ORDER BY trade_count;'''.format(creature_n,country_n,country_n,country_n,country_n)#1.2s
        print(command)
        print(command_2)
        year_table = pd.read_sql(command_2,db)
        year_table.to_csv("/Users/endlessio/Downloads/CITESDB_web/public/query_data/year_table.csv",index=False)
        fakeYear = csv.reader(open('/Users/endlessio/Downloads/CITESDB_web/public/query_data/creature_table.csv',"w"))
        writer = csv.writer(fakeYear)
        writer.writerow(("hello", "k"))
        fakeYear.close()
        fakeYearr = csv.reader(open('/Users/endlessio/Downloads/CITESDB_web/public/query_data/coutry_table.csv',"w"))
        writerr = csv.writer(fakeYearr)
        writerr.writerow(("hello", "k"))
        fakeYearr.close()

    elif len(country_n) != 0 and len(year_n) != 0  and len(creature_n) != 0:
        #command_2 = '''SELECT year, country_and_area, name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM records NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''';'''
        # command = '''SELECT country_and_area, year,name, FROM (SELECT name, trade_ID, country_and_area, year FROM ((SELECT trade_ID, year FROM records  WHERE year={}) AS record NATURAL JOIN (SELECT name, trade_ID FROM recorded_creature WHERE name={}) AS sss) AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country NATURAL JOIN country) AS aaaa  ORDER BY trade_count DESC;'''.format(
        #     year_n,creature_n,country_n,country_n,country_n
        # )
        # command_2 = '''SELECT country_and_area, year,name,  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, country_and_area, year FROM ((SELECT trade_ID, year FROM records  WHERE year={}) AS record NATURAL JOIN (SELECT name, trade_ID FROM recorded_creature WHERE name={}) AS sss) AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country NATURAL JOIN country) AS aaaa  ORDER BY trade_count DESC;'''.format(
        #     year_n,creature_n,country_n,country_n,country_n
        # )
        command = '''SELECT trade_ID,country_and_area,year,name FROM(
(SELECT trade_ID, year FROM records WHERE year={}) AS record
NATURAL JOIN (SELECT trade_ID, name FROM recorded_creature WHERE name = '{}') AS crecord
NATURAL JOIN (SELECT trade_ID,ISO FROM import WHERE ISO = '{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country
NATURAL JOIN (SELECT ISO, country_and_area FROM country WHERE ISO='{}') AS hhhh
);'''.format(year_n,creature_n,country_n,country_n,country_n,country_n)#2s
        command_2 = '''SELECT country_and_area,year,name,COUNT(DISTINCT trade_ID) AS trade_count FROM(
(SELECT trade_ID, year FROM records WHERE year={}) AS record
NATURAL JOIN (SELECT trade_ID, name FROM recorded_creature WHERE name = '{}') AS crecord
NATURAL JOIN (SELECT trade_ID,ISO FROM import WHERE ISO = '{}' UNION SELECT trade_ID, ISO FROM export WHERE ISO='{}' UNION SELECT trade_ID, ISO FROM re_export WHERE ISO='{}') AS all_country
NATURAL JOIN (SELECT ISO, country_and_area FROM country WHERE ISO='{}') AS hhhh
);'''.format(year_n,creature_n,country_n,country_n,country_n,country_n)#1.3s
        print(command)
        print(command_2)
        spec = pd.read_sql(command_2,db)
        spec.to_csv("/Users/endlessio/Downloads/CITESDB_web/public/query_data/spec.csv",index=False)

        
    
    all_tale = pd.read_sql(command,db)
    all_tale.to_csv("/Users/endlessio/Downloads/CITESDB_web/public/query_data/all_table.csv",index=False)