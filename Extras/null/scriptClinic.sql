DROP DATABASE AnaVisClin;
CREATE DATABASE AnaVisClin;
USE AnaVisClin;

-- Creación de tabla Paciente
CREATE TABLE Paciente (
    idPaciente INT AUTO_INCREMENT PRIMARY KEY,
    tipoIdendificacion VARCHAR(24) NOT NULL,
    numeroIdentificacion CHAR(15) NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    apellido VARCHAR(60) NOT NULL,
    telefono VARCHAR(10) NOT NULL,
    ciudad VARCHAR(60) NOT NULL DEFAULT 'Quito',
    direccion VARCHAR(250) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    fechaNacimiento DATE NOT NULL,
    alergia TEXT,
    sexo ENUM('Masculino', 'Femenino') NOT NULL,
    grupoSanguineo CHAR(8) NOT NULL,
    estadoCivil ENUM('Soltero', 'Divorciado', 'Casado', 'Viudo', 'Unión libre') NOT NULL,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT correo_uk UNIQUE (correo),
    CONSTRAINT telefono_uk UNIQUE (telefono),
    CONSTRAINT numeroIdentificacion_uk UNIQUE (numeroIdentificacion)
);

-- Creación de tabla ContactoEmergencia 
CREATE TABLE ContactoEmergencia (
    idContacto INT AUTO_INCREMENT PRIMARY KEY,
    idPaciente INT,
    nombre VARCHAR(60) NOT NULL,
    apellido VARCHAR(60) NOT NULL,
    telefono VARCHAR(10) NOT NULL,
    direccion VARCHAR(250) NOT NULL DEFAULT 'Quito',
    correo VARCHAR(100) NOT NULL,
    parentesco VARCHAR(30) NOT NULL,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT telefonoCE_uk UNIQUE (telefono),
    CONSTRAINT correoCE_uk UNIQUE (correo),
    CONSTRAINT Fk_codigoPacienteCE FOREIGN KEY (idPaciente)
        REFERENCES Paciente(idPaciente)
);

-- Creación de tabla Recepcionista 
CREATE TABLE Recepcionista (
    idRecepcionista TINYINT AUTO_INCREMENT PRIMARY KEY,
    cedula CHAR(10) NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    apellido VARCHAR(60) NOT NULL,
    telefono VARCHAR(10) NOT NULL,
    direccion VARCHAR(250) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT telefonoR_uk UNIQUE (telefono),
    CONSTRAINT correoR_uk UNIQUE (correo),
    CONSTRAINT cedulaR_uk UNIQUE (cedula)
);


-- Creación de tabla Doctor
CREATE TABLE Doctor (
    idDoctor TINYINT AUTO_INCREMENT PRIMARY KEY,
    cedula CHAR(10) NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    apellido VARCHAR(60) NOT NULL,
    telefono VARCHAR(10) NOT NULL,
    direccion VARCHAR(250) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT cedulaDoc_uk UNIQUE (cedula),
    CONSTRAINT correoD_uk UNIQUE (correo),
    CONSTRAINT telefonoD_uk UNIQUE (telefono)
);


-- Creación de tabla Especialidad
CREATE TABLE Especialidad (
    idEspecialidad TINYINT AUTO_INCREMENT PRIMARY KEY,
    nombreEspecialidad VARCHAR(40) NOT NULL,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT nombreEspecialidadE_uk UNIQUE (nombreEspecialidad)
);


-- Creación de tabla Horario
CREATE TABLE Horario (
    idHorario TINYINT AUTO_INCREMENT,
    dia CHAR(10) NOT NULL,
    horaInicio TIME NOT NULL,
    horaFin TIME NOT NULL,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT Pk_idEspecialidadED PRIMARY KEY (idHorario)
);


-- Creación de tabla EspecialidadDoctor
CREATE TABLE EspecialidadDoctor (
    idEspecialidadDoc TINYINT AUTO_INCREMENT PRIMARY KEY,
    idEspecialidad TINYINT,
    idDoctor TINYINT,
    idHorario TINYINT,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT Fk_codigoDoctorEs FOREIGN KEY (idDoctor) REFERENCES Doctor(idDoctor),
    CONSTRAINT Fk_EspecialidadEs FOREIGN KEY (idEspecialidad) REFERENCES Especialidad(idEspecialidad),
    CONSTRAINT Fk_idHorarioE FOREIGN KEY (idHorario) REFERENCES Horario(idHorario)
);


-- Creación de tabla NominaDoctor
CREATE TABLE NominaDoctor (
    idNomina TINYINT AUTO_INCREMENT PRIMARY KEY,
    idEspecialidad TINYINT,
    idDoctor TINYINT,
    idHorario TINYINT,
    monto DECIMAL(10, 2),
    fechaInicio DATE NOT NULL,
	fechaFin DATE NOT NULL,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT Fk_codigoDoctorEs2 FOREIGN KEY (idDoctor) REFERENCES Doctor(idDoctor),
    CONSTRAINT Fk_EspecialidadEs2 FOREIGN KEY (idEspecialidad) REFERENCES Especialidad(idEspecialidad),
    CONSTRAINT Fk_idHorarioE2 FOREIGN KEY (idHorario) REFERENCES Horario(idHorario)
);

-- Creación de tabla Cita
CREATE TABLE Cita (
    idCita TINYINT AUTO_INCREMENT PRIMARY KEY,
    idEspecialidadDoc TINYINT,
    idPaciente INT,
    idRecepcionista TINYINT,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    fechaDiaCita DATETIME NOT NULL,
    confirmacion BIT NOT NULL,
    pendiente BIT DEFAULT 0,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT Fk_codigoPacienteCita FOREIGN KEY (idPaciente) REFERENCES Paciente(idPaciente),
    CONSTRAINT Fk_idEspecialidadDocCt FOREIGN KEY (idEspecialidadDoc) REFERENCES EspecialidadDoctor(idEspecialidadDoc),
    CONSTRAINT Fk_Recepcionistaid FOREIGN KEY (idRecepcionista) REFERENCES Recepcionista(idRecepcionista)
);


