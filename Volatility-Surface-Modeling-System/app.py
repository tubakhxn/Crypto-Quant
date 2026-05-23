

import subprocess
import sys

def auto_install(packages):
    for package in packages:
        try:
            __import__(package.split("==")[0].replace("-", "_"))
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])


auto_install(["streamlit", "plotly", "numpy", "pandas", "scikit-learn", "scipy", "yfinance", "ccxt"])

import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from scipy.stats import norm

st.set_page_config(page_title="Volatility Surface Modeling System", layout="wide")

st.markdown("""
<style>
body {
    background-color: #05070d;
}
.stApp {
    background: linear-gradient(180deg, #05070d, #0c111d);
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("Volatility Surface Modeling System")

np.random.seed(42)
time_index = pd.date_range("2025-01-01", periods=300, freq="min")
prices = np.cumsum(np.random.randn(300)) + 100

df = pd.DataFrame({
    "timestamp": time_index,
    "price": prices,
    "volume": np.random.randint(100, 5000, 300),
    "volatility": np.abs(np.random.randn(300)),
    "spread": np.random.rand(300) / 10
})

col1, col2 = st.columns(2)

with col1:
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["price"],
        mode="lines",
        name="Price"
    ))
    fig.update_layout(
        template="plotly_dark",
        title="Institutional Market Feed",
        height=420
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    heatmap = go.Figure(data=go.Heatmap(
        z=np.random.randn(20,20)
    ))
    heatmap.update_layout(
        template="plotly_dark",
        title="Liquidity Heatmap",
        height=420
    )
    st.plotly_chart(heatmap, use_container_width=True)

st.subheader("Quantitative Analytics")

metric_cols = st.columns(4)
metric_cols[0].metric("PnL", f"${round(np.random.randn()*5000,2)}")
metric_cols[1].metric("Sharpe", round(np.random.rand()*3,2))
metric_cols[2].metric("Volatility", round(df["volatility"].mean(),4))
metric_cols[3].metric("Spread", round(df["spread"].mean(),4))

X = np.arange(len(df)).reshape(-1,1)
y = df["price"].values
model = LinearRegression()
model.fit(X,y)
pred = model.predict(X)

forecast_fig = go.Figure()
forecast_fig.add_trace(go.Scatter(x=df["timestamp"], y=y, name="Observed"))
forecast_fig.add_trace(go.Scatter(x=df["timestamp"], y=pred, name="Predicted"))
forecast_fig.update_layout(template="plotly_dark", title="Predictive Modeling Layer")
st.plotly_chart(forecast_fig, use_container_width=True)

clusters = KMeans(n_clusters=3, random_state=42, n_init=10).fit(df[["price","volatility"]])
df["cluster"] = clusters.labels_

cluster_fig = go.Figure()
cluster_fig.add_trace(go.Scatter(
    x=df["price"],
    y=df["volatility"],
    mode="markers",
    marker=dict(color=df["cluster"]),
))
cluster_fig.update_layout(template="plotly_dark", title="Market Regime Clustering")
st.plotly_chart(cluster_fig, use_container_width=True)

st.dataframe(df.tail(25), use_container_width=True)
