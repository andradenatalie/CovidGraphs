import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

USERNAME_PASSWORD_PAIRS = [
    ['Natalie', '002'], ['username', 'password']
]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

cov_data = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data"
                       "/csse_covid_19_daily_reports/05-03-2020.csv")

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)
server = app.server


app.layout = html.Div(children=[
    html.H1(children='COVID-19 worldwide results',
            style={

                'font-family': "Open Sans",
            },
            ),
    html.H2(children='Last Update:05-03-2020',
            style={

                'font-family': "Open Sans"
            },
            ),

    dcc.Graph(
            id='example-graph0',
            figure={
                'data': [
                    go.Bar(
                        x=cov_data['Country_Region'],
                        y=cov_data['Confirmed'],
                        marker={'color': 'rgb(210,105,30)'}
                    )

                ],
                'layout': {
                    'title': 'Confirmed by country',

                }
            },
        ),
    dcc.Graph(
        id='example-graph1',
        figure={
            'data': [
                go.Bar(
                    x=cov_data['Country_Region'],
                    y=cov_data['Recovered'],
                    marker={'color': 'rgb(51,204,153)'}
                )

            ],
            'layout': {
                'title': 'Recovery by contry',

            }
        },
    ),
    dcc.Graph(
        id='example-graph2',
        figure={
            'data': [
                go.Bar(
                    x=cov_data['Country_Region'],
                    y=cov_data['Deaths'],
                    marker={'color': 'rgb(200,204,53)'}
                )

            ],
            'layout': {
                'title': 'Fatalities by country'
            }
        },
    ),
    html.H5("Developed by Natalie Andrade",
            style={

                'font-family': "Open Sans"
            }
            ),

])

if __name__ == '__main__':
    app.run_server(debug=True)
