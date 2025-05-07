import pandas as pd
dataFrameUsuarios = pd.read_excel("./data/usuarios_sistema_completo.xlsx")

#print(dataFrameUsuarios['contrasena'].unique())




#1. Solo estudiantes
soloEstudiantes=dataFrameUsuarios.query('tipo_usuario=="estudiante"')
#print(soloEstudiantes)

#2. Solo profesores
soloDocentes=dataFrameUsuarios.query('tipo_usuario=="docente"')
#print(soloDocentes)

#3. Todos excepto estudiantes
exceptoEstudiantes=dataFrameUsuarios.query('tipo_usuario != "estudiante"')
#print(exceptoEstudiantes)

#4. Filtrar por especialidad
filtrarEspecialidad=dataFrameUsuarios.query('`especialidad` == "Ingenieria de Sistemas"')
#print(filtrarEspecialidad)

#5. Excluir una especialidad
excluirEspecialidad=dataFrameUsuarios.query('`especialidad` != "Ingenieria de Sistemas"')
#print(excluirEspecialidad)

#6. Excluir administrativos
excluirAdministratios=dataFrameUsuarios.query('especialidad != "administrativo"')
#print(excluirAdministratios)

#7. Direcciones en medellin
direccionesConMedellin=dataFrameUsuarios[dataFrameUsuarios["direccion"].str.contains("medellin", case=False, na=False)]
#print(direccionesConMedellin)

#8. Direcciones terminadas en sur
terminanEnSur = dataFrameUsuarios[dataFrameUsuarios["direccion"].str.lower().str.endswith("sur", na=False)]
#print(terminanEnSur)

#9. Direcciones que inician con calle
inicianConCalle=dataFrameUsuarios[dataFrameUsuarios["direccion"].str.lower().str.startswith("calle", na=False)]
#print(inicianConCalle)

#10.Especialidades que contienen la palabra datos
contienenDatos=dataFrameUsuarios[dataFrameUsuarios["especialidad"].str.contains("datos", case=False, na=False)]
#print(contienenDatos)

#11. instructores en itagui
instructoresItagui=dataFrameUsuarios.query('tipo_usuario == "instructor" and direccion == "itagui"')
#print(instructoresItagui)

#12. nacidos despues de 2000
dataFrameUsuarios["fecha_nacimiento"] = pd.to_datetime(dataFrameUsuarios["fecha_nacimiento"], errors="coerce")
nacidosDespues2000 = dataFrameUsuarios[dataFrameUsuarios["fecha_nacimiento"].dt.year > 2000]
#print(nacidosDespues2000)

#13. nacidos en los 90
nacidosEnLos90=dataFrameUsuarios[(dataFrameUsuarios["fecha_nacimiento"].dt.year >= 1990) &
                                   (dataFrameUsuarios["fecha_nacimiento"].dt.year < 2000)]
#print(nacidosEnLos90)

#14. direcciones en envigado
direccionesEnEnvigado=dataFrameUsuarios.query('direccion == "envigado"')
#print(direccionesEnEnvigado)

#15. especialdiades que empizan por I
especialidadesI=dataFrameUsuarios[dataFrameUsuarios["especialidad"].str.startswith("I", na=False)]
#print(especialidadesI)

#16. Usuarios sin dirección
sinDireccion=dataFrameUsuarios[dataFrameUsuarios["direccion"].isna()]
#print(sinDireccion)

#17. Usuarios sin especialidad
sinEspecialidad=dataFrameUsuarios[dataFrameUsuarios["especialidad"].isna()]
#print(sinEspecialidad)

#18. profesores que viven en sabaneta
profesoresSabaneta=dataFrameUsuarios.query('tipo_usuario=="docente" and direccion=="Sabaneta"')
#print(profesoresSabaneta)

#19. aprendices que viven en bello
aprendicesBello = dataFrameUsuarios.query('tipo_usuario=="estudiante" and direccion=="Bello"')
#print(aprendicesBello)

