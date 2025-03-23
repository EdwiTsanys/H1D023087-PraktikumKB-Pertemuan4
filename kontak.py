import os # untuk membersihkan layar terminal agar tampilan lebih rapi.
import pickle  # untuk menyimpan dan membaca data kontak dari file

# File tempat menyimpan data kontak
FILE_NAME = "contacts.pkl"

# Cek apakah file kontak sudah ada, jika tidak, buat dictionary kosong
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "rb") as file:
        contacts = pickle.load(file)  # Memuat data kontak dari file
else:
    contacts = {}  # Jika file belum ada, buat dictionary kosong

# Fungsi untuk menyimpan kontak ke dalam file
def save_contacts():
    with open(FILE_NAME, "wb") as file:
        pickle.dump(contacts, file)  # Menyimpan dictionary kontak ke dalam file menggunakan pickle

# Fungsi untuk menambahkan kontak baru
def add_contact():
    name = input("Masukkan nama kontak: ").strip()  # Input nama kontak
    phone = input("Masukkan nomor telepon: ").strip()  # Input nomor telepon

    if name in contacts:
        print("Kontak dengan nama ini sudah ada!")  # Cek apakah nama sudah ada di kontak
    else:
        contacts[name] = phone  # Menambahkan kontak ke dictionary
        save_contacts()  # Menyimpan kontak ke file
        print("Kontak berhasil ditambahkan!")

# Fungsi untuk menampilkan semua kontak yang tersimpan
def show_contacts():
    if not contacts:
        print("Tidak ada kontak yang tersimpan.")  # Cek jika kontak masih kosong
    else:
        print("\nDaftar Kontak:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")  # Menampilkan semua kontak dalam format "Nama: Nomor"

# Fungsi untuk mencari kontak berdasarkan nama
def search_contact():
    name = input("Masukkan nama yang ingin dicari: ").strip()  # Input nama yang dicari
    if name in contacts:
        print(f"{name}: {contacts[name]}")  # Menampilkan kontak jika ditemukan
    else:
        print("Kontak tidak ditemukan.")  # Pesan jika kontak tidak ada

# Fungsi untuk menghapus kontak berdasarkan nama
def delete_contact():
    name = input("Masukkan nama kontak yang akan dihapus: ").strip()  # Input nama yang akan dihapus
    if name in contacts:
        del contacts[name]  # Menghapus kontak dari dictionary
        save_contacts()  # Menyimpan perubahan ke file
        print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan.")  # Pesan jika kontak tidak ada

# Fungsi utama untuk menampilkan menu dan menangani pilihan pengguna
def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # Membersihkan layar (Windows: cls, Linux/Mac: clear)
        print("=== MENU MANAJEMEN KONTAK ===")
        print("1. Tambah Kontak")
        print("2. Lihat Semua Kontak")
        print("3. Cari Kontak")
        print("4. Hapus Kontak")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")  # Input pilihan menu

        if pilihan == "1":
            add_contact()  # Panggil fungsi untuk menambahkan kontak
        elif pilihan == "2":
            show_contacts()  # Panggil fungsi untuk menampilkan kontak
            input("\nTekan Enter untuk kembali ke menu...")  # Menunggu input agar pengguna bisa membaca hasil
        elif pilihan == "3":
            search_contact()  # Panggil fungsi untuk mencari kontak
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == "4":
            delete_contact()  # Panggil fungsi untuk menghapus kontak
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == "5":
            print("Keluar dari program. Sampai jumpa!")
            break  # Keluar dari loop dan menghentikan program
        else:
            print("Pilihan tidak valid!")  # Menampilkan pesan jika input tidak sesuai

# Menjalankan fungsi utama jika script ini dijalankan secara langsung
if __name__ == "__main__":
    main()
