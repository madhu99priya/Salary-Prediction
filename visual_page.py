import matplotlib.pyplot as plt
from config import config
import streamlit as st
import seaborn as sns
from dataset import load_df

def change_country_name(name):
    if name == "United Kingdom of Great Britain and Northern Ireland":
        return "UK"
    
    if name == "United States of America":
        return "US"
    return name

st.cache_data()
def load():
    df = load_df()
    df["Country"] = df["Country"].apply(change_country_name)
    return df

def plot_age(df):
    age = df["Age"].value_counts()
    age_df = age.to_frame()
    labels = age.index
    values = age.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=age_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        st.pyplot(fig)

st.cache_data()
def plot_remotework(df):
    remotework = df["RemoteWork"].value_counts()
    remotework_df = remotework.to_frame()
    labels = remotework.index
    values = remotework.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=remotework_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        st.pyplot(fig)

st.cache_data()
def plot_edlevel(df):
    edlevel = df["EdLevel"].value_counts()
    edlevel_df = edlevel.to_frame()
    labels = edlevel.index
    values = edlevel.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=edlevel_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        st.pyplot(fig)

st.cache_data()
def plot_country(df):
    country = df["Country"].value_counts()
    country_df = country.to_frame()
    labels = country.index
    values = country.values

    col1, col2 = st.columns(2)
    
    with col1: 
        # st.bar_chart(x=labels, y=values)
        st.bar_chart(data=country_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        st.pyplot(fig)

st.cache_data()
def plot_yearscodepro(df):
    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="YearsCodePro", hue="EdLevel", kde=True, bins=30)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="YearsCodePro", hue="RemoteWork", kde=True, bins=30)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

def plot_devtype(df):
    available_types = [col for col in config.TYPES if col in df.columns]
    missing_types = [col for col in config.TYPES if col not in df.columns]

    if missing_types:
        st.warning(f"Missing dev types (not in data): {missing_types}")

    if not available_types:
        st.error("No valid developer type columns found in the DataFrame.")
        return

    type_df = df[available_types].sum().sort_values(ascending=False).to_frame()

    col1, col2 = st.columns(2)
    
    with col1:
        st.bar_chart(data=type_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=type_df.values.flatten(), labels=type_df.index, autopct='%.0f%%')
        st.pyplot(fig)


def plot_programlang(df):
    # Check which language columns are available and missing
    available_langs = [lang for lang in config.LANGUAGE if lang in df.columns]
    missing_langs = [lang for lang in config.LANGUAGE if lang not in df.columns]

    # Warn if any are missing
    if missing_langs:
        st.warning(f"Missing language columns (not in data): {missing_langs}")

    if not available_langs:
        st.error("No valid programming language columns found in the DataFrame.")
        return

    # Create a DataFrame from the sum of language columns
    lang_df = df[available_langs].sum().sort_values(ascending=False).to_frame()

    labels = lang_df.index
    values = lang_df.values.flatten()

    # Plotting
    col1, col2 = st.columns(2)
    
    with col1: 
        st.bar_chart(data=lang_df)

    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        ax.axis('equal')
        st.pyplot(fig)


def plot_platform(df):
    # Identify available and missing platform columns
    available_platforms = [plat for plat in config.PLATFORM if plat in df.columns]
    missing_platforms = [plat for plat in config.PLATFORM if plat not in df.columns]

    # Display warning for missing columns
    if missing_platforms:
        st.warning(f"Missing platform columns (not in data): {missing_platforms}")

    if not available_platforms:
        st.error("No valid platform columns found in the DataFrame.")
        return

    # Summing the platform columns and preparing the data
    platform_df = df[available_platforms].sum().sort_values(ascending=False).to_frame()

    labels = platform_df.index
    values = platform_df.values.flatten()

    # Plotting
    col1, col2 = st.columns(2)
    
    with col1: 
        st.bar_chart(data=platform_df)

    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        ax.axis('equal')
        st.pyplot(fig)


def plot_tools(df):
    # Identify available and missing tools columns
    available_tools = [tool for tool in config.TOOLS if tool in df.columns]
    missing_tools = [tool for tool in config.TOOLS if tool not in df.columns]

    # Display warning for missing columns
    if missing_tools:
        st.warning(f"Missing tool columns (not in data): {missing_tools}")

    if not available_tools:
        st.error("No valid tool columns found in the DataFrame.")
        return

    # Summing the tools columns and preparing the data
    tools_df = df[available_tools].sum().sort_values(ascending=False).to_frame()

    labels = tools_df.index
    values = tools_df.values.flatten()

    # Plotting
    col1, col2 = st.columns(2)
    
    with col1: 
        st.bar_chart(data=tools_df)

    with col2:
        fig, ax = plt.subplots()
        ax.pie(x=values, labels=labels, autopct='%.0f%%')
        ax.axis('equal')  # Equal aspect ratio ensures the pie is circular.
        st.pyplot(fig)


def plot_salary(df):
    fig = plt.figure(figsize=(9, 7))
    ax = sns.boxplot(data=df, x="Country", y="Salary")
    plt.xticks(rotation=90)
    st.pyplot(fig)

    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="Salary", hue="EdLevel", kde=True)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="Salary", hue="Age", kde=True)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

    fig = plt.figure(figsize=(9, 7))
    ax = sns.histplot(data=df, x="Salary", hue="RemoteWork", kde=True)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    st.pyplot(fig)

def visual_page():
    df = load()
    st.header("Data Visualization :bar_chart:")
    st.write("Visualize Stack Overflow Annual Survey 2024 processed")
    
    st.markdown("## Age :birthday:")
    plot_age(df)

    st.markdown("## Remote Work :airplane_departure:")
    plot_remotework(df)

    st.markdown("## Education Level :female-teacher:")
    plot_edlevel(df)

    st.markdown("## Country :flag-vn:")
    plot_country(df)

    st.markdown("## Years of Experience :calendar:")
    plot_yearscodepro(df)
    
    st.markdown("## Developer Type :computer:")
    plot_devtype(df)

    st.markdown("## Programming Language :snake:")
    plot_programlang(df)

    st.markdown("## Platform :cloud:")
    plot_platform(df)

    st.markdown("## Tools :whale:")
    plot_tools(df)

    st.markdown("## Salary :money_with_wings:")
    plot_salary(df)