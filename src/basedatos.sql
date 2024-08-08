CREATE DATABASE IF NOT EXISTS energias_egemsa;
use energias_egemsa;

CREATE TABLE energias(
    id              int(25) auto_increment not null,
    local_time      varchar(100),
    timestam        varchar(255),
    KWh_del         varchar(255) not null,
    KWh_rec         varchar(255) not null,
    KVARh_Q1        varchar(255) not null,
    KVARh_Q2        varchar(255) not null,
    KVARh_Q3        varchar(255) not null,
    KVARh_Q4        varchar(255) not null,
    VII_prom        varchar(255) not null,

    -- CONSTRAINT pk_usuarios PRIMARY KEY(id),
    -- CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

-- CREATE TABLE notas(
--     id          int(25) auto_increment not null,
--     usuario_id  int(25) not null,
--     titulo      varchar(255) not null,
--     descripcion MEDIUMTEXT,
--     CONSTRAINT pk_notas PRIMARY KEY(id),
--     CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)

-- )ENGINE=InnoDb;