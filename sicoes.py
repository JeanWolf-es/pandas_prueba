#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 08:11:39 2020

@author: jeanwolf
"""
import xlrd
import pandas as pd
# Abrimos el fichero excel
# Luego Leer las celdas del libro de nombres 
# contenido_celda = Sheet1.cell_value(x,x) (tratar de hacer un for)

document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-1005728-0-E F400.xlsx")


Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_A
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a001 = Sheet1

document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-1017497-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_A
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a002 = Sheet1

pd.concat([a001, a002]).to_csv("dat001.csv")

