DDL_QUERY =  '''
CREATE TABLE dim_persona (
    idpersona INT NOT NULL PRIMARY KEY,
    tipo_persona VARCHAR(20),
    nombre VARCHAR(100),
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(20),
    direccion VARCHAR(70),
    telefono VARCHAR(20),
    email VARCHAR(50)
)
;

CREATE TABLE dim_articulo (
    idarticulo INT NOT NULL PRIMARY KEY,
    codigo VARCHAR(50),
    nombre_articulo VARCHAR(100),
    precio_venta DECIMAL(11 , 2 ),
    stock INT,
    nombre_categoria VARCHAR(100)
)
;

CREATE TABLE dim_fechas (
    id_fecha VARCHAR(100) NOT NULL PRIMARY KEY,
    fecha DATETIME,
    año INT,
    mes INT,
    trimestre INT,
    dia INT,
    dia_semana INT,
    hora INT,
    minuto INT,
    finde INT
);

CREATE TABLE dim_tipo (
    idtipo INT NOT NULL PRIMARY KEY,
    tipo VARCHAR(20)
);

CREATE TABLE tabla_hechos (
    iddetalle_tran INT PRIMARY KEY,
    id_tran int,
    idarticulo INT REFERENCES dim_articulo (idarticulo),
    idpersona INT REFERENCES dim_persona (idpersona),
    id_fecha VARCHAR(100) REFERENCES dim_fechas (id_fecha),
    idtipo INT REFERENCES dim_tipo (idtipo),
    cantidad INT,
    precio INT,
    descuento INT
); '''