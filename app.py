import dash
from dash import dcc
from dash import html

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
    )
    ])



if __name__ == "__main__":
    app.run(debug=True)
    #app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=False) 