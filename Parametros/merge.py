sql_sentence = [
        """
            INSERT INTO dim_paciente (idPaciente, tipoIdendificacion, numeroIdentificacion, nombre, apellido, ciudad, direccion, fechaNacimiento, alergia, sexo, grupoSanguineo)
            SELECT ext_pa.idPaciente, ext_pa.tipoIdendificacion, ext_pa.numeroIdentificacion, ext_pa.nombre, ext_pa.apellido, ext_pa.ciudad, ext_pa.direccion, ext_pa.fechaNacimiento, ext_pa.alergia, ext_pa.sexo, ext_pa.grupoSanguineo
            FROM temporal AS ext_pa
            ON DUPLICATE KEY UPDATE
            tipoIdendificacion = ext_pa.tipoIdendificacion,
            numeroIdentificacion = ext_pa.numeroIdentificacion,
            nombre = ext_pa.nombre,
            apellido = ext_pa.apellido,
            ciudad = ext_pa.ciudad,
            direccion = ext_pa.direccion,
            fechaNacimiento = ext_pa.fechaNacimiento,
            alergia = ext_pa.alergia,
            sexo = ext_pa.sexo,
            grupoSanguineo = ext_pa.grupoSanguineo;
        """
        ,
        """        
            INSERT INTO dim_doctor (idDoctor, cedula, nombre, apellido)
            SELECT ext_pa.idDoctor, ext_pa.cedula, ext_pa.nombre, ext_pa.apellido
            FROM temporal AS ext_pa
            ON DUPLICATE KEY UPDATE
            cedula = ext_pa.cedula,
            nombre = ext_pa.nombre,
            apellido = ext_pa.apellido;
        """
        ,
        """ 
            INSERT INTO dim_especialidad (idEspecialidad, nombreEspecialidad)
            SELECT ext_pa.idEspecialidad, ext_pa.nombreEspecialidad
            FROM temporal AS ext_pa
            ON DUPLICATE KEY UPDATE
            nombreEspecialidad = ext_pa.nombreEspecialidad;
        """
        ,
        """ 
            INSERT INTO dim_horario (idHorario, dia, horaInicio, horaFin)
            SELECT ext_pa.idHorario, ext_pa.dia, ext_pa.horaInicio, ext_pa.horaFin
            FROM temporal AS ext_pa
            ON DUPLICATE KEY UPDATE
            dia = ext_pa.dia,
            horaInicio = ext_pa.horaInicio,
            horaFin = ext_pa.horaFin;
        """
        ,
        """
            INSERT INTO dim_especialidaddoctor (idEspecialidadDoc, idEspecialidad, idDoctor, idHorario)
            SELECT ext_pa.idEspecialidadDoc, ext_pa.idEspecialidad, ext_pa.idDoctor, ext_pa.idHorario
            FROM temporal AS ext_pa
            ON DUPLICATE KEY UPDATE
            idEspecialidad = ext_pa.idEspecialidad,
            idDoctor = ext_pa.idDoctor,
            idHorario = ext_pa.idHorario;
        """
        ,
        """
            INSERT INTO dim_nominadoctor (idNomina, idEspecialidad, idDoctor, idHorario, monto, fechaInicio, fechaFin)
            SELECT ext_pa.idNomina, ext_pa.idEspecialidad, ext_pa.idDoctor, ext_pa.idHorario, ext_pa.monto, ext_pa.fechaInicio, ext_pa.fechaFin
            FROM temporal AS ext_pa
            ON DUPLICATE KEY UPDATE
            idEspecialidad = ext_pa.idEspecialidad,
            idDoctor = ext_pa.idDoctor,
            idHorario = ext_pa.idHorario,
            monto = ext_pa.monto,
            fechaInicio = ext_pa.fechaInicio,
            fechaFin = ext_pa.fechaFin;
        """
        ,
        """
            INSERT INTO dim_nomenclaturaprocedimiento (codigoProcs, descripcion)
            SELECT ext_pa.codigoProcs, ext_pa.descripcion
            FROM temporal AS ext_pa
            ON DUPLICATE KEY UPDATE
            codigoProcs = ext_pa.codigoProcs,
            descripcion = ext_pa.descripcion;
        """
        
        ,
        """
            INSERT INTO dim_catalogopiezadental (codigoPieza, numeroDiente, cuadrante)
            SELECT ext_pa.codigoPieza, ext_pa.numeroDiente, ext_pa.cuadrante
            FROM temporal AS ext_pa
            ON DUPLICATE KEY UPDATE
            numeroDiente = ext_pa.numeroDiente,
            cuadrante = ext_pa.cuadrante;
        """
        ,
        """
            INSERT INTO dim_codigocie10 (codigoCIE, descripcion)
            SELECT ext_pa.codigoCIE, ext_pa.descripcion
            FROM temporal AS ext_pa
            ON DUPLICATE KEY UPDATE
            descripcion = ext_pa.descripcion;
        """
        ,
        """
            INSERT INTO fact_cita (idCita, idEspecialidadDoc, idPaciente, fecha, fechaDiaCita, confirmacion, pendiente)
            SELECT ext_pa.idCita, ext_pa.idEspecialidadDoc, ext_pa.idPaciente, ext_pa.fecha, ext_pa.fechaDiaCita, ext_pa.confirmacion, ext_pa.pendiente
            FROM temporal AS ext_pa
            ON DUPLICATE KEY UPDATE
            idEspecialidadDoc = ext_pa.idEspecialidadDoc,
            idPaciente = ext_pa.idPaciente,
            fecha = ext_pa.fecha,
            fechaDiaCita = ext_pa.fechaDiaCita,
            confirmacion = ext_pa.confirmacion,
            pendiente = ext_pa.pendiente;
        """
        ,
        """
            INSERT INTO dim_historiaclinicageneral (idHistoriaG, idPaciente, grupoPrioritario)
            SELECT ext_pa.idHistoriaG, ext_pa.idPaciente, ext_pa.grupoPrioritario
            FROM temporal AS ext_pa
            ON DUPLICATE KEY UPDATE
            idPaciente = ext_pa.idPaciente,
            grupoPrioritario = ext_pa.grupoPrioritario;
        """
        ,
        """
            INSERT INTO dim_historiaclinicaodontologica (idHistoriaO, idHistoriaG, motivoAtencion)
            SELECT ext_pa.idHistoriaO, ext_pa.idHistoriaG, ext_pa.motivoAtencion
            FROM temporal AS ext_pa
            ON DUPLICATE KEY UPDATE
            idHistoriaO = ext_pa.idHistoriaO,
            idHistoriaG = ext_pa.idHistoriaG,
            motivoAtencion = ext_pa.motivoAtencion;
        """
        ,
        """
            INSERT INTO dim_diagnostico (idDiagnostico, idHistoriaO, codigoProcs, codigoPieza, codigoCIE, observacion)
            SELECT ext_pa.idDiagnostico, ext_pa.idHistoriaO, ext_pa.codigoProcs, ext_pa.codigoPieza, ext_pa.codigoCIE, ext_pa.observacion
            FROM temporal AS ext_pa
            ON DUPLICATE KEY UPDATE
            idHistoriaO = ext_pa.idHistoriaO,
            codigoProcs = ext_pa.codigoProcs,
            codigoPieza = ext_pa.codigoPieza,
            codigoCIE = ext_pa.codigoCIE,
            observacion = ext_pa.observacion;
        """
]

