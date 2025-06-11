import pandas as pd

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")


#ANTES DE FILTRAR COMO ANALISTAS DE DATOS DEBES CONOCER (EXPLORAR LA FUENTE PRIMARIA)
#print(dataFrameAsistencia['estado'].unique())
#print(dataFrameAsistencia['estrato'].unique())
#print(dataFrameAsistencia['medio_transporte'].unique())


#FILTROS Y CONDICIONES PARA TRANSOFRMAR DATOS
#1. Reportar todos los estudiantes que asistieron
estudiantesQueAsistieron=dataFrameAsistencia.query('estado=="asistio"')
#print(estudiantesQueAsistieron)

#2. Reportar todos los estudiantes que faltaron
estudiantesQueFaltaron=dataFrameAsistencia.query('estado == "inasistencia"')
#print(estudiantesQueFaltaron)

#3. Reportar todos los estudiantes que llegaron tarde(Justificado)
estudiantesQueFaltaronJustificado=dataFrameAsistencia.query('estado=="justificado"')
#print(estudiantesQueFaltaronJustificado)

#4. Reportar todos los estudiantes de estrato 1
estudiantesEstratoUno=dataFrameAsistencia.query('estrato==1')
#print(estudiantesEstratoUno)

#5. Reportar todos los estudiantes de estratos altos
estudiantesEstratoAlto=dataFrameAsistencia.query('estrato >= 4')
#print(estudiantesEstratoAlto)


#6. Reportar todos los estudaintes que llegan en metro
estudiantesQueUsanMetro=dataFrameAsistencia.query('medio_transporte=="metro"')
#print(estudiantesQueUsanMetro)

#7. Reportar todos los estudaintes que llegan en bicicleta
estudiantesQueUsanBicicleta=dataFrameAsistencia.query('medio_transporte=="bicicleta"')
#print(estudiantesQueUsanBicicleta)

#8. Reportar todos los estudiantes que no caminan para llegar a la u
estudiantesQueNoCaminan=dataFrameAsistencia.query('medio_transporte!="a pie"')
#print(estudiantesQueNoCaminan)

#9. Reportar todos los registros de asistencia del mes de junio

#fechas_invalidas = dataFrameAsistencia[~pd.to_datetime(dataFrameAsistencia["fecha"], errors="coerce").notna()]
#print(fechas_invalidas)

dataFrameAsistencia["fecha"] = pd.to_datetime(dataFrameAsistencia["fecha"])
dataFrameAsistencia["mes"] = dataFrameAsistencia["fecha"].dt.month
asistenciasJunio = dataFrameAsistencia.query("mes == 6 and estado == 'asistio'")
#print(asistenciasJunio)

#10. Reportar los estudaintes que faltaron y usan bus para llegar a la u
estudiantesQueFaltanUsanBus=dataFrameAsistencia.query('medio_transporte=="bus" and estado=="inasistencia"')
#print(estudiantesQueFaltanUsanBus)

#11. Reportar estudiantes que usan bus y son de estratos altos
estudiantesQueUsanBusEstratoAlto=dataFrameAsistencia.query('medio_transporte=="bus" and estrato >=4')
#print(estudiantesQueUsanBusEstratoAlto)

#12. Reportar estudiantes que usan bus y son de estratos bajos
estudiantesQueUsanBusEstratoBajo=dataFrameAsistencia.query('medio_transporte=="bus" and estrato <=3')
#print(estudiantesQueUsanBusEstratoBajo)

#13. Reportar estudiantes que llegan tarde y son de estrato 3,4,5 o 6
estudiantesQueLleganTardeEstarto3456=dataFrameAsistencia.query('estado=="justificado" and estrato >=3')
#print(estudiantesQueLleganTardeEstarto3456)

#14. Reportar estudiantes que usan transportes ecologicos 
estudiantesQueUsanTransporteEcologico=dataFrameAsistencia.query('medio_transporte in ["metro", "bicicleta", "a pie"]')
#print(estudiantesQueUsanTransporteEcologico)

#15. Reportar estudiantes que faltan y usan carro para transportarse
estudiantesQueFaltanUsanCarro=dataFrameAsistencia.query('estado=="inasistencia" and medio_transporte=="carro"')
#print(estudiantesQueFaltanUsanCarro)

#16. Reportar estudiantes que asisten son estratos altos y caminan
estudiantesQueAsistieronEstratosAltosApie=dataFrameAsistencia.query('medio_transporte=="a pie" and estrato >=4 and estado=="asistio"')
#print(estudiantesQueAsistieronEstratosAltosApie)

