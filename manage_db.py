# -*- coding: utf-8 -*-

import pandas as pd
import sqlite3

def df2SQL(df,baseDados,tabela):
    conexao = sqlite3.connect(baseDados)
    df.to_sql(tabela, conexao, if_exists="replace")  
    conexao.close()
    
