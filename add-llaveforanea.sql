--Pregunta 2

--Agregar tabla "Restaurantes"
Create table restaurantes(rut serial primary key not null, nombre varchar(255), direccion varchar(255))

-- Agrgar a las tablas con las que se relaciona la llave foranea "rut"

Alter table colaboradores add rut_rest int ,FOREign key (rut_rest);
Alter table cartas add rut_rest int ,FOREign key (rut_rest);
Alter table roles add rut_rest int ,FOREign key (rut_rest);
Alter table boleta add rut_rest int ,FOREign key (rut_rest);

-------Pregunta 3

--1- Nombre del cliente, del repartidor y la fecha del pedido para todas las devoluciones

    select clientes.nombre, colaboradores.nombre from clientes,colaboradores,roles,pedidos,despachos 
    where cliente.rut=pedidos.rut_cliente and colaboradores.rut=despachos.rut_repartidor and pedidos.codigo=despachos.pedido_id 
    and colaboradores.rut=cumplen.colab_rut and roles.id=rol_id and roles.nombre="repartidor".


--2- Nombre del cliente que ha realizado la mayor cantidad de pedidos durante el año 2019.

    -- consulta para mostrar los que han devuelto productos durante 2019
    select clientes.nombre from clientes, pedidos , estados where clientes.rut=pedidos.rut_cliente and pedidos.estado_id=estado.id and 
    estado.nombre="Devolucion" and year(pedidos.timestamp)=2019

    -- contarlos por cada cliente

    select count(*) from (select clientes.nombre from clientes, pedidos , estados where clientes.rut=pedidos.rut_cliente 
    and pedidos.estado_id=estado.id and estado.nombre="Devolucion" and year(pedidos.timestamp)=2019) as t1 group by clientes.nombre 

    -- sacar maximo 
    select max(t2.count) from (select count(*) from (select clientes.nombre from clientes, pedidos , estados where clientes.rut=pedidos.rut_cliente 
    and pedidos.estado_id=estado.id and estado.nombre="Devolucion" and year(pedidos.timestamp)=2019) as t1 group by clientes.nombre) as t2

--3- Nombre del plato que ha sido parte de la mayor cantidad de devoluciones
    -- cantidad de devoluciones por plato
    select item. nombre, count(*) from items, pedidos, estados,contienen where items.sku=contienen.sku and contienen.pedido_codigo=pedidos.codigo 
    and pedidos.estado_id=estados.id and estados.nombre="devolucion" group by item having count=max(select count(*) from items, pedidos, estados,contienen where items.sku=contienen.sku and contienen.pedido_codigo=pedidos.codigo 
    and pedidos.estado_id=estados.id and estados.nombre="devolucion" group by item);

--4- Nombre del repartidor, del cliente, el límite de plazo de entrega y la hora efectiva de entrega para todos los pedidos retrasados
    select colaboradores.nombre, clientes.nombre , despachos.hora_limite from clientes, colaboradores, pedidos, despachos,estados where 
    clientes.rut=pedidos.rut_cliente and pedidos.codigo=despachos.pedido_id and colaborador.rut=despachos.colaborador_id and estados.id=pedidos.estado_id and estados.nombre="atrasados".
    
--5- Duración menor, superior y promedio de las rutas de despacho.
    select min(rutas.tiempo_final),max(rutas.tiempo_final),avg(rutas.tiempo_final) from rutas
