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
        s_minus = self.nombre_min
        s_mayus = self.nombre_may

        r = (f"#include <stdio.h>\n"
            f"#include <stdlib.h>\n"
            f"#include <string.h>\n"
            f"#include \"utn.h\"\n"
            f"#include \"{s_mayus}.h\"\n\n"

            f"static int lastId=0;\n\n"

            f"void {s_minus}_idInit(int id)\n"
            f"{{\n"
            f"    lastId=id+1;\n"
            f"}}\n\n"

            f"int {s_minus}_idGenerator()\n"
            f"{{\n"
            f"    return lastId++;\n"
            f"}}\n\n"

            f"int {s_minus}_setIdStr({s_mayus}* this,char* idStr)\n"
            f"{{\n"
            f"    int ret=-1;\n"
            f"    int bufferId;\n"
            f"    if(this!=NULL && idStr!=NULL)\n"
            f"    {{\n"
            f"        if(utn_isValidInt(idStr))\n"
            f"        {{\n"
            f"            bufferId = atoi(idStr);\n"
            f"            if(!{s_minus}_setId(this,bufferId))\n"
            f"            {{\n"
            f"                ret=0;\n"
            f"            }}\n"
            f"        }}\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n"

            f"int {s_minus}_setId({s_mayus}* this,int id)\n"
            f"{{\n"
            f"    int ret=-1;\n"
            f"    if(this!=NULL && id>=0)\n"
            f"    {{\n"
            f"        this->id=id;\n"
            f"        ret=0;\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n"

            f"int {s_minus}_getId({s_mayus}* this,int* id)\n"
            f"{{\n"
            f"    int ret=-1;\n"
            f"    if(this!=NULL&&id!=NULL)\n"
            f"    {{\n"
            f"        *id=this->id;\n"
            f"        ret=0;\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n"

            f"{s_mayus}* {s_minus}_new()\n"
            f"{{\n"
            f"    return ({s_mayus}*)malloc(sizeof({s_mayus}));\n"
            f"}}\n\n"

            f"int {s_minus}_delete({s_mayus}* this)\n"
            f"{{\n"
            f"    int ret=-1;\n"
            f"    if(this!=NULL)\n"
            f"    {{\n"
            f"        free(this);\n"
            f"        ret=0;\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n"

            f"int {s_minus}_compareId(void* pElementA,void* pElementB)\n"
            f"{{\n"
            f"    int ret = 0;\n"
            f"    if((({s_mayus}*)pElementA)->id > (({s_mayus}*)pElementB)->id)\n"
            f"    {{\n"
            f"        ret = 1;\n"
            f"    }}\n"
            f"    if((({s_mayus}*)pElementA)->id < (({s_mayus}*)pElementB)->id)\n"
            f"    {{\n"
            f"        ret = -1;\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n")

        return r

    def _generar_int(self,campo):
        s_minus = self.nombre_min
        s_mayus = self.nombre_may
        c_minus = campo.nombre_min
        c_mayus = campo.nombre_may

        r = (f"int {s_minus}_set{c_mayus}Str({s_mayus}* this,char* {c_minus}Str)\n"
            f"{{\n"
            f"    int ret=-1;\n"
            f"    int buffer{c_mayus};\n"
            f"    if(this!=NULL)\n"
            f"        {{\n"
            f"            if(utn_isValidInt({c_minus}Str))\n"
            f"            {{\n"
            f"                buffer{c_mayus} = atoi({c_minus}Str);\n"
            f"                if(!{s_minus}_set{c_mayus}(this,buffer{c_mayus}))\n"
            f"                {{\n"
            f"                    ret=0;\n"
            f"                }}\n"
            f"            }}\n"
            f"        }}\n"
            f"    return ret;\n"
            f"}}\n\n"

            f"int {s_minus}_set{c_mayus}({s_mayus}* this,int {c_minus})\n"
            f"{{\n"
            f"    int ret=-1;\n"
            f"    if(this!=NULL && {c_minus}>=0)\n"
            f"    {{\n"
            f"        this->sueldo={c_minus};\n"
            f"        ret=0;\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n"

            f"int {s_minus}_get{c_mayus}({s_mayus}* this,int* {c_minus})\n"
            f"{{\n"
            f"    int ret=-1;\n"
            f"    if(this!=NULL && {c_minus}!=NULL)\n"
            f"    {{\n"
            f"        *{c_minus}=this->{c_minus};\n"
            f"        ret=0;\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n"

            f"int {s_minus}_compare{c_mayus}(void* pElementA,void* pElementB)\n"
            f"{{\n"
            f"    int ret = 0;\n"
            f"    if((({s_mayus}*)pElementA)->{c_minus} > (({s_mayus}*)pElementB)->{c_minus})\n"
            f"    {{\n"
            f"        ret = 1;\n"
            f"    }}\n"
            f"    if((({s_mayus}*)pElementA)->{c_minus} < (({s_mayus}*)pElementB)->{c_minus})\n"
            f"    {{\n"
            f"        ret = -1;\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n")

        return r

    def _generar_float(self,campo):
        s_minus = self.nombre_min
        s_mayus = self.nombre_may
        c_minus = campo.nombre_min
        c_mayus = campo.nombre_may

        r = (f"int {s_minus}_set{c_mayus}Str({s_mayus}* this,char* {c_minus}Str)\n"
            f"{{\n"
            f"    int ret=-1;\n"
            f"    int buffer{c_mayus};\n"
            f"    if(this!=NULL)\n"
            f"    {{\n"
            f"        if(utn_isValidFloat({c_minus}Str))\n"
            f"        {{\n"
            f"            buffer{c_mayus} = atof({c_minus}Str);\n"
            f"            if(!{s_minus}_set{c_mayus}(this,buffer{c_mayus}))\n"
            f"            {{\n"
            f"                ret=0;\n"
            f"            }}\n"
            f"        }}\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n"

            f"int {s_minus}_set{c_mayus}({s_mayus}* this,float {c_minus})\n"
            f"{{\n"
            f"    int ret=-1;\n"
            f"    if(this!=NULL && {c_minus}>=0)\n"
            f"    {{\n"
            f"        this->sueldo={c_minus};\n"
            f"        ret=0;\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n"

            f"int {s_minus}_get{c_mayus}({s_mayus}* this,float* {c_minus})\n"
            f"{{\n"
            f"    int ret=-1;\n"
            f"    if(this!=NULL && {c_minus}!=NULL)\n"
            f"    {{\n"
            f"        *{c_minus}=this->{c_minus};\n"
            f"        ret=0;\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n"

            f"int {s_minus}_compare{c_mayus}(void* pElementA,void* pElementB)\n"
            f"{{\n"
            f"    int ret = 0;\n"
            f"    if((({s_mayus}*)pElementA)->{c_minus} > (({s_mayus}*)pElementB)->{c_minus})\n"
            f"    {{\n"
            f"        ret = 1;\n"
            f"    }}\n"
            f"    if((({s_mayus}*)pElementA)->{c_minus} < (({s_mayus}*)pElementB)->{c_minus})\n"
            f"    {{\n"
            f"        ret = -1;\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n")

        return r
    
    def _generar_string(self,campo):
        s_minus = self.nombre_min
        s_mayus = self.nombre_may
        c_minus = campo.nombre_min
        c_mayus = campo.nombre_may

        r = (f"int {s_minus}_set{c_mayus}({s_mayus}* this,char* {c_minus})\n"
            f"{{\n"
            f"    int ret=-1;\n"
            f"    if(this != NULL && utn_isValidName({c_minus}))\n"
            f"    {{\n"
            f"        strncpy(this->{c_minus},{c_minus},sizeof(this->{c_minus}));\n"
            f"        ret=0;\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n"

            f"int {s_minus}_get{c_mayus}({s_mayus}* this,char* {c_minus})\n"
            f"{{\n"
            f"    int ret=-1;\n"
            f"    if(this!=NULL && {c_minus}!=NULL)\n"
            f"    {{\n"
            f"        strncpy({c_minus},this->{c_minus},sizeof(this->{c_minus}));\n"
            f"        ret=0;\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n"

            f"int {s_minus}_compare{c_mayus}(void* pElementA,void* pElementB)\n"
            f"{{\n"
            f"    int ret = 0;\n"
            f"    if(strcmp((({s_mayus}*)pElementA)->{c_minus},(({s_mayus}*)pElementB)->{c_minus})>0)\n"
            f"    {{\n"
            f"        ret = 1;\n"
            f"    }}\n"
            f"    if(strcmp((({s_mayus}*)pElementA)->{c_minus},(({s_mayus}*)pElementB)->{c_minus})<0)\n"
            f"    {{\n"
            f"        ret = -1;\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n")
            
        return r

    def _generar_condicion(self,campo):        
        if campo.tipo == TipoDeCampo.INT.value or campo.tipo == TipoDeCampo.FLOAT.value or campo.tipo == TipoDeCampo.FKEY.value:
            return f'||{self.nombre_min}_set{campo.nombre_may}Str(aux,{campo.nombre_min}Str)'

        elif campo.tipo == TipoDeCampo.STRING.value:
            return f'||{self.nombre_min}_set{campo.nombre_may}(aux,{campo.nombre_min}Str)'

    def _generar_parametros(self,campo):
        return f',char* {campo.nombre_min}Str'

    def generar_cuerpo(self):
        condicion = ""
        parametros = ""
        cuerpo = self._generar_includes()

        for campo in self.campos:

            condicion += self._generar_condicion(campo)
            parametros += self._generar_parametros(campo)

            if campo.tipo == TipoDeCampo.INT.value or campo.tipo == TipoDeCampo.FKEY.value:
                cuerpo += self._generar_int(campo)

            elif campo.tipo == TipoDeCampo.FLOAT.value:
                cuerpo += self._generar_float(campo)
            
            elif campo.tipo == TipoDeCampo.STRING.value:
                cuerpo += self._generar_string(campo)

        minuns = self.nombre_min
        mayus = self.nombre_may

        new = (f"{mayus}* {minuns}_newParametros({parametros})\n"
            f"{{\n"
            f"    {mayus}* aux;\n"
            f"    aux={minuns}_new();\n"
            f"    if(aux!=NULL)\n"
            f"    {{\n"
            f"        if({condicion})\n"
            f"        {{\n"
            f"            {minuns}_delete(aux);\n"
            f"            aux=NULL;\n"
            f"        }}\n"
            f"    }}\n"
            f"    return aux;\n"
            f"}}\n\n")

        return cuerpo + new

    def _generar_includes_h(self):
        minus = self.nombre_min
        mayus = self.nombre_may

        campos = '    int id;\n'

        for campo in self.campos:
            if(campo.tipo == TipoDeCampo.STRING.value):
                campos += f"    char {campo.nombre_min}[128];\n"

            elif(campo.tipo == TipoDeCampo.INT.value or campo.tipo == TipoDeCampo.FKEY.value):
                campos += f"    int {campo.nombre_min};\n"

            elif(campo.tipo == TipoDeCampo.FLOAT.value):
                campos += f"    float {campo.nombre_min};\n"

        r = (f"#ifndef {mayus}_H_INCLUDED\n"
            f"#define {mayus}_H_INCLUDED\n\n"

            f"typedef struct\n"
            f"{{\n"
            f"{campos}"
            f"}}{mayus};\n\n"

            f"void {minus}_idInit(int id);\n"
            f"int {minus}_idGenerator();\n\n"

            f"{mayus}* {minus}_new();\n"
            f"int {minus}_delete({mayus}* this);\n\n"

            f"int {minus}_setIdStr({mayus}* this,char* idStr);\n"
            f"int {minus}_setId({mayus}* this,int id);\n"
            f"int {minus}_getId({mayus}* this,int* id);\n"
            f"int {minus}_compareId(void* p{mayus}A,void* p{mayus}B);\n\n")

        return r

    def _generar_int_h(self,campo):
        c_min = campo.nombre_min
        c_may = campo.nombre_may
        s_min = self.nombre_min
        s_may = self.nombre_may
        r = (f"int {s_min}_set{c_may}Str({s_may}* this,char* {c_min}Str);\n"
            f"int {s_min}_set{c_may}({s_may}* this,int {c_min});\n"
            f"int {s_min}_get{c_may}({s_may}* this,int* {c_min});\n"
            f"int {s_min}_compare{c_may}(void* p{s_may}A,void* p{s_may}B);\n\n")

        return r

    def _generar_float_h(self,campo):
        c_min = campo.nombre_min
        c_may = campo.nombre_may
        s_min = self.nombre_min
        s_may = self.nombre_may
        r = (f"int {s_min}_set{c_may}Str({s_may}* this,char* {c_min}Str);\n"
            f"int {s_min}_set{c_may}({s_may}* this,float {c_min});\n"
            f"int {s_min}_get{c_may}({s_may}* this,float* {c_min});\n"
            f"int {s_min}_compare{c_may}(void* p{s_may}A,void* p{s_may}B);\n\n")

        return r

    def _generar_string_h(self,campo):
        c_min = campo.nombre_min
        c_may = campo.nombre_may
        s_min = self.nombre_min
        s_may = self.nombre_may
        r = (f"int {s_min}_set{c_may}({s_may}* this,char* {c_min});\n"
            f"int {s_min}_get{c_may}({s_may}* this,char* {c_min});\n"
            f"int {s_min}_compare{c_may}(void* p{s_may}A,void* p{s_may}B);\n\n")

        return r

    def _generar_parametro_h(self,campo):
        return f",char* {campo.nombre_min}Str"

    def generar_cuerpo_h(self):
        parametros = "char* idStr"
        cuerpo = self._generar_includes_h()

        for campo in self.campos:
            parametros += self._generar_parametro_h(campo)
            if campo.tipo == TipoDeCampo.INT.value or campo.tipo== TipoDeCampo.FKEY.value:
                cuerpo += self._generar_int_h(campo)

            elif campo.tipo == TipoDeCampo.FLOAT.value:
                cuerpo += self._generar_float_h(campo)
            
            elif campo.tipo == TipoDeCampo.STRING.value:
                cuerpo += self._generar_string_h(campo)

        new = f"{self.nombre_may}* {self.nombre_min}_newParametros({parametros});\n\n"

        return cuerpo + new

    def _generar_controler_load_c(self):
        s_min = self.nombre_min
        s_may = self.nombre_may
        r = (f"/** \\brief Carga los datos de los {s_min} desde el archivo data.csv (modo texto).\n"
            f" *\n"
            f" * \param path char*\n"
            f" * \param this LinkedList*\n"
            f" * \\return int\n"
            f" *\n"
            f" */\n"
            f"int controller_load{s_may}FromText(char* path, LinkedList* this)\n"
            f"{{\n"
            f"    int ret=0;\n"
            f"    FILE* pFile;\n"
            f"    pFile = fopen(path,\"r\");\n"
            f"    ret=parser_{s_may}FromText(pFile, this);\n"
            f"    fclose(pFile);\n"
            f"    return ret;\n"
            f"}}\n\n")

        return r

    def _generar_controler_lastId_c(self):
        s_min = self.nombre_min
        s_may = self.nombre_may
        r = (f"/** \\brief Obtiene el mayor id del LinkedList y lo carga en la estructura {s_may}.\n"
            f"*\n"
            f"* \param this LinkedList*\n"
            f"* \\return int\n"
            f"*\n"
            f"*/\n"
            f"int controller_lastId{s_may}(LinkedList* this)\n"
            f"{{\n"
            f"    {s_may}* buffer;\n"
            f"    int bufferId;\n"
            f"    int auxId = -1;\n"
            f"    int ret = -1;\n"
            f"    int i;\n"
            f"    int len;\n"
            f"    if(this!=NULL)\n"
            f"    {{\n"
            f"        len=ll_len(this);\n"
            f"        for(i=0; i<len; i++)\n"
            f"        {{\n"
            f"            buffer=({s_may}*)ll_get(this,i);\n"
            f"            {s_min}_getId(buffer,&bufferId);\n"
            f"            if(bufferId>auxId)\n"
            f"            {{\n"
            f"                auxId=bufferId;\n"
            f"            }}\n"
            f"        }}\n"
            f"        {s_min}_idInit(auxId);\n"
            f"        ret = 0;\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n")
        
        return r

    def _generar_buffers_parser(self):
        r = ""
        for campo in self.campos:
            r += f"char buffer{campo.nombre_may}[4096];\n"
        
        return r

    def _generar_mascara_parser(self):
        r = ""
        for campo in self.campos:
            r += "%[^,],"
        
        return r

    def _generar_variables_buffer(self):
        r = ""
        for campo in campos:
            r += f",buffer{campo.nombre_may}"
        
        return r

    def generar_parser_c(self):
        s_min = self.nombre_min
        s_may = self.nombre_may

        r = (f"#include <stdio.h>\n"
            f"#include <stdlib.h>\n"
            f"#include \"LinkedList.h\"\n"
            f"#include \"{s_may}.h\"\n\n"
            f"/** \brief Parsea los datos los datos del tipo {s_may} desde el archivo recibido como parametro (modo texto).\n"
            f" *\n"
            f" * \param path char*\n"
            f" * \param pArrayList{s_may} LinkedList*\n"
            f" * \return int\n"
            f" *\n"
            f" */\n"
            f"int parser_{s_may}FromText(FILE* pFile , LinkedList* pArrayList{s_may})\n"
            f"{{\n"
            f"    int ret= 0;\n"
            f"    char bufferId[4096];\n"
            f"    {self._generar_buffers_parser()}"
            f"    {s_may} *p{s_may}\n\n"
            f"    if(pFile!=NULL && pArrayList{s_may}!=NULL)\n"
            f"    {{\n"
            f"        fscanf(pFile,\"[^\\n]\\n\");\n"
            f"        while(!feof(pFile))\n"
            f"        {{\n"
            f"            fscanf(pFile,\"{self._generar_mascara_parser}%[^\\n]\\n\", bufferId{self._generar_variables_buffer()});\n\n"
            f"            p{s_may} = {s_min}_newParametros(bufferId{self._generar_variables_buffer()});\n\n"
            f"            if(p{s_may} != NULL)\n"
            f"            {{\n"
            f"                if(!ll_add(pArrayList{s_may},p{s_may}))\n"
            f"                {{\n"
            f"                    ret++;\n"
            f"                }}\n"
            f"            }}\n"
            f"        }}\n"
            f"    }}\n"
            f"    return ret;\n"
            f"}}\n\n")

    def generar_parser_h(self):
        return f"int parser_{self.nombre_may}FromText(FILE* pFile , LinkedList* pArrayList{self.nombre_may});"

    