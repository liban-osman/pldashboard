import streamlit as st
import pandas as pd
from PIL import Image
from IPython.display import HTML

players= pd.read_csv('data/players.csv')
shots= pd.read_csv('data/player_shots.csv')
team_data= pd.read_csv('data/team_data.csv')
matches= pd.read_csv('data/matches.csv')
players1 = pd.read_csv('player_data_full.csv',low_memory=False)

class HomePage:
    def __init__(self):
        return
    
    def table():
        tbl = team_data[["Position","logo","Points","Team","Matches Played","Wins",
        "Draws","Losses","Goals","Goals Against"]]
        tbl.set_index(["Position"])
        return tbl


#pd.read_csv('player_data_full.csv')

st.write("""
# Premier League Statistics
""")

top5 = players.iloc[:5]

p = list(players.iloc[:5]["player_name"])

st.subheader("Top 5 Goal Scoreres")
col1, col2, col3, col4, col5= st.columns(5)
cols = [col1, col2, col3, col4, col5]

for x in range(len(cols)):
    with cols[x]:
        st.image("player_images/"+ p[0].replace(' ','_') +".png")
        name = top5.iloc[x]["player_name"]
        goals = str(top5.iloc[x]["goals"]) + " Goals"
        assists = str(top5.iloc[x]["assists"]) + " Assists"
        html = f"""<h6>{name}</h6>"""
        html2 = f"""<h6>{goals}</h6>"""
        html2 = f"""<h6>{assists}</h6>"""
        st.markdown(html, unsafe_allow_html=True)
        st.markdown(html2, unsafe_allow_html=True)



def standing():
    st.subheader("Current Standings")
    st.dataframe(
    HomePage.table(),use_container_width=True,
    column_config={
        "logo": st.column_config.ImageColumn(
            "Logo", help="Streamlit app preview screenshots"
        )
    }, hide_index=True,)

standing()




		
