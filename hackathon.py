import numpy as np
import pandas as pd
import plotly.graph_objs as go


m = pd.read_pickle("m.pkl")
future = m.make_future_dataframe(periods=500)


forecast = m.predict(future)


print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
