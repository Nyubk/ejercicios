
* **Eliminar columnas a partir del nombre**

test.drop(columns={'Unnamed: 3','Unnamed: 4'}, axis=1)

Cambiar una sola columna con .rename()

<df = df.rename(columns={'columna_vieja': 'columna_nueva'})>

***#Esto es útil si solo quieres cambiar una o algunas columnas sin afectar las demás.***

Cambiar todos los nombres de columna

df.columns = ['nuevo_nombre1', 'nuevo_nombre2', 'nuevo_nombre3']

CONOCER NOMBRE EXACTO DE LAS COLUMNAS
print(test.columns.tolist())

COPIAR EL VALOR DEL CAMPO SUPERIOR AL LOS CAMPOS NaN

df = df.apply(lambda col: col.fillna(col.name), axis=0)

CAMBIAR NOMBRE DE COLUMNA

