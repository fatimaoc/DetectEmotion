import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from sklearn import preprocessing
from sklearn import decomposition
from sklearn.decomposition import PCA
import numpy as np # algèbre linéaire
import pandas as pd
import plotly.graph_objs as go

df_total=pd.read_csv('Emotion_final.csv')
nb_data = 50
n_comp = 8


nav_menu = dbc.Nav(
    [
        dbc.NavLink(style={'color':'#DCDCDC'},children=["Home "], active=True, href="/"),
        dbc.NavLink(style={'color':'#DCDCDC'},children=["Raw Data Analysis"], href="/apps/app1"),
        dbc.NavLink(style={'color':'#DCDCDC'},children=["Sentiment Analysis NLP"], href="/apps/app2"),
        
    ]
)




layout = html.Div(style={'backgroundColor':'#5b5857', 'padding-top':'2vh', 'padding-botton':'4vh'},children=[
 nav_menu,

  html.H1(style={'text-align': 'center', 'color':'#DCDCDC', 'margin-top':'2vh', 'margin-bottom':'3vh'} , children=[ "Résultats de classification issus du premier jeu de donnée"]),
  html.Section(style={},children=[
    html.Article(style={'display':'flex', 'justify-content':'space-around', 'margin-top':'9vh', 'margin-bottom':'8vh'},children=[
      html.Div(style={'height':'40vh','width':'23vw'},children=[
        html.P(style={'text-align': 'center', 'color':'#DCDCDC',},children=['Cercle des corrélations F1 et F2']),
        html.Img(src=app.get_asset_url('../assets/F1.png'), style={'height':'40vh', 'width':'23vw'})
      ]),
      html.Div(style={'height':'40vh','width':'23vw'},children=[
        html.P(style={'text-align': 'center', 'color':'#DCDCDC',},children=['Cercle des corrélations F3 et F4']),
        html.Img(src=app.get_asset_url('../assets/F3-F4.png'), style={'height':'40vh', 'width':'23vw'})
      ]),
      html.Div(style={'height':'40vh','width':'23vw'},children=[
        html.P(style={'text-align': 'center', 'color':'#DCDCDC',},children=['Cercle des corrélations F5 et F6']),
        html.Img(src=app.get_asset_url('../assets/F5-F6.png'), style={'height':'40vh', 'width':'23vw'})
      ]),
      html.Div(style={'height':'40vh','width':'23vw',},children=[
        html.P(style={'text-align': 'center', 'color':'#DCDCDC',},children=['Cercle des corrélations F7 et F8']),
        html.Img(src=app.get_asset_url('../assets/F7-F8.png'), style={'height':'40vh', 'width':'23vw'})
      ]),
    ]),
    html.H2(style={'text-align': 'center', 'color':'#DCDCDC', 'margin-top':'10vh', 'margin-bottom':'3vh'} , children=["Eboulis des valeurs propres"]),
    html.Article(style={},children=[
      html.Div(style={'height':'70vh', 'width':'62vw', 'margin-top':'10vh'},children=[
        dcc.Graph(
        
        
    ),
      
         
      ]),
      html.Div(style={}, children=[
        
      ])
    ])
   ])
  
   
])

