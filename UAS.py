inventaris = {
    "1": {"nama": "rokok", "stok": 45, "harga": 20000},
    "2": {"nama": "gelas", "stok": 68, "harga": 12000},
    "3": {"nama": "kopi", "stok": 120, "harga": 3000},
}
while True:
    print("\n=== PROGRAM SISTEM INVENTARIS ===")
    print("1. tambah stok")
    print("2. kurangi stok")
    print("3. peringatan stok rendah")
    print("4. hitung total nilai barang")
    print("5. laporan penjualan")
    print("6. ekspor data ke CSV")
    print("7. keluar")
    pilihan = input("pilih menu: ")

    if pilihan == "1":
        kode = input("masukkan kode barang: ")
        if kode in inventaris:
            jumlah = int(input("masukkan jumlah yang ingin ditambahkan: "))
            inventaris[kode]["stok"] += jumlah
            print("stok berhasil ditambah.")
        else:
            print("kode barang tidak ditemukan.")

    elif pilihan == "2":
        kode = input("masukkan kode barang: ")
        if kode in inventaris:
            jumlah = int(input("masukkan jumlah yang ingin dikurangi: "))
            if inventaris[kode]["stok"] >= jumlah:
                inventaris[kode]["stok"] -= jumlah
                print("stok berhasil dikurangi.")
            else:
                print("stok tidak mencukupi.")
        else:
            print("kode barang tidak ditemukan.")

    elif pilihan == "3":
        print("\nbarang dengan stok rendah:")
        for kode, barang in inventaris.items():
            if barang["stok"] < 10:
                print(f"{barang['nama']} - Stok: {barang['stok']}")

    elif pilihan == "4":
        total = 0
        for barang in inventaris.values():
            total += barang["stok"] * barang["harga"]
        print(f"total nilai barang di inventaris: Rp{total:,}")

    elif pilihan == "5":
        print("\n=== laporan penjualan ===")
        print("belum ada data penjualan.")

    elif pilihan == "6":
        nama_file = input("masukkan nama file (contoh: inventaris.csv): ")
        with open(nama_file, mode='w') as file:
            file.write("kode,nama barang,stok,harga satuan\n")
            for kode, barang in inventaris.items():
                file.write(f"{kode},{barang['nama']},{barang['stok']},{barang['harga']}\n")
        print(f"data berhasil diekspor ke {nama_file}")

    elif pilihan == "7":
        print("keluar dari program. terima kasih.")
        break

    else:
        print("pilihan tidak valid. silakan coba lagi.")



