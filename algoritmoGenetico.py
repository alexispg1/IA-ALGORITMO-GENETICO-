import random
from random import randint 
import numpy as np
import scipy as sp
import matplotlib.pylab as plt
import tkinter.filedialog
import tkinter as tk

def poblacionInicial(poblacionInicial,cantidadEnfermeras):
    cantidadIndividuos=0
    poblacion=[]
    enfermeras=[]
    semana=[]
    dias=[]
    dias_de_la_semana=6
    while cantidadIndividuos<poblacionInicial:
        for i in range(cantidadEnfermeras): ##lleno el vector de enfermeras del 0 al 6 un numero representa a un nurse
            enfermeras.append(i)
        copia_enfermeras=enfermeras[:]
        poblacion.append(copia_enfermeras)##gen la pocicion i=0 guardo un vector de 6 pociciones
        enfermeras.clear() 
        semana_auxiliar=[]
        for j in range(len(poblacion[cantidadIndividuos])):#polbacion de 0,1 ++
            for k in range(dias_de_la_semana):
                dias.append(k)
            copia_dias=dias[:]
            dias.clear()
            semana_auxiliar.append(copia_dias)
        semana.append(semana_auxiliar)
        cantidadIndividuos=cantidadIndividuos+1

    generandoHorasSalariadas(poblacion,semana)

def generandoHorasSalariadas(poblacion,semana):
    horario_enfermera_por_dia=[]
    horario_enfermera_por_semana=[]
    horarios_enfermeras_por_semanas=[]
    for c in range(len(semana)):
        for d in range(len(poblacion[0])*len(semana[0][0])):
            departamento=random.randint(1,2)
            horas_trabajadas=random.randint(6,9)
            if horas_trabajadas==9:
                horario_enfermera_por_dia.append(departamento)
                horario_enfermera_por_dia.append(horas_trabajadas)
                extra=1
                horario_enfermera_por_dia.append(1)
                copia_horario_enfermera_por_dia=horario_enfermera_por_dia[:]
            else:
                horario_enfermera_por_dia.append(departamento)
                horario_enfermera_por_dia.append(horas_trabajadas)
                extra=random.randint(0,1)
                horario_enfermera_por_dia.append(extra)
                copia_horario_enfermera_por_dia=horario_enfermera_por_dia[:]
            horario_enfermera_por_dia.clear()    
            horario_enfermera_por_semana.append(copia_horario_enfermera_por_dia)
        copia_horario_enfermera_por_semana=horario_enfermera_por_semana[:]
        horario_enfermera_por_semana.clear()
        horarios_enfermeras_por_semanas.append(copia_horario_enfermera_por_semana)      
    fitness(poblacion,semana,horarios_enfermeras_por_semanas)


