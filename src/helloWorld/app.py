import dash
from dash import html, dcc
#import dash_core_components as dcc # Legacy import
import plotly.express as px
import pandas as pd 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "MTL", "NYC"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City")

# Layout

## Formatation components
### Dash HTML Components
app.layout = html.Div(id="div1",
    children=[
        html.H1("Hello Dash", id="h1", style={"textAlign": "center", "color": "#023e8a"}),
        html.Div("Dash: A web application framework for Python.", id="div2", style={"textAlign": "center", "color": "#023e8a"}),
        #### Dash Core Components
        dcc.Graph(figure=fig, id="graph")
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
