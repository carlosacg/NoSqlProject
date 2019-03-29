import json
import os

def separate_semicolon(cadena): #SEPARA UNA CADENA POR PUNTO Y COMAS
    x = 0
    separador = 0
    lista=[]
    while x<len(cadena):
        cadena = cadena.replace(".","_")
        cadena = cadena.replace(" ","_")
        if cadena[x]==';': 
            if cadena[separador:separador+1] != " ": 
                lista.append(cadena[separador:x])
                separador=x+1
            else: 
                lista.append(cadena[separador+1:x])
                separador=x+1   
        if x == int(len(cadena))-1:
            if(cadena[separador:x+1]!=""):
                lista.append(cadena[separador:x+1])
        x+=1
    return lista

def separate_point(cadena):  #SEPARA UNA CADENA POR COMAS
    x = 0
    separador = 0
    lista=[]
    while x<len(cadena):
        cadena = cadena.replace(".","_")
        cadena = cadena.replace(" ","_")
        if cadena[x]==',':
            if cadena[separador:separador+1] != " ":
                lista.append(cadena[separador:x])
                separador=x+1
            else: 
                lista.append(cadena[separador+1:x])
                separador=x+1   
        if x == int(len(cadena))-1:
            if(cadena[separador:x+1]!=""):
                lista.append(cadena[separador:x+1])
        x+=1
    return lista

def with_out_utf(cadena): #QUITA CARACTERES NO ADMITIDOS POR EL TURTLE VALIDATOR
    cadena = cadena.replace("'","_")
    cadena = cadena.replace("~","_")
    cadena = cadena.replace("#","_")
    cadena = cadena.replace("?","_")
    cadena = cadena.replace("¿","_")
    cadena = cadena.replace("\"","_")
    cadena = cadena.replace("+","_")
    cadena = cadena.replace("\\","-")
    cadena = cadena.replace("(","-")
    cadena = cadena.replace(")","-")
    cadena = cadena.replace("<","-")
    cadena = cadena.replace(">","-")
    cadena = cadena.replace("%","-")
    cadena = cadena.replace(",","-")
    cadena = cadena.replace("[","-")
    cadena = cadena.replace("]","-")
    cadena = cadena.replace("{","-")
    cadena = cadena.replace("}","-")
    cadena = cadena.replace("!","_")
    cadena = cadena.replace("·","_")
    cadena = cadena.replace("$","_")
    cadena = cadena.replace("&","_")
    cadena = cadena.replace("¬","_")
    cadena = cadena.replace("/","_")
    cadena = cadena.replace("=","_")
    cadena = cadena.replace("ç","_")
    cadena = cadena.replace("*","_")
    cadena = cadena.replace("º","_")
    cadena = cadena.replace("ª","_")
    cadena = cadena.replace("@","_")
    cadena = cadena.replace(";","_")
    cadena = cadena.replace("-","_")
    cadena = cadena.replace("|","_")
    cadena = cadena.replace(":","_")
    cadena = cadena[1:len(cadena)]
    return cadena

