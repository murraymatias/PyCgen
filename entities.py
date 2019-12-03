from enum import Enum

class TipoDeCampo(Enum):
    INT = 0
    FLOAT = 1
    STRING = 2
    FKEY = 3


class Campo():
    def __init__(self,tipo=TipoDeCampo.INT,nombre=''):
        self.nombre_min = nombre.lower()
        self.nombre_may = nombre.lower().capitalize()
        self.tipo = tipo


class Estructura():
    def __init__(self,nombre='',campos=[]):
        self.nombre_min = nombre.lower()
        self.nombre_may = nombre.lower().capitalize()
        self.campos = campos
    
    def _generar_includes(self):
        return '''#include <stdio.h>
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

        '''.format(min=self.nombre_min,may=self.nombre_may)

    def _generar_int(self,campo):
        return '''int {structMin}_set{campoMay}Str({structMay}* this,char* {campoMin}Str)
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

        '''.format(campoMin=campo.nombre_min,campoMay=campo.nombre_may,structMin=self.nombre_min,structMay=self.nombre_may)

    def _generar_float(self,campo):
        return '''int {structMin}_set{campoMay}Str({structMay}* this,char* {campoMin}Str)
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

        '''.format(campoMin=campo.nombre_min,campoMay=campo.nombre_may,structMin=self.nombre_min,structMay=self.nombre_may)
    
    def _generar_string(self,campo):
        return '''int {strucMin}_set{campoMay}({structMay}* this,char* {campoMin})
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

        '''.format(campoMin=campo.nombre_min,campoMay=campo.nombre_may,strucMin=self.nombre_min,structMay=self.nombre_may)

    def _generar_condicion(self,campo):
        if campo.tipo == TipoDeCampo.INT or campo.tipo == TipoDeCampo.FLOAT or campo.tipo == TipoDeCampo.FKEY:
            return '||{structMin}_set{campoMayus}Str(aux,{campoMin}Str)'.format(structMin=self.nombre_min,campoMayus=campo.nombre_may,campoMin=campo.nombre_min)
        elif campo.tipo == TipoDeCampo.STRING:
            return '||{structMin}_set{campoMayus}(aux,{campoMin}Str)'.format(structMin=self.nombre_min,campoMayus=campo.nombre_may,campoMin=campo.nombre_min)

    def _generar_parametros(self,campo):
        return ',char* {campoMin}Str'.format(campoMin=campo.nombre_min)

    def _generar_cuerpo(self):
        condicion = ''
        parametros = ''
        cuerpo = ''
        for campo in self.campos:

            condicion += self._generar_condicion(campo)
            parametros += self._generar_parametros(campo)

            if campo.tipo == TipoDeCampo.INT or campo.tipo== TipoDeCampo.FKEY:
                cuerpo += self._generar_int(campo)

            elif campo.tipo == TipoDeCampo.FLOAT:
                cuerpo += self._generar_float(campo)
            
            elif campo.tipo == TipoDeCampo.STRING:
                cuerpo += self._generar_string(campo)

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

        '''.format(structMin=self.nombre,structMay=self.nombre_may,head=parametros,condition=condicion)

        return cuerpo + newParam