temporal = ["SELECT idPaciente, tipoIdendificacion, numeroIdentificacion, nombre, apellido, ciudad, direccion, fechaNacimiento, alergia, sexo, grupoSanguineo FROM ext_paciente",
            "SELECT idDoctor, cedula, nombre, apellido FROM ext_doctor",
            "SELECT idEspecialidad, nombreEspecialidad FROM ext_especialidad",
            "SELECT idHorario, dia, horaInicio, horaFin FROM ext_horario",
            "SELECT idEspecialidadDoc, idEspecialidad, idDoctor, idHorario FROM ext_especialidaddoctor",
            "SELECT idNomina, idEspecialidad, idDoctor, idHorario, monto, fechaInicio, fechaFin FROM ext_nominadoctor",
            "SELECT codigoProcs, descripcion FROM ext_nomenclaturaprocedimiento",
            "SELECT codigoPieza, numeroDiente, cuadrante FROM ext_catalogopiezadental",
            "SELECT codigoCIE, descripcion FROM ext_codigocie10",
            "SELECT idCita, idEspecialidadDoc, idPaciente, fecha, fechaDiaCita, confirmacion, pendiente FROM ext_cita",
            "SELECT idHistoriaG, idPaciente, grupoPrioritario FROM ext_historiaclinicageneral",
            "SELECT idHistoriaO, idHistoriaG, motivoAtencion FROM ext_historiaclinicaodontologica",
            "SELECT idDiagnostico, idHistoriaO, codigoProcs, codigoPieza, codigoCIE, observacion FROM ext_diagnostico"
            ]