#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 08:11:39 2020

@author: jeanwolf
"""
import xlrd
import pandas as pd
# Abrimos el fichero excel
document = xlrd.open_workbook("Form400_XLS_2019/1900000.xlsx")


# Leer las celdas del libro de nombres 
Sheet1 = document.sheet_by_index(0)
# contenido_celda = Sheet1.cell_value(x,x) (tratar de hacer un for)
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

# print(data)

dat001 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
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

# Leer las celdas del libro de nombres 
Sheet2 = document.sheet_by_index(0)
# contenido_celda = Sheet2.cell_value(x,x) (tratar de hacer un for)
t001 = Sheet2.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet2.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet2.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet2.cell_value(46,0) #Modalidad de contratación
t019 = Sheet2.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet2.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet2.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet2.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet2.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet2.cell_value(86,0) #Código >> que significa
t022 = Sheet2.cell_value(94,0) #Causal de la contratación
t008 = Sheet2.cell_value(108,0) #Gestión
t018 = Sheet2.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet2.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet2.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet2.cell_value(130,0) #Normativa utilizada
t010 = Sheet2.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet2.cell_value(136,0) #Entidad
t012 = Sheet2.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet2.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet2.cell_value(161,0) #Tipo de contratación
t015 = Sheet2.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet2.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet2.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet2.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet2.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet2.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet2.cell_value(182,0) #Moneda del contrato
t028 = Sheet2.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet2.cell_value(216,0) #Empresa
t030 = Sheet2.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet2.cell_value(225,0) #Nro de contrato
t032 = Sheet2.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet2.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet2.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet2.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet2.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet2.cell_value(279,0) #Partida presupuestaria
t038 = Sheet2.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet2.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet2.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet2.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet2.cell_value(287,0) #Unidad de medida_A
t043 = Sheet2.cell_value(303,0) #Unidad de medida_B
t044 = Sheet2.cell_value(295,0) #Precio unitario_A
t045 = Sheet2.cell_value(305,0) #Precio unitario_B
t046 = Sheet2.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet2.cell_value(326,0) #La cantidad es fija_A
t048 = Sheet2.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet2.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet2.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet2.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet2.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet2.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet2.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet2.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio



data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

# print(data)

dat002 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
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

# Leer las celdas del libro de nombres 
Sheet3 = document.sheet_by_index(0)
# contenido_celda = Sheet3.cell_value(x,x) (tratar de hacer un for)
t001 = Sheet3.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet3.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet3.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet3.cell_value(46,0) #Modalidad de contratación
t019 = Sheet3.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet3.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet3.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet3.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet3.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet3.cell_value(86,0) #Código >> que significa
t022 = Sheet3.cell_value(94,0) #Causal de la contratación
t008 = Sheet3.cell_value(108,0) #Gestión
t018 = Sheet3.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet3.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet3.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet3.cell_value(130,0) #Normativa utilizada
t010 = Sheet3.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet3.cell_value(136,0) #Entidad
t012 = Sheet3.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet3.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet3.cell_value(161,0) #Tipo de contratación
t015 = Sheet3.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet3.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet3.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet3.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet3.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet3.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet3.cell_value(182,0) #Moneda del contrato
t028 = Sheet3.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet3.cell_value(216,0) #Empresa
t030 = Sheet3.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet3.cell_value(225,0) #Nro de contrato
t032 = Sheet3.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet3.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet3.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet3.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet3.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet3.cell_value(279,0) #Partida presupuestaria
t038 = Sheet3.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet3.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet3.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet3.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet3.cell_value(287,0) #Unidad de medida_A
t043 = Sheet3.cell_value(303,0) #Unidad de medida_B
t044 = Sheet3.cell_value(295,0) #Precio unitario_A
t045 = Sheet3.cell_value(305,0) #Precio unitario_B
t046 = Sheet3.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet3.cell_value(326,0) #La cantidad es fija_A
t048 = Sheet3.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet3.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet3.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet3.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet3.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet3.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet3.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet3.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio



data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

# print(data)

dat003 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
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

# Leer las celdas del libro de nombres 
Sheet4 = document.sheet_by_index(0)
# contenido_celda = Sheet4.cell_value(x,x) (tratar de hacer un for)
t001 = Sheet4.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet4.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet4.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet4.cell_value(46,0) #Modalidad de contratación
t019 = Sheet4.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet4.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet4.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet4.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet4.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet4.cell_value(86,0) #Código >> que significa
t022 = Sheet4.cell_value(94,0) #Causal de la contratación
t008 = Sheet4.cell_value(108,0) #Gestión
t018 = Sheet4.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet4.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet4.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet4.cell_value(130,0) #Normativa utilizada
t010 = Sheet4.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet4.cell_value(136,0) #Entidad
t012 = Sheet4.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet4.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet4.cell_value(161,0) #Tipo de contratación
t015 = Sheet4.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet4.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet4.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet4.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet4.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet4.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet4.cell_value(182,0) #Moneda del contrato
t028 = Sheet4.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet4.cell_value(216,0) #Empresa
t030 = Sheet4.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet4.cell_value(225,0) #Nro de contrato
t032 = Sheet4.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet4.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet4.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet4.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet4.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet4.cell_value(279,0) #Partida presupuestaria
t038 = Sheet4.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet4.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet4.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet4.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet4.cell_value(287,0) #Unidad de medida_A
t043 = Sheet4.cell_value(303,0) #Unidad de medida_B
t044 = Sheet4.cell_value(295,0) #Precio unitario_A
t045 = Sheet4.cell_value(305,0) #Precio unitario_B
t046 = Sheet4.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet4.cell_value(326,0) #La cantidad es fija_A
t048 = Sheet4.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet4.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet4.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet4.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet4.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet4.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet4.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet4.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio



data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

# print(data)

dat004 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
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

# Leer las celdas del libro de nombres 
Sheet5 = document.sheet_by_index(0)
# contenido_celda = Sheet5.cell_value(x,x) (tratar de hacer un for)
t001 = Sheet5.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet5.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet5.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet5.cell_value(46,0) #Modalidad de contratación
t019 = Sheet5.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet5.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet5.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet5.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet5.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet5.cell_value(86,0) #Código >> que significa
t022 = Sheet5.cell_value(94,0) #Causal de la contratación
t008 = Sheet5.cell_value(108,0) #Gestión
t018 = Sheet5.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet5.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet5.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet5.cell_value(130,0) #Normativa utilizada
t010 = Sheet5.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet5.cell_value(136,0) #Entidad
t012 = Sheet5.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet5.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet5.cell_value(161,0) #Tipo de contratación
t015 = Sheet5.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet5.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet5.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet5.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet5.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet5.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet5.cell_value(182,0) #Moneda del contrato
t028 = Sheet5.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet5.cell_value(216,0) #Empresa
t030 = Sheet5.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet5.cell_value(225,0) #Nro de contrato
t032 = Sheet5.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet5.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet5.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet5.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet5.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet5.cell_value(279,0) #Partida presupuestaria
t038 = Sheet5.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet5.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet5.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet5.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet5.cell_value(287,0) #Unidad de medida_A
t043 = Sheet5.cell_value(303,0) #Unidad de medida_B
t044 = Sheet5.cell_value(295,0) #Precio unitario_A
t045 = Sheet5.cell_value(305,0) #Precio unitario_B
t046 = Sheet5.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet5.cell_value(326,0) #La cantidad es fija_A
t048 = Sheet5.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet5.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet5.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet5.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet5.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet5.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet5.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet5.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio



data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

# print(data)

dat005 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
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


# Leer las celdas del libro de nombres 
Sheet6 = document.sheet_by_index(0)
# contenido_celda = Sheet6.cell_value(x,x) (tratar de hacer un for)
t001 = Sheet6.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet6.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet6.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet6.cell_value(46,0) #Modalidad de contratación
t019 = Sheet6.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet6.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet6.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet6.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet6.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet6.cell_value(86,0) #Código >> que significa
t022 = Sheet6.cell_value(94,0) #Causal de la contratación
t008 = Sheet6.cell_value(108,0) #Gestión
t018 = Sheet6.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet6.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet6.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet6.cell_value(130,0) #Normativa utilizada
t010 = Sheet6.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet6.cell_value(136,0) #Entidad
t012 = Sheet6.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet6.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet6.cell_value(161,0) #Tipo de contratación
t015 = Sheet6.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet6.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet6.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet6.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet6.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet6.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet6.cell_value(182,0) #Moneda del contrato
t028 = Sheet6.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet6.cell_value(216,0) #Empresa
t030 = Sheet6.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet6.cell_value(225,0) #Nro de contrato
t032 = Sheet6.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet6.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet6.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet6.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet6.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet6.cell_value(279,0) #Partida presupuestaria
t038 = Sheet6.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet6.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet6.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet6.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet6.cell_value(287,0) #Unidad de medida_A
t043 = Sheet6.cell_value(303,0) #Unidad de medida_B
t044 = Sheet6.cell_value(295,0) #Precio unitario_A
t045 = Sheet6.cell_value(305,0) #Precio unitario_B
t046 = Sheet6.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet6.cell_value(326,0) #La cantidad es fija_A
t048 = Sheet6.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet6.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet6.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet6.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet6.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet6.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet6.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet6.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio



data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

# print(data)

dat006 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
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




