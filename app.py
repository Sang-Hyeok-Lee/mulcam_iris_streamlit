# -*- coding:utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scikit_learn as sklearn
import plotly

def main():
    st.markdown("# Hello World")
    st.write(np.__version__)
    st.write(pd.__version__)
    st.write(plt.__version__)
    st.write(sns.__version__)
    st.write(sklearn.__version__)
    st.write(plotly.__version__)
if __name__ == "__main__":
    main()
