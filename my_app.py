import streamlit as st

st.markdown("""
<style>
body {
    color: #fff;
    background-color: #3b1717;
}
</style>
    """, unsafe_allow_html=True)


# Set the page title and icon
st.set_page_config(page_title="My Streamlit App", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded")

# Define a dictionary with page names and content
PAGES = {
    "Cup of Joe": {
        "picture": "streamlit/first.png",
        "picture_logo": "streamlit/socmed.png",
        "movies": "streamlit/movies.png",
        "activities": "streamlit/activities.png",
        "description": "The Filipino band, Cup of Joe, was formed by six talented lads from Baguio namely vocalists Edgar Gian Bernardino and Raphaell Ridao, pianist Vixen “Xen” Gareza, lead guitarist Antonio Gabriel “Gab” Fernandez, bassist Raphael “Seve” Severino and rhythm guitarist Clint Joules “CJ” Fernandez and almost all of them came from a family with musical backgrounds.",
        "followers": "1.5 Million Listeners, 73.4 Thousand Followers ",
        "movies_desc": "Music Featured in 3 Movies and 3 Shows",
        "activities_desc": "Performed in UP Fair and had their First Collab"
    },
    "Exploratory Data Analysis": {
        
        "eda_1_title":"Estranghero Streams",
        "eda_1": "streamlit/eda_1.png",
        "eda_1_desc":"Estranghero Streams",

        "eda_2_title":"Audio Features of Estranghero to Other Tracks",
        "eda_2": "streamlit/eda_2.png",
        "eda_2_desc":"Estranghero Streams",

        "eda_3_title":"Audio Features Comparison to other OPM Artists",
        "fellow": "streamlit/fellow.png",
        "eda_3": "streamlit/eda_3.png",
        "eda_3_desc":"Estranghero Streams",


    },
    "Objectives": {
        "objectives": "<h1 style='font-weight:bold; font-size: 36px;'>Goal: Make Cup of Joe perform better on Spotify locally while still remaining true to their sound</h1><br><ul style='font-size: 28px;'><li><b>Identify their genre and describe their sound</b></li><li><b>Compare with and get lessons from related artists</b></li><li><b>Recommend artists to collaborate with</b></li></ul>",
        "objectives_pic" : "streamlit/objectives_pic.png"
    },

    "Machine Learning Pipeline": {
        "pipeline_title" : "Pipeline",
        "pipeline" : "streamlit/pipeline.png"
    },

    "Genre Classification": {

        "genre_1": "streamlit/genre_1.png",
        "genre_2": "streamlit/genre_2.png",

        "genre_class_title" : "Genre Classifier",
        "top_5" : "Top Five Songs are of Five Differnt Genres",
        "genres" : "Folk, Country, And Indie are the Genres of the Most of Cup of Joe's Songs"

    },
    "Recommender Engine": {
        "bpm_distance": "streamlit/bpm_distance.png",
        "recom_title": "Recommender Engine",
        "Manhattan_dist": "Manhattan Distance",
        "Eucli_dist": "Euclidean Distance",

        "manhat": "streamlit/manhattan.png",
        "eucli": "streamlit/eucli.png",


        "cup_v_artists": "streamlit/cup_v_artst.png",
        "cup_v_songs": "streamlit/cup_v_songs.png",
        "cup_v_artists_t": "Cup of Joe VS Recommended Aritsts",
        "cup_v_songs_t": "Cup of Joe VS Recommended Songs",

        "cup_v_artists_d": "Cup of Joe would benefit from partnering either of the recommended artists, as these artists have around 6 to 29x the total number of streams than the band.",
        "cup_v_songs_d": "Aside from 4 of the 5 songs playing at the same tempo (118 BPM), these songs have close values of Energy, Danceability, and Valence. Most recommended artists would be Shanti Dope, Zack Tabudlo and Al James due to 1) contrast in style and 2) voice.",


    },
    "Spotify Deployment": {
        "spotify": "Listen to the Recommended Songs via Spotify!",
    },
}

# Add a title for the sidebar
st.sidebar.title("G4SH Sprint 3 Output")

# Create a radio button in the sidebar to select the page
page = st.sidebar.radio("Go to", list(PAGES.keys()))

if page == "Cup of Joe":
    st.write(f"# {page}")
    st.image(PAGES[page]["picture"], width=1000)
    st.write(PAGES[page]["description"])
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["followers"])), unsafe_allow_html=True)
    st.image(PAGES[page]["picture_logo"], width=1000)
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["movies_desc"])), unsafe_allow_html=True)
    st.image(PAGES[page]["movies"], width=1000)
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["activities_desc"])), unsafe_allow_html=True)
    st.image(PAGES[page]["activities"], width=1000)
