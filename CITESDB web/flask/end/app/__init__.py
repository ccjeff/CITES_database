from flask import Flask
import flask
import json
import pandas as pd
# from sqlalchemy.dialects.mysql import pymysql, mysqldb
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
        # db = connect('root','')
        # query(creature,country,year,db)
        time.sleep(5)
    return "done!"



def connect(user,pwd,host="127.0.0.1",port="3306",database="cites"):
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

    command = '''SELECT year, country_and_area, name FROM (SELECT name, trade_ID, year FROM creature NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country

    all_info = pd.read_sql(command,db)
    all_info.to_csv('all_table.csv',sep='\t',index=False)

    creature_ = country_=year_ = ''

    if len(country_n) !=0 or len(year_n) != 0:
        creature_ = creature_n+','
    if len(year_n) != 0:
        country_ = country_n+','

    # command_2 = '''SELECT year, country_and_area, name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM creature NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' GROUP BY '''+creature_+country_+year_+" WITH ROLLUP;"

    # print(command_2)
    # count_table = pd.read_sql(command_2,db)
    # count_table.to_csv('count_table.csv',sep='\t',index=False)

    if len(year_n) != 0 and len(country_n) == 0 and len(creature) == 0:
        #2 is classfied by country, 3 is by creature
        command_2 = '''SELECT year, country_and_area,  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM creature NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' GROUP BY country_and_area ORDER BY trade_count DESC; '''
        command_3 = '''SELECT year,  name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM creature NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' GROUP BY name ORDER BY trade_count DESC; '''
        country_table = pd.read_sql(command_2,db)
        country_table.to_csv('country_table.csv',sep='\t',index=False)
        creature_table = pd.read_sql(command_3,db)
        creature_table.to_csv('creature.csv',sep='\t',index=False)

    elif len(country_n) == 0 and len(creature) != 0 and len(year) == 0:
        #2 is classfied by year, 3 is country
        command_2 =  '''SELECT year, name,  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM creature NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' GROUP BY year ORDER BY trade_count DESC; '''
        command_3 =  '''SELECT country_and_area, name  COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM creature NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' GROUP BY country_and_area ORDER BY trade_count DESC; '''
        year_table = pd.read_sql(command_2,db)
        country_table = pd.read_sql(command_3,db)
        year_table.to_csv('year_table.csv',sep = '\t',index=False)
        country_table.to_csv('country_table.csv',sep='\t',index=False)
    
    elif len(country_n) != 0  and len(creature_n) ==0 and len(year) == 0:
        #2 is creature, 3 is year
        command_2 = '''SELECT  country_and_area, name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM creature NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' GROUP BY name ORDER BY trade_count DESC;'''
        command_3 = '''SELECT year, country_and_area, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM creature NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' GROUP BY year ORDER BY trade_count DESC;'''
        creature_table = pd.read_sql(command_2,db)
        year_table = pd.read_sql(command_3,db)
        creature_table.to_csv("creature_table.csv",sep='\t',index=False)
        year_table.to_csv("year_tale.csv",sep='\t',index=False)

    elif len(year_n) !=0  and len(country_n) != 0 and len(creature_n) == 0:
         command_2 = '''SELECT year, country_and_area, name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM creature NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' ORDER BY trade_count DESC;'''
         creature_table = pd.read_sql(command_2,db)
         creature_table.to_csv("creature_table.csv",sep='\t',index=False)
    elif len(year_n) !=0 and len(creature_n) != 0 and len(country_n) == 0:
        command_2 = '''SELECT year, country_and_area, name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM creature NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' ORDER BY trade_count DESC;'''
        country_table = pd.read_sql(command_2)
        country_table.to_csv("country_table.csv",sep='\t',index=False)
    elif len(country_n) != 0 and len(creature_n) != 0 and len(year) == 0:
        command_2 = '''SELECT year, country_and_area, name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM creature NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''' ORDER BY trade_count DESC;'''
        year_table = pd.read_sql(command_2,db)
        year_table.to_csv("year_table.csv",sep='\t',index=False)
    elif len(country_n) != 0 and len(year_n) != 0  and len(creature_n) != 0:
        command_2 = '''SELECT year, country_and_area, name, COUNT(DISTINCT trade_ID) AS trade_count FROM (SELECT name, trade_ID, year FROM creature NATURAL JOIN recorded_creature'''+creature+year+''' AS crecords NATURAL JOIN (SELECT trade_ID, ISO FROM import UNION SELECT trade_ID, ISO FROM export UNION SELECT trade_ID, ISO FROM re_export) AS all_country NATURAL JOIN country'''+country_ano+''';'''
        spec = pd.read_sql(command_2,db)
        spec.to_csv("spec.csv",sep='\t',index=False)
