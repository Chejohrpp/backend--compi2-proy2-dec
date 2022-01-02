import os
from sklearn import linear_model
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error
from datetime import datetime

import funciones.Primarias as Primarias

ROOT_PATH = os.environ.get('ROOT_PATH')

path = "reportes/test.csv"

### Prediccion de infectados en un Pais ###
def infectadosPais(file,pais,celda_confirmados,celda_fecha,dias_predicir=0):

    ### GET DataFrame  ###############################################
    df = Primarias.getDataFrame(file)
    if(df.empty):
        print ('Error, no hay un dataframe')
        return False 

    ######### Limpiar los datos ##########################################

    l_encoder = preprocessing.LabelEncoder()
    fecha_encoder = l_encoder.fit_transform(df[celda_fecha].to_numpy())


    ##### Asginamos Variables ##########################################
    y = df[celda_confirmados] # celda de Y
    x = np.array(fecha_encoder).reshape(-1,1) #celda de X

    # ##datos extras##
    # fecha_encoder_50 = l_encoder.fit_transform(df[celda_fecha].to_numpy())
    # y_50 = df[celda_confirmados]
    # plt.scatter(fecha_encoder_50,y_50,color="blue")

    #### build ###############################################################
    grado = 3
    poly_feature = PolynomialFeatures(grado)
    x_transform = poly_feature.fit_transform(x)

    #### Train ###############################################################

    #algorithm
    l_reg = linear_model.LinearRegression()

    model = l_reg.fit(x_transform,y)
    y_predictions = model.predict(x_transform)

    # plt.plot(fecha_encoder,y_predictions,color="red",linewidth=4)

    #### Calculate ###########################################################
    rmse = np.sqrt(mean_squared_error(y,y_predictions))
    print("rmse:",rmse)
    r2 = r2_score(y,y_predictions)
    print ("r^2:",r2)    
    
    #### Prediccion ##########################################################
    min_d = 0.0
    max_d = dias_predicir + len(y)  ##Esto tiene que ser variable
    # x_new = np.linspace(min_d,max_d)
    x_new = np.arange(max_d).reshape(-1,1)
    # x_new = np.array(x_new).reshape(-1,1)
    x_new_transform = poly_feature.fit_transform(x_new)
    y_new_predicted = model.predict(x_new_transform)

    print("Para el dia {0} contagios seran".format(max_d),y_new_predicted[-1]) ##Imprime la ultima prediccion

    #### Graph #######################################################################
    title = 'grado usado {}; RMSE = {}; R^2={:.3f}'.format(grado,round(rmse,2),r2)
    plt.title("Prediccion de infectados en un Pais\n"+title,fontsize=10)
    plt.xlabel("dias trancurridos")
    plt.ylabel("contagiados confirmados")
    plt.plot(x_new,y_new_predicted,color="red",linewidth=3)
    # plt.savefig("fig1.png")
    plt.show()

# infectadosPais(path,'Guatemala','confirmados','fecha',0)
        
########### Predicción de casos confirmados por día #######################################
def contagiosDia(file,pais,dias_predec=0):
    ### GET DataFrame  ###############################################
    df = Primarias.getDataFrame(file)
    if(df.empty):
        print ('Error, no hay un dataframe')
        return False
    df = transDFcontagiosDia(df,pais)

    ######### Limpiar los datos ##########################################
    df_fecha = np.array([])
    for i in df["fecha"].to_numpy():
        df_fecha = np.append(df_fecha,datetime.strptime(i, '%m/%d/%y'))

    l_encoder = preprocessing.LabelEncoder()
    fecha_encoder = l_encoder.fit_transform(df_fecha)

    ##### Asginamos Variables ##########################################
    y = df["casos_nuevos"] # celda de Y
    x = np.array(fecha_encoder).reshape(-1,1) #celda de X
    plt.bar(fecha_encoder,y)
    # plt.show()

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
    rmse = np.sqrt(mean_squared_error(y,y_predictions))
    r2 = r2_score(y,y_predictions)

    #### Prediccion ##########################################################
    min_d = 0.0
    max_d = dias_predec + len(y)  ##Esto tiene que ser variable
    # x_new = np.linspace(min_d,max_d)
    x_new = np.arange(max_d).reshape(-1,1)
    # x_new = np.array(x_new).reshape(-1,1)
    x_new_transform = poly_feature.fit_transform(x_new)
    y_new_predicted = model.predict(x_new_transform)
    print("Para el dia {0} contagios seran".format(max_d),y_new_predicted[-1]) ##Imprime la ultima prediccion

    #### Graph #######################################################################
    title = 'grado usado {}; RMSE = {}; R^2={:.3f}'.format(grado,round(rmse,2),r2)
    plt.title("Prediccion de infectados en un Pais\n"+title,fontsize=10)
    plt.xlabel("dias trancurridos")
    plt.ylabel("contagiados confirmados")
    plt.plot(x_new,y_new_predicted,color="red",linewidth=3)
    # plt.savefig("fig1.png")
    plt.show()


def transDFcontagiosDia(df,pais):
    df = df[df["Country/Region"].str.contains(pais)] ## country/region  se cambia
    df_datos = df.filter(regex="^[1-9]*\d/")
    confirmados = df_datos.to_numpy()
    fechas = np.asanyarray(df_datos.columns)
    confirmados = confirmados.ravel()
    casosNuevos = np.array([])
    ant = None
    for i in confirmados:
        if (ant == None):
            ant = i
            casosNuevos = np.append(casosNuevos,[i])
        else:
            case = i - ant
            casosNuevos = np.append(casosNuevos,[case])
            ant = i
    df_new = pd.DataFrame()
    df_new["fecha"] = fechas
    df_new["casos_nuevos"] = casosNuevos
    return df_new

path_2 = "reportes\global.csv"
contagiosDia(path_2,'Guatemala',20)