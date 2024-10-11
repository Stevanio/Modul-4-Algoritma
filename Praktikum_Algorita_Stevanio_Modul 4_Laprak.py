# Program untuk menentukan jumlah hari dalam suatu bulan dan tahun menggunakan perulangan while

def is_leap_year(year):
    # Mengecek apakah tahun merupakan tahun kabisat
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

while True:
    # Meminta input bulan dan tahun dari pengguna
    month = int(input("Masukkan bulan (1-12): "))
    year = int(input("Masukkan tahun: "))

    # Mengecek input bulan apakah valid
    if month < 1 or month > 12:
        print("Bulan tidak valid, silakan masukkan angka 1 hingga 12.")
        continue  # Mengulangi perulangan jika input bulan tidak valid

    # Menentukan jumlah hari berdasarkan bulan
    if month == 2:
        # Jika Februari, cek apakah tahun kabisat
        if is_leap_year(year):
            days = 29
        else:
            days = 28
    elif month in [4, 6, 9, 11]:
        days = 30  # April, Juni, September, November memiliki 30 hari
    else:
        days = 31  # Selain itu memiliki 31 hari

    print(f"Jumlah hari di bulan {month} tahun {year} adalah {days} hari.")
    
    # Menanyakan apakah ingin melanjutkan
    ulangi = input("Apakah Anda ingin mengecek bulan lain? (y/n): ").lower()
    if ulangi != 'y':
        break  # Keluar dari perulangan jika pengguna tidak ingin melanjutkan
