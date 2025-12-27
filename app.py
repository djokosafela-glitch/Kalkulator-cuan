import streamlit as st
# Kode untuk menyembunyikan ikon GitHub dan Menu Streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .viewerBadge_container__1QS13 {display: none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Pengaturan Judul & Tema
st.set_page_config(page_title="Kalkulator Cuan & HPP", page_icon="💰")
st.title("📊 Dashboard Analisa Cuan & HPP")
st.markdown("---")

# Sidebar untuk Input
st.sidebar.header("🛠️ Input Data Produk")
nama_produk = st.sidebar.text_input("Nama Produk", "Produk Digital A")
biaya_tetap = st.sidebar.number_input("Biaya Tetap (Sewa, Gaji, dll)", min_value=0, value=1000000)
jumlah_produksi = st.sidebar.number_input("Target Jumlah Penjualan/Produksi", min_value=1, value=100)

# Input Bahan Baku / HPP
st.subheader("1. Perhitungan HPP (Harga Pokok Penjualan)")
col1, col2 = st.columns(2)
with col1:
    biaya_bahan = st.number_input("Total Biaya Bahan/Produksi", min_value=0, value=5000000)
with col2:
    biaya_operasional = st.number_input("Biaya Operasional Lainnya", min_value=0, value=500000)

hpp_per_unit = (biaya_bahan + biaya_operasional + (biaya_tetap / jumlah_produksi)) / 1

st.info(f"**HPP per Unit:** Rp {hpp_per_unit:,.0f}")

# Perhitungan Cuan
st.markdown("---")
st.subheader("2. Target Harga & Profit")
harga_jual = st.number_input("Tentukan Harga Jual per Unit (Rp)", min_value=0, value=150000)

profit_per_unit = harga_jual - hpp_per_unit
margin_profit = (profit_per_unit / harga_jual) * 100 if harga_jual > 0 else 0

# Menampilkan Hasil
c1, c2, c3 = st.columns(3)
c1.metric("Profit/Unit", f"Rp {profit_per_unit:,.0f}")
c2.metric("Margin Profit", f"{margin_profit:.2f}%")
c3.metric("Total Potensi Cuan", f"Rp {profit_per_unit * jumlah_produksi:,.0f}")

# Grafik Sederhana (Opsional)
if profit_per_unit > 0:
    st.success(f"🔥 Bagus! Anda mendapatkan cuan Rp {profit_per_unit:,.0f} per produk.")
else:
    st.error("⚠️ Peringatan: Harga jual masih di bawah HPP! Anda berisiko rugi.")
  
