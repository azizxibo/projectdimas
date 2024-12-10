import streamlit as st
from PIL import Image
from io import BytesIO

# Judul aplikasi
st.title("Aplikasi Sederhana Rotasi Gambar")

# Upload gambar
uploaded_file = st.file_uploader("Unggah gambar Anda", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Baca gambar
    image = Image.open(uploaded_file)
    
    # Tampilkan gambar asli
    st.image(image, caption="Gambar Asli", use_column_width=True)
    
    # Pilih derajat rotasi
    angle = st.slider("Rotasi (derajat):", 0, 360, 0)
    
    # Rotasi gambar
    rotated_image = image.rotate(angle, expand=True)
    
    # Tampilkan gambar setelah rotasi
    st.image(rotated_image, caption=f"Gambar Diputar {angle}°", use_column_width=True)
    
    # Pilih format unduhan
    format_option = st.radio("Pilih format unduhan:", options=["PNG", "JPEG"])
    
    # Tombol unduh gambar
    img_byte_array = BytesIO()
    rotated_image.save(img_byte_array, format=format_option)
    img_byte_array = img_byte_array.getvalue()
    
    st.download_button(
        label="Unduh Gambar",
        data=img_byte_array,
        file_name=f"rotated_image.{format_option.lower()}",
        mime=f"image/{format_option.lower()}",
    )
