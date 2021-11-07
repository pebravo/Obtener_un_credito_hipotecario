nombre_cliente=input('ingrese su nombre:  ')
rut_cliente=input('ingrese su rut: ')
nacionalidad=input('ingrese nacionalidad: ')
sueldo=int(input('ingrese su sueldo: '))
antiguedad=int(input('ingrese su antiguedad laboral: '))
morosidades=input('indique si tiene morosidad: ')


valido1 = 0
while valido1 == 0:
    monto_credito=int(input('ingrese el monto a solicitar: '))
    if monto_credito >=500000:
        valido1 = 1
    else:
        print('debe solicitar un monto sobre 500.000')

valido2 = 0
while valido2 == 0:
    cuotas_credito=int(input('ingrese el numero de cuotas: '))
    if cuotas_credito >=3 and cuotas_credito <=84:
        valido2 = 1
    else:
        print('debe solicitar en otro numero de cuotas')

monto_max=(sueldo*10)
cuotas_tasa =(monto_credito/cuotas_credito)
valor_cuota=(cuotas_tasa*1.46)
total=(valor_cuota*cuotas_credito)
var=int(total)


edad_cliente=int(input('ingrese su edad: '))
if edad_cliente >=24 and edad_cliente <=79 and sueldo >=300000 and antiguedad >=3 and nacionalidad == 'chilena' and morosidades =='no' :
     print('--------------------------------------------------')
     print(nombre_cliente,        rut_cliente)
     print('--------------------------------------------------')
     print('cumple con los requisitos')
     print('sueldo: ',sueldo)
     print('monto Máximo: $',monto_max)
     print('Monto Solicitado: $',monto_credito)
     print('Tasa mensual: 1.46%')
     print('cuotas: ',cuotas_credito)
     print('Monto a Pagar: ',var)
else:
    print('--------------------------------------------------')
    print(nombre_cliente,        rut_cliente)
    print('No cumple con los requisitos')
    print('--------------------------------------------------')
        
