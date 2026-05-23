import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="Stock Market Analysis Dashboard",
    layout="wide"
)

st.title("📈 Stock Market Analysis Dashboard")

# --------------------------------
# LOAD DATA
# --------------------------------

df = pd.read_csv(
    "data/final_processed/clean_stock_data.csv"
)

df['date'] = pd.to_datetime(df['date'])

# --------------------------------
# SIDEBAR
# --------------------------------

st.sidebar.header("Filter Options")

selected_stock = st.sidebar.selectbox(
    "Select Stock",
    sorted(df['ticker'].unique())
)

# Filter stock
stock_df = df[df['ticker'] == selected_stock]

# --------------------------------
# KPI SECTION
# --------------------------------

latest_close = stock_df.iloc[-1]['close']
highest_price = stock_df['high'].max()
lowest_price = stock_df['low'].min()
avg_volume = stock_df['volume'].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Latest Close", f"{latest_close:.2f}")
col2.metric("Highest Price", f"{highest_price:.2f}")
col3.metric("Lowest Price", f"{lowest_price:.2f}")
col4.metric("Average Volume", f"{avg_volume:,.0f}")

# --------------------------------
# STOCK PRICE TREND
# --------------------------------

st.subheader(f"{selected_stock} Closing Price Trend")

fig1 = px.line(
    stock_df,
    x='date',
    y='close',
    title=f"{selected_stock} Closing Prices"
)

st.plotly_chart(fig1, use_container_width=True)

# --------------------------------
# VOLUME ANALYSIS
# --------------------------------

st.subheader(f"{selected_stock} Volume Analysis")

fig2 = px.bar(
    stock_df,
    x='date',
    y='volume',
    title=f"{selected_stock} Trading Volume"
)

st.plotly_chart(fig2, use_container_width=True)

# --------------------------------
# DAILY RETURNS
# --------------------------------

stock_df = stock_df.sort_values('date')

stock_df['daily_return'] = stock_df['close'].pct_change()

st.subheader(f"{selected_stock} Daily Returns")

fig3 = px.line(
    stock_df,
    x='date',
    y='daily_return',
    title=f"{selected_stock} Daily Returns"
)

st.plotly_chart(fig3, use_container_width=True)

# --------------------------------
# DATA TABLE
# --------------------------------

st.subheader("Stock Data Table")

st.dataframe(stock_df.tail(20))

# --------------------------------
# FOOTER
# --------------------------------

st.markdown("---")
st.markdown("Developed using Streamlit, Pandas, Plotly")