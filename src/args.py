#Esta función proporciona soporte a los parámetros de la consola:

def parseator():

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("-Nombre", type=str,help="Muestra los resultados del nombre elegido")

    parser.add_argument("-Empresa", type=str,help="Muestra los resultados de la empresa elegida")

    parser.add_argument("-Genero", type=str,help="Muestra los resultados del género elegido")

    parser.add_argument("-Mejores", type=str,help="Muestra los mejores resultados")

    parser.add_argument("-Tamaño", type=int,help="Modula la cantidad de filas del dataset final")

    parser.add_argument("-Pdf",  action='store_true',help="Genera un PDF")

    args = parser.parse_args()

    return args