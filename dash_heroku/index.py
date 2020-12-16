import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2, app3, dashbord
import dash_bootstrap_components as dbc

nav_menu = dbc.Nav( [
        dbc.NavLink("Home", active=True, href="/"),
        #dbc.NavLink("Page 2", href="/apps/app2"),
        dbc.NavLink("Page 1", href="/apps/app1"),
        dbc.NavLink("Disabled", disabled=True, href="#"),
    ]
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    #elif pathname == '/apps/app2':
        #return app2.layout
    elif pathname == '/app3':
        return app3.layout
    elif pathname == '/':
        return dashbord.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)


    