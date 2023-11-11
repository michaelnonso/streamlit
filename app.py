import streamlit as st
import pandas as pd
import numpy as np
import time

if "photo" not in st.session_state:
    st.session_state["photo"] ="not done"

def change_photo_state():
    st.session_state["photo"]="done"

col1,col2,col3 = st.columns([1,2,1])

col1.markdown("""# This is my first app""")
col1.markdown("""Here is some more information""")

uploaded_photo=col2.file_uploader("Upload a Photo" ,on_change=change_photo_state)
col3.metric(label="Temperature", value="60 degrees", delta="3 degrees")
#camera_photo=col2.camera_input("Take a Photo",on_change=change_photo_state)


st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name

col2.markdown("""***""")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
    
col2.markdown("""***""")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

col2.markdown("""***""")




if st.session_state["photo"]=="done":
    progress_bar=col2.progress(100)
    for i in range(100):
        progress_bar.progress(i)
        time.sleep(0.01)
        
    col2.success("Photo successfully uploaded")

    with st.expander("Click here to Read more"):
        st.write("this is more information on that topic you where interested in")
        if uploaded_photo:
            st.image(uploaded_photo)
        elif camera_photo:
            st.image(camera_photo)
        else:
            pass
