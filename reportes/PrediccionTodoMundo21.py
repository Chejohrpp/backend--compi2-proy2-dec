import os
import datetime

from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

from sklearn.neural_network import MLPRegressor

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import fun_main as fm
import fun_reportes as fr
#  'Predicciones de casos y muertes en todo el mundo':{
#              'caso':21,
#             'name':'Predicciones de casos y muertes en todo el mundo',
#             'no_parametros': 4,
#             'parametros':['tiempo','celda_confirmados','celda_fallecidos'],
#             'parametros_numericos':['tiempo_predecir'],
#        }

path_imgs = 'static/imgs_temp'
name = 'Predicciones de casos y muertes en todo el mundo'

def analizar(filepath,param):
    ### Asignacion de celdas  ###############################################
    x_celda = param['tiempo']
    y_celda = param['celda_confirmados']
    y_celda2 = param['celda_fallecidos']
    tiempo_predecir = param['tiempo_predecir']
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
    limpia_x =fr.limpiarData(df,x_celda)
    limpia_y = fr.limpiarData(df,y_celda)
    limpia_y2 = fr.limpiarData(df,y_celda2)

    df_xcelda = df[x_celda]
    if (limpia_x == False or df_xcelda.dtype == 'datetime64[ns]'):
        df_xcelda = l_encod_x.fit_transform(df[x_celda])

    df_ycelda = df[y_celda]
    if (limpia_y == False or df_ycelda.dtype == 'datetime64[ns]'):
        df_ycelda = l_encod_y.fit_transform(df[y_celda])

    df_ycelda2 = df[y_celda2]
    if (limpia_y2 == False or df_ycelda2.dtype == 'datetime64[ns]'):
        df_ycelda2 = l_encod_y2.fit_transform(df[y_celda2])

    ##### Asginamos Variables ##########################################
    x = np.asarray(df_xcelda).reshape(-1,1)
    y = df_ycelda
    y2 = df_ycelda2
    ##### datos extras ##########################################
    plt.scatter(df[x_celda],df[y_celda],color="red")
    plt.scatter(df[x_celda],df[y_celda2],color="blue")
    path_aux = fr.generarUrlImg("fig_muestra.png",lista_urls_static)
    plt.xlabel(x_celda)
    # plt.ylabel(y_celda)
    plt.title("Datos ingresados\nrojo={}\nazul={}".format(y_celda,y_celda2),fontsize=10)
    plt.xticks(rotation=45)
    plt.autoscale()
    plt.savefig(path_aux,bbox_inches = "tight")
    plt.clf()
    #### build ###############################################################
    # grado = 3
    # poly_feature = PolynomialFeatures(grado)
    # x_transform = poly_feature.fit_transform(x)
    # #### Train ###############################################################
    # #algorithm
    # l_reg = linear_model.LinearRegression()
    # model = l_reg.fit(x_transform,y)
    # y_predictions = model.predict(x_transform)

    ## confirmados
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.4)
    mlr = MLPRegressor(hidden_layer_sizes=(3,3),solver='lbfgs',alpha=1e-5,random_state=1)
    model = mlr.fit(x_train,y_train)
    y_predictions = mlr.predict(x)

    ## fallecidos
    x_train2,x_test2,y_train2,y_test2 = train_test_split(x,y2,test_size=0.4)
    mlr2 = MLPRegressor(hidden_layer_sizes=(3,3),solver='lbfgs',alpha=1e-5,random_state=1)
    model2 = mlr2.fit(x_train2,y_train2)
    y_predictions2 = mlr2.predict(x)

    # #### Calculate ###########################################################    
    datos_calculados.append(" datos de construccion grafica de {}:  ".format(y_celda))
    datos_estaticos.append(" datos de construccion grafica de {}:  ".format(y_celda))
    calculate(y,y_predictions,datos_estaticos,datos_calculados,model,mlr,x_train,y_train)
    datos_calculados.append(" datos de construccion grafica de {}:  ".format(y_celda2))
    datos_estaticos.append(" datos de construccion grafica de {}:  ".format(y_celda2))
    calculate(y2,y_predictions2,datos_estaticos,datos_calculados,model2,mlr2,x_train2,y_train2)

    # #### Graph #######################################################################
    title2 = 'Azul={}\nrojo={}'.format(y_celda2,y_celda)
    plt.title(name+"\n"+title2,fontsize=10)
    plt.xlabel(x_celda)
    plt.plot(df[x_celda],y_predictions2,color="blue",linewidth=3)
    plt.plot(df[x_celda],y_predictions,color="red",linewidth=3)
    plt.xticks(rotation=45)
    path_aux = fr.generarUrlImg("fig_tendencia.png",lista_urls_static)
    plt.autoscale()
    plt.savefig(path_aux,bbox_inches = "tight")
    plt.clf()

    # #### Prediccion ##########################################################
    min_d = df_xcelda.min()
    max_d = tiempo_predecir + len(y) + min_d ##Esto tiene que ser variable
    # x_new = np.linspace(min_d,max_d)
    x_new = np.arange(min_d,max_d).reshape(-1,1)
    # x_new = np.array(x_new).reshape(-1,1)
    y_new_predicted = mlr.predict(x_new)
    y_new_predicted2 = mlr2.predict(x_new)

    # print("Para el dia {0} contagios seran".format(max_d),y_new_predicted[-1]) ##Imprime la ultima prediccion
    datos_calculados.append("Cantidad extra a predecir : " + str(tiempo_predecir))
    if (df[x_celda].dtype == 'datetime64[ns]'):
        fecha = df_xcelda.max()
        tiempo_prediccion =  l_encod_x.inverse_transform([fecha])[0] + pd.Timedelta( str(tiempo_predecir) + ' days')
        datos_calculados.append("Tiempo de prediccion : " + str(tiempo_prediccion))
    else:
        datos_calculados.append("Tiempo de prediccion : " + str(max_d-1))    
    datos_calculados.append("Resultado de Prediccion para {} : ".format(y_celda) + str(round(y_new_predicted[-1],2)))
    datos_calculados.append("Resultado de Prediccion para {} : ".format(y_celda2) + str(round(y_new_predicted2[-1],2)))

    # #### Graph #######################################################################
    title = 'Azul={}\nrojo={}'.format(y_celda2,y_celda)
    plt.title(name+"\n"+title,fontsize=10)
    plt.xlabel(x_celda)
    # plt.ylabel(y_celda)
    plt.plot(x_new,y_new_predicted2,color="blue",linewidth=3)
    plt.plot(x_new,y_new_predicted,color="red",linewidth=3)
    path_aux = fr.generarUrlImg("fig_prediccion.png",lista_urls_imgs)
    plt.savefig(path_aux)
    plt.clf()
    #### enviar los datos #######################################################################
    return fr.addData(datos_calculados,lista_urls_imgs,lista_urls_static,datos_estaticos,fr.makeConclusionPredic2(round(y_new_predicted[-1],2),round(y_new_predicted2[-1],2)),name)


def calculate(y,y_predictions,datos_estaticos,datos_calculados,model,mlr,x_train,y_train):
    # datos_calculados.append("grado usado : " + str(grado))
    rmse = np.sqrt(mean_squared_error(y,y_predictions))
    # # print("rmse:",rmse)
    datos_calculados.append("rmse : " + str(round(rmse,2)))
    datos_estaticos.append("rmse : " + str(rmse))
    # r2 = r2_score(y,y_predictions)
    r2 = mlr.score(x_train,y_train)
    # # print ("r^2:",r2)
    datos_calculados.append("r^2 : " + str(round(r2,2)))
    datos_estaticos.append("r^2 : " + str(r2))
    #### max iter
    max_iter = model.max_iter
    datos_calculados.append("maximo de iteracion : " + str(round(max_iter,2)))
    datos_estaticos.append("maximo de iteracion : " + str(max_iter))