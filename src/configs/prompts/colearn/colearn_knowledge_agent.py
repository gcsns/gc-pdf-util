colearnKnowledgeDescription = """You are Alex, a human Customer Service Representative at CoLearn responsible for assisting parents and students with inquiries about CoLearn's educational offerings. Your responses must be accurate, helpful, and based EXCLUSIVELY on the information in the CoLearn 2025 FAQ document."""

colearnKnowledgeRole = """Search in knowledge base and answer the question"""


colearnKnowledgeMdStrings = [
    """
# FAQ- CoLearn 2025

1. Q : Lokasi CoLearn dimana?
A : Kantor pusat CoLearn ada di MCC lantai 42 Sudirman, Jakarta Selatan. Alamat lengkap bisa dilihat di Google
dengan mengetik "CoLearn".

2. Q : Tersedia untuk kelas berapa aja?
A : Bimbel Online Matematika CoLearn tersedia dari kelas 4 SD - 12 SMA

3. Q : Untuk kelas 1 / 2 / 3 bisa?
A : Mohon maaf Bapak/Ibu, di CoLearn saat ini baru tersedia untuk 4 SD - 12 SMA

4. Q : Kenapa Kelas 1 - 3 tidak ada?
A : Saat ini bimbel kami fokus pada kelas 4 SD-12 SMA. Kami mempertimbangkan bahwa pembelajaran online di
tingkat tersebut lebih efektif dalam membantu siswa memahami konsep matematika dengan baik

5. Q : Mohon info bimbel untuk kelas 4?
A : Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 4 SD. 4 pertemuan per bulan (1x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/OrABEkNnKEU?si=Wa2NRtEMVk8P6MKg "

6. Q : Mohon info bimbel untuk kelas 5?
A : "Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 5 SD. 4 pertemuan per bulan (1x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/OrABEkNnKEU?si=Wa2NRtEMVk8P6MKg "

7. Q : Mohon info bimbel untuk kelas 6?
A : "Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 6 SD. 4 pertemuan per bulan (1x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/OrABEkNnKEU?si=Wa2NRtEMVk8P6MKg

8. Q : Mohon info bimbel untuk kelas 7?
A : "Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 7 SMP. 8 pertemuan per bulan (2x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/2xVerh347p4?si=cNuXJPKIWCXuLwMO "

9. Q : Mohon info bimbel untuk kelas 8?
A : "Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 8 SMP. 8 pertemuan per bulan (2x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/2xVerh347p4?si=cNuXJPKIWCXuLwMO "10. Q : Mohon info bimbel untuk kelas 9?
A : "Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 9 SMP. 8 pertemuan per bulan (2x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/2xVerh347p4?si=cNuXJPKIWCXuLwMO "

11. Q : Mohon info bimbel untuk kelas 10?
A : "Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 10 SMA. 8 pertemuan per bulan (2x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/2xVerh347p4?si=cNuXJPKIWCXuLwMO "

12.Q : Mohon info bimbel untuk kelas 11?
A : "Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 11 SMA. 8 pertemuan per bulan (2x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/2xVerh347p4?si=cNuXJPKIWCXuLwMO "13. Q : Mohon info bimbel untuk kelas 12?
A : "Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 12 SMA. 8 pertemuan per bulan (2x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/2xVerh347p4?si=cNuXJPKIWCXuLwMO "

14. Q : Selain matematika ada pelajaran apa aja untuk kelas 7 SMP?
A : "Untuk kelas 7 SMP, di bimbel online Colearn ada pilihan:
1. Paket Matematika (2x mat/minggu) - * Rp. 95.000/bulan*
2. Paket Matematika+IPA (2x mat dan 1x IPA / minggu) - * Rp. 144.000/bulan*
*Untuk IPA adalah fisika + biologi diberikan dalam bentuk rangkuman*
Durasi 60 menit/kelas

15. Q : Selain matematika ada pelajaran apa aja untuk kelas 8 SMP?
A : "Untuk kelas 8 SMP, di bimbel online Colearn ada pilihan:
1. Paket Matematika (2x mat/minggu) - * Rp. 95.000/bulan*
2. Paket Matematika+IPA (2x mat dan 1x IPA / minggu) - * Rp. 144.000/bulan*
Durasi 60 menit/kelas

16. Q : Selain matematika ada pelajaran apa aja untuk kelas 9 SMP?
A : "Untuk kelas 9 SMP, di bimbel online Colearn ada pilihan:
1. Paket Matematika (2x mat/minggu) - * Rp. 95.000/bulan*
2. Paket Matematika+IPA (2x mat dan 1x IPA / minggu) - * Rp. 144.000/bulan*
Durasi 60 menit/kelas17. Q : Selain matematika ada pelajaran apa aja untuk kelas 10 SMA?
A : "Untuk kelas 10, di bimbel online Colearn ada pilihan:
1. Paket Matematika (2x mat/minggu) - * Rp. 95.000/bulan*
2. Paket Matematika+IPA (2x mat dan 1x IPA/ minggu) - * Rp. 144.000/bulan*
*Untuk IPA adalah fisika dan kimia bergantian (sesuai silabus dari pemerintah. Biologi diberikan dalam bentuk rangkuman)*
Durasi 60 menit/kelas"

18. Q : Selain matematika ada pelajaran apa aja untuk kelas 11 SMA?
A : "Untuk kelas 11 Merdeka, di bimbel online Colearn ada pilihan:
1. Paket Matematika Merdeka (2x mat/minggu) - * Rp. 95.000/bulan*
2. Paket Matematika Merdeka+Lanjutan (3x/minggu) - * Rp. 120.000/bulan*
Durasi 60 menit/kelas
Upgrade paket:
1. Tambah Fisika / Kimia = Rp. 49.000 (1x/minggu)
2. Tambah Fisika + Kimia = Rp. 79.000 (2x/minggu)"
info_paketlain_kelas12
Selain matematika ada pelajaran apa aja untuk kelas 12 SMA?
"Untuk kelas 12
Merdeka, di bimbel online Colearn ada pilihan:
1. Paket Matematika Merdeka (2x mat/minggu) - * Rp. 95.000/bulan*
2. Paket Matematika Merdeka+Lanjutan (3x/minggu) - * Rp. 120.000/bulan*
Durasi 60 menit/kelas
Upgrade paket:
1. Tambah Fisika / Kimia = Rp. 49.000 (1x/minggu)
2. Tambah Fisika + Kimia = Rp. 79.000 (2x/minggu)"

19. Q : Untuk SD selain matematika ada apa saja?
A : Untuk SD di CoLearn fokusnya di pelajaran matematika saja Ibu20. Q : Untuk IPA kelas 7 mapel apa saja?
A : Untuk IPA kelas 7 terdiri dari Fisika dan (Biologi hanya berbentuk rangkuman saja)
21.Q : Untuk IPA kelas 8 mapel apa saja?
A : Untuk IPA kelas 8 terdiri dari Fisika dan Biologi (materi yang berjalan sesuai urutan silabus dari pemerintah)
22. Q : Untuk IPA kelas 9 mapel apa saja?
A : Untuk IPA kelas 9 terdiri dari Fisika dan Biologi (materi yang berjalan sesuai urutan silabus dari pemerintah)
23. Q : Untuk IPA kelas 10 mapel aja saja?
A : Untuk IPA kelas 10 adalah fisika dan kimia bergantian (sesuai silabus dari pemerintah. Biologi diberikan dalam bentuk rangkuman)
24. Q : Fisika/Kimia aja bisa ga?
A : Mohon maaf untuk paket Fisika/Kimia saja tidak bisa. Untuk paket tersebut pembeliannya 1 paket dengan Matematika
25. Q : Apakah ada bahasa Inggris?
A : Mohon maaf, CoLearn fokusnya di mata pelajaran matematika dan IPA saja
26. Q : Bisa untuk OSN?
A : Mohon maaf untuk OSN saat ini belum ada karena di CoLearn lebih ke pembahasan konsep materi pembelajarannya
27.Q : Gurunya tidak ke rumah ya?
A : Mohon maaf, tidak ada kelas private dan offline di CoLearn
28. Q : Apakah ada kelas private?
A : Mohon maaf, tidak ada kelas private di CoLearn29.Q : Kenapa CoLearn tidak ada offline?
A : Bimbel CoLearn hanya tersedia online. Tujuannya, agar semua murid di Indonesia bisa mendapatkan akses ke
guru-guru dengan penalaran Matematika yang kuat
30.Q : Bahasa pengantar di CoLearn menggunakan apa?
A : Pembelajaran di CoLearn full menggunakan bahasa Indonesia
31. Q : Kurikulum itu apa ya kak?
A : Kurikulum adalah rencana pembelajaran yang akan diajarkan. CoLearn menggunakan kurikulum pemerintah
(kurikulum 2013 atau merdeka)
32. Q : Pakai kurikulum apa?
A : CoLearn menggunakan kurikulum pemerintah (kurikulum 2013 atau merdeka)
33. Q : Kurikulum nasional plus bisa kak?
A : CoLearn menggunakan kurikulum pemerintah (kurikulum 2013 atau merdeka) dengan pengantar bahasa
Indonesia
34. Q : Anak saya menggunakan kurikulum IB bisa?
A : Mohon maaf untuk CoLearn menggunakan kurikulum pemerintah (kurikulum 2013 atau merdeka) dengan
pengantar bahasa Indonesia, jadi materinya berbeda
35. Q : Kalau kurikulum Cambridge apakah bisa?
A : Mohon maaf untuk CoLearn menggunakan kurikulum pemerintah (kurikulum 2013 atau merdeka) dengan
pengantar bahasa Indonesia, jadi materinya berbeda36. Q : Sekolah inter bisa?
A : Mohon maaf untuk CoLearn menggunakan kurikulum pemerintah (kurikulum 2013 atau merdeka) dengan pengantar bahasa Indonesia, jadi materinya berbeda
37. Q : Materi di CoLearn bagaimana?
A : Materi di CoLearn sesuai dengan kurikulum pemerintah (kurikulum 2013 atau merdeka) yang sedang berjalan.
38. Q : Urutan materinya ga sama kayak sekolah ya?
A : Materi di CoLearn terkadang lebih lambat atau lebih cepat dibandingkan sekolah, sehingga urutannya tidak akan selalu sama. CoLearn fokus membantu anak agar bisa paham konsep Matematika dengan guru yang mempunyai penalaran Matematika yang kuat
39. Q : Materinya bisa lebih cepat dari sekolah?
A : Materi di CoLearn terkadang lebih lambat atau lebih cepat dibandingkan sekolah, sehingga urutannya tidak akan selalu sama.CoLearn fokus membantu anak agar bisa paham konsep Matematika dengan guru yang mempunyai penalaran Matematika yang kuat
40. Q : Materinya bisa request sesuai sekolah?
A : Mohon maaf tidak bisa, materi di CoLearn sesuai dengan kurikulum pemerintah (kurikulum 2013 atau merdeka) yang sedang berjalan
41. Q : Belajar dari 0 (dasar) bisa ga?
A : Mohon maaf tidak bisa, di Colearn materinya berjalan mengikuti urutan silabus yang berjalan menggunakan Kurikulum Merdeka/2013
42. Q : Kelas baru, materi dari pertama atau mengikuti timeline silabus?
A : "Di CoLearn materi yang berjalan sesuai dengan silabus (urutan) materi dari pemerintah, untuk kelas yang terlewat bisa mengakses rangkuman materi berupa PDF. Kelas pertama dimulai sesuai dengan timeline yang ada di silabus43. Q : Kelasnya sudah berjalan, kalau anak baru bergabung gimana?
A : Di CoLearn materi yang berjalan sesuai dengan silabus (urutan) materi dari pemerintah, untuk kelas yang terlewat bisa mengakses rangkuman materi berupa PDF
44. Q : Kelasnya sudah di mulai?
A : Benar Ibu, karena di CoLearn materi yang berjalan sesuai dengan silabus (urutan) materi dari pemerintah, untuk kelas yang terlewat bisa mengakses rangkuman materi berupa PDF
45. Q : PTS itu apa konsepnya?
A : Baik, untuk materi PAS biasanya akan mereview atau mengulang materi yang sebelumnya, Ibu info_upgrade_kelas Kelas 5 tetapi pinginnya les yg untuk kelas 6 bolah? Baik ibu kakak paham, untuk pembelajaran di CoLearn sebaiknya mengikuti kelas anak saat ini. Karena di Colearn materinya berjalan mengikuti silabus pemerintah. Jika tidak mengikuti sesuai kelasanak dikhawatirkan tidak terbantu sebab materinya berbeda
46. Q : 1 kelas berapa orang?
A : {untuk kelas SD} Maksimal jumlah murid/kelas di SD adalah 30 agar semua murid bisa dapat akses kepada guru yang kompeten dan terlatih dengan harga terjangkau
47.Q : 1 kelas berapa orang?
A : {untuk SMP} Maksimal jumlah murid/kelas di SMP adalah 70 agar semua murid bisa dapat akses kepada guru yang kompeten dan terlatih dengan harga terjangkau
48. Q : 1 kelas berapa orang?
A : {untuk SMA) Maksimal jumlah murid/kelas di SMA adalah 70 agar semua murid bisa dapat akses kepada guru yang kompeten dan terlatih dengan harga terjangkau49.Q : Kenapa jumlah murid SD lebih sedikit dari SMP tapi harganya sama?
A : Dikarenakan jumlah maksimal murid SD dikelasnya setengah dari jumlah maksimal murid di SMP / SMA Ibu
50.Q : Kenapa SD pertemuannya 1 kali dalam seminggu?
A : Dikarenakan jumlah maksimal murid SD dikelasnya setengah dari jumlah maksimal murid di SMP / SMA Ibu
51. Q : Kalau saya mau ikut pertemuannya 2 kali dalam seminggu bisa untuk SD?
A : Mohon maaf tidak bisa Ibu, jika ikut dua kali dalam seminggu materinya akan sama karena tetap berjalan
sesuai dengan urutan silabus
52.Q : Untuk kelasnya seperti apa?
A : Untuk kelasnya adalah kelas pembahasan materi dimana konsep yang besar akan kami bagi menjadi
konsep-konsep kecil sehingga mudah untuk murid mengikuti dan memahami. Di dalam kelas akan diselingi
dengan soal yang dibahas bersama untuk mengetahui pemahaman murid
53. Q : Pembelajaran di CoLearn bagaimana?
A : Untuk pembelajarannya online dua arah dimana murid bisa berinteraksi dengan guru dan teman belajar
(melalui zoom) saat kelas berlangsung
54. Q : Bisa terkontrol semua ga kak dengan jumlah yg besar?
A : "Baik ibu, kakak paham kekhawatirannya, untuk guru-guru kami sudah melalui pelatihan selama 6 bulan
sebelum mengajar murid. Di CoLearn bisa coba kelasnya 1 bulan jika tidak cocok ada garansi uang kembali
100%."
55. Q : Apakah kelasnya efektif?
A : "Baik ibu, kakak paham kekhawatirannya, untuk guru-guru kami sudah melalui pelatihan selama 6 bulan
sebelum mengajar murid. Di CoLearn bisa coba kelasnya 1 bulan jika tidak cocok ada garansi uang kembali
100%."56. Q : Anak saya ADHD / inklusi / anak berkebutuhan khusus (ABK) lainnya?
A : Baik kakak paham atas yang dihadapi, namun di CoLearn kelasnya bersama-sama dengan teman lainnya dan
materi belajar menggunakan silabus kurikulum pemerintah yang sedang berjalan.
57. Q : Mulai kelasnya kapan?
A : Setelah pembayaran akan ada proses aktivasi, kemudian bisa mulai belajar sesuai jadwal yang dipilih.
58. Q : Ini waktu wib ya?
A : Benar, zona waktu yang digunakan di bimbel CoLearn yaitu zona Waktu Indonesia Barat (WIB)
59. Q : Jika berhalangan hadir bagaimana?
A : Jika berhalangan hadir, tersedia PDF materi yang bisa dipelajari secara mandiri
60.Q : Bisa ganti jadwal?
A : Jika nanti tidak cocok/bentrok, jadwal bisa diubah maksimal 1 kali
61. Q : Waktunya flexibel bisa kapan saja ya kak?
A : Untuk jadwalnya bisa pilih salah satu dari jadwal yang tersedia, bisa dicocokkan jadwal mana yang sesuai
untuk jadwal anak dan setiap minggunya akan sama
62. Q : Kalau kelas baru di buka lagi kapan?
A : Kakak belum bisa memastikan kapan kelas baru akan tersedia, Ibu. Jika ada kelas baru, materinya tetap
mengikuti silabus yang sedang berjalan
63. Q : Ada jadwal di hari minggu?
A : Mohon maaf Bapak/Ibu jadwal hari minggu di CoLearn tidak tersedia
64. Q : Kalau hari libur ada kelas pengganti?
A : Jika ada tanggal merah / hari libur nasional maka ada kelas pengganti yang akan diinfokan sebelumnya.65. Q : Jadwal kelas pengganti gimana?
A : Kemungkinan jam belajar kelas pengganti akan berbeda dengan jadwal sebelumnya. Informasi mengenai kelas
penganti akan diberitahukan di kelas dan dikirimkan melalui WA Kakak Siaga
66. Q : Klo seumpama mencoba 1 bln ternyata tidak lanjut tidak apa2 kan kak?
A : Tidak apa-apa Ibu, karena di CoLearn tidak terikat
67.Q : Bisa tanya soal?
A : "Mohon maaf, nomor ini adalah untuk pendaftaran bimbel online CoLearn.
Untuk pertanyaan soal bisa menggunakan fitur video penjelasan dengan cara:
1. Ketikkan soal di website atau foto soal dengan Google Lens
2. Pilih rujukan video penjelasan di Youtube CoLearn"
68. Q : Bisa tanya PR di kelas?
A : Mohon maaf (Bapak/Ibu) untuk bertanya PR saat kelas berlangsung tidak bisa, dikarenakan untuk kelas di
CoLearn membahas konsep dan materi yang sedang dipelajari
69.Q : Kalau ada tugas bisa konsul ngga kak?
A : "Jika ada pertanyaan tugas bisa menggunakan fitur video penjelasan (bisa akses 24 jam) dengan cara:
1. Ketikkan soal di website atau foto soal dengan Google Lens
2. Pilih rujukan video penjelasan di Youtube CoLearn"
70.Q : Semisal anak sy tidak paham materi yang dijelaskan apa bisa coba bertanya dengan tutornya?
A : "Jika ada yang belum dipahami di dalam kelas hanya bisa bertanya sesuai dengan materi yang dipelajari saat
kelas berlangsung71.Q : Bisa tanya pelajaran yang di sekolah sama gurunya?
A : Mohon maaf tidak bisa Ibu. Di dalam kelas hanya bisa bertanya sesuai dengan materi yang dipelajari saat kelas
berlangsung

72. Q : Cara daftarnya bagaimana?
A : Untuk daftar, mohon isi data berikut:
- Nama lengkap anak:
- Kelas:
- Kurikulum:
- Jadwal yang dipilih:
- No telp murid (WA & SMS):
- Email orang tua/murid (wajib):
- Nama orang tua:
- No telp orang tua (WA):
- Metode pembayaran:

Untuk pembayaran, bisa pilih metode transfer antar bank (BCA, Mandiri, BRI, BSI, BNI dan bank lain), e-wallet
(Gopay, OVO, Dana, Shopeepay) maupun Indomaret/Alfamart. Semua atas nama CoLearn."

73. Q : Bisa daftar untuk semester depan?
A : Baik kakak paham Ibu, sementara bisa pilih salah satu jadwalnya dahulu untuk amankan slotnya, jika nanti
tidak cocok/bentrok bisa ubah jadwal maksimal 1 kali. Apakah berkenan?

74. Q : Biaya pendaftarannya berapa?
A : Biayanya untuk paket matematika Rp95.000/bulan dan tidak ada biaya tambahan lainnya

75. Q : Bisa bayar langsung 1 semester?
A : Baik, untuk daftar bulan pertama pembayarannya 1 bulan terlebih dahulu (Bapak/Ibu), pada bulan berikutnya
tim perpanjangan paket akan menginfokan opsi pembayaran bulanan atau semesteran76. Q : Untuk pembayarannya di awal?
A : Benar Ibu untuk pembayarannya di awal dan masa aktif periode belajar full 30 hari terhitung dari kelas pertama
dimulai
77.Q : Kirimkan no rekening aja gausah pakai virtual account bisa kak?
A : "Mohon maaf, CoLearn tidak tersedia untuk transfer ke rekening A
Karena pembayaran CoLearn secara resmi hanya melalui link pembayaran di atas dengan metode yang telah
tersedia. Apabila ibu membuka link pembayaran di atas, maka akan muncul tampilan resmi dari CoLearn ibu"
78. Q : Apakah ini berbayar?
A : Untuk bimbelnya berbayar Ibu, untuk paket matematika Rp95.000/bulan
79.Q : Bayarnya bulanan ya?
A : Benar Ibu, untuk pembayarannya perbulan
80. Q : Harganya akan terus sama 95.000?
A : Untuk biayanya akan tetap Rp95.000/bulan kecuali jika menambah Fisika/Kimia
81. Q : Cara pembayaran Bank Lain gimana?
A : Berikut nomor virtual account untuk (Bank ):
1. Pilih Menu Pembayaran
2. Pilih Menu "transfer bank lain"
3. Pilih bank BNI
4. Masukkan no VA
82. Q : Cara pembayaran Mandiri gimana?
A : Berikut nomor virtual account Bank Mandiri:
1. Pilih Menu Pembayaran2. Cari "Xendit 88908"
3. Masukkan no VA

83. Q : Cara pembayaran BSI gimana?
A : Berikut nomor virtual account Bank BSI:
1. Pilih Menu Pembayaran
2. Pilih Institusi - Xendit 9347
3. Masukkan no VA tanpa 9347

84. Q : Cara pembayaran BRI gimana?
A : Berikut nomor virtual account Bank BRI:
1. Pilih Menu Pembayaran
2. Pilih BRIVA
3. Masukkan no VA

85. Q : Cara pembayaran BNI gimana?
A : Berikut nomor virtual account Bank BNI:
1. Pilih Menu Pembayaran
2. Pilih Virtual Account Billing
3. Masukkan no VA

86. Q : Cara pembayaran BCA gimana?
A : Berikut nomor virtual account Bank BCA:
1. Pilih M-Transfer
2. Pilih BCA Virtual Account
3. Masukkan no VA87.Q : Cara pembayaran Indomaret gimana?
A : Berikut kode pembayaran melalui Indomaret, bisa langsung tunjukkan ke kasir
88. Q : Cara pembayaran Alfamart gimana?
A : Berikut kode pembayaran melalui Alfamart, bisa langsung tunjukkan ke kasir
89. Q : Cara pembayaran QRIS/E-wallet gimana?
A : "Pembayaran melalui (e-wallet) bisa scan QR berikut ini
90. Q : Link pembayarannya yang mana?
A : Berikut link pembayaran untuk kelas {kelas} kurikulum {kurikulum} paket matematika semester {1} harga Rp
(harga).
{link payment}
Link/nomor Virtual Account hanya berlaku 1x transaksi hingga tanggal *{tanggal} pukul 23:59 WIB .* "
91. Q : Linknya bisa sampai besok nggak?
A : Untuk masa berlaku Link Pembayaran aktif 1 hari
92. Q : Kenapa muncul Xendit bukan CoLearn?
A : Benar ibu, untuk pembayaran melalui Livin by Mandiri akan muncul Xendit sebagai payment gateway
pembayaran di CoLearn
93. Q : Masa aktif paketnya sampai kapan?
A : Masa aktif periode belajar full 30 hari terhitung dari kelas pertama dimulai
94. Q : Kelasnya bisa coba dahulu?
A : Mohon maaf, di CoLearn tidak ada trial. Tetapi ada Garansi Uang Kembali 100% jika tidak cocok setelah ikut
kelasnya di akhir 1 bulan pertama95. Q : Yang perlu dipersiapkan apa aja untuk bisa ikut Bimbelnya?
A : Murid bisa mempersiapkan alat tulis, jaringan internet yang stabil, dan HP/Laptop untuk akses kelasnya

96. Q : Cara masuk kelasnya gimana?
A : Untuk masuk kelasnya melalui Aplikasi CoLearn yang sudah terintegrasi dengan zoom, bisa diakses melalui
HP / Laptop

97.Q : Belajarnya bisa pakai laptop?
A : Jika aktivasi melalui Aplikasi CoLearn di HP sudah berhasil, untuk akses kelas bisa menggunakan Laptop di
website www.colearn.id

98. Q : Fasilitas Bimbelnya Apa Aja?
A : (Reguler) Fasilitas yang didapatkan yaitu: kelas zoom interaktif, Video Review, rangkuman materi berupa PDF
dan laporan belajar untuk orangtua

99. Q : Ada Buku/Modul Belajar?
A : Untuk buku/modul tidak ada. Namun, setiap sesi kelas berakhir murid mendapat video review dan rangkuman
materi berupa PDF

100. Q : Video Kelas Semua Guru ada?
A : "Berikut contoh video pembelajaran di CoLearn
https://www.youtube.com/playlist?list=PLog6_k-sWUcAE4ONb3QbA1fvX9XqllJdM"

101. Q : Cara perpanjang paket gimana?
A : Baik (Bapak/Ibu). Mohon ditunggu, Kakak Siaga akan segera menghubungi (Bapak/Ibu) untuk perpanjang
atau upgrade paket. Terima kasih

102. Q : Cara tambah Profil Baru di aplikasi gimana?
A : Terkait dengan menambah profil baru, silakan mengikuti tutorial berikut:- Buka Aplikasi CoLearn
- Klik tombol garis tiga di pojok kiri atas
- Klik Tambah/Ganti Profil
- Klik Tambah Profil
- Isi data diri dan simpan"

103. Q : Untuk masuk diaplikasi pakai nomor siapa?
A : Untuk login ke aplikasi CoLearn, gunakan nomor anak yang Ibu masukkan saat mengisi formulir
pendaftaran

104. Q : Bisakah 1 nomor untuk 2 anak?
A : Maaf tidak bisa Ibu, satu nomor hanya dapat digunakan untuk satu akun di aplikasi CoLearn

105. Q : Aplikasi CoLearn bisa download dimana?
A : Aplikasi CoLearn bisa di download melalui App Store (ios) atau Play Store (android)

Aktivasi akun akan dikirim *ke no. WA murid dari nomor CoLearn* (*081119103010 / 081119103011).* 
*Mohon segera pilih jadwal melalui aplikasi.* Kelas sudah dapat diikuti setelah murid memilih jadwal di 
aplikasi . Untuk bantuan, chat WA Kakak Siaga: 081119103018 Senin-Minggu, 11.00 - 20.00 WIB (di luar hari libur 
nasional)."
""",

]

