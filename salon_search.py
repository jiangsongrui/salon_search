#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[2]:


merged_df = pd.read_csv("merged.csv")


# In[3]:


st.title("サロンサーチ")
price_limit = st.slider("最低カット价格上限", min_value=2000, max_value=8500, step=200, value=6000)
score_limit = st.slider("人気スコア下限", min_value=0.0, max_value=35.0, step=2.0, value=5.0)


# In[4]:


filtered_df = merged_df[
    (merged_df['price'] <= price_limit) & (merged_df['pop_score'] >= score_limit)
]


# In[5]:


fig = px.scatter(
    filtered_df,
    x='pop_score',
    y='price',
    hover_data=['name_salon', 'access','star', 'review'],    
    title='人気スコアと最低カット価格の散布图'
)
st.plotly_chart(fig)


# In[6]:


selected_salon = st.selectbox('查看详细信息的店铺', filtered_df['name_salon'])
if selected_salon:
    url = filtered_df[filtered_df['name_salon'] == selected_salon]['link_detail'].values[0]
    st.markdown(f"[{selected_salon}的页面]({url})", unsafe_allow_html=True)


# In[7]:


sort_key = st.selectbox(
    "请选择排名依据",
    ("star", "pop_score", "review", "price", "seats")
)
ascending = True if sort_key == "price" else False


# In[8]:


st.subheader(f"{sort_key} 排名前10的店铺")
ranking_df = filtered_df.sort_values(by=sort_key, ascending=ascending).head(10)
st.dataframe(ranking_df[["name_salon", "price", "pop_score", "star", "review", "seats", "access"]])


# In[ ]:




