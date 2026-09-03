import streamlit as st


def show():
    st.title("📊 Overview")

    st.subheader("North American Beauty Retail Market")

    st.markdown("---")

    # Key Metrics
    st.markdown("### Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Total Stores",
            value="—"
        )

    with col2:
        st.metric(
            label="United States",
            value="—"
        )

    with col3:
        st.metric(
            label="Canada",
            value="—"
        )

    with col4:
        st.metric(
            label="Beauty Categories",
            value="—"
        )

    st.markdown("---")

    # Market Overview
    st.markdown("### Market Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Store Distribution")
        st.info(
            "Store distribution analysis will be added "
            "after the retail data is prepared."
        )

    with col2:
        st.markdown("#### Category Performance")
        st.info(
            "Category performance analysis will be added "
            "after the category data is prepared."
        )

    st.markdown("---")

    # Data Status
    st.markdown("### Data Pipeline Status")

    st.write("Census / Open Data")

    st.progress(0.25)

    st.write(
        "Python ETL → MariaDB → Analytics → Streamlit"
    )