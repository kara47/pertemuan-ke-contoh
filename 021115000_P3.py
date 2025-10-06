# =================================================
# PRAKTIK PYTHON - SYNTAX, VARIABLES & COMMENTS
# Nama : Eka Putra Nugraha
# NPM : 023125255
# Skenario: Platform Konsultan Akademik Digital
# =================================================

# 1. INFORMASI BISNIS (isi sesuai skenario Anda)
nama_bisnis = "[ISI_DISINI]" 
jenis_bisnis = "Pet Shop & Grooming"
tahun_berdiri = 2025  
lokasi_bisnis = "BOGOR"  

# 2. INFORMASI PRODUK UTAMA
nama_produk = "Paket Konsultasi Riset"
harga_produk = 2500000
stok_tersedia = 15  
kategori_produk = "Researcher"  
rating_produk = 5

# 3. INFORMASI CUSTOMER TARGET
nama_customer = "Dr. Bambang (Dosen Senior"
usia_customer = 72
email_customer = "bambang@gmail.com" 
total_pembelian_sebelumnya = 2 

# 4. ASSIGNMENT INDIRECT - BACKUP DATA (WAJIB!)
# Buat backup/copy dari variabel di atas
backup_nama_bisnis = nama_bisnis  
backup_harga_produk = harga_produk  
backup_nama_customer = nama_customer
backup_stok = stok_tersedia 

# 5. PERHITUNGAN BISNIS SEDERHANA
jumlah_pembelian = 1
subtotal = harga_produk * jumlah_pembelian  
diskon_persen = 15  
nilai_diskon = subtotal * (diskon_persen / 100)  
total_bayar = subtotal - nilai_diskon  

# 6. OUTPUT INFORMASI LENGKAP
print("=" * 50)
print(f"🏪 SISTEM INFORMASI {nama_bisnis}")
print("=" * 50)
print(f"Jenis Bisnis: {jenis_bisnis}")
print(f"Lokasi: {lokasi_bisnis}")
print(f"Tahun Berdiri: {tahun_berdiri}")

print("\n📦 INFORMASI PRODUK:")
print(f"Nama Produk: {nama_produk}")
print(f"Harga: Rp {harga_produk:,}")  # format dengan koma
print(f"Stok: {stok_tersedia} unit")
print(f"Kategori: {kategori_produk}")
print(f"Rating: {rating_produk}/5.0 ⭐")

print("\n👤 INFORMASI CUSTOMER:")
print(f"Nama: {nama_customer}")
print(f"Usia: {usia_customer} tahun")
print(f"Email: {email_customer}")
print(f"Total Pembelian Sebelumnya: Rp {total_pembelian_sebelumnya:,}")

print("\n🧾 DETAIL TRANSAKSI:")
print(f"Produk: {nama_produk} x {jumlah_pembelian}")
print(f"Subtotal: Rp {subtotal:,}")
print(f"Diskon ({diskon_persen}%): Rp {nilai_diskon:,}")
print(f"TOTAL BAYAR: Rp {total_bayar:,}")

print("\n💾 DATA BACKUP TERSIMPAN:")
print(f"Backup Nama Bisnis: {backup_nama_bisnis}")
print(f"Backup Harga: Rp {backup_harga_produk:,}")
print(f"Backup Customer: {backup_nama_customer}")
print(f"Backup Stok: {backup_stok}")

print("=" * 50)
print("✅ Program selesai dijalankan!")
print(f"📚 NPM: 023125259")
print("=" * 50)