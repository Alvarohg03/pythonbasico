#Actividad 14
#fuente de datos(3):
#1.archivos(txt,csv...)
#2 bases de datos (sql: postgress,/nosql : mongodb)
#3. webservices, API Rest : Peticion get : response sml / json
import pandas as pd
import matplotlib.pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def cargar_archvivo():
    datos = pd.read_csv("C:\\Users\\Tecnicos\\Desktop\\casasboston.csv")
    # datos = datos[["RM","CRIM", "MEDV", "TOWN", "CHAS", "INDUS", "LSTAT"]]
    df = datos[["RM", "CRIM", "MEDV", "TOWN", "CHAS"]]

    df = datos.rename(columns={
        "TOWN": "CIUDAD",
        "CRIM": "INDICE_CRIMEN",
        "INDUS": "PCT_ZONA_INDUSTRIAL",
        "CHAS": "RIO_CHARLES",
        "RM": "N_HABITACIONES_MEDIO",
        "MEDV": "VALOR_MEDIANO",
        "LSTAT": "PCT_CLASE_BAJA"
    })

    #print(df.sample(5))
    #Histograma
    df.N_HABITACIONES_MEDIO.plot.hist()
    plt.show()

    #Grafico de dispersion
    df.plot.scatter(x="INDICE_CRIMEN", y="VALOR_MEDIANO", alpha=0.8)
    plt.show()

    #Grafico de barras
    valor_por_ciudad = df.groupby("CIUDAD")["VALOR_MEDIANO"].mean()
    valor_por_ciudad.head(10).plot.barh()
    plt.show()

    #Grafico de cajas
    df["VALOR_CUANTILES"] = pd.qcut(df.VALOR_MEDIANO, 5)
    df.boxplot(column="INDICE_CRIMEN", by="VALOR_CUANTILES",
               figsize=(8, 6))
    plt.show()

    #Grafico circular
    df.RIO_CHARLES.value_counts().plot.pie()
    plt.show()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

cargar_archvivo()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/



