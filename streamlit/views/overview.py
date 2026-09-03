import streamlit as st
import pandas as pd


def show():

    st.title("📊 Overview")
    st.header("North American Beauty Retail Market")

    # -------------------------
    # Sample data
    # -------------------------

    data = {
        "Country": [
            "United States",
            "United States",
            "United States",
            "Canada",
            "Canada",
            "Canada",
        ],
        "Category": [
            "Cosmetics",
            "Skincare",
            "Haircare",
            "Cosmetics",
            "Skincare",
            "Haircare",
        ],
        "Stores": [
            1200,
            950,
            780,
            320,
            280,
            210,
        ],
    }

    df = pd.DataFrame(data)

    # -------------------------
    # Filters
    # -------------------------

    st.markdown("### Filters")

    selected_country = st.selectbox(
        "Select Country",
        ["All"] + sorted(df["Country"].unique().tolist())
    )

    if selected_country != "All":
        filtered_df = df[df["Country"] == selected_country]
    else:
        filtered_df = df


    # -------------------------
    # Key Metrics
    # -------------------------

    total_stores = filtered_df["Stores"].sum()
    total_countries = filtered_df["Country"].nunique()
    total_categories = filtered_df["Category"].nunique()

    st.markdown("### Key Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Stores",
            f"{total_stores:,}"
        )

    with col2:
        st.metric(
            "Countries",
            total_countries
        )

    with col3:
        st.metric(
            "Beauty Categories",
            total_categories
        )

    st.markdown("---")

    # -------------------------
    # Store Distribution
    # -------------------------

    st.markdown("### Store Distribution by Country")

    country_data = (
        filtered_df.groupby("Country")["Stores"]
        .sum()
        .reset_index()
    )

    st.bar_chart(
        country_data,
        x="Country",
        y="Stores"
    )

    # -------------------------
    # Category Analysis
    # -------------------------

    st.markdown("### Stores by Beauty Category")

    category_data = (
        filtered_df.groupby("Category")["Stores"]
        .sum()
        .reset_index()
    )

    st.bar_chart(
        category_data,
        x="Category",
        y="Stores"
    )

    # -------------------------
    # Data Explorer
    # -------------------------

    st.markdown("### Sample Data")

    st.dataframe(
        df,
        use_container_width=True
    )