
def init(Nombre="",Empresa="",Genero="",size=0,best=False):


    #Módulos y librerías importadas

    import os
    import pandas as pd


    #Establecemos la ruta actual del archivo como principal

    current_dir = os.path.dirname(os.path.realpath(__file__)) 
    filename = os.path.join(current_dir, "Outputs/Twitts_tratados.csv")


    #Importamos el dataset

    df = pd.read_csv(filename, encoding = "ISO-8859-1")

    df2 = df

    try:


        if Nombre:

            result = df2.loc[df2['Nombre'] == f'{Nombre}'].iloc[0::,1::]

        elif Empresa:

            result = df2.loc[df2['Empresa'] == f'{Empresa}'].iloc[0::,1::]

        elif Genero:

            result = df2.loc[df2['Genero'] == f'{Genero}'].iloc[0::,1::]

        else:

            result = "El valor introducido no ha sido encontrado"


    except ValueError:

        raise ValueError("Valor Inválido")

    
    print(result)


print(init(Empresa="Gears of War 2"))

    
    


    