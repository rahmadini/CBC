# TUGAS 1 - KIJ -  DES
- ***Rahma Dini Maghfirotul Laily          5114100027***
- ***Hilma Kamilah                         5114100188***
#
#
## Pendahuluan
DES atau singkatan dari *Data Encrypted Standard* merupakan algoritma penyandian yang diadopsi dan dibakukan oleh NBS (National Bureau Standard) yang kini menjadi NIST (National Institute of Standards and Technology) pada tahun 1977 sebagai FIPS 46 (Federal Information Processing Standard). Pada mulanya, algoritma yang kini disebut DES, memiliki panjang kunci sandi 128 bit. Namun selama proses pengadopsian, NBS melibatkan NSA (National Security Agency), dan algoritma sandi ini mengalami pengurangan ukuran kunci sandi dari 128 bit menjadi 56 bit saja.
DES merupakan algoritma enkripsi blok simetris. DES dikatakan enkripsi blok karena pemrosesan data baik enkripsi maupun dekripsi, diimplementasikan per blok (dalam hal ini 8 byte). DES dikatakan enkripsi simetris karena algoritma yang digunakan untuk enkripsi relatif atau bahkan sama persis dengan algoritma yang digunakan dalam proses dekripsi. Proses enkripsi dapat didefinisikan secara sederhana sebagai proses penterjemahan data “asli” yang “jelas” dan “kasat mata” yang dapat dipahami maknanya.
#
## Tahapan
Melakukan aksi antar client dengan server, dengan cara menjalankan dua kodingan. Dimulai dari server dahulu kemudian menjalankan client. Dengan menggunakan host dan port yang sama dapat menjalankan client dan server dengan laptop yang berbeda. Tugas ini dilakukan dengan melanjutkan tugas sebelumnya sehingga dapat saling balas-balasan. chat client - server ini dilengkapi dengan enkripsi data saat mengirim pesan dari client ke server. sebelum pesan dikirimkan, program akan menjalankan fungsi enkripsi dengan menggunakan algoritma DES-CBC. Setelah itu, server akan menerima pesan yang dikirim (server bertindak sebagai server itu sendiri dan sebagai client). Sehingga saat pesan diterima, maka data yang terenkripsi akan didekripsi terlebih dahulu
kemudian pesan akan ditampilkan dalam bentuk plaintext kembali.
#
#### Referensi
1. Tugas Pemrograman Jaringan semester 5, dosen Pak Hudan.
2. http://stackoverflow.com/questions/20830738/python-client-and-server-chat
