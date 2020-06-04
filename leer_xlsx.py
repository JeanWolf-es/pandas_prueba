#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:05:25 2020

@author: jeanwolf

Para leer informacion de un archivo excel
con xlrd y pandas
"""
import xlrd
# file = "/home/jeanwolf/github/jeanwolf/pandas_prueba/data/planets.xlsx"
# openfile = xlrd.open_workbook(file)
# sheet = openfile.sheet_by_name("Hoja1")
# # print(file)
# # print("numero de filas", sheet.nrows)
# # print("numero de columnas", sheet.ncols)

# for i in range(sheet.nrows):
#     # print(sheet.cell_value(i,0), " ", sheet.cell_value(i,1))
        
# import pandas as pd
# xls = pd.ExcelFile("data/planets.xlsx")
# # print(xls.sheet_names)
# df = xls.parse("Hoja2")
# # print(df)


#trabanajando con xlrd
#Abrimos el fichero excel
document = xlrd.open_workbook("data/planets.xlsx")
 
#Podemos guardar cada una de las hojas por separado
Hoja1 = document.sheet_by_index(0)
Hoja2 = document.sheet_by_index(1)

#Leemos el numero de filas y columnas de la hoja de libros
filas_Hoja1 = Hoja1.nrows
columnas_Hoja1 = Hoja1.ncols
print("Hoja1 tiene " + str(filas_Hoja1) + " filas y " + str(columnas_Hoja1) + " columnas")
 
#Y lo mismo con la hoja de peliculas
filas_Hoja2 = Hoja2.nrows
columnas_Hoja2 = Hoja2.ncols
print("Hoja2 tiene " + str(filas_Hoja2) + " filas y " + str(columnas_Hoja2) + " columnas")
print("+++++++++++++++++++++++++++++")

#Guardamos la informacion de la celda (0,1) de la hoja de libros
#Los tipos de celda son: 0-Vacia, 1-Texto, 2-Numero, 3-Fecha, 4-Booleano, 5-Error
tipo_de_celda = Hoja1.cell_type(0,0)
print("Tipo de celda: " + str(tipo_de_celda))
 
contenido_celda = Hoja1.cell_value(1,0)
print("Contenido de la celda: \"" + str(contenido_celda) + "\"")



