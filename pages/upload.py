import streamlit as st

if "upload" not in st.session_state:
    st.subheader("Nothing to upload")
    
elif st.session_state["upload"] == True:
    st.subheader("Upload the image of the dog")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        st.write("Image uploaded successfully")
        st.write("Do you want to return the dog to the owner?")
        if st.button("Yes"):
            st.write("Dog is returned to the owner")
        else:
            st.write("Dog is not returned to the owner")
            
else:
    st.write("Nothing to upload for now !")