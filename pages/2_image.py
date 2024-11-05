import streamlit as st

st.sidebar.markdown("# :sparkles: Computer Vision :sparkles:")

# https://docs.streamlit.io/develop/api-reference/widgets/st.camera_input
# returns UploadedFile object, assigned to 'picture' variable
# UploadedFile class is subclass of BytesIO. BytesIO allows you to treat bytes as in-memory file-like objects.
# https://docs.python.org/3/library/io.html#io.BytesIO
picture = st.camera_input("Computer Vision")
if picture:
    st.write("Successful!")
    # https://docs.opencv.org/3.4/index.html
    # https://docs.streamlit.io/develop/api-reference/media/st.image
    st.image(picture,channels="RGB")
    st.write("This user interface is only a test. Your image is not saved nor retained. Have fun!")

