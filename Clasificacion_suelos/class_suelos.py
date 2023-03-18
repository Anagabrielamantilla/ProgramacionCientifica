# -*- coding: utf-8 -*-
"""class_suelos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ohLlFX7WOqqNaiOtep8PZkOKgXaQcrou
"""

def suelos_finos(grava, arena, finos, PI, LL):
  '''
  Función para clasificar los suelos 
  de grano fino según el sistema de 
  clasificación unificado. Tomado de Bras 
  (7ma edición, pág 23)

  grava : porcentaje de material tamaño grava
  arena : porcentaje de material tamaño arena 
  finos : porcentaje de material tamaño fino
  PI: índice de plasticidad 
  LL: límite líquido
  '''
  # Primera condición
  if LL>=50:
    a = 'Arcilla gruesa o limo elástico'
    b = ''

  # Segunda condición

  elif LL<50:
    if PI>7:
      b= 'CL'          
      if finos<30:
        if finos<15:
          a = 'Arcilla fina'
        else:
          if arena>=grava:
            a = 'Arcilla fina con arena'
          else: 
            a = 'Arcilla fina con grava'
      if finos>=30:
        if arena>=grava:
          if grava<15:
            a = 'Arcilla fina arenosa'
          else: 
             a = 'Arcilla fina arenosa con grava'
        elif arena<grava:
          if arena<15:
            a = 'Arcilla fina gravosa'
          elif arena>=15:
            a = 'Arcilla fina gravosa con arena'

# Hasta aquí va el primer arbole donde PI>7

   # Tercera condición
    
    elif 4<=PI<=7:
      b = 'CL-ML'      
      if finos<30:
       if finos<15:
         a = 'Arcilla limosa'
       else: 
         if arena>=grava:
           a = 'Arcilla limosa con arena'
         else: 
           a = 'Arcilla limosa con grava'
      if finos>=30:
       if arena>=grava:
         if grava<15:
           a = 'Arcilla arenosa-limosa'
         else:
           a = 'Arcilla arenosa-limosa con grava'
       elif arena<grava:
         if arena<15:
           a = 'Arcilla gravosa-limosa'
         else: 
           a = 'Arcilla gravosa-limosa con arena'

# Hasta aquí va el segundo arbol donde 4<=PI<=7

   # Cuarta condición

    elif PI<4:
      b='ML'
      if finos<30:
       if finos<15:
         a='Limo'
       else: 
         if arena>=grava:
           a='Limo con arcilla'
         else: 
           a='Limo con grava'
      if finos>=30:
       if arena>=grava:
         if grava<15:
           a='Limo arenoso'
         else:
           a='Limo arenosa con grava'
       elif arena<grava:
         if arena<15:
           a='Limo gravosa'
         else: 
           a= 'Limo gravosa con arena'

  return a + ' ' + b

