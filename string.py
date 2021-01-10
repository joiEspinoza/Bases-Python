myStr = "oahEllOwoRlD ererer hola hola"
nombre = "King"
array = [1,2,3,4,5,6]

#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------

print( "hola " + nombre )
print( f"hola { nombre }" ) # python 3.6 en adelante
print( "hola {0}".format( nombre ) )
# diferentes formas de concatenar

print( myStr.title() )
# transforma la primera letra de cada palabra a mayuscula

print( myStr.upper() )
# todo a mayuscula

print( myStr.lower() )
# todo a minuscula

print( myStr.swapcase() )
# lo que esta en minuscula pasa a mayuscula y lo que este en mayuscula pasa a minuscula

print( f"capitalize: { myStr.capitalize() }" )
# Transforma solo el primer cartacter a mayuscula

arrayStr = list( myStr )
# transforma la cadena en un array -> cadena.split("") JS

myStr2 = "-".join( arrayStr )
print( myStr2 )
# transforma array en cadena y lo une por lo q se indica

print( myStr.startswith( "ahE" ) )
# devuelve un booleano true si es que empieza con lo indicado

print( myStr.endswith( "RlD" ) )
# devuelve un booleano true si es que termina con lo indicado

print( myStr.find( "O" ) )
# inidca la primera posicion que encuentra

print( len( myStr ) )
print( len( array ) )
# cuenta la cantidad de caracteres y elementos

print( myStr.count( "o" ) )
# cuenta la cantida de veces que aparece lo indicado puede ser un caracter como una cadena

print( myStr.index( "o" ) )
# indica la posicion del primer caracter que coincida

print( myStr.isnumeric() )
# devuelve un booleano True si el dato es numerico

