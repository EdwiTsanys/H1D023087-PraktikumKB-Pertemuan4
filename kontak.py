import os
import pickle

# File penyimpanan kontak
FILE_NAME = "contacts.pkl"

# Cek apakah file kontak sudah ada, jika tidak, buat kosong
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "rb") as file:
        contacts = pickle.load(file)
else:
    contacts = {}

# Fungsi menyimpan kontak ke file
def save_contacts():
    with open(FILE_NAME, "wb") as file:
        pickle.dump(contacts, file)

# Fungsi menambahkan kontak
def add_contact():
    name = input("Masukkan nama kontak: ").strip()
    phone = input("Masukkan nomor telepon: ").strip()
    
    if name in contacts:
        print("Kontak dengan nama ini sudah ada!")
    else:
        contacts[name] = phone
        save_contacts()
        print("Kontak berhasil ditambahkan!")

# Fungsi menampilkan semua kontak
def show_contacts():
    if not contacts:
        print("Tidak ada kontak yang tersimpan.")
    else:
        print("\nDaftar Kontak:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

# Fungsi mencari kontak berdasarkan nama
def search_contact():
    name = input("Masukkan nama yang ingin dicari: ").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Kontak tidak ditemukan.")

# Fungsi menghapus kontak
def delete_contact():
    name = input("Masukkan nama kontak yang akan dihapus: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan.")

# Fungsi utama
def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== MENU MANAJEMEN KONTAK ===")
        print("1. Tambah Kontak")
        print("2. Lihat Semua Kontak")
        print("3. Cari Kontak")
        print("4. Hapus Kontak")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            add_contact()
        elif pilihan == "2":
            show_contacts()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == "3":
            search_contact()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == "4":
            delete_contact()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == "5":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