def clasificacion(grava,arena,finos,cu,cc,ip,LL):
  
  ''' 

  Función para clasificar los suelos
  a partir de ensayos de laboratorio
  según el Sistema de Clasificación 
  Unificado de Clasificación de Suelos. 
  Tomado de Braja (7ma ed, p.23)

  grava : porcentaje de material tamaño grava
  arena : porcentaje de material tamaño arena 
  finos : porcentaje de material tamaño fino
  cu: coeficiente de uniformidad
  cc: coeficiente de graduación o de curvatura
  ip: índice de plasticidad 
  LL: límite líquido
  '''

  if finos<50:
        if grava>arena: #Se clasifica como grava (G)
            if finos>12: #Porcentaje de finos mayor a 12%
                if ip<(0.73*(LL-20)) or ip>7: #indice de plasticidad mayor a 7
                    a="GC"
                    if arena < 15:
                        b="GRAVA ARCILLOSA"
                    else:
                        b="GRAVA ARCILLOSA CON ARENA"
                elif ip<(0.73*(LL-20)) or ip<4: #indice de plasticidad menor a 4
                    a="GM"
                    if arena < 15:
                        b="GRAVA LIMOSA"
                    else:
                        b="GRAVA LIMOSA CON ARENA"
                elif ip>4 and ip<7: #indice de plasticidad entre 4 y 7
                    a="GC-GM"
                    if arena < 15:
                        b="GRAVA LIMO-ARCILLOSA"
                    else:
                        b="GRAVA LIMO-ARCILLOSA CON ARENA"
            elif finos<5: #Porcentaje finos menor a 5%
                if cu>=4 and (cc<3 or cc>1):
                    a="GW"
                    if arena < 15:
                        b=("GRAVA BIEN GRADUADA")
                    else:
                        b=("GRAVA BIEN GRADUADA CON ARENA")
                else:
                    a="GP"
                    if arena < 15:
                        b=("GRAVA MAL GRADUADA")
                    else:
                        b=("GRAVA MAL GRADUADA CON ARENA")
            else: # Porcentaje finos entre 5% y 12%
                if cu>=4 and (cc>=1 and cc<=3):
                    if ip<(0.73*(LL-20)) or ip<4:
                        a="GW-GM";
                        if arena < 15:
                            b=("GRAVA BIEN GRADUADA CON LIMO")
                        else:   
                            b=("GRAVA BIEN GRADUADA CON LIMO Y ARENA")
                    else:
                        a="GW-GC";
                        if arena < 15:
                            b=("GRAVA BIEN GRADUADA CON ARCILLA")
                        else:
                            b=("GRAVA BIEN GRADUADA CON ARCILLA Y ARENA")
                elif cu<4 or (cc<1 or cc>3):
                    if ip<(0.73*(LL-20)) or ip<4:
                        a="GP-GM";
                        if arena < 15:
                            b=("GRAVA MAL GRADUADA CON LIMO")
                        else:
                            b=("GRAVA MAL GRADUADA CON LIMO Y ARENA")
                    else:
                        a="GP-GC";
                        if arena < 15:
                            b=("GRAVA MAL GRADUADA CON ARCILLA")
                        else:
                            b=("GRAVA MAL GRADUADA CON ARCILLA Y ARENA")
        else:           #Se clasifica como arena  (S)
            b=("ARENA")
            if finos>12: #Porcentaje de finos mayor a 12%
                if ip>(0.73*(LL-20)) and ip>7: #indice de plasticidad mayor a 7
                    a="SC"
                    if grava < 15:
                        b=("ARENA ARCILLOSA")
                    else:
                        b=("ARENA ARCILLOSA CON GRAVA")
                elif ip<(0.73*(LL-20))or ip<4: #indice de plasticidad menor a 4
                    a="SM"
                    if grava < 15:
                        b=("ARENA LIMOSA")
                    else:
                        b=("ARENA LIMOSA CON GRAVA")
                elif ip>4 and ip<7: #indice de plasticidad entre 4 y 7
                    a="SC-SM"
                    if grava < 15:
                        b=("ARENA LIMO-ARCILLOSA")
                    else:
                        b=("ARENA LIMO-ARCILLOSA CON GRAVA")
            elif finos<5: #Porcentaje finos menor a 5%
                if cu>=6 and (cc<3 or cc>1):
                    a="SW"
                    if grava < 15:
                        b=("ARENA BIEN GRADUADA")
                    else:
                        b=("ARENA BIEN GRADUADA CON GRAVA")
                else:
                    a="SP"
                    if grava < 15:
                        b=("ARENA MAL GRADUADA")
                    else:
                        b=("ARENA MAL GRADUADA CON GRAVA")
            else: # Porcentaje finos entre 5% y 12%
                if cu>=6 and (cc>=1 and cc<=3):
                    if ip<(0.73*(LL-20)) or ip<4:
                        a="SW-SM"
                        if grava < 15:
                            b=("ARENA BIEN GRADUADA CON LIMO")
                        else:
                            b=("ARENA BIEN GRADUADA CON LIMO Y GRAVA")
                    elif ip>(0.73*(LL-20)) or ip>7:
                        a="SW-SC"
                        if grava< 15:
                            b=("ARENA BIEN GRADUADA CON ARCILLA")
                        else:
                            b=("ARENA BIEN GRADUADA CON ARCILLA Y GRAVA")
                else:
                    if ip<(0.73*(LL-20)) or ip<4:
                        a="SP-SM"
                        if grava< 15:
                            b=("ARENA MAL GRADUADA CON LIMO")
                        else:
                            b=("ARENA MAL GRADUADA CON LIMO Y GRAVA")
                    elif ip>(0.73*(LL-20)) or ip>7:
                        a="SP-SC"
                        if grava< 15:
                            b=("ARENA MAL GRADUADA CON ARCILLA")
                        else:
                            b=("ARENA MAL GRADUADA CON ARCILLA Y GRAVA")        
    
  else:
        if LL<50: #Limite liquido menor del 50%
            if ip>7 and ip>(0.73*(LL-20)): # indice de plasticidad mayor a 7
                a="CL"
                if (100-finos)<30: # excede No. 200 < 30%
                    if (100-finos)<15:
                        b=("ARCILLA LIGERA");
                    else:
                        if arena>=grava:
                            b=('ARCILLA LIGERA CON ARENA');
                        else:
                            b=('ARCILLA LIGERA CON GRAVA');
                else: # excede No. 200 > 30%
                    if arena>grava:
                        if grava < 15:
                            b=('ARCILLA LIGERA ARENOSA')
                        else:
                            b=('ARCILLA LIGERA ARENOSA CON GRAVA')    
                    else:
                        if grava < 15:
                            b=('ARCILLA LIGERA Y TIPO GRAVA')
                        else:
                            b=('ARCILLA LIGERA Y TIPO GRAVA CON ARENA')                   
            elif ip<4 or ip<(0.73*(LL-20)): # indice de plasticidad menor a 4
                a="ML"
                if (100-finos)<30:
                    if (100-finos)<15:
                        b=('LIMO')
                    else:
                        if arena>=grava:
                            b=('LIMO CON ARENA')
                        else:
                            b=('LIMO CON GRAVA')
                else:
                    if arena>=grava:
                        if grava<=15:
                            b=('LIMO ARENOSO')
                        elif grava>15:
                            b=('LIMO ARENOSO CON GRAVA')
                    else:
                        if arena<=15:
                            b=('LIMO Y TIPO GRAVA')
                        elif arena>15:
                            b=('LIMO Y TIPO GRAVA CON ARENA')
            else: # ip entre 4 y 5
                a='CL-ML'
                if (100-finos)<30:
                    if (100-finos)<15:
                        b=('ARCILLA LIMOSA')
                    else:
                        if arena>grava:
                            b=('ARCILLA LIMOSA CON ARENA')
                        else:
                            b=('ARCILLA LIMOSA CON GRAVA')
                else:
                    if arena > grava:
                        if grava<15:
                            b=('ARCILLA LIMO-ARENOSA ')
                        elif grava>=15:
                            b=('ARCILLA LIMO-ARENOSA CON GRAVA')
                    else:
                        if arena<15:
                            b=('ARCILLA LIMOSA Y TIPO GRAVA')
                        elif arena >=15:
                            b=('ARCILLA LIMOSA Y TIPO GRAVA CON ARENA')
        else:
            if ip>= (0.73*(LL-20)):
                a='CH'
                if (100-finos)<30:
                    if (100-finos)<15:
                        b=('ARCILLA DENSA')
                    else:
                        if arena>=grava:
                            b=('ARCILLA DENSA CON ARENA')
                        elif arena<grava:
                            b=('ARCILLA DENSA CON GRAVA')
                else:
                    if arena>=grava and grava<15:
                        b=('ARCILLA DENSA ARENOSA')
                    elif arena>=grava and grava>=15:
                        b=('ARCILLA DENSA ARENOSA CON GRAVA')
                    elif arena < grava and arena<15:
                        b=('ARCILLA DENSA Y TIPO GRAVA')
                    elif arena<grava and arena>=15:
                        b=('ARCILLA DENSA Y TIPO GRAVA CON ARENA')
            else:
                a='MH'
                if (100-finos)<30:
                    if (100-finos)<15:
                        b=('LIMO ELASTICO')
                    else:
                        if arena>=grava:
                            b=('LIMO ELÁSTICO CON ARENA')
                        elif arena<grava:
                            b=('LIMO ELÁSTICO CON GRAVA')
                else:
                    if arena>=grava and grava<15:
                        b=('LIMO ELÁSTICO ARENOSO')
                    elif arena>=grava and grava>=15:
                        b=('LIMO ELÁSTICO ARENOSO CON GRAVA')
                    elif arena < grava and arena<15:
                        b=('LIMO ELÁSTICO Y TIPO GRAVA')
                    elif arena<grava and arena>=15:
                        b='LIMO ELÁSTICO Y TIPO GRAVA ARENOSO'
  return b