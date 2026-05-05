import plotly.express as px

from random_walk import RandomWalk


rw = RandomWalk()
rw.fill_walk()

fig = px.scatter(rw.x_values, rw.y_values, title="Random Walk")
fig.show()