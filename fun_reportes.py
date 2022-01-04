
import pandas as pd
from sklearn.preprocessing import LabelEncoder

path_imgs = 'static/imgs_temp'
def generarUrlImg(name,lista_urls_imgs):
    url_temp = path_imgs + '/' + name
    lista_urls_imgs.append(url_temp)
    return url_temp

def limpiarData(df,celda):
    tipo = df[celda].dtypes
    if tipo == 'O':
        try:
            df[celda] = pd.to_numeric(df[celda].str.split(',').str.join(''))
            return True
        except:
            try:
                df[celda] = pd.to_numeric(df[celda])
                return True
            except:
                try:
                  df[celda]= pd.to_datetime(df[celda])
                  return True
                except:
                    print('hay un error al covertir de string to number')
                    return False
    return True

def limpiarColumna(df,celda):
    return df.dropna(subset=[celda])


def addData(datos_calculados,lista_urls_imgs,lista_urls_static,datos_estaticos,conclusion,name):
    lista_datos ={
        'lista_urls': lista_urls_imgs,
        'calculos_reporte': datos_calculados,
        'lista_urls_static':lista_urls_static,
        'conclusion': conclusion,
        "datos_statics":datos_estaticos,
        'name_case':name
    }
    return lista_datos

def makeConclusionPredic(prediccion):
    conclusion = 'Con los todos los datos dados, se entreno al modelo para realizar la prediccion y se llego al resultado estimado que es de {}'.format(prediccion)
    return conclusion

def makeConclusionPredic2(prediccion1,prediccion2):
    conclusion = 'Con los todos los datos dados y utilizando Neural Network MLPRegressor se entreno al modelo para realizar las predicciones y se llegaron al resultado que es de {} y {} respectivamente'.format(prediccion1,prediccion2)
    return conclusion