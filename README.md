# NoSqlProject 🚀

_El proyecto consiste en construir un grafo RFD con la bibliografía recolectada los libros de Scopus. El grafo debe almacenar la información básica del artículo y las referencias a los artículos que se citan en el._

## EXPLICACIÓN.📋 

1. Descargar Apache-Jena-Fuseki del siguiente link: 
**https://www-eu.apache.org/dist/jena/binaries/apache-jena-fuseki-3.10.0.zip**
2. Ejecute el servidor de fuseki.
3. Descomprima el archivo .zip descargado
4. Abra la carpeta de apache-jena-fuseki.
5. Ejecute el comando: **./fuseki-server --update --mem /dataset** si su sistema operativo pertenece a una distribución de Linux, si su sistema operativo es Windows ejecute el comando **fuseki-server  --update  --mem /dataset**
6. Abra en el navegador de preferencia la siguiente URL: http://localhost:3030/
7. Diríjase a manage datasets
8. Cargue el archivo de extension .ttl que contiene su base de datos  RDF en upload files: 
9. Compruebe que los datos se hayan cargado correctamente con unas consultas básicas (En este caso nuestra base de datos son libros de scopus).

## Diríjase a query
**Cuente la cantidad de libros:**

**Cuente cuantos autores diferentes hay en la base de datos: **




## CREAR 🚀
_Se insertara un contacto a la base de datos_


📋 Inicialmente contamos con los siguientes datos: 

**https://ibb.co/jRfwbm2**

```
En la captura se observa que hay 2 contactos registrados en la base de datos.
```

Posteriormente queremos insertar un nuevo contacto, por lo cual cambiamos la solicitud a tipo **POST** y escribimos el contacto en formato JSON. 

**https://ibb.co/vDNVg0c**

```
En la captura se observa una solicitud tipo POST que contendra en el body un JSON con el modelo que tiene un contacto.
```

Comprobamos que el usuario se haya creado exitosamente haciendo nuevamente una solicitud **GET**: 

**https://ibb.co/z4WYztx**

```
En la captura se observa que hay 3 contactos los 2 primeros y el que acabamos de insertar por medio de la solicitud POST
```

