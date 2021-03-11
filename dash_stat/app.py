import dash
import dash_core_components as dcc
import dash_html_components as html
from utils.save_open_data import open_static_data


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


def generate_data():
    file = open_static_data()
    for index in file.items():
        app.layout.children[2].figure['data'].append({"x": index[0], "y": index[1], "type": "bar", "name": index[0]})


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[html.H1(children="Count message DASH"),
                                    html.Div(
                                        children=[
                                        html.P(children="📈", className="header-emoji"),
                                        html.H1(
                                            children="Count Message Statistic", className="header-title"
                                        ),
                                        html.P(
                                            children="Analyze data extracted from the telegram",
                                            className="header-description",
                                        ),
                                        ],
                                        className="header",
                                    ),
                                    dcc.Graph(
                                        figure={
                                            "data": [],
                                            "layout": {"title": "Statistic count messages",
                                                       'plot_bgcolor': colors['background'],
                                                        'paper_bgcolor': colors['background'],
                                                        'font': {
                                                            'color': colors['text']
                                                        }
                                                       }
                                        },
                                    )])
generate_data()

if __name__ == '__main__':
    app.run_server(debug=True)
