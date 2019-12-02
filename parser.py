def generate_includes(*args):
    header = '''#include <stdio.h>
#include <stdlib.h>
#include "LinkedList.h"
'''
    for arg in args:
        arg = arg.lower()
        arg = arg.capitalize()
        header += '''#include "{structure}.h"
'''.format(structure=arg)

    return header

def generate_text_parser(struct,fieldsList):
    struct = struct.lower()
    structCap = struct.capitalize()
    
    string = '''/** \\brief Parsea los datos de los {minus} desde el archivo data.csv (modo texto).
 *
 * \param path char*
 * \param this LinkedList*
 * \\return int
 *
 */
int parser_{mayus}FromText(FILE* pFile , LinkedList* this)
{{
    int ret= 0;
    {mayus} *pElement;
    char bufferId[4096];
    '''.format(minus=struct,mayus=structCap)
    for i in range(len(fieldsList)):
        field = fieldsList[i][1].lower()
        field = field.capitalize()
        string += '''char buffer{name}[4096];
        '''.format(name=field)
    string += '''
    if(pFile!=NULL && this!=NULL)
    {
        fscanf(pFile,"[^\\n]\\n");
        while(!feof(pFile))
        {
            fscanf(pFile,"'''
    for i in range(len(fieldsList)):
        string += "%[^,],"
    
    string += '%[^\\n]\\n",  bufferId'

    for i in range(len(fieldsList)):
        field = fieldsList[i][1].lower()
        field = field.capitalize()
        string += ',buffer{name}'.format(name=field)
    
    string += ''');
    
    pElement = {struct}_newParametros(bufferId'''.format(struct=struct)

    for i in range(len(fieldsList)):
        field = fieldsList[i][1].lower()
        field = field.capitalize()
        string += ''',buffer{name}'''.format(name=field)
    
    string += ''');

            if(pElement != NULL)
            {
                if(!ll_add(this,pElement))
                {
                    ret++;
                }
            }
        }
    }
    return ret;
}

'''
    return string

def generate_text_parser_prototype(struct):
    struct = struct.lower()
    structCap = struct.capitalize()
    string = 'int parser_{struct}FromText(FILE* pFile , LinkedList* this);'.format(struct=structCap)
    return string


estructura = 'employee'

listaCampos = [['str','nombre'],
               ['int','horasTrabajadas'],
               ['int','sueldo']]

f = open('parser.c','w+')
f.write(generate_includes(estructura))
f.write(generate_text_parser(estructura, listaCampos))
f.close()

f = open('parser.h','w+')
f.write(generate_text_parser_prototype(estructura))
f.close()