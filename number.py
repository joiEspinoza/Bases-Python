
num1 = 10   #int
num2 = 10.6 #float

#---------------------------------------------------------------------
#---------------------------------------------------------------------

print( type( num1 ) )
print( type( num2 ) )
# indica el tipo de la variable


numUsu1 = input( "ingrese primer numero a sumar: " )
numUsu2 = input( "ingrese segundo numero a sumar: " )

def suma( num1,num2 ):

    if num1.isnumeric() == False or num2.isnumeric() == False:

        return "Ambos datos deben ser un número"

    return f"Resultado: { int( num1 ) + int( num2 ) }"

print( suma( numUsu1,numUsu2 ) )

#-----------------------------------------------------------------------
