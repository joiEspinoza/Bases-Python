
print( "hi by python" )

tuples = (1,2,3,4,5)
# array inmutable

array = [ 2,5,3,4,1 ]
# array normal

array.sort()
# metodo de array ordena de menor a mayor

user = {

    "name" : "king"
}
#objeto

print( tuples[2] )
print( array[2] )
print( user )


#-------------------------------------------------------------
# function example 

animal = "pez"

def cambioNombre( name ):

    if len( name ) > 3:
        name = "Loro"
    else:
        name = "Perro"

    return name

print( cambioNombre( animal ) )

#----------------------------------------------------------------



