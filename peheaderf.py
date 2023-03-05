#Referencia> documentacion y presentacion en clase
import pefile
executable = input('Ingrese ejecutable: ')
pe = pefile.PE(executable)

#Obteniendo dlls y llamadas a APIS
for entry in pe.DIRECTORY_ENTRY_IMPORT:
    print('-------------------')
    print('DLL INFO: \n')
    print (entry.dll)
    
    print('APIS')
    for function in entry.imports:
        print ('\t', function.name)
    print('-------------------')

#Obteniendo secciones de PE HEader.

for section in pe.sections:
  print(section.Name, hex(section.VirtualAddress),
    hex(section.Misc_VirtualSize), section.SizeOfRawData )
