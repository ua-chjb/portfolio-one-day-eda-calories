from dash import Input, Output, State, exceptions
import plotly.express as px

from charts import star_chart, score_output
from data import pizza
from app import app

def callbacks_baby(app):
    @app.callback(
        Output(component_id="fig_b", component_property="figure"),
        [
            Input(component_id="dropdown1", component_property="value"),
            Input(component_id="dropdown2", component_property="value")
        ],
    )
    def function(value1, value2):
        x = pizza[value1]
        y = pizza[value2]
        color = "Brand"
        return px.scatter(x=x, y=y, color=color).update_layout({
            "title": f"{x} by {y}",
            "xaxis": {"title": f"{x.columns}"},
            "yaxis": {"title": f"{y.columns}"},
        })