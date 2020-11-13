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

def print_data(daftar_pakaian=None, harga=True, all_data=False):
	if daftar_pakaian != None and all_data == False:
		print(f"Jenis Pakaian : {daftar_pakaian}")
		print(f"HARGA : {daftar_pakaians[daftar_pakaian]['Harga']}")
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

def create_id_contact(name, harga):
	hari_ini = datetime.now()
	tahun = hari_ini.year
	bulan = hari_ini.month
	hari = hari_ini.day
	counter = len(contacts) + 1
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
		daftar_pakaians[Jenis_pakaian] = {
			"Harga" : Harga
		}
	else:
		print("Data batal disimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def searching(daftar_pakaian):
	if daftar_pakaian in daftar_pakaians:
		return True 
	else:
		return False

def find_daftar_pakaian():
	print_header("Mencari Pakaian")
	Jenis_pakaian = input("Jenis pakaian yang dicari : ")
	exists = searching(Jenis_pakaian)
	if exists:
		print("Data ditemukan")
		print_data(daftar_pakaian=Jenis_pakaian)
	else:
		print("Data yang dicari tidak ada")
	input("Tekan ENTER untuk kembali ke MENU")

def check_user_input(char):
	if char == "Q":
		print("Bye..")
		return True
	elif char == "1":
		view_daftar_pakaian()
	elif char == "2":
		add_daftar_pakaian()
	elif char == "3":
		find_daftar_pakaian()
	elif char == "4":
		()
	elif char == "5":
		()

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