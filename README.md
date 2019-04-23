# NoSqlProject 🚀

_El proyecto consiste en construir un grafo RFD con la bibliografía recolectada los libros de Scopus. El grafo debe almacenar la información básica del artículo y las referencias a los artículos que se citan en el._

## INFORME
```
https://drive.google.com/open?id=1pFQ1JqKB4TO-1f-aUdGjoBYGAz3fuhYb
```
## VIDEO EN YOUTUBE.
```
https://youtu.be/W-g6oyjBkWk

```

## PRESENTACION.
```
https://drive.google.com/file/d/14fqhgbTSAIknmHQH-et-4ByKmbgXV25V/view?usp=sharing

```

## EXPLICACIÓN.📋 

1. Descargar Apache-Jena-Fuseki del siguiente link: 
**https://www-eu.apache.org/dist/jena/binaries/apache-jena-fuseki-3.10.0.zip**
2. Ejecute el servidor de fuseki.
3. Descomprima el archivo .zip descargado
4. Abra la carpeta de apache-jena-fuseki.
5. Ejecute el comando: **./fuseki-server --update --mem /dataset** si su sistema operativo pertenece a una distribución de Linux, si su sistema operativo es Windows ejecute el comando **fuseki-server  --update  --mem /dataset**
6. Abra en el navegador de preferencia la siguiente URL: http://localhost:3030/
7. Diríjase a manage datasets

![alt text](https://github.com/carlosacg/NoSqlProject/blob/master/Images/1.png)

8. Cargue el archivo de extension .ttl que contiene su base de datos  RDF en upload files: 
![alt text](https://github.com/carlosacg/NoSqlProject/blob/master/Images/2.png)

9. Compruebe que los datos se hayan cargado correctamente con unas consultas básicas (En este caso nuestra base de datos son libros de scopus).

## CONSULTAS 
_Diríjase a query (En donde se realizan las consultas)_


**Cuente la cantidad de libros:**

![alt text](https://github.com/carlosacg/NoSqlProject/blob/master/Images/3)

**Cuente cuantos autores diferentes hay en la base de datos:**


![alt text](https://github.com/carlosacg/NoSqlProject/blob/master/Images/4.png)

