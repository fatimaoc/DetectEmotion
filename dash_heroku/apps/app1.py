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
'''def display_scree_plot(pca):
    scree = pca.explained_variance_ratio_*100
    plt.bar(np.arange(len(scree))+1, scree)
    plt.plot(np.arange(len(scree))+1, scree.cumsum(),c="red",marker='o')
    plt.xlabel("rang de l'axe d'inertie")
    plt.ylabel("pourcentage d'inertie")
    plt.title("Eboulis des valeurs propres")
    plt.show(block=False)

dfs = df_total[df_total.year==2016].iloc[:nb_data,:]
dfs = dfs.dropna()
dfs.world_rank = [each.replace('=','') for each in dfs.world_rank]
dfs.world_rank = pd.to_numeric(dfs.world_rank, errors='coerce')
dfs.income = pd.to_numeric(dfs.income, errors='coerce')
dfs.international = pd.to_numeric(dfs.international, errors='coerce')
dfs.total_score = pd.to_numeric(dfs.total_score, errors='coerce')
dfs.num_students = [str(each).replace(',','') for each in dfs.num_students]
dfs.international_students = [each.replace('%','') for each in dfs.international_students]
dfs.female_male_ratio = [str(each).split() for each in dfs.female_male_ratio]
dfs.female_male_ratio = [round((float(each[0]) / float(each[2])),2)*100 for each in dfs.female_male_ratio]
dfs.female_male_ratio = pd.to_numeric(dfs.female_male_ratio, errors='coerce')

colonnes = ['world_rank', 'total_score', 'research', 'teaching', 'citations', 'international', 'income', 'student_staff_ratio']
data_pca = dfs[colonnes]

X_ = data_pca.values
names = dfs['world_rank']
features = colonnes
X_scaled = preprocessing.StandardScaler().fit_transform(X_)
pca = decomposition.PCA(n_components=n_comp)
pca.fit(X_scaled)
# Eboulis des valeurs propres : plot avec plotly
scree = pca.explained_variance_ratio_*100
fig2_1 = go.Figure()
fig2_1.add_trace(go.Scatter(x = np.arange(len(scree))+1, 
                            y = scree.cumsum(), 
                            mode = 'lines+markers',
                            name = 'Inertie cumulée',
                            hovertemplate = "<b>Pourcentage :</b> %{y} %<br>"
                            + "<extra></extra>"))
              
fig2_1.add_trace(go.Bar(x = np.arange(len(scree))+1, 
                        y = scree,
                        name = 'Inertie par composante',
                        hovertemplate = "<b>Composante :</b> %{x}<br>" 
                            + "<b>Pourcentage :</b> %{y} %<br>"
                            + "<extra></extra>"))
fig2_1.update_layout(title="Eboulis des valeurs propres",
                     xaxis_title="Composantes",
                     yaxis_title="Inertie (%)",
                     plot_bgcolor='#1F2024' ,
                     paper_bgcolor='#1F2024',
                     font_color='#DCDCDC',
                     )'''

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

