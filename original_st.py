import streamlit as st
import pandas as pd
import json
import urllib.request as urllib2
import folium
from streamlit_folium import st_folium

df = ""

def Data(resource):
    global datas
    response = urllib2.urlopen(f'https://data.bodik.jp/api/3/action/datastore_search?resource_id={resource}')
    datas = json.loads(response.read()).get('result').get('records')
    return pd.DataFrame(datas)

def show_map(Icon):
    global resource
    df = Data(resource)
    m = folium.Map(location=[26.1245,127.4052], zoom_start=6)
    for i, row in df.iterrows():
        folium.Marker(
            [row["緯度"], row["経度"]],
            popup=row['名称'], tooltip=row["名称"],
            icon = folium.Icon(icon=Icon)
        ).add_to(m)
    st_data = st_folium(m, width=800, height=800)

def main(): 
    global resource    
    if ganre == "避難場所":
            Icon = "home"
            if location == "那覇市":
                resource = "f1edac49-5715-498e-a985-6cdb4af3b4d9"
            elif location == "南風原町":
                resource = "33f94815-1d81-4c58-8fd6-7af1f606920d"
            elif location == "南城市":
                resource = "e0d8ac3b-a4f3-43ec-9d31-604fdf2c5677"
            elif location == "宜野湾市":
                resource = "0c718732-b466-4a9a-9c6a-655682d8345a"
            elif location == "名護市":
                resource = "aa34dacb-0912-4102-a8a2-3dfba6efc006"
            elif location == "沖縄市":
                 resource = "fa87aa81-f6ce-4200-86e3-2bbc74584fee"
            elif location == "読谷村":
                resource = "35fca548-872d-46a1-a38b-64abb8d22314"
    elif ganre == "医療機関":
            Icon = "plus"
            if location == "那覇市":
                st.write("那覇市の医療データは存在しません")
                resource = "none"
            elif location == "南風原町":
                resource = "92db43f6-995a-46c4-8bf9-3c062474b47d"
            elif location == "南城市":
                resource = "24885c01-3fa5-4cbf-b9bf-0cf8d34b3683"
            elif location == "宜野湾市":
                resource = "15bbdcf4-13b5-45c4-801a-c048a959880d"
            elif location == "名護市":
                resource = "165cd882-fc6c-4d91-9721-93ebb1d6ccba"
            elif location == "沖縄市":
                 resource = "e9d44b30-7e8f-44e8-992e-9a6b5a8b7d62"
            elif location == "読谷村":
                resource = "2a4b3121-fc91-4d1d-8bf5-9cf5e3c3971d"
    elif ganre == "AED":
            Icon = "heart"
            if location == "那覇市":
                resource = "7d3365f4-71f8-420c-8a20-5252fd66f448"
            elif location == "南風原町":
                resource = "bba8638a-7265-41f6-873e-1649a34e5a18"
            elif location == "南城市":
                resource = "0106f818-dd7f-4150-bb5e-4207243d8b52"
            elif location == "宜野湾市":
                resource = "023684ba-e75c-4f7b-b422-d1c170574f8e"
            elif location == "名護市":
                resource = "dfb69833-3283-4e4a-b278-e9fd7c112145"
            elif location == "沖縄市":
                resource = "819cc401-5016-4714-b1b8-09f50ee99b30"
            elif location == "読谷村":
                resource = "bcf72280-7126-44df-81f8-fe1e39dc8679"
    elif ganre == "文化":
            Icon = "flag"
            if location == "那覇市":
                resource = "889ddb57-cf16-438e-ad69-25be2c98ec3a"
            elif location == "南風原町":
                resource = "c01d6f5a-9553-490d-82a2-222308956cbc"
            elif location == "南城市":
                resource = "928764f8-3c8d-4ad1-a269-9547bc788549"
            elif location == "宜野湾市":
                resource = "c05e9102-c5de-4fba-b84e-f65ac6b0b3e0"
            elif location == "名護市":
                resource = "617623f0-45d9-42c2-9867-24d88697e94a"
            elif location == "沖縄市":
                 resource = "3284ef22-16b0-44df-ba7b-280d6dcfd165"
            elif location == "読谷村":
                resource = "9e14e9da-b569-4f23-95a4-1eef4600c896"

    if resource != "none":
        df = Data(resource)   
    if type == "表(テーブル)":
        st.dataframe(df[['名称', '住所', '緯度', '経度']])
    else:
        show_map(Icon)

ganre = st.selectbox("ジャンル", ("避難場所", "医療機関", "AED", "文化"))
location = st.selectbox("地域", ("那覇市", "南風原町", "南城市", "宜野湾市", "名護市", "沖縄市", "読谷村"))
type = st.radio("表示タイプ", ("表(テーブル)", "マップ"))

if __name__ == "__main__":
    main()