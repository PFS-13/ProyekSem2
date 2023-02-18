import os
def isNameExist(nama) :
    read = open("Phone.txt", "r")
    while True:
        line = read.readline()
        if not line:
            break
        elif line.find(",") == -1 :
            continue
        koma = line.index(",")
        name = line[:koma]
        if name == nama :
            read.close()
            return True
    read.close()
    return False

def isNumberExist(no) :
    read = open("Phone.txt", "r")
    while True:
        line = read.readline()
        if not line:
            break
        elif line.find(",") == -1 :
            continue
        koma = line.index(",")
        Nomor = line[koma + 1:]
        if no == Nomor :
            read.close()
            return True
    read.close()
    return False

def getContact(nama) :
    read = open("Phone.txt", "r")
    lin = 0
    data = {"Nama":"","NO":"","Line":""}
    while True:
        line = read.readline()
        lin = lin + 1
        if not line:
            break
        elif line.find(",") == -1 :
            continue
        koma = line.index(",")
        name = line[:koma]
        if name == nama :
            no = line[koma + 1:]
            data["Nama"] = nama;
            data["NO"] = no;
            data["Line"] = lin;
            read.close()
            return data

def addContact() :
    nama = input("Masukkan Nama \t\t: ")
    if isNameExist(nama) :
        while(isNameExist(nama)) :
            nama = input("Nama yang diinputkan sudah ada, harap masukkan kembali yang berbeda : ")
    no = input("Masukkan No \t\t: ")
    if(isNumberExist(no)) :
        while(isNumberExist(no)) :
            no = input("No Telepon yang dimasukkan sudah ada, harap masukkan kembali \t: ")
    file = open("Phone.txt", "a")
    file.write(nama + "," +  no + "\n")
    file.close()

def showList() :
    print("Nama \t\t No Telepon\n")
    read = open("Phone.txt", "r")
    while True:
        line = read.readline()
        if not line:
            break
        elif line.find(",") == -1 :
            continue
        koma = line.index(",")
        name = line[:koma]
        no = line[koma + 1:]    
        print(name + "\t\t" + no)
    read.close()
    os.system("pause")

def updateContact() :
    nama = input("Masukkan nama kontak yang ingin diubah :")
    if isNameExist(nama) :
        data = getContact(nama)
        print("Nama \t: " + data["Nama"])
        print("Kontak \t: " + data["NO"])
        print("Masukkan -- pada bagian yang tidak ingin diubah")
        updName = input("Masukkan Nama baru \t: ")
        if isNameExist(updName) :
            while(isNameExist(updName)) :
                updName = input("Nama yang diinputkan sudah ada, harap masukkan kembali yang berbeda : ")
        updNo = input("Masukkan No Baru \t: ")
        if(isNumberExist(updNo)) :
            while(isNumberExist(updNo)) :
                updNo = input("No Telepon yang dimasukkan sudah ada, harap masukkan kembali \t: ")
        newName = data["Nama"] if updName == "--" else updName
        newNo = data["NO"] if updNo == "--" else updNo
        with open('Phone.txt', 'r') as file:
            pac = file.readlines()
        pac[data["Line"] - 1] = real = newName + "," + newNo + "\n"
        with open('Phone.txt', 'w') as file:
            file.writelines(pac)
    else :
        print("Tidak ditemukan kontak '"+nama+"'")
        os.system("pause")
        
def deleteContact() :
    nama = input("Masukkan kontak yang ingin dihapus : ")
    if isNameExist(nama) :
        data = getContact(nama)
        print("Nama \t: " + data["Nama"])
        print("Kontak \t: " + data["NO"])
        c = input("Yakin kontak ini akan dihapus ? \nKetik selain y/Y jika ingin dibatalkan : ")
        if c == 'y' or c == 'Y' :
            with open("Phone.txt", "r") as f:
                lines = f.readlines()
            with open("Phone.txt", "w") as f:
                i = 0
                for line in lines:
                    i+=1
                    if i != data["Line"]:
                        f.write(line)
    else :
        print("Tidak ditemukan kontak '" + nama + "'")
        os.system("pause")
def searchContact() :
    name = input("Masukkan nama kontak yang ingin dicari : ")
    if isNameExist(name):
        data = getContact(name)
        print("Nama \t: " + data["Nama"])
        print("Nomor \t: " + data["NO"])
    else :
        print("Nama tersebut tidak terdaftar")
    os.system("pause")
            
choice = 1
while (choice is not 0) :
    os.system("cls")
    print("="*30)
    print(" "*10 + "PHONE BOOK")
    print("="*30)
    print("\n1.Lihat list Nomor Telephone")
    print("\n2.Tambah Kontak")
    print("\n3.Ubah Kontak")
    print("\n4.Hapus Kontak")
    print("\n5.Cari Kontak")
    print("\n0.Keluar")
    choice = int(input("\n\nMasukkan pilihan anda : "))
    os.system("clear")
    if choice is 1 :    
        showList()
    elif choice is 2 : 
        addContact()
    elif choice is 3 :
        updateContact()
    elif choice is 4 : 
        deleteContact()
    elif choice is 5 :
        searchContact()
    elif choice is 0 :
        exit
    else :
        print("Maaf, inputan anda salah.\nHarap coba kembali")
        os.system("pause")
