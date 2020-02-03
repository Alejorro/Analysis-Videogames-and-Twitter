
# Analysis Videogames and Twitter


_En este proyecto se estudia el nivel de interacción social que las plataformas actuales de videojuegos han obtenido en los últimos 7 días_


_Adicionalmente se ha elaborado un programa escrito en Python para acceder a dicho estudio desde una perspectiva más interactiva_


## Comienzo 🚀


_El análisis pormenorizado de la información se sitúa en el archivo 'InformePrincipal.ipynb'_


_El programa principal para acceder a la información más detalladamente se sitúa en el archivo 'main.py'. Este programa utiliza un dataset limpiado y cacheado a posteriori del tratamiento con la API de Twitter._


_No se recomienda el uso del programa 'main_slower.py', debido a que para su utilización se necesita autentificación personal para la API de Twitter y, como su propio nombre indica, la obtención de todos los resultados se demorará cerca de dos horas._


_El resto de carpetas siguen la denominación estándar para el tipo de datos que poseen,y no requieren aclaraciones adicionales._


## Uso de 'main.py' 🔧



* **Inicio:**

_Ejecución en Bash: 'path/python3 main.py args'_



* **Parámetros opcionales de selección (se pueden combinar entre sí):**

-Nombre + 'Nombre' --> Devuelve los resultados para el nombre seleccionado (Ej. python3 main.py -Nombre 'Minecraft')

-Empresa + 'Empresa' --> Devuelve los resultados para la empresa seleccionada (Ej. python3 main.py -Empresa 'Microsoft')

-Genero + 'Género' --> Devuelve los resultados para el género seleccionado (Ej. python3 main.py -Genero 'Disparos')




* **Parámetros opcionales de ejecución:**

-Mejores --> Devuelve las máximas interacciones sociales en Twitter a elegir entre Nombre (de videojuegos), Empresa y Genero (Ej. python3 main.py -Mejores 'Empresa')





* **Parámetros opcionales de control:**

-Tamaño --> Regula el número de filas a mostrar en cualquiera de los parámetros mencionados anteriormente (Ej. python3 main.py -Genero 'Disparos' -Tamaño 5)

-Pdf --> Si se asocia este parámetro a una query, devuelve dicha query en formato PDF dentro de la carpeta 'Outputs (Ej. python3 main.py -Genero 'Disparos' -Tamaño 5 -Pdf)




## Construido con 🛠️

* [Jupyter Notebook](https://jupyter.org/) - Herramienta principal
* [Pandas](https://pandas.pydata.org/) - Manipulación de Dataframes
* [API de Twitter](https://developer.twitter.com/) - Información adicional


## Fuentes originales ✒️

* **Gregory Smith** - *Dataset de ventas de videojuegos* - (https://www.kaggle.com/gregorut/videogamesales)