import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
import io

# Judul aplikasi
st.title("Image Editing Tool")

# Upload gambar
uploaded_image = st.file_uploader("Upload gambar (PNG atau JPG)", type=["png", "jpg", "jpeg"])

if uploaded_image:
    # Baca gambar
    image = Image.open(uploaded_image)

    # Slider untuk rotasi
    rotation_angle = st.slider("Rotasi Gambar (derajat)", 0, 360, 0)
    rotated_image = image.rotate(rotation_angle)

    # Slider untuk mengatur kecerahan
    brightness_factor = st.slider("Atur Kecerahan", 0.0, 2.0, 1.0)
    brightness_enhancer = ImageEnhance.Brightness(rotated_image)
    brightened_image = brightness_enhancer.enhance(brightness_factor)

    # Slider untuk zoom
    zoom_factor = st.slider("Zoom In/Out (persen)", 50, 200, 100)
    width, height = brightened_image.size
    new_size = (int(width * zoom_factor / 100), int(height * zoom_factor / 100))
    zoomed_image = brightened_image.resize(new_size)

    # Slider untuk color grading (RGB)
    red_factor = st.slider("Adjust Red", 0.0, 2.0, 1.0)
    green_factor = st.slider("Adjust Green", 0.0, 2.0, 1.0)
    blue_factor = st.slider("Adjust Blue", 0.0, 2.0, 1.0)
    
    color_enhanced_image = zoomed_image.copy()
    r, g, b = color_enhanced_image.split()
    r = r.point(lambda i: i * red_factor)
    g = g.point(lambda i: i * green_factor)
    b = b.point(lambda i: i * blue_factor)
    color_enhanced_image = Image.merge("RGB", (r, g, b))

    # Opsi untuk mengganti background
    st.subheader("Edit Background")
    background_color = st.radio("Pilih Warna Background", ["Merah", "Biru", "Putih"])

    # Membuat background sesuai pilihan
    if background_color == "Merah":
        bg_color = (255, 0, 0)
    elif background_color == "Biru":
        bg_color = (0, 0, 255)
    else:
        bg_color = (255, 255, 255)

    # Menghilangkan background asli dan mengganti dengan warna pilihan
    bg_image = ImageOps.expand(color_enhanced_image, border=10, fill=bg_color)

    # Tampilkan gambar asli dan gambar yang sudah diubah
    st.subheader("Gambar Asli")
    st.image(image, use_column_width=True)

    st.subheader("Gambar Setelah Diatur")
    st.image(bg_image, use_column_width=True)

    # Tombol unduh
    st.subheader("Download Gambar")

    # Simpan gambar hasil sebagai PNG
    buffer_png = io.BytesIO()
    bg_image.save(buffer_png, format="PNG")
    st.download_button(
        label="Download sebagai PNG",
        data=buffer_png.getvalue(),
        file_name="edited_image_with_background.png",
        mime="image/png",
    )

    # Simpan gambar hasil sebagai JPG
    buffer_jpg = io.BytesIO()
    bg_image.convert("RGB").save(buffer_jpg, format="JPEG")
    st.download_button(
        label="Download sebagai JPG",
        data=buffer_jpg.getvalue(),
        file_name="edited_image_with_background.jpg",
        mime="image/jpeg",
    )

    # Simpan gambar hasil sebagai PDF
    buffer_pdf = io.BytesIO()
    bg_image.convert("RGB").save(buffer_pdf, format="PDF")
    st.download_button(
        label="Download sebagai PDF",
        data=buffer_pdf.getvalue(),
        file_name="edited_image_with_background.pdf",
        mime="application/pdf",
    )