def fitness(poblacion,semana,horarios_enfermeras_por_semanas):
   
    contador=0
    contador_de_tiempo_extra=0
    Horas_Trabajadas=[]
    suma_de_horas=0
    suma_de_horas_arreglo=[]
    suma_total_de_horas_por_individuo=[]
    tiempo_extra=[]
    tiempo_extra_total=[]
    ITERAR.append("1")
    if len(ITERAR)==TOTAL_DE_GENERACIONES+1:
        graficar()

    else:
        for i in range(len(horarios_enfermeras_por_semanas)):
            for j in range(len(horarios_enfermeras_por_semanas[0])):
                if(contador==len(horarios_enfermeras_por_semanas[0])/len(semana[0])-1):
                    suma_de_horas=suma_de_horas+horarios_enfermeras_por_semanas[i][j][1]
                    suma_de_horas_arreglo.append(suma_de_horas)
                    suma_de_horas=0
                    contador=0
                    if horarios_enfermeras_por_semanas[i][j][2]==1:
                        contador_de_tiempo_extra=contador_de_tiempo_extra+1
                        tiempo_extra.append(contador_de_tiempo_extra)
                        contador_de_tiempo_extra=0
                    else:
                        tiempo_extra.append(contador_de_tiempo_extra)
                        contador_de_tiempo_extra=0  
                else:
                    suma_de_horas=suma_de_horas+horarios_enfermeras_por_semanas[i][j][1]
                    contador=contador+1
                    if horarios_enfermeras_por_semanas[i][j][2]==1:
                        contador_de_tiempo_extra=contador_de_tiempo_extra+1
            copia=suma_de_horas_arreglo[:]
            suma_total_de_horas_por_individuo.append(copia)
            suma_de_horas_arreglo.clear()
            copia_t_extra=tiempo_extra[:]
            tiempo_extra_total.append(copia_t_extra)
            tiempo_extra.clear()
        pago_total_de_horas=0
        pago_total_de_horas_extra=0
    
        fitness=[]
        for k in range(len (suma_total_de_horas_por_individuo)):
            suma_horas_por_individuo=sum(suma_total_de_horas_por_individuo[k])
            suma_horas_extra_por_individuo=sum(tiempo_extra_total[k])
            pago_total_de_horas=suma_horas_por_individuo*SALARIO_MINIMO
            pago_total_de_horas_extra=suma_horas_extra_por_individuo*TIEMPO_EXTRA
            pago_total_con_tiempo_extra=pago_total_de_horas+pago_total_de_horas_extra
            fitness.append(pago_total_con_tiempo_extra)    

        tamanioInicialPoblacion=len(fitness) 
        maximo_valor=max(fitness)# obtengo el maximo valor  del fitnnes total de los individuos 
        MAXIMOS.append(maximo_valor) #el maximo valor se agrega en la lista de maximos
        minimo_valor=min(fitness)#obtengo el minimo valor  del fitnnes total de los diez indivuos 
        MINIMOS.append(minimo_valor)#el minimo valor se agrega en la lista minimos
        sumatoria=sum(fitness)#sumo toda la lista de los fitnnes total de los individuos 
        longitud=float(len(fitness))#obtengo la cantidad de individuos 
        promedio=sumatoria/longitud #obtengo el promedio
        PROMEDIOS.append(int(promedio)) #guardo el promedio en las lista promedios    
    
        pocision=fitness.index(minimo_valor)
    
        MEJORES_iNDIVIDUOS.append(poblacion[pocision])
        MEJORES_SEMANAS.append(semana[pocision])
        MEJORES_HORARIOS.append(horarios_enfermeras_por_semanas[pocision])
        mejor_horario_semanal_de_todos=horarios_enfermeras_por_semanas[pocision]
        MEJORES_PAGOS.append(fitness[pocision])
        
        ruleta(mejor_horario_semanal_de_todos,poblacion,semana,horarios_enfermeras_por_semanas,suma_total_de_horas_por_individuo,tiempo_extra_total,fitness)
