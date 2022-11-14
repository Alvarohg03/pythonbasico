print('practica')
#muestra un grafico
#de uso de metros cubicos y de numero de clientes
import pandas as pd
import matplotlib.pyplot as plt
def archivo():
    datos = pd.read_csv("C:\\Users\\Tecnicos\\Desktop\\Servei_d_aigua_-usos_i_nombre_de_clients-.csv")
    df = datos[["Ús", "any_", "m3_registrats", "núm_clients"]]

    df = datos.rename(columns={
        "m3_registrats": "METROS3",
        "núm_clients": "CLIENTES"
    })
    m3_por_uso = df.groupby("METROS3")["m3_registrats"].mean()
    m3_por_uso.head(10).plot.barh()
    plt.show()


archivo()