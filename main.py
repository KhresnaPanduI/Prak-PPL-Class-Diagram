class InstansiKesehatan:
  def __init__(self, id, nama, alamat, kontak):
    self._id = id
    self._nama = nama
    self._alamat = alamat
    self._kontak = kontak

  def setNamaInstansi(self, x):
    self._nama = x

  def setAlamatInstansi(self, x):
    self._alamat = x

  def setKontakInstansi(self, x):
    self._kontak = x

  def getNamaInstansi(self):
    return self._nama

  def getAlamatInstansi(self):
    return self._alamat

  def getKontakInstansi(self):
    return self._kontak

class Masyarakat:
  def __init__(self, id, nama, kontak):
    self._id = id
    self._nama = nama
    self._kontak = kontak

  def setNamaMasyarakat(self, x):
    self._nama = x

  def setKontakMasyarakat(self, x):
    self._kontak = x

  def getNamaMasyarakat(self):
    return self._nama

  def getKontakMasyarakat(self):
    return self._kontak

class APD:
  def __init__(self, nama, jumlah):
    self._nama = nama
    self._jumlah = jumlah

  def setNamaAPD(self, x):
    self._nama = x

  def setJumlahAPD(self, x):
    self._jumlah = x

  def getNamaAPD(self):
    return self._nama

  def getJumlahAPD(self):
    return self._jumlah

print('Masukan data')

end = False
while(end == False):
  print('1. Instansi Kesehatan: ')
  print('2. Masyarakat: ')
  print('3. APD: ')
  print('4. Selesai')
  choice = int(input('Masukan pilihan: '))

  if (choice == 1):
    id = input('id: ')
    nama = input('Nama instansi: ')
    alamat = input('Alamat Instansi: ')
    kontak = input('Kontak instansi: ')

    nama = InstansiKesehatan(id, nama, alamat, kontak)
    print('Nama: ', nama.getNamaInstansi())
    print('Alamat: ', nama.getAlamatInstansi())
    print('Kontak: ', nama.getKontakInstansi())
    print()

  elif (choice == 2):
    id = input('id: ')
    nama = input('Nama Masyarakat: ')
    kontak = input('Kontak Masyarakat: ')

    nama = Masyarakat(id, nama, kontak)

    print('Nama: ', nama.getNamaMasyarakat())
    print('Kontak: ', nama.getKontakMasyarakat())
    print()
  elif (choice == 3):
    id = input('id: ')
    nama = input('Nama APD: ')
    jumlah = input('Jumlah APD: ')

    nama = APD(nama, jumlah)

    print('Nama: ', nama.getNamaAPD())
    print('Jumlah: ', nama.getJumlahAPD())
    print()
  elif (choice == 4):
    end = True

  else:
    print('Input salah')