with open('books.json') as file: 
    libros = json.load(file)
    file = open("books.ttl", "w")
    file.write("@prefix rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>. "+ os.linesep)
    file.write("@prefix ex:<http://example.com/>. "+ os.linesep+"\n")
    for libro in libros:
        source=separate_point(libro['Source title'])
        autores_nombre=separate_point(libro['Authors'])
        autores_id=separate_semicolon(libro['Author(s) ID'])
        index_keys=separate_semicolon(libro['Index Keywords'])
        autores_keys=separate_semicolon(libro['Author Keywords'])
        referencias=separate_point(libro['References'])
        file.write("ex:Libro rdf:Abstract \""+with_out_utf(str(libro['Abstract'].encode("utf-8")))+"\"."+ os.linesep)
        file.write("ex:Libro rdf:DocumentType \""+libro['Document Type']+"\"."+ os.linesep)
        file.write("ex:Libro rdf:Title \""+with_out_utf(str(libro['Title'].encode("utf-8")))+"\"."+ os.linesep)
        file.write("ex:Libro rdf:Year \""+libro['Year']+"\"."+ os.linesep)
        if len(source) > 0 :
            file.write("ex:Libro rdf:SourceTitle _:b0."+ os.linesep)
        if len(autores_nombre) > 0:
            file.write("ex:Libro rdf:Authors _:b1."+ os.linesep)
        if len(autores_id) > 0:
            file.write("ex:Libro rdf:AuthorsID _:b2."+ os.linesep)
        if len(index_keys) > 0:
            file.write("ex:Libro rdf:IndexKeywords _:b3."+ os.linesep)
        if len(autores_keys) > 0:
            file.write("ex:Libro rdf:AuthorKeywords _:b4."+ os.linesep)
        if len(referencias) > 0:
            file.write("ex:Libro rdf:References _:b5.\n"+ os.linesep)
        x=0
        if len(source) > 0 :
            while x < len(source): 
                if x == 0:
                    file.write("_:b0    rdf:_"+str(x+1)+"  ex:"+with_out_utf(source[x])+";"+ os.linesep)
                else:
                    file.write("\trdf:_"+str(x+1)+"   ex:"+with_out_utf(source[x])+";"+ os.linesep)
                x=x+1
            file.write("\trdf:Type  ex:List.\n"+ os.linesep)  
        
        x=0
        if len(autores_nombre) > 0:
            while x < len(autores_nombre):
                if x == 0:
                    file.write("_:b1    rdf:_"+str(x+1)+"  ex:"+with_out_utf(str(autores_nombre[x].encode("utf-8")))+";"+ os.linesep)
                else:
                    file.write("\trdf:_"+str(x+1)+"   ex:"+with_out_utf(str(autores_nombre[x].encode("utf-8")))+";"+ os.linesep)
                x=x+1
            file.write("\trdf:Type  ex:List.\n"+ os.linesep)      

        x=0
        if len(autores_id) > 0:
            while x < len(autores_id):
                if x == 0:
                    file.write("_:b2    rdf:_"+str(x+1)+"  ex:"+with_out_utf(autores_id[x])+";"+ os.linesep)
                else:
                    file.write("\trdf:_"+str(x+1)+"   ex:"+with_out_utf(autores_id[x])+";"+ os.linesep)
                x=x+1
            file.write("\trdf:Type  ex:List.\n"+ os.linesep) 


        x=0
        if len(index_keys) > 0:
            while x < len(index_keys):
                if x == 0:
                    file.write("_:b3    rdf:_"+str(x+1)+"  ex:"+with_out_utf(index_keys[x])+";"+ os.linesep)
                else:
                    file.write("\trdf:_"+str(x+1)+"   ex:"+with_out_utf(index_keys[x])+";"+ os.linesep)
                x=x+1
            file.write("\trdf:Type  ex:List.\n"+ os.linesep) 

        x=0
        if len(autores_keys) > 0:
            while x < len(autores_keys):
                if x == 0:
                    file.write("_:b4    rdf:_"+str(x+1)+"  ex:"+with_out_utf(str(autores_keys[x].encode("utf-8")))+";"+ os.linesep)
                else:
                    file.write("\trdf:_"+str(x+1)+"   ex:"+with_out_utf(str(autores_keys[x].encode("utf-8")))+";"+ os.linesep)
                x=x+1
            file.write("\trdf:Type  ex:List.\n"+ os.linesep) 

        x=0
        if len(referencias) > 0:
            while x < len(referencias):
                if x == 0:
                    file.write("_:b5    rdf:_"+str(x+1)+"  ex:"+with_out_utf(str(referencias[x].encode("utf-8")))+";"+ os.linesep)
                else:
                    file.write("\trdf:_"+str(x+1)+"   ex:"+with_out_utf(str(referencias[x].encode("utf-8")))+";"+ os.linesep)
                x=x+1
            file.write("\trdf:Type  ex:List.\n"+ os.linesep) 
    
    file.close()
    print('books.ttl generado correctamente')



         
