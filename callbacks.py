from dash import Input, Output
import plotly.express as px

from charts import pizza, layout_func

def callbacks_baby(app):
    @app.callback(
        Output(component_id="fig_b", component_property="figure"),
        [
            Input(component_id="dropdown1", component_property="value"),
            Input(component_id="dropdown2", component_property="value"),
            Input(component_id="radioskycity", component_property="value")
        ],
    )
    def function(value1, value2, value3):
        x = pizza[value1]
        y = pizza[value2]
        color = pizza[value3]
        return layout_func(px.scatter(x=x, y=y, color=color, opacity=0.6, color_discrete_sequence=px.colors.qualitative.T10).update_layout({
            "title": f"'{x.name}' by '{y.name}'",
            "xaxis": {"title": f"'{x.name}'"},
            "yaxis": {"title": f"'{y.name}'"},
            "legend": {"orientation": "h", "title": "Brand", "y": -0.2}
        })).update_layout({"xaxis": {"showgrid": True, "gridcolor": "#EEEEEE"}})