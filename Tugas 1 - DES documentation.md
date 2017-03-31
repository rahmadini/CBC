# TUGAS 1 - KIJ -  DES
- ***Rahma Dini Maghfirotul Laily          5114100027***
- ***Hilma Kamilah                         5114100188***
#
#
## Pendahuluan
DES atau singkatan dari *Data Encrypted Standard* merupakan algoritma penyandian yang diadopsi dan dibakukan oleh NBS (National Bureau Standard) yang kini menjadi NIST (National Institute of Standards and Technology) pada tahun 1977 sebagai FIPS 46 (Federal Information Processing Standard). Pada mulanya, algoritma yang kini disebut DES, memiliki panjang kunci sandi 128 bit. Namun selama proses pengadopsian, NBS melibatkan NSA (National Security Agency), dan algoritma sandi ini mengalami pengurangan ukuran kunci sandi dari 128 bit menjadi 56 bit saja.
DES merupakan algoritma enkripsi blok simetris. DES dikatakan enkripsi blok karena pemrosesan data baik enkripsi maupun dekripsi, diimplementasikan per blok (dalam hal ini 8 byte). DES dikatakan enkripsi simetris karena algoritma yang digunakan untuk enkripsi relatif atau bahkan sama persis dengan algoritma yang digunakan dalam proses dekripsi. Proses enkripsi dapat didefinisikan secara sederhana sebagai proses penterjemahan data “asli” yang “jelas” dan “kasat mata” yang dapat dipahami maknanya.
#
## Tahapan Umum
Secara umum, Data Encryption Standard (DES) terbagi menjadi tiga kelompok, yaitu pemrosesan kunci, enkripsi data 64 bit dan deskripsi data 64 bit, dimana satu kelompok saling berinteraksi satu dengan yang lainnya.

Data Encryption Standard (DES) memiliki dua fungsi input, yaitu:
1. Plaintext untuk dienkripsi dengan panjang 64 bit. 
2. Kunci dengan panjang 56 bit. 
#
Skema dari pemrosesan DES adalah seperti gambar berikut :
  
![alt text](https://github.com/rahmadini/CBC/blob/master/kunci-des.jpg)
#
Proses initial permutasi (IP) Plaintext ada tiga:
1. Plaintext 64 bit diproses di Initial Permutasi (IP) dan menyusun kembali bit untuk menghasilkan permutasi input. 
2. Langkah untuk melakukan perulangan kata dari plaintext sebanyak 16 dengan melakukan fungsi yang sama, yang menghasilkan fungsi permutasi substitusi, yang mana output akhir dari hal tersebut berisi 64 bit (fungsi dari plaintext dan kunci), masuk ke swap, dan menghasilkan preouput. 
3. Preoutput diproses, dan permutasi di inverse dari initial permutasi yang akan menghasilkan ciphertext 64bit. 
#
Proses dari kunci 56 bit :
1. Kunci melewati fungsi dari permutasi 
2. Pergeseran kunci untuk memilih perulangan permutasi kunci sebanyak 16 kali yang menghasilkan Subkey(Ki) yang diproses dengan kombinasi permutasi. 
3. Perbedaan dari Subkey(Ki) akan dilakukan pergeseran kunci yang menghasilkan kombinasi plaintext 64 bit dengan kunci 56 bit. 
#
## Metode CBC
Pada tugas kali ini, kami mengerjakan enkripsi dan dekripsi dari DES menggunakan metode Cipher Block Chaining (CBC).
#### CBC
Cipher Block Chaining(CBC) adalah modus operasi untuk block cipher (salah satu di mana urutan bit dienkripsi sebagai satu kesatuan atau blok dengan kunci cipher diterapkan pada seluruh blok). *Block Chaining Cipher* menggunakan apa yang dikenal sebagai vektor inisialisasi(**IV**) dari panjang tertentu. Salah satu karakteristik kunci adalah bahwa ia menggunakan mekanisme chaining yang menyebabkan dekripsi blok ciphertext bergantung pada semua blok ciphertext sebelumnya.
- Blok-blok saling terhubung dalam enkripsi
- Blok cipher sebelumnya digunakan dalam menghitung blok cipher selanjutnya
- Menggunakan *Initial Vector* (IV) untuk memulai proses
  
![alt text](https://github.com/rahmadini/CBC/blob/master/CBC.png)
- Penggunaan enkripsi berukuran besar dan autentikasi
  
![alt text](https://github.com/rahmadini/CBC/blob/master/CBC2.png)
#### Message Padding
- Blok terakhir masih belum terisi penuh
- Bisa ditambah nilai non-data, seperti *null*
- Bisa juga ditambah 0 beserta jumlahnya
  - Contoh: [b1 b2 b3 0 0 0 0 5]
  - Tiga bit data, *padding* 0 sebanyak 5
### Kelemahan dan Kelebihan CBC
- Setiap blok tergantung blok sebelumnya
- Perubahan pada satu blok berpengaruh pada blok selanjutnya
- Memerlukan *Initialization Vector* (IV)
  - Harus diketahui *sender* dan *receiver*
  - Memerlukan kanal komunikasi atau cara pengiriman lain yang aman
#
## Tahapan CBC
Skema dari mode operasi CBC dapat digambarkan sebagai berikut:
  ![alt text](https://github.com/rahmadini/CBC/blob/master/Skema.png)
1. Mula-mula *sender* harus meng-XOR-kan plaintext dengan **IV**
2. Kemudian dienkripsi
3. Setelah itu dikirimkan ciphertext pertamanya kepada *receiver*
4. Untuk plaintext ke-2 dan selanjutnya, sebelum dienkripsi *sender* harus meng-XOR-kan terlebih dahulu dengan ciphertext sebelumnya.
5. Setelah dienkripsi, baru pesan tersebut dapat dikirimkan kepada *receiver* sebagai ciphertext 2 dan seterusnya.
6. Pada enkripsi blok pertama C0 = IV
7. IV diberikan oleh pengguna atau dibangkitkan secara acak oleh program. IV bersifat tidak rahasia.
8. Jadi untuk menghasilkan blok ciphertext pertama (Ci), IV digunakan untuk menggantikan blok ciphertext sebelumnya C0.
9. Sebaliknya pada dekripsi, blok plaintext pertama diperoleh dengan cara meng-XOR-kan IV dengan hasil dekripsi terhadap blok ciphertext pertama.
#
Secara matematis enkripsi dan dekripsi dengan mode CBC dinyatakan sebagai berikut:
  ![alt text](https://github.com/rahmadini/CBC/blob/master/endekrip.png)
#
## Sifat-sifat dari mode operasi CBC:
1. Lebih aman dari active attacks dibandingkan mode operasi ECB
2. Error pada satu ciphertext dapat berakibat parah
3. Menutupi pola plaintext
#
#### Referensi:
1. http://www.metode-algoritma.com/2016/01/kriptografi-cipher-block-chaining-cbc.html
2. http://octarapribadi.blogspot.co.id/2016/02/enkripsi-dan-dekripsi-menggunakan-rsa.html
3. https://dirpratama.wordpress.com/2012/04/11/mengenal-data-encryption-standard-des/
4. https://dirpratama.wordpress.com/2012/04/11/mengenal-data-encryption-standard-des/
5. PPT Security 04, PPT Pak Tohari.
#
# Sekian dan Terima Kasih
