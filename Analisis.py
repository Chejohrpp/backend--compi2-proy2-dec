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
import reportes.PorcetanjeHombrePais11 as case11
import reportes.AnPaisContinente12 as case12
import reportes.PromInfecEdadPais13 as case13
import reportes.MuerteRegPais14 as case14
import reportes.TendenciaInfecPaisDep15 as case15
import reportes.PorcentajeDeadPais16 as case16
import reportes.TasaCompActivosDeadConti17 as case17
import reportes.CompInfecMunPais18 as case18
import reportes.PrediccionDeadYearPais19 as case19
import reportes.TasaCreDailyDead20 as case20
import reportes.PrediccionTodoMundo21 as case21
import reportes.TasaDead22Pais as case22
import reportes.FactoresDeadPais23 as case23
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
    if caso == 11:
        lista = case11.analizar(filepath,param)
        return lista
    if caso == 12:
        lista = case12.analizar(filepath,param)
        return lista
    if caso == 13:
        lista = case13.analizar(filepath,param)
        return lista
    if caso == 14:
        lista = case14.analizar(filepath,param)
        return lista
    if caso == 15:
        lista = case15.analizar(filepath,param)
        return lista
    if caso == 16:
        lista = case16.analizar(filepath,param)
        return lista
    if caso == 17:
        lista = case17.analizar(filepath,param)
        return lista
    if caso == 18:
        lista = case18.analizar(filepath,param)
        return lista
    if caso == 19:
        lista = case19.analizar(filepath,param)
        return lista
    if caso == 20:
        lista = case20.analizar(filepath,param)
        return lista
    if caso == 21:
        lista = case21.analizar(filepath,param)
        return lista
    if caso == 22:
        lista = case22.analizar(filepath,param)
        return lista
    if caso == 23:
        lista = case23.analizar(filepath,param)
        return lista
    if caso == 24:
        lista = case24.analizar(filepath,param)
        return lista
    if caso == 25:
        lista = case25.analizar(filepath,param)
        return lista
        
    return {}