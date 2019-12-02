#Genera los includes, la inicializacion de id y set y get del campo id, devuelve un string
def init_punto_c(nombreStructura):
    nombreStructura = nombreStructura.lower()
    nombreStructuraMayus = nombreStructura.capitalize()
    string = '''#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "utn.h"
#include "{may}.h"

static int lastId=0;

void {min}_idInit(int id)
{{
    lastId=id+1;
}}

int {min}_idGenerator()
{{
    return lastId++;
}}

int {min}_setIdStr({may}* this,char* idStr)
{{
    int ret=-1;
    int bufferId;
    if(this!=NULL && idStr!=NULL)
    {{
        if(utn_isValidInt(idStr))
        {{
            bufferId = atoi(idStr);
            if(!{min}_setId(this,bufferId))
            {{
                ret=0;
            }}
        }}
    }}
    return ret;
}}

int {min}_setId({may}* this,int id)
{{
    int ret=-1;
    if(this!=NULL && id>=0)
    {{
        this->id=id;
        ret=0;
    }}
    return ret;
}}

int {min}_getId({may}* this,int* id)
{{
    int ret=-1;
    if(this!=NULL&&id!=NULL)
    {{
        *id=this->id;
        ret=0;
    }}
    return ret;
}}

{may}* {min}_new()
{{
    return ({may}*)malloc(sizeof({may}));
}}

int {min}_delete({may}* this)
{{
    int ret=-1;
    if(this!=NULL)
    {{
        free(this);
        ret=0;
    }}
    return ret;
}}

int {min}_compareId(void* pElementA,void* pElementB)
{{
    int ret = 0;
    if((({may}*)pElementA)->id > (({may}*)pElementB)->id)
    {{
        ret = 1;
    }}
    if((({may}*)pElementA)->id < (({may}*)pElementB)->id)
    {{
        ret = -1;
    }}
    return ret;
}}

'''.format(min=nombreStructura,may=nombreStructuraMayus)
    return string

def generador_int(nombreStructura,campo):
    nombreStructura = nombreStructura.lower()
    campo = campo.lower()
    nombreStructuraMayus = nombreStructura.capitalize()
    campoMayus = campo.capitalize()
    string = '''int {structMin}_set{campoMay}Str({structMay}* this,char* {campoMin}Str)
{{
    int ret=-1;
    int buffer{campoMay};
    if(this!=NULL)
    {{
        if(utn_isValidInt({campoMin}Str))
        {{
            buffer{campoMay} = atoi({campoMin}Str);
            if(!{structMin}_set{campoMay}(this,buffer{campoMay}))
            {{
                ret=0;
            }}
        }}
    }}
    return ret;
}}

int {structMin}_set{campoMay}({structMay}* this,int {campoMin})
{{
    int ret=-1;
    if(this!=NULL && {campoMin}>=0)
    {{
        this->sueldo={campoMin};
        ret=0;
    }}
    return ret;
}}

int {structMin}_get{campoMay}({structMay}* this,int* {campoMin})
{{
    int ret=-1;
    if(this!=NULL && {campoMin}!=NULL)
    {{
        *{campoMin}=this->{campoMin};
        ret=0;
    }}
    return ret;
}}

int {structMin}_compare{campoMay}(void* pElementA,void* pElementB)
{{
    int ret = 0;
    if((({structMay}*)pElementA)->{campoMin} > (({structMay}*)pElementB)->{campoMin})
    {{
        ret = 1;
    }}
    if((({structMay}*)pElementA)->{campoMin} < (({structMay}*)pElementB)->{campoMin})
    {{
        ret = -1;
    }}
    return ret;
}}

'''.format(campoMin=campo,campoMay=campoMayus,structMin=nombreStructura,structMay=nombreStructuraMayus)
    return string

def generador_float(nombreStructura,campo):
    nombreStructura = nombreStructura.lower()
    campo = campo.lower()
    nombreStructuraMayus = nombreStructura.capitalize()
    campoMayus = campo.capitalize()
    string = '''int {structMin}_set{campoMay}Str({structMay}* this,char* {campoMin}Str)
{{
    int ret=-1;
    int buffer{campoMay};
    if(this!=NULL)
    {{
        if(utn_isValidFloat({campoMin}Str))
        {{
            buffer{campoMay} = atof({campoMin}Str);
            if(!{structMin}_set{campoMay}(this,buffer{campoMay}))
            {{
                ret=0;
            }}
        }}
    }}
    return ret;
}}

int {structMin}_set{campoMay}({structMay}* this,float {campoMin})
{{
    int ret=-1;
    if(this!=NULL && {campoMin}>=0)
    {{
        this->sueldo={campoMin};
        ret=0;
    }}
    return ret;
}}

int {structMin}_get{campoMay}({structMay}* this,float* {campoMin})
{{
    int ret=-1;
    if(this!=NULL && {campoMin}!=NULL)
    {{
        *{campoMin}=this->{campoMin};
        ret=0;
    }}
    return ret;
}}

int {structMin}_compare{campoMay}(void* pElementA,void* pElementB)
{{
    int ret = 0;
    if((({structMay}*)pElementA)->{campoMin} > (({structMay}*)pElementB)->{campoMin})
    {{
        ret = 1;
    }}
    if((({structMay}*)pElementA)->{campoMin} < (({structMay}*)pElementB)->{campoMin})
    {{
        ret = -1;
    }}
    return ret;
}}

'''.format(campoMin=campo,campoMay=campoMayus,structMin=nombreStructura,structMay=nombreStructuraMayus)
    return string

