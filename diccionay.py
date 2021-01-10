product = {

"name" : "book",
"stock" : 3,
"price" : 4.99

}   

person = {

    "fName" : "King",
    "lName" : "Haw"
}

products = [

    { "name" : "book" },
    { "name" : "pencil" },
    { "name" : "eraser" }

]

#---------------------------------------------------------------
#---------------------------------------------------------------


print( product.keys() )
# crea array solo con los indices | keys

print( product.items() )
# crea un array con todo lo incluido en el dicc

print( product.get( "name" ) )
print( person.get( "fName" ) )
print( products[1].get( "name" ) )
# muestra el elemento por indice