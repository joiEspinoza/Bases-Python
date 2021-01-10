colorsSet = { "red", "green", "blue" }
#tipo set no tiene indice

#---------------------------------------------------------------
#---------------------------------------------------------------


print( type( colorsSet ) )
# muestra el tipo de elemento

print( "red" in colorsSet )
# verifica si existe en set

colorsSet.add( "black" )
print( colorsSet )
# agrega un elemento al inicio solo pasa con un set por que no tiene indice

colorsSet.remove( "red" )
print( colorsSet )
# remueve dato especifico


colorsSet.clear()
print( colorsSet )
# limpia el set