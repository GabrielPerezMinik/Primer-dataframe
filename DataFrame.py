import pandas as pd
import matplotlib.pyplot as plt

# Creación del DataFrame con datos de estudiantes
dataframe_estudiante = {
    "Nombre": ["Ruben", "Andres", "Carlos", "Marc", "Ana"],
    "Edad": [20, 22, 21, 19, 23],
    "Nota": [5, 9.0, 7.5, 8.0, 2]
}

df_estudiantes = pd.DataFrame(dataframe_estudiante)
print(df_estudiantes)

# Añadir columna 'Aprobado' al DataFrame
df_estudiantes["Aprobado"] = df_estudiantes["Nota"] >= 5
print(df_estudiantes)

# Filtrar estudiantes que han aprobado (Nota >= 5)
estudiantes_aprobados = df_estudiantes[df_estudiantes["Aprobado"]]
print(estudiantes_aprobados)

# Calcular el promedio de las notas globales
promedio = df_estudiantes["Nota"].mean()
print("Promedio general " + str(promedio))

# Calcular el promedio de las notas (Nota >= 5)
promedioAprobado = estudiantes_aprobados["Nota"].mean()
print("Promedio de la gente aprobada " + str(promedioAprobado))

# Gráfico de barras de las notas
plt.figure(figsize=(10, 6))
plt.bar(df_estudiantes["Nombre"], df_estudiantes["Nota"], color="skyblue")
plt.axhline(y=df_estudiantes["Nota"].mean(), color='r', linestyle='--', label="Promedio de Notas")
plt.xlabel("Nombre")
plt.ylabel("Nota")
plt.title("Notas de Estudiantes")
plt.legend()
plt.show()

# Gráfico circular de aprobados y no aprobados
aprobados_count = df_estudiantes["Aprobado"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(aprobados_count, labels=["Aprobado", "No Aprobado"], autopct="%1.1f%%", startangle=140, colors=["green", "lightcoral"])
plt.title("Porcentaje de Estudiantes Aprobados vs No Aprobados")
plt.show()
