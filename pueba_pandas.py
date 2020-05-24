#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 12:17:22 2020

@author: jeanwolf

Lineas para probar funciones y otros con Pandas

primeras lineas con pandas
https://primero10.blogspot.com/2020/05/trabajo-con-planes-de-seaborn.html
"""
import pandas as pd
import seaborn as sb
import os
    

# Primero importamos el dataset planets de seaborn

planets = sb.load_dataset('planets')
planets.head()

# crear carpeta donde se alojan los CSV

os.mkdir('data')

planets.to_csv("data/planets.csv")

# Crear la variable in_2008 que filtra un dato especifico de una columna. en este caso año 2008 de la columna year year
in_2008 = planets['year'] == 2008
in_2008.head()

# Un filtro en la comuna masa menor a 4
masa = planets[planets["mass"] < 4]
print (masa)

# Para crear un filtro por periodio orbital que sea mayor a 0, luego grabar en CSV
periodo = planets[planets["orbital_period"] > 0]
periodo.to_csv("data/periodo.csv")

# Para filtrar por valores nulos en el campo mass, y luego usar isnull que extrae datos nulos. Luego grabar en CSV
planets_null = planets[planets.mass.isnull()]
p = planets_null.head()
p.to_csv("data/mas_nulos.csv")

# Filtrar nulos en la columna orbital_period y grabar en un csv
planets_null = planets[planets.orbital_period.isnull()]
q = planets_null.head()
q.to_csv("data/orbital_period_nulos.csv") 

# Filtrar por valores nulos en el campo mass usar notnull para excluir los datos nulos. OJO CON ESTE MÉTODO SOLO SE VISUALIZAN 5 DATOS
planets_not_null = planets[planets.mass.notnull()]
p = planets_not_null.head()
p.to_csv("data/masa_sin_nulos.csv")

# Filtrar por dato del campo. ejemplo filtrar exoplanetas descubiertos entre 2008 y 2009. y grabar en un csv
planets_in_years = planets[planets.year.isin([2008, 2009])]
planets_in_years.head().to_csv("data/2008-2009.csv")

