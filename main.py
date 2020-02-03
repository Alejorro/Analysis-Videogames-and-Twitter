import os
import pandas as pd
from src.args import parseator
from src.gen_pdf import generate_pdf



# Configuración de Argparse:

args = parseator()

# Establecemos la ruta actual del archivo como principal:

current_dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_dir, "Outputs/Twitts_tratados.csv")

 # Importamos el dataset:

df = pd.read_csv(filename, encoding="ISO-8859-1")
df2 = df

#Arreglamos posibles problemas:

if not args.Tamaño:
    args.Tamaño = 3

# Búsqueda variables en Dataset:

if __name__ == "__main__":
    if args.Nombre and not args.Empresa and not args.Genero:
        result = df2.loc[df2['Nombre'] ==f'{args.Nombre}'].iloc[0::, 1::].head(args.Tamaño)

    elif args.Empresa and not args.Nombre and not args.Genero:
        result = df2.loc[df2['Empresa'] ==f'{args.Empresa}'].iloc[0::, 1::].head(args.Tamaño)

    elif args.Genero and not args.Nombre and not args.Empresa:
        result = df2.loc[df2['Genero'] ==f'{args.Genero}'].iloc[0::, 1::].head(args.Tamaño)

    elif args.Nombre and args.Empresa:
        result = df2.loc[df2['Nombre'] == f'{args.Nombre}'].loc[df2['Empresa']== f'{args.Empresa}'].iloc[0::, 1::].head(args.Tamaño).reset_index()

    elif args.Nombre and args.Genero:
        result = "Esta relación no tiene sentido"

    elif args.Empresa and args.Genero:
        result = df2.loc[df2['Empresa'] == f'{args.Empresa}'].loc[df2['Genero']== f'{args.Genero}'].iloc[0::, 1::].head(args.Tamaño).reset_index()


#Tops de valores:
    
try:

    if args.Mejores == 'Nombre':

        df3 = df2.groupby(['Nombre']).sum().sort_values('Contador', ascending=False).reset_index()
        result = df3[['Nombre', 'Contador']].set_index('Nombre').head(args.Tamaño)

    elif args.Mejores == 'Genero':

        df3 = df2.groupby(['Genero']).sum().sort_values('Contador', ascending=False).reset_index()
        result = df3[['Genero', 'Contador']].set_index('Genero').head(args.Tamaño)

    elif args.Mejores =='Empresa':

        df3 = df2.groupby(['Empresa']).sum().sort_values('Contador', ascending=False).reset_index()
        result = df3[['Empresa', 'Contador']].set_index('Empresa').head(args.Tamaño)
        
except NameError:
    
    print("Problemas al introducir las variables")


#Generación de PDF si procede:
try:
    if args.Pdf:
        result.to_html("Outputs/queryToPDF.html",index=False)
        generate_pdf()

        

except FileNotFoundError:
    raise FileNotFoundError("Fallo al crear el archivo CSV")

except NameError:
    raise NameError("No se puede crear PDF sin Query")



# Impresión de resultados finales (STDOUT):

try:

    if result.empty != True:
        print(result)
    else:
        print("Valores no encontrados")

except NameError:

    raise NameError("Introduce alguna variable")
