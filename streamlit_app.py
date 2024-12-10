import streamlit as st
from PIL import Image, ImageEnhance
import io

# Judul aplikasi
st.title("Brightness Adjustment Tool")

# Upload gambar
uploaded_image = st.file_uploader("Upload gambar (PNG atau JPG)", type=["png", "jpg", "jpeg"])

if uploaded_image:
    # Baca gambar
    image = Image.open(uploaded_image)

    # Slider untuk mengatur kecerahan
    brightness_factor = st.slider("Atur kecerahan", 0.0, 2.0, 1.0)

    # Terapkan kecerahan
    enhancer = ImageEnhance.Brightness(image)
    brightened_image = enhancer.enhance(brightness_factor)

    # Tampilkan gambar asli dan gambar yang sudah diubah kecerahannya
    st.subheader("Gambar Asli")
    st.image(image, use_column_width=True)

    st.subheader("Gambar Setelah Diatur Kecerahannya")
    st.image(brightened_image, use_column_width=True)

    # Tombol unduh
    st.subheader("Download Gambar")

    # Simpan gambar hasil kecerahan sebagai PNG
    buffer = io.BytesIO()
    brightened_image.save(buffer, format="PNG")
    st.download_button(
        label="Download Gambar",
        data=buffer.getvalue(),
        file_name="brightened_image.png",
        mime="image/png",
    )
