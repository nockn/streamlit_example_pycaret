# Streamlit上でPyCaretを動かす方法
[[English]](../README.md)  
StreamlitでPyCaretを動かすサンプルプログラムです。  
Qiitaに[詳細な記事](https://qiita.com/nockn/items/77d6b5f5e8f58a0b6c44)を投稿しています。  

![demo.gif](demo.gif)

## クイックスタート
> pip install streamlit>=1.5.1 pycaret>=2.3.5  
> streamlit run streamlit_app.py  

## 設定方法
ご自身のアプリで試される場合は、PyCaretの関数の引数を以下のように指定してください:

### setup関数
> html=False  
> silent=True

### plot_model関数
>display_format="streamlit"
