# Diffie-Hellman
# Kelompok F04 KIJ F
- Rahma Dini M    5114100027
- Hilma Kamilah   5114100188
#
# Pengertian
Diffie-Hellman key exchange adalah metode dimana subyek menukar kunci rahasia melalui media yang tidak aman tanpa mengekspos kunci. Metode ini diperlihatkan oleh Dr. W. Diffie dan Dr. M. E. Hellman pada tahun 1976 pada papernya “New Directions in Cryptography”. Metode ini memungkinkan dua pengguna untuk bertukar kunci rahasia melalui media yang tidak aman tanpa kunci tambahan. Metode ini memiliki dua parameter sistem, p dan g. Kedua parameter tersebut publik dan dapat digunakan oleh semua pengguna sistem. Parameter p adalah bilangan prima, dan paramater g (sering disebut generator) adalah integer yang lebih kecil dari p yang memiliki properti berikut ini: Untuk setiap bilangan n antara 1 dan p-1 inklusif, ada pemangkatan k pada g sehingga gk = n mod p

Penggunaan Algoritma Diffie-Hellman dalam pertukaran kunci dapat dilakukan secara aman dan efektif dalam pemrosesan jika dibandingkan dengan algoritma RSA yang cenderung lebih lama dalam pemrosesan algoritmanya. Proses pertukaran kunci ini dapat dilakukan lebih dari 2 orang asal memenuhi 2 prinsip yang telah dibahas tadi. Algoritma Diffie-Hellman lebih memfokuskan dalam perubahan nilai kunci dan proses matematis dalam penentuan kunci akhir yang sama. Sedangkan Algoritma RSA lebih memfokuskan pada saat enkripsi dan dekripsi.Kedua algoritma tersebut memiliki tingkat keamanan yang relatif sama kuatnya dan implementasinya pun banyak digunakan di dunia keamanan jaringan. KeduaAlgoritma ini sama-sama mengandalkan kesulitan pemfaktoran dalam bilangan yang bernilai sangat besar.Pertukaran kunci dengan cara yang aman dapat dilakukan dengan algoritma Diffie-Hellman dan algoritma RSA.
#
# Langkah-langkah
- Pilih  bilangan  prima  yang  besar,  p  dan  bilangan integer  yang  tidak  melebihi  dari  nilai  p,  g,  biasa disebut  bilangan  basis  atau  generator.  Kedua bilangan tersebut dapat diketahui secara publik.
- Pilih  sebuah  bilangan  acak  oleh  pengirim,  x, bilangan ini tidak boleh diketahui oleh orang lain.
- Pilih  sebuah  bilangan  acak  oleh  penerima,  y, bilangan ini tidak boleh diketahui oleh orang lain.
- Pengirim  menghitung  A  =  gxmod  p.  Bilangan  A ini dapat diketahui secara public
- Penerima  menghitung  B  =  gy  mod  p.  Bilangan  B ini dapat diketahui secara publik.
- Lakukan  pertukaran  bilangan  A  dan  B  terhadap pengirim dan penerima.
- Lalu Pengirim menghitung ka = Bx mod p.
- Penerima menghitung kb = Aymod p.
- Berdasarkan  hukum  aljabar  nilai  ka  sama  dengan kb atau bisa disebut ka= kb = k. Sehingga pengirim dan  penerima  tersebut  mengetahui  kunci  rahasia tersebut “k”.
#
# Referensi
- PPT KIJ F Pak Tohari
- Code Tugas Sebelumnya
- Code Tugas Progjar
