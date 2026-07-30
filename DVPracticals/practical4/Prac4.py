import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4],
    y=[2, 4, 1, 3],
    mode="lines"
))
fig.update_layout(
    updatemenus=[
        dict(
            buttons=[
                dict(
                    label="Blue",
                    method="restyle",
                    args=[{"line.color": "blue"}]
                ),
                dict(
                    label="Red",
                    method="restyle",
                    args=[{"line.color": "red"}]
                ),
                dict(
                    label="Green",
                    method="restyle",
                    args=[{"line.color": "green"}]
                ),
            ]
        )
    ]
)
fig.show()