from Consulta.extraer import extraer
from Insercion.persistir import persistir
from transformacion.tranformacion1 import trans
# tables = [ 
#           'antecedente',
#           'catalogopiezadental',
#           'cita',
#           'codigocie10',
#           'contactoemergencia',
#           'diagnostico',
#           'doctor',
#           'especialidad',
#           'especialidaddoctor',
#           'historiaclinicageneral',
#           'historiaclinicaodontologica',
#           'horario',
#           'nomenclaturaprocedimiento',
#           'nominadoctor',
#           'paciente',
#           'recepcionista'
#         ]

# # tables = ['codigocie10']

# for table in tables:
#     n = extraer(table)
#     persistir(n, table) 
    
trans()