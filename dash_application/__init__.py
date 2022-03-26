#creating the graph 
#%%
import dash
from dash import html
from flask_login.utils import login_required

from pathlib import Path
from email.utils import decode_rfc2231
import json
from urllib.request import urlopen
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from matplotlib.pyplot import show
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from urllib import response
from datetime import datetime
from dash import Input, Output

from dash_application import data_requests

df_kpi1 = pd.DataFrame(data_requests.get_kpi1()["items"])
df_kpi2 = pd.DataFrame(data_requests.get_kpi2()["items"])
df_kpi3 = pd.DataFrame(data_requests.get_kpi3()["items"])
df_kpi4= pd.DataFrame(data_requests.get_kpi4()["items"])
df_kpi5= pd.DataFrame(data_requests.get_kpi5()["items"])
df_kpi6= pd.DataFrame(data_requests.get_kpi6()["items"])


def create_kpi1():
    return html.Div([
                html.H1(children=["KPI 1 - INC raised by month"]),
                html.Div(
                    children=["""
                Volume of incidences raised by month.
            """]
                ),
                dcc.Graph(
                    id="Number of Incidences raised by month",
                    figure=px.bar(df_kpi1, x="month", y="incident_code", barmode="group", color="incident_code", height=700),
                ),
            ])

def create_kpi2():
    return html.Div([
        html.H1(children=["KPI 2 -  INC closed by month"]),
             html.Div(
                 children="""
                 Volume of incidences solved by month.
             """
             ),
             dcc.Graph(
                 id="Number of Incidences solved by month",
                 figure=px.bar(df_kpi2, x="month", y="incidences_code", barmode="group", color='month'),
             )
    ])

def create_kpi3():
    return html.Div([
        html.H1(children=["KPI 3 -  INC backlog by month"]),
             html.Div(
                 children="""
                 Volume of incidences backlog by month.
             """
             ),
             dcc.Graph(
                 id="Number of Incidences backlog by month",
                 figure=px.scatter(df_kpi3, x="month", y="incidenct_code", color="incidenct_code" )

             )
    ])

def create_kpi4():
    return html.Div([
        html.H1(children=["KPI 4 - INC per cause per month"]),
             html.Div(
                 children=["""
                     Incident Type Volume by Assigned Organisation.
                 """]
             ),
             dcc.Graph(
                 id="Priority by assign",
                 figure=px.scatter(df_kpi4, x="month", y="inc. type", title="incidences_code", color="incidences_code", height=800)
             )
    ])

def create_kpi5():
    return html.Div([
        html.H1(children=["KPI 5 -  Number of P1 not meeting SLA"]),
             html.Div(
                 children=["""
                 Volume of incidences backlog by month.
             """]
             ),
             dcc.Graph(
                 id="number of inc backlog by month",
                 figure=px.scatter(df_kpi5, x="created_date_time", y="incident_code", color="incident_code" )

             )
    ])

def create_kpi6():
    return html.Div([
        html.H1(children=["KPI 6 -  INC per domain"]),
             html.Div(
                 children=["""
                 Volume of incidences per domain.
             """]
             ),
             dcc.Graph(
                 id="number of incidences per domain ",
                 figure=px.scatter(df_kpi6, x="month", y="domain_group", color="priority", height=1000 )
             )
    ])
                         
def create_dash_application(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname="/dash/")
    dash_app.layout = html.Div(
        children=[
            html.Div(children=[
                html.H1("IBERIA DASHBOARD"),
                html.A(children="Logout", href="/logout", className="logout")
            ], className="header", style={'display': 'flex', 'justify-content': ' space-between'}),
            html.Div(children=[
                dcc.Tabs(id="tabs-styled-with-props",vertical=True, value='tab-1', children=[
                    dcc.Tab(label='Inc. Raised', value='tab-1'),
                    dcc.Tab(label='Inc. Closed', value='tab-2'),
                    dcc.Tab(label='Inc. Backlog', value='tab-3'),
                    dcc.Tab(label='SLA non-compliant', value='tab-4'),
                    dcc.Tab(label='SLA compliant', value='tab-5'),
                    dcc.Tab(label='INC per domain', value='tab-6'),
                    ], colors={
                        "border": "white",
                        "primary": "#fcd100",
                        "background": "#D7192D"
                    }),
                html.Div(children=[
                    html.Div(id='tabs-content-props')
                ], style={'width': '80%'})
                

            ], style={'display': 'flex', 'justify-content': 'space-between'})
    ])

    @dash_app.callback(Output('tabs-content-props', 'children'),
                Input('tabs-styled-with-props', 'value'))
    def render_content(tab):
        if tab == 'tab-1':
            return create_kpi1()
        elif tab == 'tab-2':
            return create_kpi2()
        elif tab == 'tab-3':
            return create_kpi3()
        elif tab == 'tab-4':
            return create_kpi4()
        elif tab == 'tab-5':
            return create_kpi5()
        elif tab == 'tab-6':
            return create_kpi6()



   



    for view_function in dash_app.server.view_functions:
        if view_function.startswith(dash_app.config.url_base_pathname):
            dash_app.server.view_functions[view_function] = login_required(
                dash_app.server.view_functions[view_function]
            )

    return dash_app

    




















  


# %%
