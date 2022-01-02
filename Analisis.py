import reportes.TendenciaPais1 as case1
import reportes.PrediccionInfecPais2 as case2
import reportes.IndiceProgresion3 as case3
import reportes.PrediccionDepartamento4 as case4
import reportes.PrediccionDeadPais5 as case5
import reportes.AnDeadPais6 as case6
import reportes.TendenciaDiaPais7 as case7
import reportes.PrediccionInfecYear8 as case8
import reportes.TendenciaVacumPais9 as case9
import reportes.AnVacumPaises10 as case10
import reportes.TendenciaInfecPaisDep15 as case15
import reportes.MuerteRegPais14 as case14
import reportes.TasaDead22Pais as case22
import reportes.ComCasosTest24 as case24
import reportes.PrediccionCasoDia25 as case25

def redirigirAnalisis(filepath,caso,name,param):
    if caso == 1:
        #Tendencia de la infección por Covid-19 en un País.
        x_celda = param['tiempo']
        y_celda = param['confirmados']
        celda_pais = param['celda_pais']
        nombre_pais = param['nombre_pais']
        lista = case1.analizar(filepath,x_celda,y_celda,celda_pais,nombre_pais)
        return lista
    if caso == 2:
        lista = case2.analizar(filepath,param)
        return lista
    if caso == 3:
        lista = case3.analizar(filepath,param)
        return lista
    if caso == 4:
        lista = case4.analizar(filepath,param)
        return lista
    if caso == 5:
        lista = case5.analizar(filepath,param)
        return lista
    if caso == 6:
        lista = case6.analizar(filepath,param)
        return lista
    if caso == 7:
        lista = case7.analizar(filepath,param)
        return lista
    if caso == 8:
        lista = case8.analizar(filepath,param)
        return lista
    if caso == 9:
        lista = case9.analizar(filepath,param)
        return lista
    if caso == 10:
        lista = case10.analizar(filepath,param)
        return lista
    if caso == 14:
        lista = case14.analizar(filepath,param)
        return lista
    if caso == 15:
        lista = case15.analizar(filepath,param)
        return lista
    if caso == 22:
        lista = case22.analizar(filepath,param)
        return lista
    if caso == 24:
        lista = case24.analizar(filepath,param)
        return lista
    if caso == 25:
        lista = case25.analizar(filepath,param)
        return lista
        
    return {}