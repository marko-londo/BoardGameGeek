import streamlit as st
import pandas as pd
import holoviews as hv
import hvplot.pandas


def show():
    col1, col2, col3 = st.columns([0.3, 1, 0.1])

    with col1:
        st.write(" ")

    with col2:
        st.image(
            "https://github.com/marko-londo/Suicide-Analysis/blob/main/Resources/Images/candles.png?raw=true",
            use_column_width="auto",
        )

    with col3:
        st.write(" ")
    st.markdown(
        "<h1 style='text-align: center;'>BoardGameGeek Dashboard<br><br></h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """

    ---

    """
    )

    with col4:
        st.write(hv.render(hv_plot, backend="bokeh"))

    with col5:
        st.markdown(
            """

"""
        )
