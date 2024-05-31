import dash
from dash import dcc
from dash import html
import plotly.express as px
from dataloader import get_traffic_data_by_date
import pandas as pd

def create_scatterbox(date_string):
    df = get_traffic_data_by_date(date_string)
    fig = px.scatter_mapbox(df, lat = "latitude", 
                            lon = "longitude",
                            color= "cluster",
                            animation_frame= "timestamp",
                            mapbox_style ="carto-darkmatter")
    return fig

data = {
    'latitude': [1.290270, 1.350000, 1.400000],
    'longitude': [103.851959, 103.800000, 103.900000]
}
df = pd.DataFrame(data)

def create_scatterbox1(date):
    fig = px.scatter_mapbox(
        df, lat="latitude", lon="longitude",
        mapbox_style="carto-positron"
    )
    return fig


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, use_pages=True , external_stylesheets=external_stylesheets, assets_folder='assets')
server = app.server

app.config.suppress_callback_exceptions = True

dash_text = '''

This is an example of a DSC dasshboard.
'''

app.layout = html.Div(children=[
    html.H1(
        children=[
            html.P(
                id='instructions',
                children=dash_text),

            ]
    ),
    dcc.Graph(
        id='example-graph',
        figure=create_scatterbox("2024-04-16")
    ),
    ])



if __name__ == "__main__":
    app.run(debug=True)
    #app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=False) 