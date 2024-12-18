import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time

# select style for scatter plot
sns.set_style('darkgrid')

st.title('Dashboard for "auto_mpg" Dataset')

def load_data():
    """Utility function for loading data"""
    df = pd.read_csv('data/clean_auto_mpg.csv')
    return df

# load data
data_ = load_data()
numeric_columns = data_.select_dtypes(['float32', 'float64', 'int32', 'int64']).columns
# print(numeric_columns)

# refresh otomatis
# time.sleep(10)
# st.experimental_rerun()

# checkbox widget
checkbox = st.sidebar.checkbox('Reveal data')
#print(checkbox)

if checkbox:
    #st.write(data)
    st.dataframe(data = data_)

# create scatterplots
st.sidebar.subheader('Scatter Plot & Joint Plot Set up')
# add select widget
select_box1 = st.sidebar.selectbox(label = 'X axis for Scatter Plot', options = numeric_columns)
select_box2 = st.sidebar.selectbox(label = 'Y axis for Scatter Plot', options = numeric_columns)

# create scatter plot
fig, ax = plt.subplots()  # Create a figure and axis
sns.scatterplot(x = select_box1, y = select_box2, data = data_, ax = ax)
ax.set_title(f'Scatter Plot for {select_box1} and {select_box2}')
st.pyplot(fig)

# create histogram
st.sidebar.subheader('Histogram Set up')
# add select widget
select_box3 = st.sidebar.selectbox(label = 'select feature for the histogram', options = numeric_columns)
# slider adjustment
bins_ = st.sidebar.slider('Number of bins', min_value = 5, max_value = 50, value = 20)

# create histogram
fig, ax = plt.subplots()  # Create a figure and axis
sns.histplot(data_[select_box3], bins = bins_, kde = True, ax = ax)
ax.set_title(f'Histogram for {select_box3}')
ax.set_xlabel(select_box3)
ax.set_ylabel('Frequency')
st.pyplot(fig)

# # combined chart histogram & scatter plot
# fig, (ax1, ax2) = plt.subplot(1, 2, figsize = (12, 5))

# # create scatter plot for combined chart histogram & scatter plot
# sns.scatterplot(x = select_box1, y = select_box2, data = data_, ax = ax1)
# ax1.set_title(f'Scatter Plot for {select_box1} and {select_box2}')
# ax1.set_xlabel(select_box1)
# ax1.set_ylabel(select_box2)

# # create histogram for combined chart
# sns.histplot(data_[select_box3], bins = bins_, kde = True, ax = ax2)
# ax2.set_title(f'histogram for {select_box1}')
# ax2.set_xlabel(select_box3)
# ax2.set_ylabel('Frequency')

# # display join plot
# plt.tight_layout()
# st.pyplot(fig)

# # create join plot
# st.sidebar.subheader('Join Plot set up')
# joinplot_checkbox = st.sidebar.checkbox('Show Join plot')
# print(joinplot_checkbox)

# if joinplot_checkbox:
#     st.subheader(f'Join Plot {select_box1} and {select_box2}')
#     joinplot = sns.jointplot(x = select_box1, y = select_box2, data = data_, kind = 'scatter', height = 6)
#     st.pyplot(joinplot.figure)

# join plot with adjustable number of bins
st.sidebar.subheader('Joint Plot Feature Set up')
select_box4 = st.sidebar.selectbox(label = 'X axis', options = numeric_columns)
select_box5 = st.sidebar.selectbox(label = 'Y axis', options = numeric_columns)
slider_bins = st.sidebar.slider('number of bins', min_value = 5, max_value = 50, value = 25)

# joint plot
jointplot = sns.jointplot(x = select_box4, y = select_box5, data = data_, kind = 'scatter', marginal_kws = {'bins' : slider_bins, 'kde' : True})
jointplot.fig.suptitle(f'Join Plot: {select_box1} and {select_box2}', y = 1.03)
st.pyplot(jointplot.figure)