#20. nacidos en el nuevo milenio
nuevoMilenio=dataFrameUsuarios[dataFrameUsuarios["fecha_nacimiento"].dt.year >= 2000]
#print(nuevoMilenio)


#1. total por tipo
totalPorTipo=dataFrameUsuarios["tipo_usuario"].value_counts()
#print(totalPorTipo)

#2. total por especialidad
totalPorEspecialidad=dataFrameUsuarios["especialidad"].value_counts()
#print(totalPorEspecialidad)
#3. cantidad de especialidades distintas
especialidadesUnicas=dataFrameUsuarios["especialidad"].nunique()
#print(especialidadesUnicas)

#4. tipos de usuario por especialidad
tiposPorEspecialidad=dataFrameUsuarios.groupby("especialidad")["tipo_usuario"].nunique()
#print(totalPorEspecialidad)

#5. usuario mas antiguo por tipo
usuarioMasAntiguo=dataFrameUsuarios.sort_values("fecha_nacimiento").groupby("tipo_usuario").first()
#print(usuarioMasAntiguo)

#6. usuario mas joven por tipo
usuarioMasJoven=dataFrameUsuarios.sort_values("fecha_nacimiento", ascending=False).groupby("tipo_usuario").first()
#print(usuarioMasJoven)

#7. primer registro por tipo
primerRegistro=dataFrameUsuarios.sort_values("id").groupby("tipo_usuario").first()
#print(primerRegistro)

#8. ultimo registro por tipo
ultimoRegistro=dataFrameUsuarios.sort_values("id", ascending=False).groupby("tipo_usuario").first()
#print(ultimoRegistro)

#9. combinacion tipo por especialidad
combinacionTipoEspecialidad=dataFrameUsuarios.groupby(["tipo_usuario", "especialidad"]).size().reset_index(name="conteo")
#print(combinacionTipoEspecialidad)

#10. el mas viejo por especialidad

dataFrameUsuarios["fecha_nacimiento"] = pd.to_datetime(
    dataFrameUsuarios["fecha_nacimiento"], errors="coerce"
)
usuariosConFecha = dataFrameUsuarios[dataFrameUsuarios["fecha_nacimiento"].notna()]
masViejoPorEspecialidad = (
    usuariosConFecha
    .sort_values("fecha_nacimiento")
    .groupby("especialidad")
    .first()
)
#print(masViejoPorEspecialidad)

#11. cuantos de cada especialidad por tipo
conteoEspecialidadPorTipo = dataFrameUsuarios.groupby(["tipo_usuario", "especialidad"]).size().unstack(fill_value=0)
#print(conteoEspecialidadPorTipo)

#12. edad promedio por tipo
dataFrameUsuarios["edad"] = pd.Timestamp.today().year - dataFrameUsuarios["fecha_nacimiento"].dt.year
edadPromedioPorTipo = dataFrameUsuarios.groupby("tipo_usuario")["edad"].mean()
#print(edadPromedioPorTipo)

#13. años de nacimeinto mas frecuente por especialidad
dataFrameUsuarios["anio"] = dataFrameUsuarios["fecha_nacimiento"].dt.year

anioNacimientoMasFrecuente = dataFrameUsuarios.groupby("especialidad")["anio"].agg(
    lambda x: x.mode().iloc[0] if not x.mode().empty else None
)
print(anioNacimientoMasFrecuente)

#14. mes de nacimiento mas frecuente por tipo
mesNacimientoFrecuente = (
    dataFrameUsuarios.assign(mes=dataFrameUsuarios["fecha_nacimiento"].dt.month)
    .groupby("tipo_usuario")["mes"]
    .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
)
#print(mesNacimientoFrecuente)

#15. UNA CONSULTA O FILTRO QUE UD PROPONGA
filtroPropuesto = dataFrameUsuarios[
    (dataFrameUsuarios["tipo_usuario"] == "docente") &
    (dataFrameUsuarios["especialidad"].str.contains("datos", case=False, na=False)) &
    (dataFrameUsuarios["fecha_nacimiento"].dt.year > 2000)
]
#print(filtroPropuesto)