def generador_string(nombreStructura,campo):
    nombreStructura = nombreStructura.lower()
    campo = campo.lower()
    nombreStructuraMayus = nombreStructura.capitalize()
    campoMayus = campo.capitalize()
    string = '''int {strucMin}_set{campoMay}({structMay}* this,char* {campoMin})
{{
    int ret=-1;
    if(this != NULL && utn_isValidName({campoMin}))
    {{
        strncpy(this->{campoMin},{campoMin},sizeof(this->{campoMin}));
        ret=0;
    }}
    return ret;
}}

int {strucMin}_get{campoMay}({structMay}* this,char* {campoMin})
{{
    int ret=-1;
    if(this!=NULL && {campoMin}!=NULL)
    {{
        strncpy({campoMin},this->{campoMin},sizeof(this->{campoMin}));
        ret=0;
    }}
    return ret;
}}

int {strucMin}_compare{campoMay}(void* pElementA,void* pElementB)
{{
    int ret = 0;
    if(strcmp((({structMay}*)pElementA)->{campoMin},(({structMay}*)pElementB)->{campoMin})>0)
    {{
        ret = 1;
    }}
    if(strcmp((({structMay}*)pElementA)->{campoMin},(({structMay}*)pElementB)->{campoMin})<0)
    {{
        ret = -1;
    }}
    return ret;
}}

'''.format(campoMin=campo,campoMay=campoMayus,strucMin=nombreStructura,structMay=nombreStructuraMayus)
    return string

def generador_campos(nombreStructura,listaCampos):
    structMin = nombreStructura.lower()
    structMay = structMin.capitalize()
    cuerpo = ''
    newParamHead = 'char* idStr'
    newParamIf = '{structMin}_setIdStr(aux,idStr)'.format(structMin=structMin)
    for i in range(len(listaCampos)):
        if listaCampos[i][0] == 'int':
            cuerpo = cuerpo + generador_int(nombreStructura,listaCampos[i][1])
            campo = listaCampos[i][1].lower()
            campoMayus = campo.capitalize()
            newParamIf = newParamIf + '||{structMin}_set{campoMayus}Str(aux,{campoMin}Str)'.format(structMin=structMin,campoMayus=campoMayus,campoMin=campo)
            newParamHead = newParamHead + ',char* {campoMin}Str'.format(campoMin=campo)
        if listaCampos[i][0] == 'float':
            cuerpo = cuerpo + generador_float(nombreStructura,listaCampos[i][1])
            campo = listaCampos[i][1].lower()
            campoMayus = campo.capitalize()
            newParamIf = newParamIf + '||{structMin}_set{campoMayus}Str(aux,{campoMin}Str)'.format(structMin=structMin,campoMayus=campoMayus,campoMin=campo)
            newParamHead = newParamHead + ',char* {campoMin}Str'.format(campoMin=campo)
        if listaCampos[i][0] == 'str':
            cuerpo = cuerpo + generador_string(nombreStructura,listaCampos[i][1])
            campo = listaCampos[i][1].lower()
            campoMayus = campo.capitalize()
            newParamIf = newParamIf + '||{structMin}_set{campoMayus}(aux,{campoMin}Str)'.format(structMin=structMin,campoMayus=campoMayus,campoMin=campo)
            newParamHead = newParamHead + ',char* {campoMin}Str'.format(campoMin=campo)
        if listaCampos[i][0] == 'fk':
            cuerpo = cuerpo + generador_int(nombreStructura,listaCampos[i][1])
            campo = listaCampos[i][1].lower()
            campoMayus = campo.capitalize()
            newParamIf = newParamIf + '||{structMin}_set{campoMayus}Str(aux,{campoMin}Str)'.format(structMin=structMin,campoMayus=campoMayus,campoMin=campo)
            newParamHead = newParamHead + ',char* {campoMin}Str'.format(campoMin=campo)
     

    newParam = '''{structMay}* {structMin}_newParametros({head})
{{
    {structMay}* aux;
    aux={structMin}_new();
    if(aux!=NULL)
    {{
        if({condition})
        {{
            {structMin}_delete(aux);
            aux=NULL;
        }}
    }}
    return aux;
}}

'''.format(structMin=structMin,structMay=structMay,head=newParamHead,condition=newParamIf)
    cuerpo = cuerpo + newParam
    return cuerpo


estructura = 'employee'

listaCampos = [['str','nombre'],
               ['int','horasTrabajadas'],
               ['int','sueldo']]



f = open(estructura+'.c','w+')
f.write(init_punto_c(estructura))
f.write(generador_campos(estructura, listaCampos))
f.close()