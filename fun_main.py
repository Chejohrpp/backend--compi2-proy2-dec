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
        'Porcentaje de hombres infectados por COVID en un Pais desde el primer caso activo':{
            'caso':11,
            'name':'Porcentaje de hombres infectados por COVID en un Pais desde el primer caso activo',
            'no_parametros': 5,
            'parametros':['celda_tiempo','celda_genero_hombre','celda_total','celda_pais'],
            'opcionales': ['nombre_pais','celda_pais'],
            'parametros_texto':['nombre_pais']
        },
        'Analisis Comparativo entre paises o continentes':{
            'caso':12,
            'name':'Analisis Comparativo entre paises o continentes',
            'no_parametros': 5,
            'parametros':['tiempo','celda_pais_continente','celda_comparacion'],
            'parametros_texto':['nombre_pais_continente_1','nombre_pais_continente_2']
        },
        'Muertes promedio por casos confirmados y edad de covid 19 en un Pais':{
            'caso':13,
            'name':'Muertes promedio por casos confirmados y edad de covid 19 en un Pais',
            'no_parametros': 5,
            'parametros':['celda_confirmados','celda_fallecidos','celda_edad','celda_pais'],
            'opcionales': ['nombre_pais','celda_pais'],
            'parametros_texto':['nombre_pais']
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
        'Porcentaje de muertes frente al total de casos en un pais, region o continente':{
            'caso':16,
            'name':'Porcentaje de muertes frente al total de casos en un pais, region o continente',
            'no_parametros': 5,
            'parametros':['celda_tiempo','celda_fallecidos','celda_total_confirmados','celda_pais_region_continente'],
            'opcionales': ['celda_pais_region_continente','nombre_pais_region_continente'],
            'parametros_texto':['nombre_pais_region_continente']
        },
        'Tasa de comportamiento de casos activos en relacion al número de muertes en un continente':{
            'caso':17,
            'name':'Tasa de comportamiento de casos activos en relacion al número de muertes en un continente',
            'no_parametros': 4,
            'parametros':['casos_activos','numero_muertes','celda_continente'],
            'opcionales': ['nombre_continente','celda_continente'],
            'parametros_texto':['nombre_continente']
        },
        'Comportamiento y clasificacion de personas infectadas por COVID-19 por municipio en un Pais':{
            'caso':18,
            'name':'Comportamiento y clasificacion de personas infectadas por COVID-19 por municipio en un Pais',
            'no_parametros': 4,
            'parametros':['celda_infectados','celda_pais','celda_municipio'],
            'parametros_texto':['nombre_pais']
        },
        'Prediccion de muertes en el ultimo día del primer año de infecciones en un pais':{
            'caso':19,
            'name':'Prediccion de muertes en el ultimo día del primer año de infecciones en un pais',
            'no_parametros': 5,
            'parametros':['tiempo','fallecido','celda_pais'],
            'opcionales': ['nombre_pais','celda_pais'],
            'parametros_texto':['nombre_pais']
        },
        'Tasa de crecimiento de casos de COVID-19 en relacion con nuevos casos diarios y tasa de muerte por COVID-19':{
            'caso':20,
            'name':'Tasa de crecimiento de casos de COVID-19 en relacion con nuevos casos diarios y tasa de muerte por COVID-19',
            'no_parametros': 3,
            'parametros':['celda_tiempo','casos_diarios','numero_muertes'],
        },
         'Predicciones de casos y muertes en todo el mundo':{
             'caso':21,
            'name':'Predicciones de casos y muertes en todo el mundo',
            'no_parametros': 4,
            'parametros':['tiempo','celda_confirmados','celda_fallecidos'],
            'parametros_numericos':['tiempo_predecir'],
       },
        'Tasa de mortalidad por (COVID-19) en un pais':{
            'caso':22,
            'name':'Tasa de mortalidad por (COVID-19) en un pais',
            'no_parametros': 5,
            'parametros':['tiempo','fallecido','celda_pais'],
            'opcionales': ['nombre_pais','celda_pais'],
            'parametros_texto':['nombre_pais']
        },
        'Factores de muerte por COVID-19 en un pais':{
            'caso':23,
            'name':'Factores de muerte por COVID-19 en un pais',
            'no_parametros': 5,
            'parametros':['tiempo','celda_fallecidos','factor_muerte','celda_pais'],
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
                'Porcentaje de hombres infectados por COVID en un Pais desde el primer caso activo','Analisis Comparativo entre paises o continentes',
                'Muertes promedio por casos confirmados y edad de covid 19 en un Pais',
                'Muertes segun regiones de un pais','Tendencia de casos confirmados de COVID en un departamento de un Pais',
                'Porcentaje de muertes frente al total de casos en un pais, region o continente','Tasa de comportamiento de casos activos en relacion al número de muertes en un continente',
                'Comportamiento y clasificacion de personas infectadas por COVID-19 por municipio en un Pais','Prediccion de muertes en el ultimo día del primer año de infecciones en un pais',
                'Tasa de crecimiento de casos de COVID-19 en relacion con nuevos casos diarios y tasa de muerte por COVID-19','Predicciones de casos y muertes en todo el mundo',
                'Tasa de mortalidad por (COVID-19) en un pais','Factores de muerte por COVID-19 en un pais',
                'Comparacion entre el numero de casos detectados y el numero de pruebas de un pais','Prediccion de casos confirmados por dia']
    return lista