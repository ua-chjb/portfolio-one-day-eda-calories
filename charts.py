import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from itertools import *

from data import pizza
############################### behind the scenes ###################################

pizza["random"] = np.random.choice(["Whoop", "Hey", "Whee"], 300)

def pull_categoricals(df):
    return [j for j in df.columns if "object" in str(df[j].dtype)]

categoricals = pull_categoricals(pizza)

def pull_continuous(df, categoricals):
    return [j for j in pizza.columns if j not in categoricals]

continuous = pull_continuous(pizza, categoricals)

############################### figures without callbacks ###################################
# # # # # # # # # # # # # # # # # # fig_c # # # # # # # # # # # # # # # # # # # # 

def two_categoricals_means(df, cat1, cat2, continuous=continuous, colors=px.colors.diverging.Spectral):
    gb = pizza.groupby(["brand", "random"])[continuous].mean()
        
    summit = gb.sum(axis=0)
    gb1 = gb / summit
    
    gb2 = gb1.reset_index().pivot(index="brand", columns="random")
    gb2.columns = ["_".join(j) for j in gb2.columns]
    return px.imshow(gb2,  color_continuous_scale=colors).update_layout({
        "title": "Both categorical variables vs continuous",
        "clickmode": "select",
    })

fig_c = two_categoricals_means(pizza, "brand", "random", continuous)

# # # # # # # # # # # # # # # # # # fig_e # # # # # # # # # # # # # # # # # # # # 

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
        fig = px.bar(x=x, y=y, opacity=1.0, hover_name=[h]*len(x)).update_traces({"marker" :{"color": next(colors)}})
        figures.append(fig.update_layout({"yaxis": {"showgrid": False}}))
    
    datum = figures[0].data + figures[1].data + figures[2].data + figures[3].data + figures[4].data + figures[5].data + figures[6].data + figures[7].data + figures[8].data + figures[9].data 
    
    print(len(datum))
    fig = go.Figure(datum).update_layout({"title": "Continuous variables, broken up by Brand",
                                            "xaxis": {"title": "Brands"},
                                            "yaxis": {"title": "Continuous variable (% of Total)"}})
    return fig
    

fig_e = bars_grouped_by_category(pizza, "brand", continuous, colorscale=px.colors.qualitative.T10)

############################### layout ###################################

paper_bgcolor="white"
plot_bgcolor="white"
font_color="black"
legend_color="white"

def layout_func(fig):
    
    fig.update_layout(
        dict(
            paper_bgcolor=paper_bgcolor,
            plot_bgcolor=plot_bgcolor,
            font={"color": font_color},
            clickmode="select",
            legend={"bgcolor":legend_color,
                    "font": {"color":font_color},
                    "title":{"font":{"color":font_color}},
                    },
            xaxis=dict(
                showgrid=False,
                zeroline=False,
            ),
            yaxis=dict(
                gridcolor="#EEEEEE",
                zeroline=False,
            )
        )
    )

    return fig.update_layout({
        "xaxis": {"mirror": False, "showline": True, "linecolor": "lightgrey", "linewidth": 2},
        "yaxis": {"mirror": False, "showline": True, "linecolor": "lightgrey", "linewidth": 2},

    })


fig_e = layout_func(fig_e)