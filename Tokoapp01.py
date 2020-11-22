from os import system
from datetime import datetime 

def print_menu():
	system("cls")
	print("Selamat datang di toko baju dan pakaian\n[1]. Lihat daftar item\n[2]. Tambah item\n[3]. Cari Item\n[4]. Update Item\n[5]. Hapus item\n[Q]. Keluar")

def print_header(msg):
	system("cls")
	print(msg)

def not_empty(container):
	if len (container) != 0:
		return True
	else:
		return False

def verify_ans(char):
	if char.upper() == "Y":
		return True
	else:
		return False

def print_data(id_contact=None, harga=True, all_data=False):
	if id_contact != None and all_data == False:
		print(f"ID : {id_contact}")
		print(f"Jenis Pakaian : {daftar_pakaians}")
		print(f"HARGA : {daftar_pakaians['Harga']}")
	elif all_data == True:
		for every_pakaian in daftar_pakaians:
			Jenis_pakaian = every_pakaian
			Harga = daftar_pakaians[every_pakaian]["Harga"]
			print(f"JENIS PAKAIAN : {Jenis_pakaian} - HARGA : {Harga}")


def view_daftar_pakaian():
	print_header("Daftar Kontak Yang Tersimpan")
	if not_empty(daftar_pakaians):
		print_data(all_data=True)
	else:
		print("Maaf tidak ada pakaian yang tersimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def create_id(name, harga):
	hari_ini = datetime.now()
	tahun = hari_ini.year
	bulan = hari_ini.month
	hari = hari_ini.day
	counter = len(daftar_pakaians) + 1
	first = name[0].upper()
	last_4 = harga[-4:]
	id_contact = ("%04d%02d%02d-C%03d%s%s" % (tahun, bulan, hari, counter, first, last_4))
	return id_contact

def add_daftar_pakaian():
	print_header("Menambahkan daftar pakaian baru")
	Jenis_pakaian = input("Jenis Pakaian \t: ")
	Harga = input("Harga \t: ")
	respon = input(f"Apakah anda yakin Menyimpan : {Jenis_pakaian} ? (Y/N)\n")
	if verify_ans(respon):
		id_contact = create_id(name=Jenis_pakaian, harga=Harga)
		daftar_pakaians[id_contact] = {
			"Nama" : Jenis_pakaian,
			"Harga" : Harga
		}
	else:
		print("Data batal disimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def searching(daftar_pakaian):
	for id_contact in daftar_pakaians:
		if daftar_pakaians[id_contact]["Nama"] == daftar_pakaian:
			return id_contact 
	else:
		return False

def find_daftar_pakaian():
	print_header("Mencari Pakaian")
	Jenis_pakaian = input("Jenis pakaian yang dicari : ")
	exists = searching(Jenis_pakaian)
	if exists:
		print("Data ditemukan")
		print_data(id_contact=exists)
	else:
		print("Data yang dicari tidak ada")
	input("Tekan ENTER untuk kembali ke MENU")

def update_daftar_pakaian():
	print(f"Nama Lama : {daftar_pakaians[Jenis_pakaian]}")
	new_name = input("Masukkan Nama baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		daftar_pakaians[Jenis_pakaian] = new_name
		
		print("Data Telah di simpan")
		print_data(id_contact)
	else:
		print("Data Batal diubah")
def delete_pakaian():
	print_header("MENGHAPUS Daftar ITEM")
	nama = input("Nama Item yang akan Dihapus : ")
	exists = searching(daftar_pakaians)
	if exists:
		print_data(id_contact=exists)
		respon = input(f"Yakin menghapus {nama} ? (Y/N)")
		if verify_ans(respon):
			del daftar_pakaians[exists]
			print("Data Telah dihpus")
		else:
			print("Data Batal dihapus")
	else:
		print("Data tidak ada")
	input("Tekan ENTER untuk kembali ke MENU")

def check_user_input(char):
	if char == "Q":
		print("Semoga harimu menyenangkan... Bye!!!.....")
		return True
	elif char == "1":
		view_daftar_pakaian()
	elif char == "2":
		add_daftar_pakaian()
	elif char == "3":
		find_daftar_pakaian()
	elif char == "4":
		update_daftar_pakaian()
	elif char == "5":
		delete_pakaian()

daftar_pakaians ={
	"Tshirt" : {
		"Harga" : "12000"
	}
	,
	"Kemeja" : {
		"Harga" : "10000"
	}
}

stop = False


while not stop :
	print_menu()
	user_input = input("Pilihan : ")
	stop = check_user_input(user_input)