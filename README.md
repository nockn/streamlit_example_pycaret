# How to run PyCaret on Streamlit
[[日本語]](/docs/README_JP.md)  
This is a demo of PyCaret running on Streamlit.

![demo.gif](/docs/demo.gif)

## QuickStart
<!--
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/nockn/streamlit_example_pycaret/main)
or
-->
> pip install streamlit>=1.5.1 pycaret>=2.3.5 scikit-learn>=1.0.2  
> streamlit run streamlit_app.py

Streamlit app is being prepared for deployment.

## Setting on your app
Set the arguments of the function as follows:
### setup
> html=False  
> silent=True  

### plot_model
>display_format="streamlit"
