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

# 'Analisis Comparativo de Vacunacion entre 2 paises':{
#             'caso':10,
#             'name':'Analisis Comparativo de Vacunacion entre 2 paises',
#             'no_parametros': 4,
#             'parametros':['tiempo','celda_pais','celda_vacunacion'],
#             'parametros_texto':['nombre_pais_1','nombre_pais_2']
#         }

# path_imgs = 'static/imgs_temp'
name = 'Analisis Comparativo de Vacunacion entre 2 paises'

def analizar(filepath,param):
    ### Asignacion de celdas  ###############################################
    x_celda = param['tiempo']
    # vacunacion_celda = param['celda_vacunacion']
    y_celda = param['celda_vacunacion']
    y_celda2 = param['celda_vacunacion']
    celda_pais = param['celda_pais']
    nombre_pais1 = param['nombre_pais_1']
    nombre_pais2 = param['nombre_pais_2']
    ### Lista de variables  ###############################################
    lista_urls_imgs = []
    lista_urls_static = []
    datos_calculados = []
    datos_estaticos = []
    l_encod_x = LabelEncoder()
    l_encod_y = LabelEncoder()
    l_encod_y2 = LabelEncoder()
    ### GET DataFrame  ###############################################
    df = fm.getDataFrame(filepath)
    if(df.empty):
        print ('Error, no hay un dataframe')
        return False
    ######### Limpiar los datos ##########################################
    
    df_pais_1 = df[df[celda_pais].str.contains(nombre_pais1)]
    df_pais_2 = df[df[celda_pais].str.contains(nombre_pais2)]

    df_pais_1 = fr.limpiarColumna(df_pais_1,x_celda)
    df_pais_1 = fr.limpiarColumna(df_pais_1,y_celda)
    df_pais_2 = fr.limpiarColumna(df_pais_2,y_celda2)

    limpia_x =fr.limpiarData(df_pais_1,x_celda)
    limpia_y = fr.limpiarData(df_pais_1,y_celda)
    limpia_y2 = fr.limpiarData(df_pais_2,y_celda2)

    df_xcelda = df_pais_1[x_celda]
    if (limpia_x == False or df_xcelda.dtype == 'datetime64[ns]'):
        df_xcelda = l_encod_x.fit_transform(df_pais_1[x_celda])

    df_xcelda2 = df_pais_2[x_celda]
    if (limpia_x == False or df_xcelda2.dtype == 'datetime64[ns]'):
        df_xcelda2 = l_encod_x.fit_transform(df_pais_2[x_celda])

    df_ycelda = df_pais_1[y_celda]
    if (limpia_y == False or df_ycelda.dtype == 'datetime64[ns]'):
        df_ycelda = l_encod_y.fit_transform(df_pais_1[y_celda])

    df_ycelda2 = df_pais_2[y_celda2]
    if (limpia_y2 == False or df_ycelda2.dtype == 'datetime64[ns]'):
        df_ycelda2 = l_encod_y2.fit_transform(df_pais_2[y_celda2])

    ##### Asginamos Variables ##########################################
    x = np.asarray(df_xcelda).reshape(-1,1)
    x2 = np.asarray(df_xcelda2).reshape(-1,1)
    y = df_ycelda
    y2 = df_ycelda2
    ##### Graph datos extras ##########################################
    plt.scatter(df_pais_1[x_celda],df_pais_1[y_celda],color="red")
    plt.scatter(df_pais_2[x_celda],df_pais_2[y_celda2],color="blue")
    path_aux = fr.generarUrlImg("fig_muestra.png",lista_urls_static)
    plt.xlabel(x_celda)
    plt.ylabel(y_celda)
    plt.title("Datos ingresados\nrojo={}\nazul={}".format(nombre_pais1,nombre_pais2),fontsize=10)
    plt.xticks(rotation=45)
    plt.autoscale()
    plt.savefig(path_aux,bbox_inches = "tight")
    plt.clf()
    #### build ###############################################################
    grado = 3
    poly_feature = PolynomialFeatures(grado)
    x_transform = poly_feature.fit_transform(x)
    x_transform2 = poly_feature.fit_transform(x2)
    #### Train ###############################################################
    #algorithm
    l_reg = linear_model.LinearRegression()
    model = l_reg.fit(x_transform,y)
    y_predictions = model.predict(x_transform)
    ########### Entrenar 2
    model2 = l_reg.fit(x_transform2,y2)
    y_predictions2 = model2.predict(x_transform2)
    #### Calculate ###########################################################
    datos_calculados.append("grado usado : " + str(grado))
    datos_calculados.append(" datos de construccion grafica de {}:  ".format(nombre_pais1))
    datos_estaticos.append(" datos de construccion grafica de {}:  ".format(nombre_pais1))
    calculate(y,y_predictions,datos_estaticos,datos_calculados,model)
    datos_calculados.append(" datos de construccion grafica de {}:  ".format(nombre_pais2))
    datos_estaticos.append(" datos de construccion grafica de {}:  ".format(nombre_pais2))
    calculate(y2,y_predictions2,datos_estaticos,datos_calculados,model2)
    
    #### Graph #######################################################################
    # title = 'grado usado {}; RMSE = {}; R^2={:.3f}'.format(grado,round(rmse,2),r2)
    # plt.title(name+"\n"+title,fontsize=10)
    # plt.xlabel(x_celda)
    # plt.ylabel(y_celda)
    # plt.plot(df[x_celda],y_predictions,color="red",linewidth=3)
    # plt.xticks(rotation=45)
    # path_aux = fr.generarUrlImg("fig_tendencia.png",lista_urls_static)
    # plt.autoscale()
    # plt.savefig(path_aux,bbox_inches = "tight")
    # plt.clf()

    #### Prediccion ##########################################################
    # min_d = df_xcelda.min()
    # max_d = tiempo_predecir + len(y) + min_d ##Esto tiene que ser variable
    # # x_new = np.linspace(min_d,max_d)
    # x_new = np.arange(min_d,max_d).reshape(-1,1)
    # # x_new = np.array(x_new).reshape(-1,1)
    # x_new_transform = poly_feature.fit_transform(x_new)
    # y_new_predicted = model.predict(x_new_transform)

    # # print("Para el dia {0} contagios seran".format(max_d),y_new_predicted[-1]) ##Imprime la ultima prediccion
    # datos_calculados.append("Cantidad extra a predecir : " + str(tiempo_predecir))
    # if (df[x_celda].dtype == 'datetime64[ns]'):
    #     fecha = df_xcelda.max()
    #     tiempo_prediccion =  l_encod_x.inverse_transform([fecha])[0] + pd.Timedelta( str(tiempo_predecir) + ' days')
    #     datos_calculados.append("Tiempo de prediccion : " + str(tiempo_prediccion))
    # else:
    #     datos_calculados.append("Tiempo de prediccion : " + str(max_d-1))    
    # datos_calculados.append("Resultado de Prediccion : " + str(round(y_new_predicted[-1],2)))

    #### Graph #######################################################################
    title = 'grado usado {}'.format(grado)
    title2 = 'Azul={}\nrojo={}'.format(nombre_pais2,nombre_pais1)
    plt.title(name+"\n"+title+"\n"+title2,fontsize=10)
    plt.xlabel(x_celda)
    plt.ylabel(y_celda)
    plt.plot(df_pais_2[x_celda],y_predictions2,color="blue",linewidth=3)
    plt.plot(df_pais_1[x_celda],y_predictions,color="red",linewidth=3)
    plt.xticks(rotation=45)
    path_aux = fr.generarUrlImg("fig_prediccion.png",lista_urls_imgs)
    plt.autoscale()
    plt.savefig(path_aux,bbox_inches = "tight")
    plt.clf()
    #### enviar los datos #######################################################################
    return fr.addData(datos_calculados,lista_urls_imgs,lista_urls_static,datos_estaticos,'En la grafica se muestra la comparacion que exite entre {} y {} para la vacunacion'.format(nombre_pais1,nombre_pais2),name)


def calculate(y,y_predictions,datos_estaticos,datos_calculados,model):
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