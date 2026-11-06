
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="World University Insights",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. THEME AND CUSTOM STYLING
# =========================================================

NAVY = "#10243A"
NAVY_LIGHT = "#183653"
GOLD = "#D4AD55"
BG = "#F4F6FA"
TEXT = "#26364A"
MUTED = "#718096"

st.markdown("""
<style>

/* MAIN APPLICATION */

.stApp {
    background-color: #F4F6FA;
    color: #26364A;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}


/* SIDEBAR */

[data-testid="stSidebar"] {
    background-color: #10243A;
}

[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: #FFFFFF !important;
}


/* SEARCH UNIVERSITY INPUT */

[data-testid="stSidebar"] [data-testid="stTextInput"] input {
    background-color: #FFFFFF !important;
    color: #26364A !important;
    -webkit-text-fill-color: #26364A !important;
    caret-color: #D4AD55 !important;
    border: 1px solid #D4AD55 !important;
    opacity: 1 !important;
}

[data-testid="stSidebar"] [data-testid="stTextInput"] input::placeholder {
    color: #718096 !important;
    -webkit-text-fill-color: #718096 !important;
    opacity: 1 !important;
}


/* SIDEBAR SELECTED TAGS */

[data-testid="stSidebar"] [data-baseweb="tag"] {
    background-color: #D4AD55 !important;
    border: 1px solid #F2DFA8 !important;
}

[data-testid="stSidebar"] [data-baseweb="tag"] * {
    color: #10243A !important;
}


/* HEADER */

.hero {
    background: linear-gradient(115deg, #10243A, #234563);
    padding: 32px 35px;
    border-radius: 16px;
    border-left: 6px solid #D4AD55;
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: clamp(38px, 4vw, 48px);
    margin-bottom: 10px;
    font-weight: 800;
    letter-spacing: -1px;
    line-height: 1.15;
}

.hero p {
    color: #DCE5EF;
    font-size: 15px;
    margin-bottom: 0;
}


/* SECTION HEADINGS */

.section-heading {
    color: #10243A;
    font-size: 22px;
    font-weight: 750;
    margin-top: 20px;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #718096;
    font-size: 13px;
    margin-bottom: 15px;
}


/* KPI CARDS */

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #E0E6EF;
    border-top: 4px solid #D4AD55;
    border-radius: 12px;
    padding: 18px;
    box-shadow: 0 3px 12px rgba(16, 36, 58, 0.05);
}

div[data-testid="stMetric"] label,
div[data-testid="stMetric"] [data-testid="stMetricValue"],
div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
    color: #10243A !important;
}


/* DASHBOARD TAB FONT VISIBILITY */

div[data-testid="stTabs"] button[role="tab"],
div[data-testid="stTabs"] button[role="tab"] *,
div[data-testid="stTabs"] button[data-baseweb="tab"],
div[data-testid="stTabs"] button[data-baseweb="tab"] *,
div[data-testid="stTabs"] [role="tab"] p,
div[data-testid="stTabs"] [role="tab"] span {
    color: #10243A !important;
    -webkit-text-fill-color: #10243A !important;
    opacity: 1 !important;
    font-weight: 700 !important;
}

/* Selected tab indicator */
div[data-testid="stTabs"] button[aria-selected="true"] {
    border-bottom: 3px solid #D4AD55 !important;
}

/* Hover state */
div[data-testid="stTabs"] button[role="tab"]:hover,
div[data-testid="stTabs"] button[role="tab"]:hover * {
    color: #183653 !important;
    -webkit-text-fill-color: #183653 !important;
    opacity: 1 !important;
}


/* INSIGHT BOXES */

.insight {
    background: #FFFFFF;
    border-left: 4px solid #D4AD55;
    border-radius: 8px;
    padding: 13px 16px;
    margin: 8px 0 18px 0;
    color: #26364A;
    font-size: 14px;
}


/* FOOTER */

.footer {
    background: #10243A;
    color: #DCE5EF;
    padding: 18px;
    border-radius: 10px;
    text-align: center;
    margin-top: 35px;
    font-size: 12px;
}

hr {
    border-color: #DCE3EC;
}


/* SIDEBAR BRANDING */
.sidebar-brand {
    padding: 12px 0 18px 0;
}

.sidebar-brand h2 {
    color: #FFFFFF !important;
    font-size: 25px;
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -0.5px;
    margin: 0;
}

.sidebar-brand h2 span {
    color: #D4AD55 !important;
}

.sidebar-tagline {
    color: #B8C7D9 !important;
    font-size: 13px;
    line-height: 1.6;
    margin-top: 12px;
}

.sidebar-info-title {
    color: #D4AD55 !important;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 10px;
}

.sidebar-info-text {
    color: #C5D1DF !important;
    font-size: 13px;
    line-height: 1.65;
}

/* COUNTRY FILTER TAGS */
[data-testid="stSidebar"] [data-baseweb="tag"] {
    background-color: #D4AD55 !important;
    border: 1px solid #F2DFA8 !important;
}

[data-testid="stSidebar"] [data-baseweb="tag"] *,
[data-testid="stSidebar"] [data-baseweb="tag"] svg {
    color: #10243A !important;
    fill: #10243A !important;
}

/* SIDEBAR FILTER ACCENTS */
[data-testid="stSidebar"] [data-testid="stSlider"] [role="slider"] {
    background-color: #D4AD55 !important;
    border-color: #D4AD55 !important;
}

/* PREDICTIVE ANALYTICS WARNING READABILITY */
[data-testid="stAlert"][data-alert-type="warning"] {
    background-color: #FFF4D6 !important;
    border: 1px solid #D4AD55 !important;
}

[data-testid="stAlert"][data-alert-type="warning"] p,
[data-testid="stAlert"][data-alert-type="warning"] span,
[data-testid="stAlert"][data-alert-type="warning"] div {
    color: #26364A !important;
    -webkit-text-fill-color: #26364A !important;
}

/* DATA EXPLORER DOWNLOAD BUTTON */
[data-testid="stDownloadButton"] button {
    background-color: #10243A !important;
    color: #FFFFFF !important;
    border: 1px solid #D4AD55 !important;
    border-radius: 9px !important;
    font-weight: 700 !important;
    padding: 10px 18px !important;
}

[data-testid="stDownloadButton"] button p,
[data-testid="stDownloadButton"] button span,
[data-testid="stDownloadButton"] button svg {
    color: #FFFFFF !important;
    fill: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}

[data-testid="stDownloadButton"] button:hover {
    background-color: #183653 !important;
    border-color: #E5C477 !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. LOAD AND PREPARE DATA
# =========================================================

DATA_PATH = (
    Path(__file__).resolve().parent
    / "WorldUniversityRankings.csv"
)


@st.cache_data
def load_data(path):

    data = pd.read_csv(
        path,
        encoding="utf-8-sig"
    )

    data.columns = (
        data.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    numeric_columns = [
        "university_rank",
        "no_of_student",
        "no_of_student_per_staff",
        "overall_score",
        "teaching_score",
        "research_score",
        "citations_score",
        "industry_income_score",
        "international_outlook_score"
    ]

    for column in numeric_columns:

        if column in data.columns:

            data[column] = pd.to_numeric(
                data[column]
                .astype(str)
                .str.replace(",", "", regex=False),
                errors="coerce"
            )

    if "international_student" in data.columns:

        data["international_student_pct"] = pd.to_numeric(
            data["international_student"]
            .astype(str)
            .str.replace("%", "", regex=False),
            errors="coerce"
        )

    return data


try:

    df = load_data(DATA_PATH)

except FileNotFoundError:

    st.error(
        "WorldUniversityRankings.csv was not found. "
        "Place the CSV file in the same folder as app.py."
    )

    st.stop()


required_columns = [
    "name_of_university",
    "location",
    "overall_score",
    "university_rank"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:

    st.error(f"Missing required columns: {missing_columns}")
    st.stop()


df = df.dropna(
    subset=["name_of_university", "location"]
).copy()

df["location"] = df["location"].astype(str).str.strip()

df = df[df["location"] != ""]


# =========================================================
# 4. SIDEBAR FILTERS AND INFORMATION
# =========================================================

# SIDEBAR BRANDING
st.sidebar.markdown(
    """
    <div class="sidebar-brand">
        <h2>
            WORLD<br>
            UNIVERSITY<br>
            <span>INSIGHTS</span>
        </h2>
        <div style="
            width: 85px;
            height: 4px;
            background: #D4AD55;
            margin-top: 15px;
        "></div>
        <div class="sidebar-tagline">
            Global Rankings.<br>
            Deeper Insights.<br>
            Smarter Decisions.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.divider()

# DASHBOARD FILTERS
st.sidebar.markdown("### Dashboard Filters")

countries = sorted(df["location"].unique().tolist())

selected_countries = st.sidebar.multiselect(
    "Select Country",
    options=countries,
    default=countries
)

valid_ranks = df["university_rank"].dropna()

if valid_ranks.empty:
    st.error("No valid university rank values were found.")
    st.stop()

min_rank = int(valid_ranks.min())
max_rank = int(valid_ranks.max())

rank_range = st.sidebar.slider(
    "University Rank Range",
    min_value=min_rank,
    max_value=max_rank,
    value=(min_rank, max_rank)
)

search_name = st.sidebar.text_input(
    "Search University",
    placeholder="Enter university name..."
)

st.sidebar.divider()

# ABOUT THIS DASHBOARD
st.sidebar.markdown(
    """
    <div class="sidebar-info-title">
        ABOUT THIS DASHBOARD
    </div>
    <div class="sidebar-info-text">
        An interactive data analytics dashboard of the
        World University Rankings 2023 dataset, providing
        insights into global university performance
        through visualization and predictive analytics.
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.divider()

# DATA SOURCE
st.sidebar.markdown(
    """
    <div class="sidebar-info-title">
        DATA SOURCE
    </div>
    <div class="sidebar-info-text">
        World University Rankings 2023<br>
        Source: Kaggle
    </div>
    """,
    unsafe_allow_html=True
)

# FILTERED DATA
filtered = df[
    df["location"].isin(selected_countries)
    & df["university_rank"].between(
        rank_range[0],
        rank_range[1]
    )
].copy()

if search_name.strip():
    filtered = filtered[
        filtered["name_of_university"].str.contains(
            search_name.strip(),
            case=False,
            na=False
        )
    ]

if filtered.empty:
    st.warning(
        "No universities match the selected filters. "
        "Please adjust your selections."
    )
    st.stop()

# =========================================================
# 5. HERO HEADER
# =========================================================

st.markdown("""
<div class="hero">
    <h1>World University Insights</h1>
    <p>
        An interactive analytics dashboard exploring global
        university rankings, institutional performance,
        and predictive insights.
    </p>
</div>
""", unsafe_allow_html=True)


st.caption(
    f"Currently displaying {len(filtered):,} universities "
    f"across {filtered['location'].nunique():,} countries."
)


# =========================================================
# 6. KPI CARDS
# =========================================================

st.markdown(
    '<div class="section-heading">Performance Overview</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Key indicators based on the selected universities.'
    '</div>',
    unsafe_allow_html=True
)


k1, k2, k3, k4, k5 = st.columns(5)


k1.metric(
    "Universities",
    f"{len(filtered):,}"
)


k2.metric(
    "Countries",
    f"{filtered['location'].nunique():,}"
)


k3.metric(
    "Average Overall Score",
    f"{filtered['overall_score'].mean():.2f}"
    if filtered["overall_score"].notna().any()
    else "N/A"
)


k4.metric(
    "Average Teaching Score",
    f"{filtered['teaching_score'].mean():.2f}"
    if "teaching_score" in filtered.columns
    and filtered["teaching_score"].notna().any()
    else "N/A"
)


k5.metric(
    "Average Research Score",
    f"{filtered['research_score'].mean():.2f}"
    if "research_score" in filtered.columns
    and filtered["research_score"].notna().any()
    else "N/A"
)


# =========================================================
# 7. CHART THEME
# =========================================================

def style_chart(fig, height=390):

    fig.update_layout(
        height=height,
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(
            family="Arial",
            color=TEXT,
            size=12
        ),
        title_font=dict(
            size=17,
            color=NAVY
        ),
        margin=dict(
            l=20,
            r=20,
            t=65,
            b=30
        ),
        legend_title_text="",
        hoverlabel=dict(
            bgcolor="#183653",
            font=dict(
                color="#FFFFFF",
                size=13
            ),
            bordercolor="#D4AD55"
        )
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="#E9EDF3",
        zeroline=False,
        tickfont=dict(color=TEXT, size=11),
        title_font=dict(color=NAVY, size=12)
    )

    fig.update_yaxes(
        showgrid=False,
        zeroline=False,
        tickfont=dict(color=TEXT, size=11),
        title_font=dict(color=NAVY, size=12)
    )

    fig.update_layout(
        legend=dict(
            font=dict(color=TEXT, size=10),
            bgcolor="rgba(255,255,255,0.85)"
        )
    )

    return fig


# =========================================================
# 8. DASHBOARD TABS
# =========================================================

overview_tab, country_tab, predictive_tab, explorer_tab = st.tabs([
    "OVERVIEW",
    "COUNTRY ANALYSIS",
    "PREDICTIVE ANALYTICS",
    "DATA EXPLORER"
])


# =========================================================
# TAB 1: OVERVIEW
# =========================================================

with overview_tab:

    st.markdown(
        '<div class="section-heading">University Performance</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Explore leading institutions and the distribution '
        'of university performance.'
        '</div>',
        unsafe_allow_html=True
    )


    col1, col2 = st.columns(2)


    with col1:

        st.subheader("Top 10 Universities by Overall Score")

        top_universities = (
            filtered.dropna(subset=["overall_score"])
            .nlargest(10, "overall_score")
            .sort_values("overall_score")
        )

        if not top_universities.empty:

            fig1 = px.bar(
                top_universities,
                x="overall_score",
                y="name_of_university",
                orientation="h",
                text="overall_score",
                color="overall_score",
                color_continuous_scale=[
                    "#B9C9DA",
                    "#183653",
                    "#D4AD55"
                ],
                labels={
                    "overall_score": "Overall Score",
                    "name_of_university": "University"
                }
            )

            fig1.update_traces(
                texttemplate="%{text:.1f}",
                textposition="outside"
            )

            fig1.update_layout(
                coloraxis_showscale=False,
                xaxis_range=[
                    0,
                    min(105, top_universities["overall_score"].max() + 12)
                ]
            )

            st.plotly_chart(
                style_chart(fig1),
                use_container_width=True
            )

        else:

            st.info("No overall score data is available for this selection.")

        st.markdown(
            '<div class="insight">'
            '<b>Insight:</b> This chart identifies the '
            'universities with the highest overall scores '
            'within the current filters.'
            '</div>',
            unsafe_allow_html=True
        )


    with col2:

        st.subheader("Distribution of Overall Scores")

        score_data = filtered.dropna(
            subset=["overall_score"]
        )

        fig2 = px.histogram(
            score_data,
            x="overall_score",
            nbins=25,
            color_discrete_sequence=[GOLD],
            labels={
                "overall_score": "Overall Score",
                "count": "Number of Universities"
            }
        )

        fig2.update_layout(
            yaxis_title="Number of Universities"
        )

        st.plotly_chart(
            style_chart(fig2),
            use_container_width=True
        )

        st.markdown(
            '<div class="insight">'
            'The score distribution helps identify where most '
            'universities are concentrated and whether high-performing '
            'institutions are less common.'
            '</div>',
            unsafe_allow_html=True
        )


    st.divider()

    col3, col4 = st.columns(2)


    with col3:

        st.subheader("University Representation by Country")

        country_counts = (
            filtered.groupby("location")
            .size()
            .reset_index(name="university_count")
            .nlargest(12, "university_count")
            .sort_values("university_count")
        )

        fig3 = px.bar(
            country_counts,
            x="university_count",
            y="location",
            orientation="h",
            color="university_count",
            color_continuous_scale=[
                "#C7D4E2",
                "#183653",
                "#D4AD55"
            ],
            labels={
                "university_count": "Number of Universities",
                "location": "Country"
            }
        )

        fig3.update_layout(
            coloraxis_showscale=False
        )

        st.plotly_chart(
            style_chart(fig3),
            use_container_width=True
        )

        st.markdown(
            '<div class="insight">'
            'This visualization shows which countries have '
            'the largest representation in the rankings dataset.'
            '</div>',
            unsafe_allow_html=True
        )


    with col4:

        st.subheader("Teaching vs. Research Performance")

        comparison = filtered.dropna(
            subset=["teaching_score", "research_score"]
        )

        fig4 = px.scatter(
            comparison,
            x="teaching_score",
            y="research_score",
            color="location",
            hover_name="name_of_university",
            opacity=0.75,
            labels={
                "teaching_score": "Teaching Score",
                "research_score": "Research Score",
                "location": "Country"
            }
        )

        # With one selected country/university, the legend adds no
        # comparison value and can look like an extra plotted point.
        if comparison["location"].nunique() <= 1:
            fig4.update_layout(showlegend=False)

        st.plotly_chart(
            style_chart(fig4),
            use_container_width=True
        )

        st.markdown(
            '<div class="insight">'
            'Compare teaching and research performance to identify '
            'how universities perform across these two dimensions.'
            '</div>',
            unsafe_allow_html=True
        )


# =========================================================
# TAB 2: COUNTRY ANALYSIS
# =========================================================

with country_tab:

    st.markdown(
        '<div class="section-heading">Country-Level Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Compare university representation and average performance '
        'across countries.'
        '</div>',
        unsafe_allow_html=True
    )


    aggregation = {
        "University_Count": ("name_of_university", "count"),
        "Average_Overall_Score": ("overall_score", "mean")
    }

    if "teaching_score" in filtered.columns:
        aggregation["Average_Teaching_Score"] = (
            "teaching_score", "mean"
        )

    if "research_score" in filtered.columns:
        aggregation["Average_Research_Score"] = (
            "research_score", "mean"
        )


    # Keep all countries in the count summary. A missing score should not
    # remove a country that still has universities in the filtered dataset.
    country_summary = (
        filtered.groupby("location")
        .agg(**aggregation)
        .reset_index()
    )

    country_score_summary = country_summary.dropna(
        subset=["Average_Overall_Score"]
    )


    left, right = st.columns(2)


    with left:

        st.subheader("Average Overall Score by Country")

        country_scores = country_score_summary.nlargest(
            15,
            "Average_Overall_Score"
        ).sort_values("Average_Overall_Score")

        fig5 = px.bar(
            country_scores,
            x="Average_Overall_Score",
            y="location",
            orientation="h",
            text="Average_Overall_Score",
            color="Average_Overall_Score",
            color_continuous_scale=[
                "#C7D4E2",
                "#183653",
                "#D4AD55"
            ],
            labels={
                "Average_Overall_Score": "Average Overall Score",
                "location": "Country"
            }
        )

        fig5.update_traces(
            texttemplate="%{text:.2f}",
            textposition="outside",
            textfont=dict(color="#183653", size=11),
            cliponaxis=False
        )

        fig5.update_layout(
            coloraxis_showscale=False,
            xaxis_range=[
                0,
                country_scores["Average_Overall_Score"].max() * 1.12
            ],
            margin=dict(l=20, r=55, t=45, b=45)
        )

        st.plotly_chart(
            style_chart(fig5, 430),
            use_container_width=True
        )

        st.markdown(
            '<div class="insight">'
            '<b>Insight:</b> This chart ranks countries by the average '
            'overall score of universities with an available score. '
            'A higher average indicates stronger average performance '
            'within the selected records.'
            '</div>',
            unsafe_allow_html=True
        )


    with right:

        st.subheader("University Count by Country")

        count_data = country_summary.nlargest(
            15,
            "University_Count"
        ).sort_values("University_Count")

        fig6 = px.bar(
            count_data,
            x="University_Count",
            y="location",
            orientation="h",
            text="University_Count",
            color="University_Count",
            color_continuous_scale=[
                "#C7D4E2",
                "#183653",
                "#D4AD55"
            ],
            labels={
                "University_Count": "Number of Universities",
                "location": "Country"
            }
        )

        fig6.update_traces(
            texttemplate="%{text:.0f}",
            textposition="outside",
            textfont=dict(color="#183653", size=11),
            cliponaxis=False
        )

        fig6.update_layout(
            coloraxis_showscale=False,
            xaxis_range=[
                0,
                count_data["University_Count"].max() * 1.12
            ],
            margin=dict(l=20, r=55, t=45, b=45)
        )

        st.plotly_chart(
            style_chart(fig6, 430),
            use_container_width=True
        )

        st.markdown(
            '<div class="insight">'
            '<b>Insight:</b> This chart compares the number of universities '
            'represented in each country. A larger count indicates greater '
            'representation in the selected rankings data, not necessarily '
            'higher average performance.'
            '</div>',
            unsafe_allow_html=True
        )


    st.subheader("Country Performance Summary")

    format_columns = {
        column: "{:.2f}"
        for column in country_summary.columns
        if column.startswith("Average_")
    }

    country_table = (
        country_summary.sort_values(
            "Average_Overall_Score",
            ascending=False,
            na_position="last"
        )
        .rename(columns={
            "location": "Country",
            "University_Count": "University Count",
            "Average_Overall_Score": "Average Overall Score",
            "Average_Teaching_Score": "Average Teaching Score",
            "Average_Research_Score": "Average Research Score"
        })
    )

    readable_format_columns = {
        column: "{:.2f}"
        for column in country_table.columns
        if column.startswith("Average ")
    }

    st.dataframe(
        country_table.style.format(readable_format_columns, na_rep="—"),
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# TAB 3: PREDICTIVE ANALYTICS
# =========================================================

with predictive_tab:

    st.markdown(
        '<div class="section-heading">Predictive Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Evaluation of machine learning models used to estimate '
        'university overall scores using institutional characteristics.'
        '</div>',
        unsafe_allow_html=True
    )


    st.info(
        "The models use four non-score institutional predictors: "
        "international student percentage, country frequency, "
        "estimated staff count, and female percentage."
    )


    # ACTUAL RESULTS FROM THE COMPLETED NOTEBOOK

    model_results = pd.DataFrame({

        "Model": [
            "Baseline (Mean)",
            "Linear Regression",
            "Random Forest"
        ],

        "Testing MAE": [
            12.228,
            9.708,
            7.340
        ],

        "Testing RMSE": [
            14.991,
            11.776,
            9.522
        ],

        "Testing R2": [
            -0.002,
            0.382,
            0.596
        ]

    })


    best_model = model_results.loc[
        model_results["Testing RMSE"].idxmin()
    ]


    m1, m2, m3 = st.columns(3)


    m1.metric(
        "Best Model",
        best_model["Model"]
    )


    m2.metric(
        "Testing MAE",
        f"{best_model['Testing MAE']:.3f}"
    )


    m3.metric(
        "Testing R²",
        f"{best_model['Testing R2']:.3f}"
    )


    st.divider()

    st.subheader("Model Performance Comparison")

    st.caption(
        "Lower MAE and RMSE indicate smaller prediction errors. "
        "Higher R² indicates better explanatory performance."
    )


    st.dataframe(
        model_results.style.format({
            "Testing MAE": "{:.3f}",
            "Testing RMSE": "{:.3f}",
            "Testing R2": "{:.3f}"
        }),
        use_container_width=True,
        hide_index=True
    )


    metric_choice = st.selectbox(
        "Select evaluation metric",
        ["Testing RMSE", "Testing MAE", "Testing R2"]
    )


    metric_chart = px.bar(
        model_results,
        x="Model",
        y=metric_choice,
        color="Model",
        color_discrete_sequence=[
            "#AAB9C9",
            "#183653",
            "#D4AD55"
        ],
        text=metric_choice,
        title=f"Model Comparison: {metric_choice}"
    )


    metric_chart.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside",
        textfont=dict(
            color="#183653",
            size=13
        ),
        cliponaxis=False
    )

    metric_chart.update_layout(
        uniformtext_minsize=11,
        uniformtext_mode="show",
        yaxis=dict(
            automargin=True,
            zeroline=True,
            zerolinecolor="#AAB9C9"
        ),
        margin=dict(
            l=40,
            r=50,
            t=75,
            b=50
        )
    )

    st.plotly_chart(
        style_chart(metric_chart, 400),
        use_container_width=True
    )


    st.divider()

    st.subheader("Random Forest Feature Importance")


    importance_data = pd.DataFrame({

        "Feature": [
            "International Student Percentage",
            "Country Frequency",
            "Estimated Staff Count",
            "Female Percentage"
        ],

        "Importance": [
            0.4636,
            0.2199,
            0.2121,
            0.1044
        ]

    })


    importance_sorted = importance_data.sort_values(
        "Importance"
    )


    importance_chart = px.bar(
        importance_sorted,
        x="Importance",
        y="Feature",
        orientation="h",
        text="Importance",
        color="Importance",
        color_continuous_scale=[
            "#C7D4E2",
            "#183653",
            "#D4AD55"
        ],
        labels={
            "Importance": "Importance Score",
            "Feature": "Institutional Characteristic"
        }
    )


    importance_chart.update_traces(
        texttemplate="%{text:.4f}",
        textposition="outside",
        textfont=dict(
            color="#183653",
            size=13
        ),
        cliponaxis=False
    )

    importance_chart.update_layout(
        coloraxis_showscale=False,
        xaxis_range=[0, 0.58],
        margin=dict(
            l=35,
            r=65,
            t=45,
            b=45
        )
    )


    st.plotly_chart(
        style_chart(importance_chart, 370),
        use_container_width=True
    )


    st.markdown(
        """
        <div class="insight">
            <b>Key finding:</b> International student percentage
            received the highest feature importance score (0.4636),
            making it the most influential predictor in the Random
            Forest model among the four selected characteristics.
        </div>
        """,
        unsafe_allow_html=True
    )


    st.subheader("Model Interpretation")


    st.write(
        "Random Forest achieved the best testing performance, "
        "with an MAE of 7.340, RMSE of 9.522, and R² of 0.596. "
        "It performed better than Linear Regression and the "
        "baseline model on the held-out test dataset."
    )


    st.markdown(
        """
        <div style="
            background-color: #FFF4CC;
            color: #263445;
            padding: 16px 18px;
            border-left: 5px solid #D4AD55;
            border-radius: 8px;
            font-size: 14px;
            line-height: 1.6;
        ">
            <b>Overfitting Consideration:</b>
            Random Forest had a training R² of 0.876 compared
            with a testing R² of 0.596. This difference suggests
            possible overfitting. Feature importance indicates
            predictive contribution, not causation.
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# TAB 4: DATA EXPLORER
# =========================================================

with explorer_tab:

    st.markdown(
        '<div class="section-heading">University Data Explorer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Explore, review, and export university records '
        'from the selected dataset.'
        '</div>',
        unsafe_allow_html=True
    )


    possible_columns = [
        "university_rank",
        "name_of_university",
        "location",
        "no_of_student",
        "international_student",
        "overall_score",
        "teaching_score",
        "research_score"
    ]

    display_columns = [
        column
        for column in possible_columns
        if column in filtered.columns
    ]


    sort_options = [
        column
        for column in [
            "university_rank",
            "overall_score",
            "name_of_university"
        ]
        if column in filtered.columns
    ]


    sort_option = st.selectbox(
        "Sort records by",
        options=sort_options
    )


    ascending = sort_option != "overall_score"


    explorer_data = filtered[
        display_columns
    ].sort_values(
        sort_option,
        ascending=ascending,
        na_position="last"
    )


    st.dataframe(
        explorer_data,
        use_container_width=True,
        hide_index=True,
        height=500
    )


    csv_data = explorer_data.to_csv(
        index=False
    ).encode("utf-8")


    st.download_button(
        label="Download Filtered University Data",
        data=csv_data,
        file_name="filtered_university_rankings.csv",
        mime="text/csv"
    )


# =========================================================
# 9. FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    <b>WORLD UNIVERSITY INSIGHTS</b><br>
    World University Rankings 2023 Dataset<br>
    Foundations of Business Analytics | Academic Project
</div>
""", unsafe_allow_html=True)