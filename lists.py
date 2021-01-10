arrayColors = [ "red", "green", "blue", "red" ]
arrayNumbers = [ 4,2,3,1,5 ]

#-------------------------------------------------------------------
#-------------------------------------------------------------------

print( list( range( 0, 11 ) ) )
# crea un array del 0 al 10

# print( dir( arrayColors ) )
# muestra los metodos asociadas al tipo de dato

print( len( arrayColors ) )
# cantidad de elementos dentro del array

print( "blue" in arrayColors )
# devulve un booleano True en caso de que encuentre lo señalado dentro del array

arrayColors.append( "black" )
print( arrayColors )
# agrega un nuevo elemento al array


arrayColors.extend( [ "yellow", "white" ] )
arrayColors.extend( ( "brown", "grey" ) )
print( arrayColors )
# agrega mas de un elemento al array debe ser un arry o una tuple

arrayColors.insert( 2, "pink" )
arrayColors.insert( len(arrayColors), "orange" )
print( arrayColors )
# agrega un nuevo elemento al array en la posicion que se le indique

arrayColors.pop( 3 )
print( arrayColors )
# elimina por defecto el ultimo elemento pero se le puede indicar la posicion que se desa eliminar

arrayColors.remove( "white" )
print( arrayColors )
# elimina un elemento especifico del array

arrayColors.sort()
arrayNumbers.sort()
print( arrayColors )
print( arrayNumbers )
# ordena los elementos de forma alfabetica o de menor a mayor

arrayColors.sort( reverse = True )
arrayNumbers.sort( reverse = True )
print( arrayColors )
print( arrayNumbers )
# al reves

print( arrayColors.index( "orange" ) )
# devulve el indice del elemento indicado

print( arrayColors.count( "red" ) )
# cuenta la cantidad de elementos indicado dentro del array

arrayColors.clear()
print( arrayColors )
# vacia el array

