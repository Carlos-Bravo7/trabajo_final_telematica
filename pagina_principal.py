from dash import Dash, html, Input, Output, ctx, dcc, State
import pandas as pd
import os
import io

archivo = 'bd.csv'

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children= "Red social",),
    html.P(children= "Creacion y destruccion de contenedores para usuarios",),
    html.Div(dcc.Input(id='nombre', type='text',placeholder='ingrese su nombre')),
    html.Div(dcc.Input(id='puerto', type='text',placeholder='ingrese su puerto')),
    html.Div(dcc.Input(id='contraseña', type='text',placeholder='ingrese su contraseña')),
    html.Button('crear usuario', id='btn-nclicks-1', n_clicks=0),
    html.Button('cerrar sesion', id='btn-nclicks-2', n_clicks=0),
    html.Button('borrar usuario', id='btn-nclicks-3', n_clicks=0),
    html.Div(id='container-button-timestamp')
])

@app.callback(
    Output('container-button-timestamp', 'children'),
    Input('btn-nclicks-1', 'n_clicks'),
    Input('btn-nclicks-2', 'n_clicks'),
    Input('btn-nclicks-3', 'n_clicks'),
    State('nombre', 'value'),
    State('puerto', 'value'),
    State('contraseña', 'value')
)
def displayClick(btn1, btn2, btn3, nombre, puerto, contraseña):
    msg = "None of the buttons have been clicked yet"
    if "btn-nclicks-1" == ctx.triggered_id:
        comando = 'docker run -d -p'+puerto+':80 --name '+nombre+ ' trabajo_final python3.10 perfil.py carlos'
        os.system(comando)
        msg = "el contenedor se ha creado"
        
        csv = open(archivo, "a")
        linea = nombre+","+ puerto+","+ contraseña+"\n"
        csv.write(linea)
        csv.close()
    
    elif "btn-nclicks-2" == ctx.triggered_id:
        comando2 = 'docker stop '+ nombre
        os.system(comando2)
        msg = "la sesion se ha cerrado exitosamente"
    elif "btn-nclicks-3" == ctx.triggered_id:
        comando3 = 'docker rm '+ nombre
        os.system(comando3)
        msg = "ha borrado su cuenta exitosamente"
        
        a = pd.read_csv('bd.csv')
        borr = len(a)
        a.drop(borr - 1)
        
    return html.Div(msg)

if __name__ == '__main__':
    app.run_server(debug=True)

