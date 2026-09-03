import streamlit as st


def show():
    st.title("Welcome to Beauty Retail BI 👋")

    st.subheader("North American Beauty Retail Analytics")

    st.markdown("---")

    st.write(
        """
        This dashboard provides interactive visualizations 
        and insights into the North American beauty retail market.
        """
    )

    st.markdown("### Key Metrics")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Stores", "-")

    with col2:
        st.metric("Countries", "2")

    with col3:
        st.metric("Beauty Categories", "-")

    with col4:
        st.metric("Data Status", "In Progress")

    st.markdown("---")

    st.markdown("### Project Overview")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 📊 Data Analysis")
        st.write("Analyze data and market trends.")

    with col2:
        st.markdown("### 🏪 Retail Stores")
        st.write("Explore stores across North America.")

    with col3:
        st.markdown("### 💄 Product Categories")
        st.write("Analyze product categories and their performance.")