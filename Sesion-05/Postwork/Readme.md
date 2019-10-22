 `Fundamentos de Python para Data Analysis`> `[Sesión 05]`  

## Postwork

### OBJETIVO 
 - Realizar limpieza, normalización e integración de datos en el proyecto personal. 

#### DESARROLLO
**Acerca de la limpieza, normalización e integración de datos.**  

En esta sesión vimos acerca de cómo podemos limpiar los datos, normalizarlos, e integrar datos de diferentes dataframes en uno solo. Para ello, en tu proyecto ten en mente las siguientes acciones, siempre pensando en la estructura de tu proyecto:  

**Tips:**

Los datos limpios y descriptivos siempre serán mucho mejor para el resultado que cualquier algoritmo de IA; si tus datos están sucios, no importa que tengas el mejor poder de cómputo o los algoritmos más sofisticados, tus resultados serán mediocres. 
Recuerda: basura entra, basura sale.  

Cuando hagas Dataframes, procura hacer copias en cada paso, las cuales te permitan hacer un “rollback” en caso de que algo haya salido mal. Es terrible el tener que volver a empezar la limpieza de datos desde cero.  

Procura mappear datos en información que te haga sentido. Si la información que vas a utilizar puede representarse fácilmente con números, ¡adelante!  

No todos los datos deben normalizarse, por ejemplo: Si normalizas la latitud / longitud, se vuelven datos inutilizables. Si realmente tienes que normalizar algo así, puedes hacerlo en una Serie de PANDAS de copia, y luego unirlo con join a tu dataframe.  

Primero haz la integración de datos y después haz la limpieza. Si limpias tus datasets y luego los integras, es posible que te encuentres limpiando doble. Es mejor limpiar una sola vez al final de la integración. Sin embargo, esto no es una regla: Si tu consideras que es mejor limpiar primero, sigue tu instinto en ello.  

