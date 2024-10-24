import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from itertools import *

from data import pizza

############################### above the fold ###################################

# # # # # # # # # # # # # # # # # # fig_c # # # # # # # # # # # # # # # # # # # # 

def heatmap_allfeatures_pearson(df, colors="Oryel"):

    df = df.select_dtypes(["number"])

    corr = df.corr().round(2)
    mask = np.zeros_like(df.corr(), dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    corr = corr.mask(mask)

    g = px.imshow(corr, text_auto=True, color_continuous_scale=colors, zmin=-1, zmax=1)

    g.update_layout(
    { "template": "plotly_white",
     "title": "Pearson's Correlation",
    "xaxis":{"showgrid": False,
             "zeroline": False},
    "yaxis": {"showgrid": False,
             "zeroline": False},
   }).update_traces({"xgap": 5,"ygap":5})

    return g

fig_c = heatmap_allfeatures_pearson(pizza, colors="RdYlBu_r")


# # # # # # # # # # # # # # # # # # fig_e # # # # # # # # # # # # # # # # # # # # 
def pull_categoricals(df):
    return [j for j in df.columns if "object" in str(df[j].dtype)]

categoricals = pull_categoricals(pizza)

def pull_continuous(df, categoricals):
    return [j for j in pizza.columns if j not in categoricals]

continuous = pull_continuous(pizza, categoricals)

def bars_grouped_by_category(df, thecategory, continuous, colorscale):
    
    gb = df.groupby([thecategory])[continuous].mean().drop(["id"], axis=1)
    
    summit = gb.sum(axis=0)
    gb1 = gb / summit
    
    colors = cycle(iter(colorscale))
    
    figures = []
    
    for h in gb.index:
        mask = ( gb.index == h )
        gb2 = gb1[mask]
        x = gb2.columns.values
        y = gb2.values.flatten()
        fig = px.bar(x=x, y=y, opacity=0.8, hover_name=[h]*len(x)).update_traces({"marker" :{"color": next(colors)}})
        figures.append(fig.update_layout({"yaxis": {"showgrid": False}}))
    
    datum = figures[0].data + figures[1].data + figures[2].data + figures[3].data + figures[4].data + figures[5].data + figures[6].data + figures[7].data + figures[8].data + figures[9].data 
    
    print(len(datum), len(pizza["brand"].unique()))
    fig = go.Figure(datum).update_layout({"title": "Continuous variables, broken up by Brand",
                                            "xaxis": {"title": "Brands"},
                                            "yaxis": {"title": "Continuous variable (% of Total)"}})
    return fig
    

fig_e = bars_grouped_by_category(pizza, "brand", continuous, colorscale=px.colors.qualitative.T10)