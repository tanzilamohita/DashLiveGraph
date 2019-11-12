import datetime
import pandas_datareader.data as web
import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly
import random
import plotly.graph_objs as go
from collections import deque

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*1000
        ),
    ], style={'width': '98%', 'margin-left': 10, 'margin-right': 10, 'max-width': 50000}
)


@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])
def update_graph_scatter(n):
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1, 0.1))

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode='lines+markers',
            #fill="tozeroy",
            fillcolor="#6897bb"
            )

    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                                yaxis=dict(range=[min(Y), max(Y)]),
                                                #margin={'l': 50, 'r': 1, 't': 45, 'b': 1},
                                                title='Live Graph')}


if __name__ == '__main__':
    app.run_server(debug=True)

#
# app = dash.Dash()
# #input_data = 'TSLA'
# app.layout = html.Div(
#     [
#
#         dcc.Graph(id='live-graph', animate=True),
#         dcc.Interval(
#             id='graph-update',
#             interval=1*1000
#         ),
#     ]
# )
#
#
# # @app.callback(Output('live-graph', 'figure'),
# #                [Input('graph-update', 'n_intervals')])
# # def update_graph_scatter(n):
# #     # start = datetime.datetime(2015, 1, 1)
# #     # end = datetime.datetime.now()
# #     # df = web.DataReader(input_data, 'yahoo', start, end)
# #     # df.reset_index(inplace=True)
# #     # df.set_index("Date", inplace=True)
# #     # df = df.drop("Adj Close", axis=1)
# #     # X = df.index
# #     # Y = df.Close
# #     input = pd.read_csv('data.csv')
# #     x = input['x_value']
# #     X = input['total_1']
# #     Y = input['total_2']
# #
# #     data = plotly.graph_objs.Scatter(
# #                 x=list(X),
# #                 y=list(Y),
# #                 name='Scatter',
# #                 mode='lines+markers'
# #                 )
# #
# #     return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
# #                                                      yaxis=dict(range=[min(Y), max(Y)]),)}
# #
# #
# # if __name__ == '__main__':
# #     app.run_server(debug=True)

