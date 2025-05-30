-- Crear base de datos
CREATE DATABASE IF NOT EXISTS PandaTaT;
USE PandaTaT;

-- Tabla de roles
CREATE TABLE IF NOT EXISTS Roles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL
);

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS Usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    rol_id INT,
    FOREIGN KEY (rol_id) REFERENCES Roles(id)
);

-- Tabla de estados de pedidos
CREATE TABLE IF NOT EXISTS Estado_pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    estado VARCHAR(50) NOT NULL
);

-- Tabla de pedidos
CREATE TABLE IF NOT EXISTS Pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    descripcion TEXT,
    fecha DATE,
    usuario_id INT,
    estado_id INT,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id),
    FOREIGN KEY (estado_id) REFERENCES Estado_pedidos(id)
);

-- Insertar roles
INSERT INTO Roles (nombre) VALUES ('Administrador'), ('Gerente de zona'), ('Vendedor'), ('Cliente');

-- Insertar usuarios
INSERT INTO Usuarios (nombre, correo, rol_id) VALUES
('Ana Admin', 'ana@admin.com', 1),
('Carlos Gerente', 'carlos@gerente.com', 2),
('Victor Vendedor', 'victor@ventas.com', 3),
('Claudia Cliente', 'claudia@cliente.com', 4);

-- Insertar estados de pedidos
INSERT INTO Estado_pedidos (estado) VALUES
('Enviado'),
('Cancelado'),
('Pagado'),
('Reenviado');

-- Insertar pedidos
INSERT INTO Pedidos (descripcion, fecha, usuario_id, estado_id) VALUES
('Pedido de ejemplo 1', '2024-06-01', 3, 1),
('Pedido cancelado', '2024-06-03', 3, 2),
('Pedido pagado', '2024-06-04', 4, 3),
('Reenvío de pedido', '2024-06-06', 4, 4);
