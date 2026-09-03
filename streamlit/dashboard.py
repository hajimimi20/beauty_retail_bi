import streamlit as st

from pages import home
from pages import overview


# Page configuration
st.set_page_config(
    page_title = "Beauty Retail BI",
    page_icon = "💄",
    layout = "wide",
)

#-----------------
# Sidebar
#-----------------
st.sidebar.title("Beauty Retail BI")
page = st.sidebar.radio(
  "Navigation",
  [
   "Home",
   "Overview",
   "Store Analysis",
   "Category Analysis",
   "Data Explorer",
  ],
 )

#-----------------
# Page routing
#-----------------

if page == "Home":
    home.show()

elif page == "Overview":
    overview.show()

elif page == "Store Analysis":
    st.title("🏪 Store Analysis")
    st.info(
        "Stores analysis will be developed later."
    )

elif page == "Category Analysis":
    st.title("💄 Category Analysis")
    st.info(
        "Category analysis will be developed later."
    )

elif page == "Data Explorer":
    st.title("🔍 Data Explorer")
    st.info(
        "Data explorer will be developed later."
    )



#-----------------
# Store Analysis
#-----------------
elif page == "Store Analysis":
    st.title("🏪 Store Analysis")
    st.info(
        "Stores analysis will be added after the data is prepared."
    )

#-----------------
# Category Analysis
#-----------------
elif page == "Category Analysis":
    st.title("💄 Category Analysis")
    st.info(
        "Category analysis will be added after the category mapping is completed."
    )

#-----------------
# Data Explorer
#-----------------
elif page == "Data Explorer":
    st.title("🔍 Data Explorer")
    st.info(
        "Data explorer will be connected to the DB later."
    )