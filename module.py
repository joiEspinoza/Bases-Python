import datetime
import customeModule
from colorama import Fore, Back, Style, init
init( convert = True )
#conf necesaria para que funcione colorama en windows

#------------------------------------------------------
#------------------------------------------------------


print( datetime.date.today() )
# devuelve fecha actual

print( datetime.timedelta( minutes = 70 ) )
# transforma minutos en horas

print( customeModule.add( 4,5 ) )
print( customeModule.rest( 4,5 ) )
# ejecucion de funciones dentro del CM

print(Back.GREEN + 'and with a green background')
# aplicacion de colorama