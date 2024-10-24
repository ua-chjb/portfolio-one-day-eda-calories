from dash import html, dcc
import dash_bootstrap_components as dbc
import numpy as np

from charts import pizza, continuous, fig_c, fig_e

############################### components ###################################

Comp_A = dbc.Card(
    dbc.CardBody([
        html.H1("Segments of Pizza Brands")
    ])
)

Comp_B = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="fig_b")
    ])
)

Comp_C = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_c, id="fig_c")
    ])
)

Comp_D = dbc.Card(
    dbc.CardBody([
        html.Div([
            html.P("Color: Brand"),
            dcc.Dropdown(
                options=continuous,
                value=continuous[0],
                multi=False,
                searchable=False,
                id="dropdown1",
                ),
            dcc.Dropdown(
                options=continuous,
                value=continuous[1],
                multi=False,
                searchable=False,
                id="dropdown2",
                ),
        ], className="flex_daddy"),
    ]),
)
Comp_E = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_e, id="fig_e")
    ])
)



############################### skeleton ###################################

atf = html.Div([
    html.Div([
        Comp_A
    ], className="flexdaddy title"),
    html.Div([
        html.Div([
            Comp_B
        ], className="atf_charts_left"),
        html.Div([
            html.Div([
                Comp_C
            ], className="heatmap_chart"),
            html.Div([
                Comp_D
            ], className="selector_component"),
        ], className="flexdaddy atf_charts_right"),
    ], className=" flexdaddy atf_charts"),
], className="flexdaddy biggest")

btf = html.Div([
    Comp_E
])


############################### aggregation ###################################



