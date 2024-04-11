DDL_QUERY =  '''
CREATE TABLE IF NOT EXISTS categoria(
    idcategoria INT PRIMARY KEY,
    nombre varchar(50),
    descripcion varchar(255),
    estado bit
);

CREATE TABLE IF NOT EXISTS rol(
    idrol INT PRIMARY KEY,
    nombre varchar(30),
    descripcion varchar(255),
    estado bit
);

CREATE TABLE IF NOT EXISTS persona(
    idpersona INT PRIMARY KEY,
	tipo_persona varchar(20),
    nombre varchar(100),
    tipo_documento varchar(20),
    num_documento varchar(20),
    direccion varchar(70),
    telefono varchar(20),
    email varchar(50)
);

CREATE TABLE IF NOT EXISTS articulo(
    idarticulo INT PRIMARY KEY,
    idcategoria int,
    codigo varchar(50),
    nombre varchar(100),
    precio_venta decimal(11,2),
    stock int,
    descripcion varchar(255),
    imagen varchar(20),
    estado bit,
    
    CONSTRAINT fk_idcategoria
        FOREIGN KEY (idcategoria)
            REFERENCES categoria(idcategoria)
);

CREATE TABLE IF NOT EXISTS usuario(
    idusuario INT PRIMARY KEY,
    idrol int,
    nombre varchar(100),
    tipo_documento varchar(20),
    num_documento varchar(20),
    direccion varchar(70),
    telefono varchar(20),
    email varchar(50),
    clave varchar(255),
    estado bit,

    CONSTRAINT fk_idrol
        FOREIGN KEY (idrol)
            REFERENCES rol(idrol)

);

CREATE TABLE IF NOT EXISTS venta(
    idventa INT PRIMARY KEY,
    idcliente int,
    idusuario int,
    tipo_comprobante varchar(20),
    serie_comprobante varchar(7),
    num_comprobante varchar(10),
    fecha timestamp,
    impuesto decimal(4,2),
    total decimal (11,2),
    estado varchar(20),
    
    CONSTRAINT fk_idcliente
        FOREIGN KEY (idcliente)
            REFERENCES persona(idpersona),
            
	CONSTRAINT fk_idusuario
        FOREIGN KEY (idusuario)
            REFERENCES usuario(idusuario)
);

CREATE TABLE IF NOT EXISTS detalle_venta(
    iddetalle_venta INT PRIMARY KEY,
    idventa int,
    idarticulo int,
    cantidad int,
    precio decimal(11,2),
    descuento decimal (11,2),
    
    CONSTRAINT fk_idarticulo
        FOREIGN KEY (idarticulo)
            REFERENCES articulo(idarticulo),
            
	CONSTRAINT fk_idventa
        FOREIGN KEY (idventa)
            REFERENCES venta(idventa)
);

CREATE TABLE IF NOT EXISTS ingreso(
    idingreso INT PRIMARY KEY,
    idproveedor int,
    idusuario int,
    tipo_comprobante varchar(20),
    serie_comprobante varchar(7),
    num_comprobante varchar(10),
    fecha timestamp,
    impuesto decimal(4,2),
    total decimal(11,2),
    estado varchar(20),

    CONSTRAINT fk_idproveedor
        FOREIGN KEY (idproveedor)
            REFERENCES persona(idpersona),
            
	CONSTRAINT fk_idusuario2
        FOREIGN KEY (idusuario)
            REFERENCES usuario(idusuario)
);

CREATE TABLE IF NOT EXISTS detalle_ingreso(
    iddetalle_ingreso INT PRIMARY KEY,
    idingreso int,
    idarticulo int,
    cantidad int,
    precio decimal(11,2),
    
    CONSTRAINT fk_idingreso
        FOREIGN KEY (idingreso)
            REFERENCES ingreso(idingreso)
); '''