import plotly.graph_objs as go
import plotly.offline as opy

def generate_pie_chart(labels, values):
    fig = go.Figure(
        data=[go.Pie(labels=labels, values=values, hole=0.3)],
        layout=go.Layout(
            margin=dict(l=10, r=10, t=20, b=20),
            height=300,
        )
    )
    return opy.plot(fig, output_type='div') # Convert plotly's graph to HTML div