def ruleta(mejor_horario_semanal_de_todos,poblacion,semana,horarios_enfermeras_por_semanas,suma_total_de_horas_por_individuo,tiempo_extra_total,fitness):

    array_mejor_horario_semanal_de_todos=np.array(mejor_horario_semanal_de_todos)
    lista_Normal_fitness=np.array(fitness) 
    lista_mayor_a_menor_fitness=fitness  
    lista_mayor_a_menor_fitness.sort(reverse=True)
    lista_suma_fitness=[]
    suma_por_fitness=0
    
    for i in range(len(lista_mayor_a_menor_fitness)):
        suma_por_fitness=suma_por_fitness+lista_mayor_a_menor_fitness[i]
        lista_suma_fitness.append(suma_por_fitness)
    lista_suma_fitness_total=sum(lista_suma_fitness)     
    lista_porcentajes=[]
    
    for k in range(len(lista_suma_fitness)):
        porcentaje=int(lista_suma_fitness[k]/lista_suma_fitness_total*100)
        lista_porcentajes.append(porcentaje)

    array_porcentajes=np.array(lista_porcentajes)
    lista_mayor_a_menor_porcentaje=lista_porcentajes  
    lista_mayor_a_menor_porcentaje.sort(reverse=True) 
    
    intervalos=[]
    suma_intervalos=0
    for x in range(len(lista_mayor_a_menor_porcentaje)):
        suma_intervalos=suma_intervalos+lista_mayor_a_menor_porcentaje[x]
        intervalos.append(suma_intervalos)    
    suma_total_porcentajes=np.sum(array_porcentajes)
    suma_total_porcentajes=np.sum(array_porcentajes)
    
    individuos=0
    tamanioInicialPoblacion=len(semana)
    encontrado_aleatorio_1=False
    encontrado_aleatorio_2=False
    individuo1Acruzar=0
    individuo2Acruzar=0

    semana_nuevas=[]
    horarios_enfermeras_por_semanas_nuevas=[]
    while individuos<tamanioInicialPoblacion:
        aleatorio_1=random.randint(0,suma_total_porcentajes)
        aleatorio_2=random.randint(0,suma_total_porcentajes)
        for k in range(len(intervalos)) :
            if k==0 and aleatorio_1<=intervalos[k] :
                individuo1Acruzar=k
                encontrado_aleatorio_1=True
            if aleatorio_1<=intervalos[k] and aleatorio_1>intervalos[k-1]:
                individuo1Acruzar=k
                encontrado_aleatorio_1=True
            if k==0 and aleatorio_2<=intervalos[k] :
                individuo2Acruzar=k
                encontrado_aleatorio_2=True
            if aleatorio_2<=intervalos[k] and aleatorio_2>intervalos[k-1]:   
                individuo2Acruzar=k
                encontrado_aleatorio_2=True
            if(encontrado_aleatorio_1==True and encontrado_aleatorio_2==True): 
                #BUSCAR EN PORCENTAJES DECENDENTES
                numero1_porcentaje=lista_mayor_a_menor_porcentaje[individuo1Acruzar]
                numero2_porcentaje=lista_mayor_a_menor_porcentaje[individuo2Acruzar]
                #BUCAR LOS PORCENTAJES NORMALES
                lista_porcentajes_normal=list(array_porcentajes)
                pocision_1=lista_porcentajes_normal.index(numero1_porcentaje)
                pocision_2=lista_porcentajes_normal.index(numero2_porcentaje)
                #BUSCAR EN FITNNES DECENDENTE 
                numero1_de_fitness_dec=lista_mayor_a_menor_fitness[pocision_1]
                numero2_de_fitness_dec=lista_mayor_a_menor_fitness[pocision_2]
                #BUSCAR LAS POCICIONES EN FITNESS NORMAL 
                pocision1_fitness_normal=list(lista_Normal_fitness).index(numero1_de_fitness_dec)
                pocision2_fitness_normal=list(lista_Normal_fitness).index(numero2_de_fitness_dec)
                #ENCONTRAMOS LOS NUMEROS DEL FITNESS NORMAL
                numero1_de_fitness=lista_Normal_fitness[pocision1_fitness_normal]
                numero2_de_fitness=lista_Normal_fitness[pocision2_fitness_normal]
                #ENCONTRAMOS LAS POCISIONES DE LOS NUMERO DEL FITNESS NORMAL
                pocision1_fitness_cruza=list(lista_Normal_fitness).index(numero1_de_fitness)
                pocision2_fitness_cruza=list(lista_Normal_fitness).index(numero2_de_fitness)
                #aqui mando a llamar ala cruza y mutacion 
                Hijo_1,Hijo_2,horarios_enfermeras_por_semanas_1,horarios_enfermeras_por_semanas_2=cruza_mutacion(pocision1_fitness_cruza,pocision2_fitness_cruza,poblacion,semana,horarios_enfermeras_por_semanas)
                #creando la nueva poblacion 
                if individuos+1==len(semana):
                    semana_nuevas.append(Hijo_1)
                    horarios_enfermeras_por_semanas_nuevas.append(horarios_enfermeras_por_semanas_1)
                else:   
                    semana_nuevas.append(Hijo_1)
                    semana_nuevas.append(Hijo_2)
                    horarios_enfermeras_por_semanas_nuevas.append(horarios_enfermeras_por_semanas_1)
                    horarios_enfermeras_por_semanas_nuevas.append(horarios_enfermeras_por_semanas_2)
                break    
        encontrado_aleatorio_1=False
        encontrado_aleatorio_2=False 
        individuos=len(semana_nuevas)   

    aux_array_mejor_horario_semanal_de_todos=array_mejor_horario_semanal_de_todos.tolist()
    horarios_enfermeras_por_semanas_nuevas.remove(horarios_enfermeras_por_semanas_nuevas[0])
    horarios_enfermeras_por_semanas_nuevas.insert(0,aux_array_mejor_horario_semanal_de_todos)
    nuevosCandidatos(poblacion,semana_nuevas,horarios_enfermeras_por_semanas_nuevas)

   
def nuevosCandidatos(poblacion,semana_nuevas,horarios_enfermeras_por_semanas_nuevas):

    fitness(poblacion,semana_nuevas,horarios_enfermeras_por_semanas_nuevas)

