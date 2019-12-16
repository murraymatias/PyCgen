

def generate_lastId(estructura):
    struct = estructura.lower()
    structMay = struct.capitalize()
    string = (f"/** \\brief Obtiene el mayor id del LinkedList y lo carga en la estructura {mayus}.\n"
                f" *\n"
                f" * \param this LinkedList*\n"
                f" * \\return int\n"
                f" *\n"
                f" */\n"
                f"int controller_lastId{mayus}(LinkedList* this)\n"
                f"{{\n"
                f"    {mayus}* buffer;\n"
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
                f"            buffer=({mayus}*)ll_get(this,i);\n"
                f"            {minus}_getId(buffer,&bufferId);\n"
                f"            if(bufferId>auxId)\n"
                f"            {{\n"
                f"                auxId=bufferId;\n"
                f"            }}\n"
                f"        }}\n"
                f"        {minus}_idInit(auxId);\n"
                f"        ret = 0;\n"
                f"    }}\n"
                f"    return ret;\n"
                f"}}\n\n")
    
    return string

def generate_searchId(estructura):
    struct = estructura.lower()
    structMay = struct.capitalize()
    string = '''/** \brief Obtiene el mayor id del LinkedList y lo carga en la estructura {mayus}.
 *
 * \param this LinkedList*
 * \param id int
 * \param index int*
 * \return int
 *
 */
int controller_search{mayus}ById(LinkedList* this,int id,int* index)
{{
    {mayus}* buffer;
    int bufferId;
    int ret = -1;
    int i;
    int len;
    if(this!=NULL)
    {{
        len=ll_len(this);
        for(i=0; i<len; i++)
        {{
            buffer=({mayus}*)ll_get(this,i);
            {minus}_getId(buffer,&bufferId);
            if(bufferId==id)
            {{
                *index=i;
                ret = 0;
            }}
        }}
    }}
    return ret;
}}

'''.format(mayus=structMay,minus=struct)

    return string

def generate_alta(estructura,listaCampos):
    struct = estructura.lower()
    structMay = struct.capitalize()
    buffers = ''
    gets = ''
    for i in range(len(listaCampos)):
        if i > 0:
            gets += '&&'
        campo = listaCampos[i][1].lower()
        campoMayus = campo.capitalize()
        if listaCampos[i][0] == 'int':
            buffers += '''int buffer{campoMayus};
            '''.format(campoMayus=campoMayus)
            gets += '''!utn_getInt(&bufferHorasTrabajadas,"Ingrese horas trabajadas: ","Valor invalido",0,INT_MAX,10)'''
        if listaCampos[i][0] == 'float':
            buffers += '''float buffer{campoMayus};
            '''.format(campoMayus=campoMayus)
            gets+= '''!utn_getFloat(&bufferHorasTrabajadas,"Ingrese horas trabajadas: ","Valor invalido",0,INT_MAX,10)'''
        if listaCampos[i][0] == 'str':
            buffers += '''char buffer{campoMayus}[128];
            '''.format(campoMayus=campoMayus)
            gets += '''!utn_getString(bufferNombre,128,"Ingrese nombre: ","Valor Invalido",1,127,10)'''
        if listaCampos[i][0] == 'fk':
            buffers += '''int buffer{campoMayus};
            '''.format(campoMayus=campoMayus)
            gets += '''!utn_getInt(&bufferHorasTrabajadas,"Ingrese horas trabajadas: ","Valor invalido",0,INT_MAX,10)'''

    string = '''/** \\brief Alta de empleados
 *
 * \param path char*
 * \param this LinkedList*
 * \\return int
 *
 */
int controller_add{mayus}(LinkedList* this)
{{
    int ret = -1;
    {mayus}* buffer{mayus};
    buffer{mayus} = {minus}_new();
    {buffer}
    
    if(this!=NULL && buffer{mayus}!=NULL)
    {{
        if({get})
        {{
            {minus}_setId(buffer{mayus},{minus}_idGenerator());
            {minus}_setNombre(bufferEmployee,bufferNombre);
            {minus}_setHorastrabajadas(bufferEmployee,bufferHorasTrabajadas);
            {minus}_setSueldo(bufferEmployee,bufferSueldo);

            ll_add(this,buffer{mayus});
        }}
        else
        {{
            {minus}_delete(buffer{mayus});
        }}

    }}
    return ret;
}}

'''.format(mayus=structMay,minus=struct,buffer=buffers,set=sets,get=gets)