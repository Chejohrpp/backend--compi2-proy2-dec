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
#             'parametros':['celda_activo','celda_genero','celda_pais'],
#             'opcionales': ['nombre_pais','celda_pais'],
#             'parametros_texto':['nombre_pais','identificador_genero']
#         }

# path_imgs = 'static/imgs_temp'
name = 'Porcentaje de hombres infectados por COVID en un Pais desde el primer caso activo'

def analizar(filepath,param):
    ### Asignacion de celdas  ###############################################
    x_celda = param['celda_activo']
    y_celda = param['celda_genero']
    celda_pais = param['celda_pais']
    nombre_pais = param['nombre_pais']
    tiempo_predecir = param['identificador_genero']
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
    plt.scatter(df[x_celda],df[y_celda],color="blue")

    path_aux = fr.generarUrlImg("fig_muestra.png",lista_urls_static)
    plt.xlabel(x_celda)
    plt.ylabel(y_celda)
    plt.title("Datos ingresados",fontsize=10)
    plt.xticks(rotation=45)
    plt.autoscale()
    plt.savefig(path_aux,bbox_inches = "tight")
    plt.clf()
    #### build ###############################################################
    grado = 12
    poly_feature = PolynomialFeatures(grado)
    x_transform = poly_feature.fit_transform(x)
    #### Train ###############################################################
    #algorithm
    # l_reg = linear_model.LinearRegression()

    # model = l_reg.fit(x_transform,y)
    # y_predictions = model.predict(x_transform)

    #### Calculate ###########################################################
    # datos_calculados.append("grado usado : " + str(grado))
    # rmse = np.sqrt(mean_squared_error(y,y_predictions))
    # # print("rmse:",rmse)
    # datos_calculados.append("rmse : " + str(round(rmse,2)))
    # datos_estaticos.append("rmse : " + str(rmse))
    # r2 = r2_score(y,y_predictions)
    # # print ("r^2:",r2)
    # datos_calculados.append("r^2 : " + str(round(r2,2)))
    # datos_estaticos.append("r^2 : " + str(r2))
    # #coef_
    # coef = model.coef_
    # datos_calculados.append("coef : " + str(coef[0]))
    # for i in range(1,len(coef)):
    #     datos_calculados.append("coef "+ str(i) +" : " + str(coef[i]))
    # datos_estaticos.append("coef : " + str(coef))
    # #intercep
    # intercept = model.intercept_
    # datos_calculados.append("intercept : " + str(intercept))
    # datos_estaticos.append("intercept : " + str(intercept))

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
    # title = 'grado usado {}; RMSE = {}; R^2={:.3f}'.format(grado,round(rmse,2),r2)
    # plt.title(name+"\n"+title,fontsize=10)
    # plt.xlabel(x_celda)
    # plt.ylabel(y_celda)
    # plt.plot(x_new,y_new_predicted,color="red",linewidth=3)
    # path_aux = fr.generarUrlImg("fig_prediccion.png",lista_urls_imgs)
    # plt.savefig(path_aux)
    # plt.clf()
    #### enviar los datos #######################################################################
    return fr.addData(datos_calculados,lista_urls_imgs,lista_urls_static,datos_estaticos,'',name)


