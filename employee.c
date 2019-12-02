#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "utn.h"
#include "Employee.h"

static int lastId=0;

void employee_idInit(int id)
{
    lastId=id+1;
}

int employee_idGenerator()
{
    return lastId++;
}

int employee_setIdStr(Employee* this,char* idStr)
{
    int ret=-1;
    int bufferId;
    if(this!=NULL && idStr!=NULL)
    {
        if(utn_isValidInt(idStr))
        {
            bufferId = atoi(idStr);
            if(!employee_setId(this,bufferId))
            {
                ret=0;
            }
        }
    }
    return ret;
}

int employee_setId(Employee* this,int id)
{
    int ret=-1;
    if(this!=NULL && id>=0)
    {
        this->id=id;
        ret=0;
    }
    return ret;
}

int employee_getId(Employee* this,int* id)
{
    int ret=-1;
    if(this!=NULL&&id!=NULL)
    {
        *id=this->id;
        ret=0;
    }
    return ret;
}

Employee* employee_new()
{
    return (Employee*)malloc(sizeof(Employee));
}

int employee_delete(Employee* this)
{
    int ret=-1;
    if(this!=NULL)
    {
        free(this);
        ret=0;
    }
    return ret;
}

int employee_compareId(void* pElementA,void* pElementB)
{
    int ret = 0;
    if(((Employee*)pElementA)->id > ((Employee*)pElementB)->id)
    {
        ret = 1;
    }
    if(((Employee*)pElementA)->id < ((Employee*)pElementB)->id)
    {
        ret = -1;
    }
    return ret;
}

int employee_setNombre(Employee* this,char* nombre)
{
    int ret=-1;
    if(this != NULL && utn_isValidName(nombre))
    {
        strncpy(this->nombre,nombre,sizeof(this->nombre));
        ret=0;
    }
    return ret;
}

int employee_getNombre(Employee* this,char* nombre)
{
    int ret=-1;
    if(this!=NULL && nombre!=NULL)
    {
        strncpy(nombre,this->nombre,sizeof(this->nombre));
        ret=0;
    }
    return ret;
}

int employee_compareNombre(void* pElementA,void* pElementB)
{
    int ret = 0;
    if(strcmp(((Employee*)pElementA)->nombre,((Employee*)pElementB)->nombre)>0)
    {
        ret = 1;
    }
    if(strcmp(((Employee*)pElementA)->nombre,((Employee*)pElementB)->nombre)<0)
    {
        ret = -1;
    }
    return ret;
}

int employee_setHorastrabajadasStr(Employee* this,char* horastrabajadasStr)
{
    int ret=-1;
    int bufferHorastrabajadas;
    if(this!=NULL)
    {
        if(utn_isValidInt(horastrabajadasStr))
        {
            bufferHorastrabajadas = atoi(horastrabajadasStr);
            if(!employee_setHorastrabajadas(this,bufferHorastrabajadas))
            {
                ret=0;
            }
        }
    }
    return ret;
}

int employee_setHorastrabajadas(Employee* this,int horastrabajadas)
{
    int ret=-1;
    if(this!=NULL && horastrabajadas>=0)
    {
        this->sueldo=horastrabajadas;
        ret=0;
    }
    return ret;
}

int employee_getHorastrabajadas(Employee* this,int* horastrabajadas)
{
    int ret=-1;
    if(this!=NULL && horastrabajadas!=NULL)
    {
        *horastrabajadas=this->horastrabajadas;
        ret=0;
    }
    return ret;
}

int employee_compareHorastrabajadas(void* pElementA,void* pElementB)
{
    int ret = 0;
    if(((Employee*)pElementA)->horastrabajadas > ((Employee*)pElementB)->horastrabajadas)
    {
        ret = 1;
    }
    if(((Employee*)pElementA)->horastrabajadas < ((Employee*)pElementB)->horastrabajadas)
    {
        ret = -1;
    }
    return ret;
}

int employee_setSueldoStr(Employee* this,char* sueldoStr)
{
    int ret=-1;
    int bufferSueldo;
    if(this!=NULL)
    {
        if(utn_isValidInt(sueldoStr))
        {
            bufferSueldo = atoi(sueldoStr);
            if(!employee_setSueldo(this,bufferSueldo))
            {
                ret=0;
            }
        }
    }
    return ret;
}

int employee_setSueldo(Employee* this,int sueldo)
{
    int ret=-1;
    if(this!=NULL && sueldo>=0)
    {
        this->sueldo=sueldo;
        ret=0;
    }
    return ret;
}

int employee_getSueldo(Employee* this,int* sueldo)
{
    int ret=-1;
    if(this!=NULL && sueldo!=NULL)
    {
        *sueldo=this->sueldo;
        ret=0;
    }
    return ret;
}

int employee_compareSueldo(void* pElementA,void* pElementB)
{
    int ret = 0;
    if(((Employee*)pElementA)->sueldo > ((Employee*)pElementB)->sueldo)
    {
        ret = 1;
    }
    if(((Employee*)pElementA)->sueldo < ((Employee*)pElementB)->sueldo)
    {
        ret = -1;
    }
    return ret;
}

Employee* employee_newParametros(char* idStr,char* nombreStr,char* horastrabajadasStr,char* sueldoStr)
{
    Employee* aux;
    aux=employee_new();
    if(aux!=NULL)
    {
        if(employee_setIdStr(aux,idStr)||employee_setNombre(aux,nombreStr)||employee_setHorastrabajadasStr(aux,horastrabajadasStr)||employee_setSueldoStr(aux,sueldoStr))
        {
            employee_delete(aux);
            aux=NULL;
        }
    }
    return aux;
}