#17. Reportar estudiantes que son estratos bajos y justifican su iniasistencia
estudiantesEstratoBajoJustificados=dataFrameAsistencia.query('estado=="justificado" and estrato <=3')
#print(estudiantesEstratoBajoJustificados)

#18. Reportar estudiantes que son estratos altos y justifican su iniasistencia
estudiantesEstratoAltoJustificados=dataFrameAsistencia.query('estado=="justificado" and estrato >=4')
#print(estudiantesEstratoAltoJustificados)

#19. Reportar estudiantes que usan carro y justifican su inasistencia
estudiantesQueUsanCarroJustificados=dataFrameAsistencia.query('estado=="justificado" and medio_transporte=="carro"')
#print(estudiantesQueUsanCarroJustificados)

#20. Reportar estudiantes que faltan y usan metro y son estratos medios
estudiantesQueUsanMetroFaltanEstartoMedio=dataFrameAsistencia.query('estado=="inasistencia" and medio_transporte=="metro" and estrato >=3 and estrato <=4')
#print(estudiantesQueUsanMetroFaltanEstartoMedio)


#########################################################################################################################################################

#AGRUPACIONES Y CONTEOS SOBRE LOS DATOS
#1. Contar cada registro de asistencia por cada estado
conteoRegistrosPorEstado=dataFrameAsistencia.groupby('estado').size().reset_index(name="cantidad_estudiantes")
#print(conteoRegistrosPorEstado)

#2. Numero de registros por estrato
conteoRegistrosPorEstrato=dataFrameAsistencia.groupby('estrato').size().reset_index(name="cantidad_estudiantes")
#print(conteoRegistrosPorEstrato)

#3. Cantidad de estudiantes por medio de transporte
cantidadDeEstudiantesTransporte=dataFrameAsistencia.groupby("medio_transporte")["id_estudiante"].nunique().reset_index(name="cantidad_estudiantes")
#print(cantidadDeEstudiantesTransporte)

#4. Cantidad de registros por grupo
cantidadDeResgistrosPorGrupo=dataFrameAsistencia.groupby("id_grupo").size().reset_index(name="cantidad_registros")
#print(cantidadDeResgistrosPorGrupo)

#5. Cruce entre estado y medio de transporte
cruceEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size().reset_index(name="cantidad_estudiantes")
#print(cruceEstadoMedioTransporte)

#6. Promedio de estrato por estado de asistencia
promedioEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].mean()
#print(promedioEstratoPorEstado)

#7. Estrato promedio por medio de transporte
estartoPromedioPorTransporte=dataFrameAsistencia.groupby("medio_transporte")["estrato"].mean().reset_index(name="estrato_promedio")
#print(estartoPromedioPorTransporte)

#8. Maximo estrato por estado de asistencia
estratoMaximoPorAsistencia=dataFrameAsistencia.groupby("estado")["estrato"].max().reset_index(name="estrato_maximo")
#print(estratoMaximoPorAsistencia)

#9. Minimo estrato por estado de asistencia
estratoMinimoPorAsistencia=dataFrameAsistencia.groupby("estado")["estrato"].min().reset_index(name="estrato_minimo")
#print(estratoMinimoPorAsistencia)

#10.Conteo de asistencias por grupo y por estado
conteoAsistenciasPorGrupoEstado =dataFrameAsistencia.groupby(["id_grupo", "estado"]).size().reset_index(name="cantidad")
#print(conteoAsistenciasPorGrupoEstado)

#11. Transporte usado por cada grupo
trasporteUsadoPorGrupo=dataFrameAsistencia.groupby(["id_grupo","medio_transporte"]).size().reset_index(name="cantidad_personas")
#print(trasporteUsadoPorGrupo)

#12. cuantos grupos distintos registraron asistencia por fecha
asistenciaPorFechaGruposDistintos=dataFrameAsistencia.groupby("fecha")["id_grupo"].nunique().reset_index(name="grupos_distintos")
#print(asistenciaPorFechaGruposDistintos)

#13. Promedio de estrato por fecha
promedioEstratoPorFecha=dataFrameAsistencia.groupby("fecha")["estrato"].mean().reset_index(name="promedio_estarto")
#print(promedioEstratoPorFecha)

#14. Numero de tipos de estado por transporte
numeroTipoEstadoPorTransporte=dataFrameAsistencia.groupby("medio_transporte")["estado"].nunique().reset_index(name="tipos_estado")
#print(numeroTipoEstadoPorTransporte)

#15. Primer Registro de cada grupo
primerRegistroPorGrupo=dataFrameAsistencia.groupby("id_grupo").first().reset_index()
#print(primerRegistroPorGrupo)
