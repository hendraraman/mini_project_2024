import cv2
import numpy as np
import streamlit as st


if "current_level" in st.session_state:
    if st.session_state["current_level"] == 1:
    # Load the image
        img = cv2.imread('all_data/level_images/man_blur.png')
        st.subheader("The original image is ")
        st.image(img)  

        # Define the Laplacian kernel
        # laplacian_kernel = np.array([[0, 1, 0],
        #                               [1, -4, 1],
        #                               [0, 1, 0]])

        laplacian_kernel = np.array([[-1, -1, -1],
                                    [-1, 8, -1],
                                    [-1, -1, -1]])
        st.subheader("The sharpened image is ")

        # Apply the Laplacian kernel to each color channel
        sharpened = np.zeros_like(img, dtype=np.float32)
        for i in range(3):
            sharpened[:, :, i] = cv2.filter2D(img.astype(np.float32)[:, :, i], -1, laplacian_kernel)

        # Merge the Laplacian with the original image
        sharpened = cv2.addWeighted(img.astype(np.float32), 1, sharpened, 0.5, 0)

        # Convert the sharpened image back to 8-bit unsigned integer
        sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)
        st.image(sharpened)
        # Display the sharpened image
        cv2.imshow('Sharpened Image', sharpened)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    else:
        st.header("You are not in the correct level to view this page")
else:
    st.header("You are not in the correct level to view this page")