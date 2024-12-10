import streamlit as st
from PIL import Image

# Judul aplikasi
st.title("Aplikasi Rotasi Gambar")

# Upload gambar
uploaded_file = st.file_uploader("Unggah gambar Anda", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Baca gambar yang diunggah
    image = Image.open(uploaded_file)
    
    # Tampilkan gambar asli
    st.subheader("Gambar Asli")
    st.image(image, caption="Gambar yang diunggah", use_column_width=True)
    
    # Slider untuk menentukan derajat rotasi
    angle = st.slider("Pilih derajat rotasi", min_value=0, max_value=360, value=0, step=1)
    
    # Rotasi gambar
    rotated_image = image.rotate(angle, expand=True)
    
    # Tampilkan gambar setelah rotasi
    st.subheader("Gambar Setelah Rotasi")
    st.image(rotated_image, caption=f"Gambar diputar {angle}°", use_column_width=True)
    
 # Tombol download
    st.download_button(
        label=f"Download Image as {format_type}",
        data=img_for_download,
        file_name=f"edited_image.{format_type.lower()}",
        mime=f"image/{format_type.lower()}" if format_type != "PDF" else "application/pdf"
    )
