import streamlit as st
import time

# --- 1. Fungsi untuk Memuat CSS Kustom ---
def local_css(file_name):
    """Membaca file CSS lokal dan memasukkannya ke Streamlit."""
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"File CSS '{file_name}' tidak ditemukan. Pastikan file berada di direktori yang sama.")

# Panggil fungsi untuk memuat CSS
local_css("style.css")

# --- 2. Konfigurasi Halaman & Variabel 🎂 ---
st.set_page_config(layout="centered", page_title="Happy Birthday!")

# Ganti dengan nama penerima yang sebenarnya
nama_penerima = "Khaerunnisah Indri Wijaya" 
# Ganti dengan path ke file video Anda (contoh: 'video_ultah.mp4')
video_path = 'path_ke_video_anda.mp4' 
# Ganti dengan path ke file foto prank Anda
prank_foto_path = 'prank_photo.jpg' # PENTING: Sediakan file ini di folder yang sama

# --- 3. Konten Utama Halaman Ulang Tahun ---

st.markdown('<div class="birthday-card">', unsafe_allow_html=True)

# Judul Utama
st.markdown(f'# 🎉 Selamat Ulang Tahun, {nama_penerima}! 🎉', unsafe_allow_html=True)

st.markdown("---")

# --- BAGIAN VIDEO 🎥 ---
st.markdown("### Spesial untukmu! ✨")
try:
    # Menggunakan st.video() dengan parameter yang sudah diperbarui
    st.video(video_path, format="video/mp4", start_time=0) 
    st.caption("HAPPY BIRTHDAY SAYANGKUU!! WISHING U A LIFETIME OF HAPPINESS!")
except Exception:
    # Pesan kesalahan jika video tidak ditemukan atau format tidak didukung
    st.warning(f"Video gagal dimuat. Pastikan file '{video_path}' ada di direktori yang sama atau URL valid.")
# --- AKHIR BAGIAN VIDEO ---

st.markdown("---")

# Pesan Ulang Tahun
st.markdown("""
<div class="message-box">
    <p>Selamat ulang tahun ya, sayangku!
        Semoga kamu selalu panjang umur, sehat, diberkahi dalam semua hal, dikuatkan dalam hal apapun, dipermudah semua keinginan kamu.
        Aku doain semua cita-cita dan harapanmu bisa tercapai, dapet kerjaan yang bikin kamu nyaman.
        Pasti aku doain 
        Semoga apa yang kamu usahain dilancarkan Allah 💖🎂</p>
    <p class="signature">- Dari FAUZI</p>
</div>
""", unsafe_allow_html=True)

# Tombol interaktif (Prank)
st.markdown('<div class="center-button">', unsafe_allow_html=True)
if st.button('JANGAN DI KLIK! 🎈'):
    st.balloons() # Animasi balon Streamlit
    
    # Placeholder untuk pesan loading/prank
    prank_placeholder = st.empty()
    
    # Pesan loading
    prank_placeholder.info("MENGUNGGAH FILE RAHASIA... TUNGGU SEBENTAR...")
    time.sleep(2) # Memberi jeda 2 detik untuk efek loading
    
    # Hapus pesan loading
    prank_placeholder.empty()

    # Tampilkan foto prank
    try:
        # Menggunakan st.image() dengan parameter yang sudah diperbarui
        st.image(prank_foto_path, caption="SURPRISEEE! ❤️❤️❤️", use_container_width=True) 
        st.markdown('<h2 style="color: #ff69b4; text-align: center; font-family: \'Pacifico\', cursive;">Love you, sayangku! ❤️🧡💛💚💙💜</h2>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Foto prank '{prank_foto_path}' tidak ditemukan. Pastikan file ada di direktori yang sama.")
    
    # Animasi Hati (HTML/CSS Kustom)
    st.markdown("""
    <style>
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    .heart-animation {
        font-size: 3em;
        animation: heartbeat 1.5s infinite;
        display: inline-block;
        margin: 0 10px;
        color: #ff0000;
    }
    </style>
    <div style="text-align: center; margin-top: 30px;">
        <span class="heart-animation">❤️</span>
        <span class="heart-animation" style="animation-delay: 0.5s;">🧡</span>
        <span class="heart-animation" style="animation-delay: 1s;">💛</span>
    </div>
    """, unsafe_allow_html=True)


st.markdown('</div>', unsafe_allow_html=True)