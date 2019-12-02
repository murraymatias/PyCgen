#Genera los includes, la inicializacion de id y set y get del campo id, devuelve un string
def init_punto_c(nombreStructura,listaCampos):
    nombreStructura = nombreStructura.lower()
    nombreStructuraMayus = nombreStructura.capitalize()
    campos = 'int id;'
    for i in range(len(listaCampos)):
        campo = listaCampos[i][1].lower()
        if(listaCampos[i][0] == 'str'):
            campos = campos + '''
        char {campo}[128];'''.format(campo=campo)
        else:
            campos = campos + '''
        {tipo} {campo};'''.format(tipo=listaCampos[i][0],campo=campo)

    string = '''#ifndef {may}_H_INCLUDED
#define {may}_H_INCLUDED
typedef struct
{{
    {campos}
}}{may};
void {min}_idInit(int id);
int {min}_idGenerator();

{may}* {min}_new();
int {min}_delete({may}* this);

int {min}_setIdStr({may}* this,char* idStr);
int {min}_setId({may}* this,int id);
int {min}_getId({may}* this,int* id);
int {min}_compareId(void* p{may}A,void* p{may}B);

'''.format(min=nombreStructura,may=nombreStructuraMayus,campos=campos)
    return string

def generador_int(nombreStructura,campo):
    nombreStructura = nombreStructura.lower()
    campo = campo.lower()
    nombreStructuraMayus = nombreStructura.capitalize()
    campoMayus = campo.capitalize()
    string = '''int {structMin}_set{campoMay}Str({structMay}* this,char* {campoMin}Str);
int {structMin}_set{campoMay}({structMay}* this,int {campoMin});
int {structMin}_get{campoMay}({structMay}* this,int* {campoMin});
int {structMin}_compare{campoMay}(void* p{structMay}A,void* p{structMay}B);

'''.format(campoMin=campo,campoMay=campoMayus,structMin=nombreStructura,structMay=nombreStructuraMayus)
    return string

def generador_float(nombreStructura,campo):
    nombreStructura = nombreStructura.lower()
    campo = campo.lower()
    nombreStructuraMayus = nombreStructura.capitalize()
    campoMayus = campo.capitalize()
    string = '''int {structMin}_set{campoMay}Str({structMay}* this,char* {campoMin}Str);
int {structMin}_set{campoMay}({structMay}* this,float {campoMin});
int {structMin}_get{campoMay}({structMay}* this,float* {campoMin});
int {structMin}_compare{campoMay}(void* p{structMay}A,void* p{structMay}B);

'''.format(campoMin=campo,campoMay=campoMayus,structMin=nombreStructura,structMay=nombreStructuraMayus)
    return string

def generador_string(nombreStructura,campo):
    nombreStructura = nombreStructura.lower()
    campo = campo.lower()
    nombreStructuraMayus = nombreStructura.capitalize()
    campoMayus = campo.capitalize()
    string = '''int {strucMin}_set{campoMay}({structMay}* this,char* {strucMin});
int {strucMin}_get{campoMay}({structMay}* this,char* {strucMin});

'''.format(campoMin=campo,campoMay=campoMayus,strucMin=nombreStructura,structMay=nombreStructuraMayus)
    return string

def generador_campos(nombreStructura,listaCampos):
    structMin = nombreStructura.lower()
    structMay = structMin.capitalize()
    cuerpo = ''
    newParamHead = 'char* idStr'
    for i in range(len(listaCampos)):
        if listaCampos[i][0] == 'int':
            cuerpo = cuerpo + generador_int(nombreStructura,listaCampos[i][1])
            campo = listaCampos[i][1].lower()
            newParamHead = newParamHead + ',char* {campoMin}Str'.format(campoMin=campo)
        if listaCampos[i][0] == 'float':
            cuerpo = cuerpo + generador_float(nombreStructura,listaCampos[i][1])
            campo = listaCampos[i][1].lower()
            newParamHead = newParamHead + ',char* {campoMin}Str'.format(campoMin=campo)
        if listaCampos[i][0] == 'str':
            cuerpo = cuerpo + generador_string(nombreStructura,listaCampos[i][1])
            campo = listaCampos[i][1].lower()
            newParamHead = newParamHead + ',char* {campoMin}Str'.format(campoMin=campo)
        if listaCampos[i][0] == 'fk':
            cuerpo = cuerpo + generador_int(nombreStructura,listaCampos[i][1])
            campo = listaCampos[i][1].lower()
            newParamHead = newParamHead + ',char* {campoMin}Str'.format(campoMin=campo)
     
    
    newParam = '''{structMay}* {structMin}_newParametros({head});

'''.format(structMin=structMin,structMay=structMay,head=newParamHead)
    cuerpo = cuerpo + newParam
    return cuerpo

estructura = 'employee'

listaCampos = [['str','nombre'],
               ['int','horasTrabajadas'],
               ['int','sueldo']]



f = open(estructura+'.h','w+')
f.write(init_punto_c(estructura,listaCampos))
f.write(generador_campos(estructura, listaCampos))
f.write('''
#endif''')
f.close()