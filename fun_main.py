import os

import pandas as pd
import numpy as np

def getName(file):
    root, extension = file.split('.')
    # print(extension)
    if(extension == 'csv'):
        return 'file.csv'
    elif(extension == 'json'):
        return 'file.json'
    elif(extension == 'xlsx'):
        return 'file.xlsx'
    elif(extension == 'xls'):
        return 'file.xls'
    else:
        return 'file'

def getDataFrame(file):
    if file == '':
        return pd.DataFrame()
    root, extension = os.path.splitext(file)
    if(extension == '.csv'):
        df = pd.read_csv(file)
        return df
    elif(extension == '.json'):
        df = pd.read_json(file)
        return df
    elif(extension == '.xlsx' or extension == '.xls'):
        df = pd.read_excel(file)
        return df
    else:
        return pd.DataFrame()


def getColumnas(file):
    df = getDataFrame(file)
    columnas = np.asarray(df.columns).tolist()
    return columnas


def getlistadoAnalysis():
    lista = {
        'Tendencia de la infección por Covid-19 en un Pais':{
            'caso':1,
            'name':'Tendencia de la infección por Covid-19 en un Pais',
            'no_parametros': 4,
            'parametros':['tiempo','confirmados','celda_pais'],
            'opcionales': ['celda_pais','nombre_pais'],
            'parametros_texto':['nombre_pais']
        },
        'Predicción de infectados en un Pais':{
            'caso':2,
            'name':'Predicción de infectados en un Pais',
            'no_parametros': 5,
            'parametros':['tiempo','confirmados','celda_pais'],
            'opcionales': ['celda_pais','nombre_pais'],
            'parametros_numericos':['tiempo_predecir'],
            'parametros_texto':['nombre_pais']
        },
        'Indice de Progresion de la pandemia':{
            'caso':3,
            'name':'Indice de Progresion de la pandemia',
            'no_parametros': 2,
            'parametros':['tiempo','confirmados']
        },
        'Prediccion de mortalidad por COVID en un Departamento':{
            'caso':4,
            'name':'Prediccion de mortalidad por COVID en un Departamento',
            'no_parametros': 5,
            'parametros':['tiempo','fallecido','celda_departamento'],
            'opcionales': ['nombre_departamento','celda_departamento'],
            'parametros_numericos':['tiempo_predecir'],
            'parametros_texto':['nombre_departamento']
        },
        'Prediccion de mortalidad por COVID en un Pais':{
            'caso':5,
            'name':'Prediccion de mortalidad por COVID en un Pais',
            'no_parametros': 5,
            'parametros':['tiempo','fallecido','celda_pais'],
            'opcionales': ['nombre_pais','celda_pais'],
            'parametros_numericos':['tiempo_predecir'],
            'parametros_texto':['nombre_pais']
        },
        'Analisis del numero de muertes por coronavirus en un Pais':{
            'caso':6,
            'name':'Analisis del numero de muertes por coronavirus en un Pais',
            'no_parametros': 5,
            'parametros':['tiempo','fallecido','confirmados','celda_pais'],
            'parametros_texto':['nombre_pais'],
            'opcionales': ['nombre_pais','celda_pais']
        },
        'Tendencia del numero de infectados por dia de un Pais':{
            'caso':7,
            'name':'Tendencia del numero de infectados por dia de un Pais',
            'no_parametros': 4,
            'parametros':['tiempo','confirmados','celda_pais'],
            'opcionales': ['nombre_pais','celda_pais'],
            'parametros_texto':['nombre_pais']
        },
         'Prediccion de casos de un pais para un año':{
             'caso':8,
            'name':'Prediccion de casos de un pais para un año',
            'no_parametros': 4,
            'parametros':['tiempo','confirmados','celda_pais'],
            'opcionales': ['celda_pais','nombre_pais'],
            'parametros_texto':['nombre_pais']
       },
       'Tendencia de la vacunacion de en un Pais':{
            'caso':9,
            'name':'Tendencia del numero de infectados por dia de un Pais',
            'no_parametros': 4,
            'parametros':['tiempo','vacunacion','celda_pais'],
            'opcionales': ['nombre_pais','celda_pais'],
            'parametros_texto':['nombre_pais']
        },
        'Analisis Comparativo de Vacunacion entre 2 paises':{
            'caso':10,
            'name':'Analisis Comparativo de Vacunacion entre 2 paises',
            'no_parametros': 4,
            'parametros':['tiempo','celda_pais','celda_vacunacion'],
            'parametros_texto':['nombre_pais_1','nombre_pais_2']
        },
        'Muertes segun regiones de un pais':{
            'caso':14,
            'name':'Muertes segun regiones de un pais',
            'no_parametros': 6,
            'parametros':['tiempo','fallecidos','celda_pais','celda_region'],
            'parametros_texto':['nombre_pais','nombre_region']
        },
        'Tendencia de casos confirmados de COVID en un departamento de un Pais':{
            'caso':15,
            'name':'Tendencia de casos confirmados de COVID en un departamento de un Pais',
            'no_parametros': 6,
            'parametros':['tiempo','confirmados','celda_pais','celda_departamento'],
            'parametros_texto':['nombre_pais','nombre_departamento']
        },
        'Tasa de mortalidad por (COVID-19) en un pais':{
            'caso':22,
            'name':'Tasa de mortalidad por (COVID-19) en un pais',
            'no_parametros': 5,
            'parametros':['tiempo','fallecido','celda_pais'],
            'opcionales': ['nombre_pais','celda_pais'],
            'parametros_texto':['nombre_pais']
        },
        'Comparacion entre el numero de casos detectados y el numero de pruebas de un pais':{
            'caso':24,
            'name':'Comparacion entre el numero de casos detectados y el numero de pruebas de un pais',
            'no_parametros': 5,
            'parametros':['tiempo','casos_detectados','pruebas','celda_pais'],
            'opcionales': ['nombre_pais','celda_pais'],
            'parametros_texto':['nombre_pais']
        },
        'Prediccion de casos confirmados por dia':{
            'caso':25,
            'name':'Prediccion de casos confirmados por dia',
            'no_parametros': 3,
            'parametros':['tiempo','confirmados'],
            'parametros_numericos':['tiempo_predecir']
        }
    }
    return lista

def listaAnalisisNombres():
    lista = ['Tendencia de la infección por Covid-19 en un Pais','Predicción de infectados en un Pais',
                'Indice de Progresion de la pandemia','Prediccion de mortalidad por COVID en un Departamento',
                'Prediccion de mortalidad por COVID en un Pais','Analisis del numero de muertes por coronavirus en un Pais',
                'Tendencia del numero de infectados por dia de un Pais','Prediccion de casos de un pais para un año',
                'Tendencia de la vacunacion de en un Pais','Analisis Comparativo de Vacunacion entre 2 paises',
                'Muertes segun regiones de un pais','Tendencia de casos confirmados de COVID en un departamento de un Pais',
                'Tasa de mortalidad por (COVID-19) en un pais',
                'Comparacion entre el numero de casos detectados y el numero de pruebas de un pais','Prediccion de casos confirmados por dia']
    return lista