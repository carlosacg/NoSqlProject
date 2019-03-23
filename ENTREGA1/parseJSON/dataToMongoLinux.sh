##ESTE COMANDO COPIARA EL ARCHIVO JSON EN NUESTRO CONTENEDOR scopus-cancer
docker cp ./books.json scopus-books:/books.json

##IMPORTAMOS LOS DATOS A NUESTRA BASE DE DATOS scopus EN LA COLECCION books
docker exec scopus-books mongoimport -d scopus -c books --file ./books.json --jsonArray

docker exec -it scopus-books mongo
