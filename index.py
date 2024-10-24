from dash import html, dcc
import dash_bootstrap_components as dbc
import numpy as np

from charts import pizza, continuous, categoricals, fig_c, fig_e

############################### components ###################################

Comp_A = dbc.Card(
    dbc.CardBody([
        html.H1("Pizza Brands"),
        html.P("Try to find unique segments by selecting different x and y variables.", className="subtitletext")
    ], className="titlecenter"), className="knucklepuck titlewidth"
)

Comp_B = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="fig_b", className="height100p")
    ]), className="knucklepuck"
)

Comp_C = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_c, id="fig_c", className="height50p1")
    ]), className="knucklepuck"
)

Comp_D = dbc.Card(
    dbc.CardBody([
        html.Div([
            html.Div([
                html.Div([

                    html.P("X:", className="selectors"),

                    dcc.Dropdown(
                        options=[j for j in continuous if j not in "id"],
                        value=continuous[1],
                        multi=False,
                        searchable=False,
                        clearable=False,
                        id="dropdown1",
                        placeholder="x",
                        className="ddchildren",
                        maxHeight=800,
                    ),

                ], className="displaythisinline"),
                html.Div([

                    html.P("Y:", className="selectors"),

                    dcc.Dropdown(
                        options=[j for j in continuous if j not in "id"],
                        value=continuous[1],
                        multi=False,
                        searchable=False,
                        clearable=False,
                        id="dropdown2",
                        placeholder="y",
                        className="ddchildren",
                        maxHeight=800,
                    ),
                    
                ], className="displaythisinline"),


            ], className="selectorleft flexdaddy"),
            html.Div([
                dcc.RadioItems(
                    options=["random", "brand"],
                    value="random",
                    id="radioskycity",
                    inline=False,
                ),
            ],className="selectorright"),
        ], className="flexdaddy height50p2")
    ]), className="knucklepuck"
)

Comp_E = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_e, id="fig_e")
    ]), className="knucklepuck",
)



############################### skeleton ###################################

atf = html.Div([
    html.Div([
        Comp_A
    ]),
    html.Div([
        html.Div([
            Comp_B
        ], className="atf_charts_left"),
        html.Div([
            html.Div([
                Comp_D
            ], className="selector_component"),
            html.Div([
                Comp_C
            ], className="heatmap_chart"),
        ], className="flexdaddy atf_charts_right"),
    ], className="flexdaddy atf_charts"),
], className="flexdaddy biggest")

btf = html.Div([
    Comp_E
])


############################### aggregation ###################################


lyt = dbc.Container([
    atf,
    btf
])