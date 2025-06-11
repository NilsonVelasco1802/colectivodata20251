import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


############################ Asistencia ############################

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")


#Graficas
#Grafica de barras

#1
colors = ["#845ec2", "#d65db1", "#ff6f91", "#ff9671", "#ffc75f", "#f9f871"]
plt.figure(figsize=(8, 5))
sns.countplot(x='estado', data=dataFrameAsistencia, palette=colors)
plt.title('Cantidad De Registros Por Estado De Asistencia')
plt.xlabel("Estado De Asistencia")
plt.ylabel("Cantidad De Registros")
#plt.tight_layout()
#plt.savefig("./img/grafica_1.png")
#plt.show()
plt.close()


#2
plt.figure(figsize=(8, 5))
sns.countplot(x='medio_transporte', data=dataFrameAsistencia, palette=colors)
plt.title('Cantidad De Registros Por Medio De Transporte')
plt.xlabel("Medio De Transporte")
plt.ylabel("Cantidad De Registros")
#plt.tight_layout()
#plt.savefig("./img/grafica_2.png")
#plt.show()
plt.close()


#3
plt.figure(figsize=(8, 5))
sns.countplot(x='estrato', data=dataFrameAsistencia, palette=colors)
plt.title('Cantidad De Registros Por Estrato')
plt.xlabel("Estrato")
plt.ylabel("Cantidad De Registros")
#plt.tight_layout()
#plt.savefig("./img/grafica_3.png")
#plt.show()
plt.close()


#Grafica de torta

#4
conteoMedioTransporte=dataFrameAsistencia['medio_transporte'].value_counts()
plt.figure(figsize=(5,5))
plt.pie(
    conteoMedioTransporte,
    labels=conteoMedioTransporte.index,
    autopct='%1.1f%%',
    colors=sns.color_palette("Reds")
)
plt.title('Distribucion De Medio De Transporte')
#plt.tight_layout()
#plt.savefig("./img/grafica_4.png")
#plt.show()
plt.close()


#5
conteoRegistrosPorEstado=dataFrameAsistencia["estado"].value_counts()
plt.figure(figsize=(5,5))
plt.pie(
    conteoRegistrosPorEstado,
    labels=conteoRegistrosPorEstado.index,
    autopct='%1.1f%%',
    colors=sns.color_palette("Blues")
)
plt.title('Distribucion De estados')
#plt.tight_layout()
#plt.savefig("./img/grafica_5.png")
#plt.show()
plt.close()


#6
conteoEstrato=dataFrameAsistencia['estrato'].value_counts()
plt.figure(figsize=(5,5))
plt.pie(
    conteoEstrato,
    labels=conteoEstrato.index,
    autopct='%1.1f%%',
    colors=sns.color_palette("Greens")
)
plt.title('Distribucion De Estratos')
#plt.tight_layout()
#plt.savefig("./img/grafica_6.png")
#plt.show()
plt.close()




#Grafico de barras agrupadas
#se aplica cuando hice cruces en el dateframe

#7
cruceEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size().unstack(fill_value=0)
cruceEstadoMedioTransporte.plot(
    kind='bar',
    figsize=(10,6),
    color=colors
)
plt.title('Registros Por Estado De Asistencia Y Medio De Transporte')
plt.xlabel("Estado De Asistencia")
plt.ylabel("Cantidad De Registros")
plt.legend(title="Medio De Transporte")
#plt.tight_layout()
#plt.savefig("./img/grafica_7.png")
#plt.show()
plt.close()


#8
cruceEstratoPorEstado=dataFrameAsistencia.groupby(['estado','estrato']).size().unstack(fill_value=0)
cruceEstratoPorEstado.plot(
    kind='bar',
    figsize=(10,6),
    color=colors
)
plt.title('Registro de estado por asistencia')
plt.xlabel("Estado De Asistencia")
plt.ylabel("Cantidad De Registros")
plt.legend(title="Estratos")
#plt.tight_layout()
#plt.savefig("./img/grafica_8.png")
#plt.show()
plt.close()


#Grafica de lineas

#9
plt.figure()
df_fecha = dataFrameAsistencia.groupby("fecha").size()
df_fecha.plot(marker='o')
plt.title("Cantidad de registros por fecha")
plt.ylabel("Cantidad")
plt.xlabel("Fecha")
#plt.savefig("./img/grafica_9.png")
#plt.tight_layout()
#plt.show()
plt.close()


#Historiagrama
#10
plt.figure()
sns.histplot(dataFrameAsistencia["estrato"], bins=5)
plt.title("Histograma del Estrato")
plt.ylabel("Cantidad")
#plt.tight_layout()
#plt.savefig("./img/grafica_10.png")
#plt.show()
plt.close()


############################ Usuarios ############################

dataFrameUsuarios = pd.read_excel("./data/usuarios_sistema_completo.xlsx")

#Grafica de barras

#1
plt.figure(figsize=(8, 5))
sns.countplot(x='tipo_usuario', data=dataFrameUsuarios, palette=colors)
plt.title('Cantidad De Usuarios Por Tipo De Usuario')
plt.xlabel("Tipo De Usuario")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.savefig("./img/grafica_11.png")
plt.show()

#2
plt.figure(figsize=(8, 5))
sns.countplot(x='especialidad', data=dataFrameUsuarios, palette=colors)
plt.title('Cantidad De Usuarios Por Especialidad')
plt.xlabel("Especialidad")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.savefig("./img/grafica_12.png")
plt.show()


#Grafica de torta


#3
conteo_tipo_usuario = dataFrameUsuarios['tipo_usuario'].value_counts()
plt.figure(figsize=(5,5))
plt.pie(conteo_tipo_usuario, labels=conteo_tipo_usuario.index, autopct='%1.1f%%', colors=sns.color_palette("Pastel1"))
plt.title('Distribución Por Tipo De Usuario')
plt.tight_layout()
plt.savefig("./img/grafica_13.png")
plt.show()

#4
conteo_especialidad = dataFrameUsuarios['especialidad'].value_counts()
plt.figure(figsize=(5,5))
plt.pie(conteo_especialidad, labels=conteo_especialidad.index, autopct='%1.1f%%', colors=sns.color_palette("Pastel2"))
plt.title('Distribución Por Especialidad')
plt.tight_layout()
plt.savefig("./img/grafica_14.png")
plt.show()


#Barras agrupadas


#5
cruce_tipo_esp = dataFrameUsuarios.groupby(['tipo_usuario', 'especialidad']).size().unstack(fill_value=0)
cruce_tipo_esp.plot(kind='bar', figsize=(10,6), color=colors)
plt.title('Usuarios Por Tipo De Usuario Y Especialidad')
plt.xlabel("Tipo De Usuario")
plt.ylabel("Cantidad")
plt.legend(title="Especialidad")
plt.tight_layout()
plt.savefig("./img/grafica_15.png")
plt.show()


#Historiagrama

#6

from datetime import datetime
dataFrameUsuarios['fecha_nacimiento'] = pd.to_datetime(dataFrameUsuarios['fecha_nacimiento'], errors='coerce')
hoy = pd.Timestamp(datetime.today())
dataFrameUsuarios['edad'] = (hoy - dataFrameUsuarios['fecha_nacimiento']).dt.days // 365
plt.figure(figsize=(8, 5))
sns.histplot(dataFrameUsuarios['edad'].dropna(), bins=8, color="#4a47a3")
plt.title('Histograma De Edades De Usuarios')
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("./img/grafica_16.png")
plt.show()