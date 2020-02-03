
def limpiador(df):

#Importación de bibliotecas y módulos

    import pandas as pd
    from functions import changeToBusiness

#Limpieza de valores nulos:

    df2 = df.dropna().fillna(0)

#Renombrado de columnas:

    df2.rename(columns={'Rank':'Ranking','Name':'Nombre', 'Platform':'Empresa', 'Year':'Fecha','Genre':'Genero', 'Publisher':'Editor', 'NA_Sales':'NA_Ventas', 'EU_Sales':'EU_Ventas', 'JP_Sales':'JP_Ventas', 'Other_Sales':'Otras_Ventas','Global_Sales':'Ventas_Globales'}, inplace=True)

    df2 = df2[['Ranking', 'Nombre', 'Empresa', 'Fecha', 'Genero','Ventas_Globales']]

#Cambio de tipo de columnas problematicas:

    df2["Fecha"] = df2.Fecha.astype(int)

#Ordenación de Dataframe en función de columna "Fecha" en orden ascendente a partir del año 2008:

    df3 = df2.loc[df2['Fecha']>2007].sort_values(['Fecha','Ranking'], ascending=True).reset_index(drop=True)

#Agrupación de las consolas en función de su fabricante:

    df3.Empresa = df3["Empresa"].apply(changeToBusiness)

#Traducción de géneros al idioma español:

    df3.Genero = df3["Genero"].apply(local_translation)

#Se reduce la envergadura del dataframe para su correcto uso junto a la API de Twitter (Sólo permite 180 request cada 15 minutos en versión gratuita):

    df4 = df3.sort_values(by=['Empresa','Fecha','Ventas_Globales'],ascending=True).reset_index(drop=True)

    df5 = estructure_df(df4).reset_index(drop=True)

#Fin de la limpieza inicial

    return df5

 
