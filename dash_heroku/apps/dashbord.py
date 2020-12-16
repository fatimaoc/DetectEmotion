import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import dash_bootstrap_components as dbc
from app import app
import numpy as np
import plotly.graph_objs as go

nav_menu = dbc.Nav(
    [
        dbc.NavLink("Home ", active=True, href="/"),
        dbc.NavLink("Raw Data Analysis", href="/apps/app1"),
        dbc.NavLink("Sentiment Analysis NLP", href="/apps/app2")
                
    ]
)

layout = html.Div([
    html.Br(),
    nav_menu,
    html.Br(),
    html.Br(),
    html.H1(style={'text-align': 'center','color':'black'} , children=["DASHBOARD ANALYSE NLP ROUE DES EMOTIONS"]),
    html.H2(style={'text-align': 'center','color':'black'} , children=["brief de fin de bloc "]),
    html.H6(style={'text-align': 'center','color':'black'} , children=["Décembre 2020 Fatima MOUSSAOUI"]),
    html.Br(),
    html.Br(),
    html.H2(style={'text-align': 'left','color':'black'} , children=["Contexte :"]),
    html.P(style={'margin':'auto','text-align': 'left','color':'black'} , children=['''\
    Construit d’après les travaux du psychologue américain Robert Plutchik,\
    la roue des émotions est un modèle des émotions humaines et peut facilement servir à définir\ 
    des personnages, ainsi que leur évolution dans une trame narrative. Est-il possible\
    d'identifier des émotions dans des phrases narratives issues de communications écrites ?''']),
    html.Br(),
    html.Br(),
    
         
    html.Section(style={'display':'flex'}, children=[
    
    html.Img(style={'display':'block','margin':'auto','height':'400px','border-radius':'50%','border': '2px solid  #45b39d'},id='image_roue', src=app.get_asset_url('roue.png')),])
    

     
   
                    
    ]),    
    
  

