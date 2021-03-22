import streamlit as st
import numpy as np
import pandas as pd
from mysql.connector import Error
import mysql.connector
import random
from test import test

def main():
    st.title('아직 미정')
    menu=['문제','기록']
    choice=st.sidebar.selectbox('메뉴',menu)

    if choice=='문제':
        test()
        

 








if __name__=='__main__':
    main()

    
