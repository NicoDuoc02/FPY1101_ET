import random
import csv
import os
import time
trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
opciones=0
programador="Nicolas Lorca"
rut_programador="22.069.002-4"
try:
    with open('Sueldos.csv','r') as archivo:
        print("Leyendo el archivo")
except(FileNotFoundError):
    with open('Sueldos.csv','w') as archivo:
        writer=csv.writer(archivo)
        print("Archivo Creado")

def menu ():
    print("Bienvenido")
    print("1.Generar sueldos random")
    print("2.Clasificar Sueldo")
    print("3.Ver estadisticas")
    print("4.Reporte de sueldos")
    print("5.Salir")

def sueldosran():
    with open('Sueldos.csv','w') as archivo: 
        os.system('cls')
        writer=csv.writer(archivo)
        writer.writerow(['Trabajador','Sueldo Base','Descuento Salud','Descuento AFP','Sueldo liquido'])
        for i in trabajadores:
            sueldo=random.randint(300000,2500000)
            descuento_salud=int(sueldo*0.07)
            descuento_afp=int(sueldo*0.12)
            sueldo_liquido=sueldo-descuento_salud-descuento_afp
            writer.writerow([i,sueldo,descuento_salud,descuento_afp,sueldo_liquido])
        print("se Han generados sueldos random")
        time.sleep(2)
def clasificarsueldo():
    with open('Sueldos.csv','r')as archivo:
        read=csv.DictReader(archivo)
        sueldo_menores_800k=0
        sueldo_superior_800k=0
        sueldo_superior_2m=0
        sueldo_total=0
        os.system('cls')
        for x in read:
            trabajador=x['Trabajador']
            sueldo_base=int(x['Sueldo Base'])
            sueldo_total += sueldo_base
            if sueldo_base < 800000:
                sueldo_menores_800k += 1 
                print("Sueldo menor $800.000")
                print("Nombre empleado\tsueldo")
                print(sueldo_menores_800k,trabajador,"\t$",sueldo_base)
                time.sleep(1) 
            elif sueldo_base >= 800000 :    
                sueldo_superior_800k +=1
                if sueldo_base <=2000000:
                    print("Sueldo Entre $800.000 y $2.000.000")
                    print("Nombre empleado\tsueldo")
                    print(sueldo_superior_800k,trabajador,"\t$",sueldo_base)
                    time.sleep(1) 
            elif sueldo_base > 2000000:
                print("Sueldo superior a $2.000.000")
                print("Nombre empleado\tsueldo")
                print(sueldo_superior_2m,trabajador,"\t$",sueldo_base)
                time.sleep(1) 
        time.sleep(2)
        
def ver_estadisticas():
    with open('Sueldos.csv','r')as archivo:
        read=csv.DictReader(archivo)
        opciones=0
        os.system('cls')
        while opciones != 5:
            print("1.Sueldo mas alto")
            print("2.Sueldo mas bajo")
            print("3.Promedio de sueldos")
            print("4.Media geometrica")
            print("5.Salir")
            try:
                opciones=int(input("Ingrese la opcion que desea:"))
            except(ValueError):
                print("Error al ingreso de datos")
                continue
            
            Nom_sueldo_alto=""
            sueldo_alto=0
            Nom_sueldo_bajo=""
            sueldo_bajo=1e10
           
           #Sueldo mas alto 
            if opciones ==1:
                with open('Sueldos.csv','r')as archivo:
                    os.system('cls')
                    read=csv.DictReader(archivo)
                    print("El sueldo mas Alto es")
                    for i in read:
                        trabajador=i['Trabajador']
                        sueldo_base=int(i['Sueldo Base'])     
                        if sueldo_base > sueldo_alto:
                            Nom_sueldo_alto=trabajador
                            sueldo_alto=sueldo_base
                    
                    print("Trabajador\tSueldo")
                    print(Nom_sueldo_alto,"\t",sueldo_alto)
                    i=""
                archivo.close
                time.sleep(2)
            #Sueldo mas bajo
            elif opciones == 2:
                with open('Sueldos.csv','r')as archivo:
                    read=csv.DictReader(archivo)
                    print("El sueldo mas bajo es")
                    for i in read:
                        trabajador=i['Trabajador']
                        sueldo_base=int(i['Sueldo Base'])     
                        if sueldo_base < sueldo_bajo:
                            Nom_sueldo_bajo=trabajador
                            sueldo_bajo=sueldo_base
                    print("Trabajador\tSueldo")
                    print(Nom_sueldo_bajo,"\t",sueldo_bajo)
                    i=""
                archivo.close        
                time.sleep(2)
            
            #Promedio de sueldo 
            elif opciones== 3:
                with open('Sueldos.csv','r')as archivo:
                    read=csv.DictReader(archivo)
                    print("El sueldo promedio es de: ",end="")
                    sueldo_total=0
                    count=0
                    for i in read:
                        sueldo_base=int(i['Sueldo Base'])
                        sueldo_total += sueldo_base
                        count+=1
                    promedio=sueldo_total//count
                    print(promedio)
                archivo.close
                time.sleep(2)   
            
            elif opciones == 4:
                with open('Sueldos.csv','r')as archivo:
                    read=csv.DictReader(archivo)
                    print("La media geometrica es de: ",end="")
                    sueldo_total=0
                    count=0
                    for i in read:
                        sueldo_base=int(i['Sueldo Base'])
                        sueldo_total += sueldo_base
                        count+=1
                    media_geo=int(sueldo_total//(count**0.5))
                    print(media_geo)
                archivo.close
                time.sleep(2)
            
            else:
                print("Saliendo ")

def reporte_sueldos():
     os.system('cls')
     with open('Sueldos.csv','r')as archivo:
        read=csv.DictReader(archivo)
        print("Nombre Empleado\t\t\tSueldo Base\t\t\tDescuento Salud\t\t\tDescuento AFP\t\t\tSueldo liquido")
        for i in read:
            trabajador=i['Trabajador']
            sueldo=(int(i['Sueldo Base']))
            descuento_salud=int(sueldo*0.07)
            descuento_afp=int(sueldo*0.12)
            sueldo_liquido=sueldo-descuento_salud-descuento_afp
            print(trabajador,"\t\t\t",sueldo,"\t\t\t",descuento_salud,"\t\t\t",descuento_afp,"\t\t\t",sueldo_liquido)
            time.sleep(4)

def salir():
    os.system('cls')
    print("Finalizando Programa...")
    print("Desarrollado por: " + programador)
    print("Rut: " + rut_programador)
    time.sleep(1)
while opciones != 5:
    menu()
    try:
        opciones=int(input("Ingrese la opcion que desea realizar: "))
    except(ValueError):
        print("dato erroneo")
        continue
    if opciones == 1:
        sueldosran()
    elif opciones == 2:
        clasificarsueldo()
    elif opciones == 3:
        ver_estadisticas()
    elif opciones == 4:
        reporte_sueldos()
    else:
        salir()