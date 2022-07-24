# scraper-jadwal-sholat
Scraper jadwal sholat dari KEMENAG Indonesia.

## Inisialisasi & pengetahuan.

Kemungkinan website KEMENAG menggunakan _framework_ PHP CI (_Code Igniter_). Setiap kali kita melakukan `request`, maka yang pertama kali di cek adalah `session` pada `cookies`.

Jadi, jika `session` tidak ditemukan, maka halaman hanya akan dimuat secara standar, yaitu tanpa memuat `<option></option>` untuk pilihan Provinsi dan Kabupaten. Oleh sebab itu, ketika melakukan `request` pertama kali, kita harus menyimpan `cookies` tujuannya untuk di gunakan pada `request` berikutnya.

<details>
  <summary>Lihat contoh</summary>

```python
import requests

url_awal = "https://bimasislam.kemenag.go.id/jadwalshalat"

sesi = requests.session()

# ini adalah inisialisasi awal untuk mendapatkan cookies
# <option></option> masih belum di tampilkan oleh server
inisialisasi = sesi.get(url_awal)
data_cookies = inisialisasi.cookies

# ini adalah request kedua setelah kita mendapatkan cookies
# <option></option> sudah di tampilkan oleh server
ada = sesi.get(url_awal, cookies=data_cookies)
print(sesi.content)

# ... <select id="search_prov">\n\t
# <option value=\'<token>\'  >PUSAT</option> ...
# <select> ...
```
</details>

  
## Cara menggunakan modul ini
```py
from . import Sholat

jadwal = Sholat

```


#### Mencari Kota / Kabupaten misal : hulu
```py
kota = jadwal.cari_kabupaten("hulu")
print(kota) 
```
<details>
  <summary>Lihat hasil</summary>
  
```json
{
    "KAB. INDRAGIRI HULU": {"provinsi": "RIAU","x": "<tokenize>","y": "<tokenize>"},
    "KAB. ROKAN HULU": {"provinsi": "RIAU","x": "<tokenize>","y": "<tokenize>"},
    ...
    "KAB. HULU SUNGAI TENGAH": {"provinsi": "KALIMANTAN SELATAN","x": "<tokenize>","y": "<tokenize>"},
}
```
</details>

#### Mencari Provinsi misal : papua
```py
provinsi = jadwal.cari_provinsi("papua")
print(provinsi)
```
<details>
  <summary>Lihat hasil</summary>
  
```json
{
    "KAB. ASMAT": {"provinsi": "PAPUA","x": "<tokenize>","y": "<tokenize>"},
    "KAB. BIAK NUMFOR": {"provinsi": "PAPUA","x": "<tokenize>","y": "<tokenize>"},
    ...
    "KAB. BOVEN DIGOEL": {"provinsi": "PAPUA","x": "<tokenize>","y": "<tokenize>"},
    "KAB. DEIYAI": {"provinsi": "PAPUA","x": "<tokenize>","y": "<tokenize>"}
}
```
</details>


#### Menampilkan jadwal sehari 
```py
sehari = jadwal.sehari("KAB. BOVEN DIGOEL", 2022, 12, 23)
print(sehari)
```

<details>
  <summary>Lihat hasil</summary>
  
```json
{
  "prov": "PAPUA",
  "kabko": "KAB. BOVEN DIGOEL",
  "lintang": "6\u00b0 5' 52.91\" S",
  "bujur": "140\u00b0 17' 48.81\" E",
  "data": {
    "2022-12-23": {
      "tanggal": "Jumat, 23/12/2022",
      "imsak": "03:50",
      "subuh": "04:00",
      "terbit": "05:20",
      "dhuha": "05:49",
      "dzuhur": "11:41",
      "ashar": "15:08",
      "maghrib": "17:55",
      "isya": "19:11"
    }
  }
}
```
</details>


#### Menampilkan jadwal sebulan 
```py
sebulan = jadwal.sebulan("KAB. ROKAN HULU", 2022, 8)
print(sebulan)
```


<details>
  <summary>Lihat hasil</summary>
  
```json
{
  "prov": "RIAU",
  "kabko": "KAB. ROKAN HULU",
  "lintang": "0\u00b0 53' 45.22\" N",
  "bujur": "100\u00b0 18' 29.86\" E",
  "data": {
    "2022-08-01": {
      "tanggal": "Senin, 01/08/2022",
      "imsak": "04:52",
      "subuh": "05:02",
      "terbit": "06:17",
      "dhuha": "06:45",
      "dzuhur": "12:29",
      "ashar": "15:50",
      "maghrib": "18:33",
      "isya": "19:45"
    },
    "2022-08-02": {
      "tanggal": "Selasa, 02/08/2022",
      "imsak": "04:52",
      "subuh": "05:02",
      "terbit": "06:17",
      "dhuha": "06:45",
      "dzuhur": "12:29",
      "ashar": "15:50",
      "maghrib": "18:33",
      "isya": "19:44"
    },

    ...
}
```