def cruza_mutacion(pocision1_fitness_cruza,pocision2_fitness_cruza,poblacion,semana,horarios_enfermeras_por_semanas):

    semana_1=semana[pocision1_fitness_cruza]
    semana_2=semana[pocision2_fitness_cruza]
    veces_a_recorrer=len(semana_1)
    Hijo_nuevo1=[]
    Hijo_nuevo2=[]
    for i in range(veces_a_recorrer):
        numero1_random=random.randint(1,len(semana[0][0])-3)
        Auxiliar1_semana1=semana_1[i]
        Auxiliar2_semana2=semana_2[i]
        parte_A1__semana1=Auxiliar1_semana1[0:numero1_random]
        parte_A2__semana1=Auxiliar1_semana1[numero1_random:]
        parte_B1__semana2=Auxiliar2_semana2[0:numero1_random]
        parte_B2__semana2=Auxiliar2_semana2[numero1_random:]
        nuevo_individuo_1=parte_A1__semana1+parte_B2__semana2
        nuevo_individuo_2=parte_B1__semana2+parte_A2__semana1
        Hijo_nuevo1.append(nuevo_individuo_1)
        Hijo_nuevo2.append(nuevo_individuo_2)

    auxililiar1_horarios_enfermeras_por_semanas=horarios_enfermeras_por_semanas[pocision1_fitness_cruza]
    auxililiar2_horarios_enfermeras_por_semanas=horarios_enfermeras_por_semanas[pocision2_fitness_cruza]
    
    for j in range(len(auxililiar1_horarios_enfermeras_por_semanas)):
        provabilidad_mutacion=random.randint(0,100)
        if provabilidad_mutacion<=PROBABILIDAD_DE_MUTACION:
            horas_trabajadas=random.randint(6,9)
            auxililiar1_horarios_enfermeras_por_semanas[j][1]=horas_trabajadas

    for k in range(len(auxililiar2_horarios_enfermeras_por_semanas)):
        provabilidad_mutacion_1=random.randint(0,100)
        if provabilidad_mutacion_1<=PROBABILIDAD_DE_MUTACION:
            horas_trabajadas_1=random.randint(6,9)
            auxililiar2_horarios_enfermeras_por_semanas[k][1]=horas_trabajadas_1
   
    return Hijo_nuevo1,Hijo_nuevo2,auxililiar1_horarios_enfermeras_por_semanas,auxililiar2_horarios_enfermeras_por_semanas

    
def graficar():
 
    print(MEJORES_PAGOS)
    valor_minimo=min(MEJORES_PAGOS)
    pocision_valor_minimo=MEJORES_PAGOS.index(valor_minimo)
    print("MEJORES INDIVIDUOS")
    print(MEJORES_iNDIVIDUOS[pocision_valor_minimo])
    print("MEJORES SEMANAS")
    print(MEJORES_SEMANAS[pocision_valor_minimo])
    print("MEJORES HORARIOS ")
    print(MEJORES_HORARIOS[pocision_valor_minimo])
    print("MEJOR PAGO ")
    print(MEJORES_PAGOS[pocision_valor_minimo])

    plt.title("Evolución del Fitness")
    plt.plot(MAXIMOS,linestyle='-', label = "peores casos")
    plt.plot(PROMEDIOS,linestyle='-', label = "casos promedios")
    plt.plot(MINIMOS,linestyle='-', label = "mejores casos")
    plt.ylabel("Salarios de las Enfermeras") 
    plt.xlabel("Generación")  
    plt.legend()
    plt.show()
    


SALARIO_MINIMO=80
TIEMPO_EXTRA=50
MAXIMOS=[]
MINIMOS=[]
PROMEDIOS=[]

MEJORES_iNDIVIDUOS=[]
MEJORES_SEMANAS=[]
MEJORES_HORARIOS=[]
MEJORES_PAGOS=[]

PROBABILIDAD_DE_MUTACION=60
CANTIDAD_DE_POBLACION=8
CANTIDAD_DE_ENFERMERAS=5
ITERAR=[]
TOTAL_DE_GENERACIONES=200
ITERAR=[]
poblacionInicial(CANTIDAD_DE_POBLACION,CANTIDAD_DE_ENFERMERAS)




