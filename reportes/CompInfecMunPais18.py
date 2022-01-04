import os

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

# 'Comportamiento y clasificacion de personas infectadas por COVID-19 por municipio en un Pais':{
#             'caso':18,
#             'name':'Comportamiento y clasificacion de personas infectadas por COVID-19 por municipio en un Pais',
#             'no_parametros': 4,
#             'parametros':['celda_infectados','celda_pais','celda_municipio'],
#             'parametros_texto':['nombre_pais']
#         }

# path_imgs = 'static/imgs_temp'
name_report = 'Comportamiento y clasificacion de personas infectadas por COVID-19 por municipio en un Pais'

def analizar(filepath,param):
    ### Asignacion de celdas  ###############################################
    x_celda = param['celda_municipio']
    y_celda = param['celda_infectados']
    celda_pais = param['celda_pais']
    nombre_pais = param['nombre_pais']
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
    df = fr.limpiarColumna(df,x_celda)
    df = fr.limpiarColumna(df,y_celda)
    limpia_x = fr.limpiarData(df,x_celda)
    limpia_y = fr.limpiarData(df,y_celda)

    if celda_pais != "" and nombre_pais != "":
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

    # ##datos extras##
    path_aux = fr.generarUrlImg("fig_muestra.png",lista_urls_static)
    plt.bar(df[x_celda],df[y_celda],width=0.3)
    plt.xlabel(x_celda)
    plt.ylabel(y_celda)
    plt.title("Data ingresada",fontsize=10)
    plt.xticks(rotation=45)
    plt.autoscale()
    for i in range(len(df[y_celda])):
        plt.annotate(str(df[y_celda].iloc[i]), xy=(df[x_celda].iloc[i],df[y_celda].iloc[i]), ha='center', va='bottom')
    plt.savefig(path_aux,bbox_inches = "tight")
    plt.clf()

    #### build ###############################################################
    grado = 8
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
    path_aux = fr.generarUrlImg("fig_tendencia.png",lista_urls_imgs)
    plt.bar(df[x_celda],df[y_celda],width=0.3)
    plt.xlabel(x_celda)
    plt.ylabel(y_celda)
    plt.title(name_report,fontsize=10)
    plt.xticks(rotation=45)
    plt.autoscale()
    for i in range(len(df[y_celda])):
        plt.annotate(str(df[y_celda].iloc[i]), xy=(df[x_celda].iloc[i],df[y_celda].iloc[i]), ha='center', va='bottom')
    plt.savefig(path_aux,bbox_inches = "tight")
    plt.clf()

    #### Prediccion ##########################################################
    ## no se realiza predicion aqui

    #### Graph #######################################################################
    title = 'grado usado {}; RMSE = {}; R^2={:.3f}'.format(grado,round(rmse,2),r2)
    plt.title(name_report+"\n"+title,fontsize=10)
    plt.xlabel(x_celda)
    plt.ylabel(y_celda)
    plt.plot(df[x_celda],y_predictions,color="red",linewidth=3)
    plt.xticks(rotation=45)
    path_aux = fr.generarUrlImg("fig_Prediccion.png",lista_urls_imgs)
    plt.autoscale()
    plt.savefig(path_aux,bbox_inches = "tight")
    plt.clf()
    # plt.show()
    return fr.addData(datos_calculados,lista_urls_imgs,lista_urls_static,datos_estaticos,'En la grafica de barras se muestra el comportamiento de infectados por municipio con una construccion de la grafica de grado {}'.format(grado),name_report)