-- Creación de tabla HistoriaClinicaGeneral
CREATE TABLE IF NOT EXISTS HistoriaClinicaGeneral (
    idHistoriaG INT AUTO_INCREMENT PRIMARY KEY,
    idPaciente INT,
    fecha DATETIME NOT NULL,
    sector VARCHAR(50) NOT NULL,
    grupoPrioritario VARCHAR(50) NOT NULL,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT Fk_codigoPacienteHG FOREIGN KEY (idPaciente) REFERENCES Paciente(idPaciente)
);


-- Creación de tabla HistoriaClinicaOdontologica
CREATE TABLE IF NOT EXISTS HistoriaClinicaOdontologica (
    idHistoriaO INT AUTO_INCREMENT PRIMARY KEY,
    idCita TINYINT,
    idHistoriaG INT,
    embarazo BIT NOT NULL,
    presionArterial CHAR(7) NOT NULL,
    temperatura CHAR(5) NOT NULL,
    frecuenciaRespiratoria CHAR(5) NOT NULL,
    frecuenciaCardiaca CHAR(5) NOT NULL,
    motivoAtencion TEXT NOT NULL,
    enfermedadActual TEXT NOT NULL,
    tomaMedicamento BIT NOT NULL,
    nombreMedicamento TEXT DEFAULT NULL,
    ihos TEXT NOT NULL,
    gingivitis BIT DEFAULT 0,
    oclusion BIT DEFAULT 0,
    tipoOclusion VARCHAR(9) NOT NULL,
    enfermedadPeriodontal BIT DEFAULT 0,
    fluorosis BIT DEFAULT 0,
    indiceCpo TINYINT NOT NULL,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT Fk_idCitaHO FOREIGN KEY (idCita) REFERENCES Cita(idCita),
    CONSTRAINT Fk_idHG FOREIGN KEY (idHistoriaG) REFERENCES HistoriaClinicaGeneral(idHistoriaG),
    CONSTRAINT chk_tipoOclusionHO CHECK (tipoOclusion IN ('Angle I', 'Angle II', 'Angle III'))
);

-- Creación de tabla Antecedente
CREATE TABLE IF NOT EXISTS Antecedente (
    idAntecedente TINYINT AUTO_INCREMENT PRIMARY KEY,
    idHistoriaO INT,
    tipo VARCHAR(10) NOT NULL,
    grupo VARCHAR(50) NOT NULL,
    antecedente TEXT NOT NULL,
    valorDescripcion TEXT NOT NULL,
    observacion TEXT DEFAULT NULL,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT Fk_idHOA FOREIGN KEY (idHistoriaO) REFERENCES HistoriaClinicaOdontologica(idHistoriaO),
    CONSTRAINT chk_tipoA CHECK (tipo IN ('Personal', 'Familiar'))
);

-- Creación de tabla NomenclaturaProcedimiento
CREATE TABLE IF NOT EXISTS NomenclaturaProcedimiento (
    codigoProcs CHAR(13),
    descripcion TEXT NOT NULL,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT Pk_codigoProcsNm PRIMARY KEY (codigoProcs)
);


-- Creación de tabla catalogoPiezaDental
CREATE TABLE IF NOT EXISTS catalogoPiezaDental (
    codigoPieza CHAR(5) NOT NULL,
    numeroDiente CHAR(2) NOT NULL,
    cuadrante VARCHAR(16) NOT NULL,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT Pk_codigoPieza PRIMARY KEY (codigoPieza)
);


-- Creación de tabla codigoCIE10
CREATE TABLE IF NOT EXISTS codigoCIE10 (
    codigoCIE CHAR(4) NOT NULL,
    descripcion TEXT NOT NULL,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT Pk_codigoCIE10 PRIMARY KEY (codigoCIE)
);

-- Creación de tabla Odontograma
CREATE TABLE IF NOT EXISTS Odontograma (
    idOdontograma INT AUTO_INCREMENT,
    idHistoriaO INT,
    codigoProcs CHAR(13),
    codigoPieza CHAR(5),
    codigoCIE CHAR(4),
    observacion TEXT DEFAULT NULL,
    procedimientosRealizados VARCHAR(13) NOT NULL,
    imagenOdontograma LONGBLOB NOT NULL,
    detalleIndicacion TEXT DEFAULT NULL,
    descripcion TEXT DEFAULT NULL,
    recomendacion TEXT DEFAULT NULL,
    fechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuarioCreacion CHAR(60) DEFAULT NULL,
    CONSTRAINT Pk_idOdontograma PRIMARY KEY (idOdontograma),
    CONSTRAINT Fk_idHOOd FOREIGN KEY (idHistoriaO) REFERENCES HistoriaClinicaOdontologica(idHistoriaO),
    CONSTRAINT Fk_codigoProcsOd FOREIGN KEY (codigoProcs) REFERENCES NomenclaturaProcedimiento(codigoProcs),
    CONSTRAINT Fk_codigoPiezaOd FOREIGN KEY (codigoPieza) REFERENCES catalogoPiezaDental(codigoPieza),
    CONSTRAINT Fk_codigoCIEOd FOREIGN KEY (codigoCIE) REFERENCES codigoCIE10(codigoCIE),
    CONSTRAINT chk_procedimientosRealizados CHECK (procedimientosRealizados IN ('Por realizar', 'Realizado'))
);