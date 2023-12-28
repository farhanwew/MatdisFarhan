#  kode program final projek Matematika Diskrit
# Sistem Data Apotek (sorting)
#  Muhammad Naufal Arifin (5054231006)
#  Muhammad Farhan Arya wicaksono (5054231011)


import os,time

data_obat = [
    ["Parasetamol", 2022, 1, 150, 5000],
    ["Amoksisilin", 2022, 5, 100, 7000],
    ["Omeprazol", 2023,7 ,  80, 10000],
    ["Loratadin", 2022, 8, 120, 6000],
    ["Ibuprofen", 2023, 4, 90, 8000],
    ["Dexamethasone", 2023, 9, 110, 7500],
    ["Cetirizine", 2023, 12, 95, 5500],
    ["Asterol", 2023, 2, 20, 10000],
    ["Acyclovir", 2022, 6, 18, 40000]
]

sort_angka = ['1', '2', '3', '4', '5']     

nama_bulan = [
    "Januari",
    "Februari",
    "Maret",
    "April",
    "Mei",
    "Juni",
    "Juli",
    "Agustus",
    "September",
    "Oktober",
    "November",
    "Desember"
]

kriteria = ["Nama Obat", "Tahun Produksi",  "Bulan Produksi" , "Stok", "Harga"]
orderby = ["ASCENDING", 'DESCENDING']


def welocme_program(): #2 Pembukaan program 
    print("Selamat datang sistem data Apotek Jaya")
    print("ketik apa saja untuk melanjutkan :)")
    print("=" * 38)
    a = input("====> ")
    menu()
        

def menu():  #3 diberikan pilihan dua pilihan
    clear()
    print('''   
PILIH MENU
1) sort data  
2) keluar program
'''
)
    a = input("pilih menu: ") #menginput  salah satu opsi 
    if  a == '1': # jika memeilih 1 maka program lanjut ke tahap berikutnya yaitu sorting data
        clear()
        filter()
    elif a == '2':  # jika memeilih 2 maka program selesai
        clear()
        print("Sampai Jumpa :)")
        exit()
    else:           # jika inputan tidak ada pada opsi maka akan memanggil ulang fungsi menu
        salah_input()
        menu()
        
def filter(): #4 diberikan opsi untuk mensorting berdasarkan kriteria tertentu
    print(
'''
Sorting bedasarkan:
1) Nama obat
2) Tahun produksi
3) Bulan produksi
4) stok
5) harga      
''')
    
    sort = input("pilih sorting:")# menginput salah satu opsi yang ada
    
    if sort not in sort_angka:
        salah_input()
        filter()
    
    ob = order_by()  # memanggil fungsi order_by yaitu memilih cara sorting degan ASC atau DESC
    
    clear()
    merge_sort(data_obat, ob, int(sort) - 1)  # memanggil fungsi merge sort. fungsi akan mensorting bedasarkan kriteria yang dipilih
    
    daftar(int(sort), ob)  # menampilkan hasil sorting
    opsi_kembali()
    
    
def opsi_kembali(): 
    print("1) Kembali ke menu utama ")
    print("2) kembali ke menu sebelumnya")
    pil = input("=====>")
    if pil=="1":
        menu()
    elif pil == "2":
        clear()
        filter()
    else:
        salah_input()
        opsi_kembali()
        
        
def order_by(): # memelih cara pengurutan secara ASC atau DESC
    clear()
    print("Mengurutkan dengan:")
    print("1) DESC (nilai tertinggi ke nilai terendah)")
    print("2) ASC  (nilai terendah ke nilai tertinggi)")
    pilihan = input("=======>")
    if pilihan == "1":
        return 1
    elif pilihan == "2":  
        return 0
    else:
        salah_input()
        return order_by()
    
def daftar(sort, ob): # menampilkan semua data hasil sorting
    clear()
    print(f"<sorting berdasarkan {kriteria[sort-1]} secara {orderby[ob]}>")
    print("+----------------+----------------+----------------+------+---------+")
    print("| Nama Obat      | Tahun Produksi | Bulan Produksi | Stok | Harga   |")
    print("+----------------+----------------+----------------+------+---------+")
    for obat in data_obat:
        nama, tahun, bulan, stok, harga = obat
        print(f"| {nama:<14} | {tahun:^14} | {nama_bulan[bulan-1]:<14} | {stok:^4} |RP.{harga:^5} |")
    print()
    
def merge_sort(arr, reverse, sort): # merge sort sebagai fungsi sorting 
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Rekursi merge_sort untuk kedua bagian array
        merge_sort(left_half, reverse, sort)
        merge_sort(right_half, reverse, sort)

        i = j = k = 0

        # Penggabungan dua bagian yang telah diurutkan kembali menjadi satu array
        while i < len(left_half) and j < len(right_half):
            if (not reverse and left_half[i][sort] < right_half[j][sort]) or (reverse and left_half[i][sort] > right_half[j][sort]):
                # Pengurutan naik jika reverse=False 
                # Pengurutan turun jika reverse=True
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def clear():  # untuk menclear terminal
    time.sleep(1)
    os.system('cls')

def salah_input(): # jika salah input 
    clear()
    time.sleep(1)
    print("Maaf Anda salah memasukan input !")
    
    
    
    
welocme_program() # 1st. memulai program