elif page == "Exploratory Data Analysis":
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["eda_1_title"])), unsafe_allow_html=True)
    st.image(PAGES[page]["eda_1"], width=1000)
    st.write(PAGES[page]["eda_1_desc"])

    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["eda_2_title"])), unsafe_allow_html=True)
    st.image(PAGES[page]["eda_2"], width=1000)
    st.write(PAGES[page]["eda_2_desc"])

    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["eda_3_title"])), unsafe_allow_html=True)
    st.image(PAGES[page]["fellow"], width=1000)
    st.image(PAGES[page]["eda_3"], width=1000)
    st.write(PAGES[page]["eda_3_desc"])
elif page == "Objectives":
    st.write(PAGES[page]["objectives"], unsafe_allow_html=True)
    st.image(PAGES[page]["objectives_pic"], width=1000)
elif page == "Machine Learning Pipeline":
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["pipeline_title"])), unsafe_allow_html=True)
    st.image(PAGES[page]["pipeline"], width=1000)
elif page == "Genre Classification":
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["genre_class_title"])), unsafe_allow_html=True)
    st.write("<h1 style='font-weight: bold; font-size: 36px;'></h1><ul style='font-size: 24px;'><li>To tag a genre for each track of Cup of Joe and identify their most salient genre for use in a recommender engine to find relevant songs and artists</li><li>Genre: Country, Electronic, Folk, Indie, Jazz, Pop, R&B, Reggae, Rock</li><li>Features: danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo</li><li>Models considered: K-Nearest Neighbors, Supported Vector Model, Random Forest Classifier</li><li>Best model: Random Forest Classifier</li><li>Accuracy: 52%</li></ul>", unsafe_allow_html=True)
    
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["genres"])), unsafe_allow_html=True)
    st.image(PAGES[page]["genre_1"], width=500)
    st.write("<ul style='font-size: 24px;'><li>These three genres share the audio feature of being somewhat danceable.</li><li>These three genres are spread in terms of energy and valence", unsafe_allow_html=True)
    
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["top_5"])), unsafe_allow_html=True)
    st.image(PAGES[page]["genre_2"], width=500)
    st.write("<ul style='font-size: 24px;'><li>Their top ten songs have two folk songs and three country songs.</li><li>Folk songs and country songs make up more than half of the OPM charting songs.</li><li>Explore folk and country.</li></ul>", unsafe_allow_html=True)


elif page == "Recommender Engine":
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["recom_title"])), unsafe_allow_html=True)
    st.image(PAGES[page]["bpm_distance"], width=500)
    st.write("<ul style='font-size: 24px;'><li>Seeder song is “Estranghero”, as recommended by Cup of Joe itself.</li><li>Only OPM artists were considered to increase likelihood of collaboration.</li><li>Manhattan and Euclidean methods were considered, based on closeness of tempo to the seeder track.</li></ul>", unsafe_allow_html=True)

    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["Manhattan_dist"])), unsafe_allow_html=True)
    st.image(PAGES[page]["manhat"], width=800)

    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["Eucli_dist"])), unsafe_allow_html=True)
    st.image(PAGES[page]["eucli"], width=800)

    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["cup_v_artists_t"])), unsafe_allow_html=True)
    st.image(PAGES[page]["cup_v_artists"], width=800)
    st.write(PAGES[page]["cup_v_artists_d"])

    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["cup_v_songs_t"])), unsafe_allow_html=True)
    st.image(PAGES[page]["cup_v_songs"], width=800)
    st.write(PAGES[page]["cup_v_songs_d"])

elif page == "Spotify Deployment":
    st.write("<h1 style='font-weight: bold'>{}</h1>".format("{}".format(PAGES[page]["spotify"])), unsafe_allow_html=True)
    st.write("<iframe src='https://open.spotify.com/embed/playlist/3TMgfzviKkiiLgVf2e3GXb' width='100%' height='380' frameborder='0' allowtransparency='true' allow='encrypted-media'></iframe>", unsafe_allow_html=True)
