import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Page Configuration
st.set_page_config(page_title="Gamification Analysis Dashboard", layout="wide")

# Title and Introduction
st.title("Teaching-Learning Gamification Analysis")
st.markdown("""
This interactive dashboard explores the impact of gamification strategies on student performance 
across 6 different missions and 5 key dimensions.
""")

# Load Data
@st.cache_data
def load_data():
    # Adjusted path to find the processed data from the src folder
    data_path = os.path.join('data', 'processed', 'cleaned_gamification_data.csv')
    return pd.read_csv(data_path)

try:
    df = load_data()

    # Sidebar Filters
    st.sidebar.header("Dashboard Filters")
    selected_missions = st.sidebar.multiselect(
        "Select Missions to Analyze:",
        options=sorted(df['mission'].unique()),
        default=sorted(df['mission'].unique())
    )

    # Filter data based on selection
    filtered_df = df[df['mission'].isin(selected_missions)]

    # Layout: Top Metrics
    st.subheader("Key Performance Metrics")
    categories = ['motivation', 'role_performance', 'task_completion', 'learning_interaction', 'group_integration']
    
    cols = st.columns(len(categories))
    for col, cat in zip(cols, categories):
        avg_val = filtered_df[cat].mean()
        col.metric(label=cat.replace('_', ' ').title(), value=f"{avg_val:.2f}")

    st.divider()

    # Layout: Visualizations
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Dimension Profile (Radar Chart)")
        avg_values = filtered_df[categories].mean().tolist()
        
        fig_radar = go.Figure(data=go.Scatterpolar(
            r=avg_values + [avg_values[0]],
            theta=[c.replace('_', ' ').title() for c in categories] + [categories[0].replace('_', ' ').title()],
            fill='toself',
            line_color='#1f77b4',
            name='Average Scores'
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 4])),
            showlegend=False
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    with col2:
        st.subheader("Performance Trend Analysis")
        trend_df = filtered_df.groupby('mission')[categories].mean().reset_index()
        # Reshape data for better plotting
        trend_melted = trend_df.melt(id_vars='mission', var_name='Dimension', value_name='Score')
        
        fig_line = px.line(trend_melted, x='mission', y='Score', color='Dimension', markers=True,
                          color_discrete_sequence=px.colors.qualitative.Safe)
        fig_line.update_layout(yaxis_range=[1, 4], xaxis_title="Mission Number", yaxis_title="Average Score")
        st.plotly_chart(fig_line, use_container_width=True)

    # Data Preview Section
    with st.expander("View Raw Filtered Data"):
        st.dataframe(filtered_df)

except Exception as e:
    st.error(f"Error loading data: {e}")
    st.info("Please ensure 'data/processed/cleaned_gamification_data.csv' exists.")

print("Dashboard logic is ready!")