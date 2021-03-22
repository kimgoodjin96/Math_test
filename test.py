import streamlit as st
import numpy as np
import pandas as pd
from mysql.connector import Error
import mysql.connector
import random


def test():

    random_number=random.randint(1,9)
    random_number2=random.randint(1,9)
    
    st.subheader('다음 문제를 맞춰보세요.')

    st.write(str(random_number)+'X'+str(random_number2))

    answer=st.number_input('정답을 입력하세요',min_value=0)
    if random_number * random_number2 == answer:
        st.write('정답입니다')
        print('정답')


    
   

    



if __name__=='__main__':
    test()