# scraper-jadwal-sholat
Scraper jadwal sholat dari KEMENAG Indonesia.

## Inisialisasi & pengetahuan.

Kemungkinan website KEMENAG menggunakan _framework_ PHP CI (_Code Igniter_). Setiap kali kita melakukan `request`, maka yang pertama kali di cek adalah `session` pada `cookies`. Jadi, jika `session` tidak ditemukan.

Maka halaman hanya akan dimuat secara standar, yaitu tanpa memuat `<option></option>` untuk pilihan Provinsi dan Kabupaten. Oleh sebab itu, ketika melakukan `request` pertama kali, kita harus menyimpan `cookies` tujuannya untuk di gunakan pada `request` berikutnya.

Misal :

```python
import requests

url_awal = "https://bimasislam.kemenag.go.id/jadwalshalat"

sesi = requests.session()
inisialisasi = sesi.get(url_awal)

data_cookies = inisialisasi.cookies



```
