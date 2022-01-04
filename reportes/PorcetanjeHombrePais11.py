import os
import datetime

from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import fun_main as fm
import fun_reportes as fr

# 'Porcentaje de hombres infectados por COVID en un Pais desde el primer caso activo':{
#             'caso':11,
#             'name':'Porcentaje de hombres infectados por COVID en un Pais desde el primer caso activo',
#             'no_parametros': 5,
#             'parametros':['celda_tiempo','celda_genero_hombre','celda_total','celda_pais'],
#             'opcionales': ['nombre_pais','celda_pais'],
#             'parametros_texto':['nombre_pais']
#         }

# path_imgs = 'static/imgs_temp'
name = 'Porcentaje de hombres infectados por COVID en un Pais desde el primer caso activo'

def analizar(filepath,param):
    ### Asignacion de celdas  ###############################################
    x_celda = param['celda_tiempo']
    hombre_celda = param['celda_genero_hombre']
    total_celda = param['celda_total']
    celda_pais = param['celda_pais']
    nombre_pais = param['nombre_pais']
    y_celda = 'porcentaje'
    ### Lista de variables  ###############################################
    lista_urls_imgs = []
    lista_urls_static = []
    datos_calculados = []
    datos_estaticos = []
    l_encod_x = LabelEncoder()
    l_encod_y = LabelEncoder()
    ### GET DataFrame  ###############################################
    df = fm.getDataFrame(filepath)
    if(df.empty):
        print ('Error, no hay un dataframe')
        return False
    ######### Limpiar los datos ##########################################
    df = fr.limpiarColumna(df,hombre_celda)
    df = fr.limpiarColumna(df,total_celda)
    df[y_celda] = round((df[hombre_celda]/df[total_celda])*100,2)
    df = df.fillna({y_celda:0})
    df = fr.limpiarColumna(df,x_celda)
    df = fr.limpiarColumna(df,y_celda)
    limpia_x =fr.limpiarData(df,x_celda)
    limpia_y = fr.limpiarData(df,y_celda)
    if nombre_pais != "" and celda_pais != "":
        df = df[df[celda_pais].str.contains(nombre_pais)]
        datos_calculados.append("Pais Utilizado : " + str(nombre_pais))

    df_xcelda = df[x_celda]
    if (limpia_x == False or df_xcelda.dtype == 'datetime64[ns]'):
        df_xcelda = l_encod_x.fit_transform(df[x_celda])

    df_ycelda = df[y_celda]
    if (limpia_y == False or df_ycelda.dtype == 'datetime64[ns]'):
        df_ycelda = l_encod_y.fit_transform(df[y_celda])

    ##### Asginamos Variables ##########################################
    x = np.asarray(df_xcelda).reshape(-1,1)
    y = df_ycelda
    ##### datos extras ##########################################
    path_aux = fr.generarUrlImg("fig_muestra.png",lista_urls_static)
    plt.bar(df[x_celda],df[y_celda],width=0.3)
    plt.xlabel(x_celda)
    plt.ylabel(y_celda)
    plt.title("Data ingresada\nporcentaje en %",fontsize=10)
    plt.xticks(rotation=45)
    plt.autoscale()
    # for i in range(len(df[y_celda])):
    #     plt.annotate(str(df[y_celda].iloc[i]), xy=(df[x_celda].iloc[i],df[y_celda].iloc[i]), ha='center', va='bottom')
    plt.savefig(path_aux,bbox_inches = "tight")
    plt.clf()

    #### build ###############################################################
    grado = 6
    poly_feature = PolynomialFeatures(grado)
    x_transform = poly_feature.fit_transform(x)
    #### Train ###############################################################
    #algorithm
    l_reg = linear_model.LinearRegression()

    model = l_reg.fit(x_transform,y)
    y_predictions = model.predict(x_transform)

    #### Calculate ###########################################################
    datos_calculados.append("grado usado : " + str(grado))
    rmse = np.sqrt(mean_squared_error(y,y_predictions))
    # print("rmse:",rmse)
    datos_calculados.append("rmse : " + str(round(rmse,2)))
    datos_estaticos.append("rmse : " + str(rmse))
    r2 = r2_score(y,y_predictions)
    # print ("r^2:",r2)
    datos_calculados.append("r^2 : " + str(round(r2,2)))
    datos_estaticos.append("r^2 : " + str(r2))
    #coef_
    coef = model.coef_
    datos_calculados.append("coef : " + str(coef[0]))
    for i in range(1,len(coef)):
        datos_calculados.append("coef "+ str(i) +" : " + str(coef[i]))
    datos_estaticos.append("coef : " + str(coef))
    #intercep
    intercept = model.intercept_
    datos_calculados.append("intercept : " + str(intercept))
    datos_estaticos.append("intercept : " + str(intercept))

    #### Graph #######################################################################

    plt.bar(df[x_celda],df[y_celda],width=0.3)
    plt.xlabel(x_celda)
    plt.ylabel(y_celda)
    plt.title(name+"\nporcentaje en %",fontsize=10)
    plt.xticks(rotation=45)
    for i in range(len(df[y_celda])):
        plt.annotate(str(df[y_celda].iloc[i]), xy=(df[x_celda].iloc[i],df[y_celda].iloc[i]), ha='center', va='bottom')
    plt.savefig(path_aux,bbox_inches = "tight")
    path_aux = fr.generarUrlImg("fig_tendencia.png",lista_urls_imgs)
    plt.autoscale()
    plt.savefig(path_aux,bbox_inches = "tight")
    plt.clf()

    #### Prediccion ##########################################################

    #### Graph #######################################################################
    title = 'grado usado {}; RMSE = {}; R^2={:.3f}'.format(grado,round(rmse,2),r2)
    plt.title(name+"\n"+title,fontsize=10)
    plt.xlabel(x_celda)
    plt.ylabel(y_celda)
    plt.xticks(rotation=45)
    plt.plot(df[x_celda],y_predictions,color="red",linewidth=3)
    path_aux = fr.generarUrlImg("fig_prediccion.png",lista_urls_imgs)
    plt.autoscale()
    plt.savefig(path_aux,bbox_inches = "tight")
    plt.clf()
    #### enviar los datos #######################################################################
    return fr.addData(datos_calculados,lista_urls_imgs,lista_urls_static,datos_estaticos,'Se muestra el grafico de barras los porcentajes de infectados de hombres, ademas se dieron los datos para que puedan realizar una construccion de una grafica de prediccion de grado {}'.format(grado),name)


