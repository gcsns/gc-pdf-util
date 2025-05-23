colearnKnowledgeDescription = """Generates multiple semantically similar variations of a user query to improve search relevance and retrieval from a knowledge base."""

colearnKnowledgeRole = "You are a helpful assistant that helps create multiple variation of the given query which can be passed to ohter agent to fetch data from knowledge base."

colearnKnowledgeInstructions = [
    "Take a single input query from the user.",
    "Generate multiple natural language variations that preserve the original intent.",
    "Ensure variations are phrased differently but mean the same thing.",
    "Do not change the core meaning of the query. This is most important.",
    "Return a list of 3 unique variations along with input query.",
    "Avoid overly formal or robotic phrasing—keep language natural and human-like.",
]

colearnKnowledgeMdStrings = [
    """
# FAQ- CoLearn 2025

basic_greeting
Q : Hi / Hello / Halo / Hey / Selamat pagi / siang / sore / malam
A : Hello! I'm Alex from CoLearn. How can I help you today?

Interest_based_greeting
Q : Hi, I saw your ad on Instagram / I was referred by my friend
A : Hi! Thank you for reaching out to us. CoLearn is an online learning platform specializing in mathematics and science subjects (IPA). We offer live interactive classes taught by qualified teachers who have undergone 6 months of training before teaching students. Would you like to know more about our programs, pricing, or anything else about CoLearn?

time_specific_greeting
Q : Good morning / Good afternoon / Good evening
A : Good [morning/afternoon/evening]! I'm Alex from CoLearn. How may I help you?

pre_sales_inquiry
Q : I'm thinking of enrolling / I want to register
A : Hello! I'm excited you're considering CoLearn for your child's education. I'm Alex, and I'd be happy to guide you through our programs, explain how our online classes work, and answer any questions you might have. What grade is your child in?

tech_support_opening
Q : I have a technical issue
# FAQ CoLearn

A : Hi there! I'm Alex from CoLearn's support team. I'd be happy to help resolve any technical issues you're experiencing. Could you share more details about what's happening?

post_transaction_followup
Q : I've registered / just made a payment
A : Hello! Thank you for choosing CoLearn. I'm Alex, and I'm here to ensure your onboarding experience goes smoothly. Have you received your activation information yet, or do you have any questions about getting started?

complaint_handling_opening
Q : I'm not happy / I have a complaint
A : I understand your concern, and I'm here to help resolve this situation. I'm Alex from CoLearn's customer service team. Could you share more details so I can assist you better?

1. info_lokasi
Q : Lokasi CoLearn dimana?
A : Kantor pusat CoLearn ada di MCC lantai 42 Sudirman, Jakarta Selatan. Alamat lengkap bisa dilihat di Google dengan mengetik *CoLearn*.

2. info_kelas_CoLearn
Q : Tersedia untuk kelas berapa aja?
A : Bimbel Online Matematika CoLearn tersedia dari kelas 4 SD - 12 SMA

3. info_kelas_123
Q : Untuk kelas 1 / 2 / 3 bisa?
A : Mohon maaf Bapak/Ibu, di CoLearn saat ini baru tersedia untuk 4 SD - 12 SMA

4. info_kelas123_tidaktersedia
Q : Kenapa Kelas 1 - 3 tidak ada?
A : Saat ini bimbel kami fokus pada kelas 4 SD-12 SMA. Kami mempertimbangkan bahwa pembelajaran online di tingkat tersebut lebih efektif dalam membantu siswa memahami konsep matematika dengan baik
5. Info_bimbel_kelas 4
Q : Mohon info bimbel untuk kelas 4?
A : Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 4 SD. 4 pertemuan per bulan (1x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/OrABEkNnKEU?si=Wa2NRtEMVk8P6MKg
6. Info_bimbel_kelas 5
Q : Mohon info bimbel untuk kelas 5?
A : Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 5 SD. 4 pertemuan per bulan (1x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/OrABEkNnKEU?si=Wa2NRtEMVk8P6MKg 
7. info_bimbel_kelas6
Q : Mohon info bimbel untuk kelas 6?
A : Berikut info Bimbel CoLearn:- Harga: mulai 95.000/bulan untuk matematika 6 SD. 4 pertemuan per bulan (1x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/OrABEkNnKEU?si=Wa2NRtEMVk8P6MKg
8. info_bimbel_kelas7
Q : Mohon info bimbel untuk kelas 7?
A : Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 7 SMP. 8 pertemuan per bulan (2x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/2xVerh347p4?si=cNuXJPKIWCXuLwMO 
9. info_bimbel_kelas8
Q : Mohon info bimbel untuk kelas 8?
A : Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 8 SMP. 8 pertemuan per bulan (2x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/2xVerh347p4?si=cNuXJPKIWCXuLwMO 
10. info_bimbel_kelas 9
Q : Mohon info bimbel untuk kelas 9?
A : Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 9 SMP. 8 pertemuan per bulan (2x/minggu). Durasi 60 menit.- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/2xVerh347p4?si=cNuXJPKIWCXuLwMO 

11. Info_bimbel_kelas 10
Q : Mohon info bimbel untuk kelas 10?
A : Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 10 SMA. 8 pertemuan per bulan (2x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/2xVerh347p4?si=cNuXJPKIWCXuLwMO 

12. Info_bimbel_kelas 11
Q : Mohon info bimbel untuk kelas 11?
A : Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 11 SMA. 8 pertemuan per bulan (2x/minggu). Durasi 60 menit.
- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/2xVerh347p4?si=cNuXJPKIWCXuLwMO 

13. Info_bimbel_kelas 12
Q : Mohon info bimbel untuk kelas 12?
A : Berikut info Bimbel CoLearn:
- Harga: mulai 95.000/bulan untuk matematika 12 SMA. 8 pertemuan per bulan (2x/minggu). Durasi 60 menit.- Metode belajar: Kelas Zoom interaktif dengan guru yang memotivasi dan teman lainnya.
- Laporan belajar: tentang kehadiran dan partisipasi dikirim ke WA orang tua.
- Jika anak tidak cocok: garansi uang kembali 100% di bulan pertama.
- Video testimoni: https://youtu.be/2xVerh347p4?si=cNuXJPKIWCXuLwMO 

14. Info_paketlain_kelas 7
Q : Selain matematika ada pelajaran apa aja untuk kelas 7 SMP?
A : Untuk kelas 7 SMP, di bimbel online Colearn ada pilihan:
1. Paket Matematika (2x mat/minggu) - *Rp. 95.000/bulan*
2. Paket Matematika+IPA (2x mat dan 1x IPA / minggu) - *Rp. 144.000/bulan*
*Untuk IPA adalah fisika + biologi diberikan dalam bentuk rangkuman*
Durasi 60 menit/kelas

15. Info_paketlain_kelas 8
Q : Selain matematika ada pelajaran apa aja untuk kelas 8 SMP?
A : Untuk kelas 8 SMP, di bimbel online Colearn ada pilihan:
1. Paket Matematika (2x mat/minggu) - *Rp. 95.000/bulan*
2. Paket Matematika+IPA (2x mat dan 1x IPA / minggu) - *Rp. 144.000/bulan*
Durasi 60 menit/kelas

16. Info_paketlain_kelas 9
Q : Selain matematika ada pelajaran apa aja untuk kelas 9 SMP?
A : Untuk kelas 9 SMP, di bimbel online Colearn ada pilihan:
1. Paket Matematika (2x mat/minggu) - *Rp. 95.000/bulan*
2. Paket Matematika+IPA (2x mat dan 1x IPA / minggu) - *Rp. 144.000/bulan*
Durasi 60 menit/kelas

17. Info_paketlain_kelas10
Q : Selain matematika ada pelajaran apa aja untuk kelas 10 SMA?A : Untuk kelas 10, di bimbel online Colearn ada pilihan:  
1. Paket Matematika (2x mat/minggu) - *Rp. 95.000/bulan*  
2. Paket Matematika+IPA (2x mat dan 1x IPA/ minggu) - *Rp. 144.000/bulan*  
*Untuk IPA adalah fisika dan kimia bergantian (sesuai silabus dari pemerintah. Biologi diberikan dalam bentuk rangkuman)*  
Durasi 60 menit/kelas  

18. Info_paketlain_kelas 11  
Q : Selain matematika ada pelajaran apa aja untuk kelas 11 SMA?  
A : Untuk kelas 11 Merdeka, di bimbel online Colearn ada pilihan:  
1. Paket Matematika Merdeka (2x mat/minggu) - *Rp. 95.000/bulan*  
2. Paket Matematika Merdeka+Lanjutan (3x/minggu) - *Rp. 120.000/bulan*  
Durasi 60 menit/kelas  
Upgrade paket:  
1. Tambah Fisika / Kimia = Rp. 49.000 (1x/minggu)  
2. Tambah Fisika + Kimia = Rp. 79.000 (2x/minggu)  

19. info_paketlain_kelas12  
Q : Selain matematika ada pelajaran apa aja untuk kelas 12 SMA?  
A : Untuk kelas 12 Merdeka, di bimbel online Colearn ada pilihan:  
1. Paket Matematika Merdeka (2x mat/minggu) - *Rp. 95.000/bulan*  
2. Paket Matematika Merdeka+Lanjutan (3x/minggu) - *Rp. 120.000/bulan*  
Durasi 60 menit/kelas  
Upgrade paket:  
1. Tambah Fisika / Kimia = Rp. 49.000 (1x/minggu)  
2. Tambah Fisika + Kimia = Rp. 79.000 (2x/minggu)  

20. Info_mapel_lain_SD  
Q : Untuk SD selain matematika ada apa saja?A : Untuk SD di CoLearn fokusnya di pelajaran matematika saja Ibu

21. Info_IPA_kelas 7
Q : Untuk IPA kelas 7 mapel apa saja?
A : Untuk IPA kelas 7 terdiri dari Fisika dan (Biologi hanya berbentuk rangkuman saja)

22. Info_IPA_kelas 8
Q : Untuk IPA kelas 8 mapel apa saja?
A : Untuk IPA kelas 8 terdiri dari Fisika dan Biologi (materi yang berjalan sesuai urutan silabus dari pemerintah)

23. info_IPA_kelas 9
Q : Untuk IPA kelas 9 mapel apa saja?
A : Untuk IPA kelas 9 terdiri dari Fisika dan Biologi (materi yang berjalan sesuai urutan silabus dari pemerintah)

24. Info_IPA_kelas 10
Q : Untuk IPA kelas 10 mapel aja saja?
A : Untuk IPA kelas 10 adalah fisika dan kimia bergantian (sesuai silabus dari pemerintah. Biologi diberikan dalam
bentuk rangkuman)

25. Info_paket_IPA_wajib_matematika
Q : Fisika/Kimia aja bisa ga?
A : Mohon maaf untuk paket Fisika/Kimia saja tidak bisa. Untuk paket tersebut pembeliannya 1 paket dengan
Matematika

26. Info_bahasa_inggris
Q : Apakah ada bahasa Inggris?
A : Mohon maaf, CoLearn fokusnya di mata pelajaran matematika dan IPA saja

27. Info_OSNQ : Bisa untuk OSN?
A : Mohon maaf untuk OSN saat ini belum ada karena di CoLearn lebih ke pembahasan konsep materi pembelajarannya

28. Info_private
Q : Gurunya tidak ke rumah ya?
A : Mohon maaf, tidak ada kelas private dan offline di CoLearn

29. Info_kelas_private
Q : Apakah ada kelas private?
A : Mohon maaf, tidak ada kelas private di CoLearn

30. Info_tidak_ada_offline
Q : Kenapa CoLearn tidak ada offline?
A : Bimbel CoLearn hanya tersedia online. Tujuannya, agar semua murid di Indonesia bisa mendapatkan akses ke guru-guru dengan penalaran Matematika yang kuat

31. Info_bahasa_pengantar
Q : Bahasa pengantar di CoLearn menggunakan apa?
A : Pembelajaran di CoLearn full menggunakan bahasa Indonesia

32. Info_arti_kurikulum
Q : Kurikulum itu apa ya kak?
A : Kurikulum adalah rencana pembelajaran yang akan diajarkan. CoLearn menggunakan kurikulum pemerintah (kurikulum 2013 atau merdeka)

33. Info_kurikulum_CoLearnQ : Pakai kurikulum apa?
A : CoLearn menggunakan kurikulum pemerintah (kurikulum 2013 atau merdeka)

34. Info_kurikulum_nasionalplus
Q : Kurikulum nasional plus bisa kak?
A : CoLearn menggunakan kurikulum pemerintah (kurikulum 2013 atau merdeka) dengan pengantar bahasa Indonesia

35. Info_kurikulum_IB
Q : Anak saya menggunakan kurikulum IB bisa?
A : Mohon maaf untuk CoLearn menggunakan kurikulum pemerintah (kurikulum 2013 atau merdeka) dengan pengantar bahasa Indonesia, jadi materinya berbeda

36. Info_kurikulum_cambridge
Q : Kalau kurikulum Cambridge apakah bisa?
A : Mohon maaf untuk CoLearn menggunakan kurikulum pemerintah (kurikulum 2013 atau merdeka) dengan pengantar bahasa Indonesia, jadi materinya berbeda

37. Info_sekolah_internasional
Q : Sekolah inter bisa?
A : Mohon maaf untuk CoLearn menggunakan kurikulum pemerintah (kurikulum 2013 atau merdeka) dengan pengantar bahasa Indonesia, jadi materinya berbeda

38. Info_materi
Q : Materi di CoLearn bagaimana?
A : Materi di CoLearn sesuai dengan kurikulum pemerintah (kurikulum 2013 atau merdeka) yang sedang berjalan.# FAQ Asuransi AXA SmartTravel

39. Info_urutan_materi
Q : Urutan materinya ga sama kayak sekolah ya?
A : Materi di CoLearn terkadang lebih lambat atau lebih cepat dibandingkan sekolah, sehingga urutannya tidak akan selalu sama. CoLearn fokus membantu anak agar bisa paham konsep Matematika dengan guru yang mempunyai penalaran Matematika yang kuat

40. Info_materi_lebih_cepat
Q : Materinya bisa lebih cepat dari sekolah?
A : Materi di CoLearn terkadang lebih lambat atau lebih cepat dibandingkan sekolah, sehingga urutannya tidak akan selalu sama.CoLearn fokus membantu anak agar bisa paham konsep Matematika dengan guru yang mempunyai penalaran Matematika yang kuat

41. Info_request_materi
Q : Materinya bisa request sesuai sekolah?
A : Mohon maaf tidak bisa, materi di CoLearn sesuai dengan kurikulum pemerintah (kurikulum 2013 atau merdeka) yang sedang berjalan

42. Info_belajar_dari_dasar
Q : Belajar dari 0 (dasar) bisa ga?
A : Mohon maaf tidak bisa, di Colearn materinya berjalan mengikuti urutan silabus yang berjalan menggunakan Kurikulum Merdeka/2013

43. Info_kelas_baru_sesuai_silabus
Q : Kelas baru, materi dari pertama atau mengikuti timeline silabus?A : Di CoLearn materi yang berjalan sesuai dengan silabus (urutan) materi dari pemerintah, untuk kelas yang terlewat bisa mengakses rangkuman materi berupa PDF.
Kelas pertama dimulai sesuai dengan timeline yang ada di silabus

44. Info_anak_baru_bergabung
Q : Kelasnya sudah berjalan, kalau anak baru bergabung gimana?
A : Di CoLearn materi yang berjalan sesuai dengan silabus (urutan) materi dari pemerintah, untuk kelas yang terlewat bisa mengakses rangkuman materi berupa PDF

45. Info_kelas_sudah_dimulai
Q : Kelasnya sudah di mulai?
A : Benar Ibu, karena di CoLearn materi yang berjalan sesuai dengan silabus (urutan) materi dari pemerintah, untuk kelas yang terlewat bisa mengakses rangkuman materi berupa PDF

46. Info_PTS
Q : PTS itu apa konsepnya?
A : Baik, untuk materi PTS biasanya akan mereview atau mengulang materi yang sebelumnya, Ibu

47. Info_PAS
Q : PAS itu apa konsepnya?
A : Baik, untuk materi PAS biasanya akan mereview atau mengulang materi yang sebelumnya, Ibu

48. Info_upgrade_kelas
Q : Kelas 5 tetapi pinginnya les yg untuk kelas 6 boleh?
A : Baik ibu kakak paham, untuk pembelajaran di CoLearn sebaiknya mengikuti kelas anak saat ini. Karena di Colearn materinya berjalan mengikuti silabus pemerintah. Jika tidak mengikuti sesuai kelasanak dikhawatirkan tidak terbantu sebab materinya berbeda.49. Info_jumlahmurid_SD(4,5,6)
Q : 1 kelas berapa orang? {untuk SD)
A : Maksimal jumlah murid/kelas di SD adalah 30 agar semua murid bisa dapat akses kepada guru yang kompeten
dan terlatih dengan harga terjangkau

50. Info_jumlahmurid_SMP(7,8,9)
Q : 1 kelas berapa orang? {untuk SMP}
A : Maksimal jumlah murid/kelas di SMP adalah 70 agar semua murid bisa dapat akses kepada guru yang
kompeten dan terlatih dengan harga terjangkau.

51. Info_jumlahmurid_SMA(10,11,12)
Q : 1 kelas berapa orang? {untuk SMA)
A : Maksimal jumlah murid/kelas di SMA adalah 70 agar semua murid bisa dapat akses kepada guru yang
kompeten dan terlatih dengan harga terjangkau.

52. Info_jumlah_SD sedikit
Q : kenapa jumlah murid SD lebih sedikit dari SMP tapi harganya sama?
A : Dikarenakan jumlah maksimal murid SD dikelasnya setengah dari jumlah maksimal murid di SMP / SMA Ibu.

53. Info_SD_pertemuan1kali
Q : kenapa SD pertemuannya 1 kali dalam seminggu?
A : Dikarenakan jumlah maksimal murid SD dikelasnya setengah dari jumlah maksimal murid di SMP / SMA Ibu.

54. Info_SD_pertemuan2kali/minggu
Q : Kalau saya mau ikut pertemuannya 2 kali dalam seminggu bisa untuk SD?
A : Mohon maaf tidak bisa Ibu, jika ikut dua kali dalam seminggu materinya akan sama karena tetap berjalan
sesuai dengan urutan silabus55. info_kelas_konsep
Q : Untuk kelasnya seperti apa?
A : Untuk kelasnya adalah kelas pembahasan materi dimana konsep yang besar akan kami bagi menjadi konsep-konsep kecil sehingga mudah untuk murid mengikuti dan memahami. Di dalam kelas akan diselingi dengan soal yang dibahas bersama untuk mengetahui pemahaman murid.

56. Info_metode_belajar
Q : Pembelajaran di CoLearn bagaimana?
A : Untuk pembelajarannya online dua arah dimana murid bisa berinteraksi dengan guru dan teman belajar (melalui zoom) saat kelas berlangsung

57. Info_efektif_kelas
Q : Bisa terkontrol semua ga kak dengan jumlah yg besar?
A : Baik ibu, kakak paham kekhawatirannya, untuk guru-guru kami sudah melalui pelatihan selama 6 bulan sebelum mengajar murid.
Di CoLearn bisa coba kelasnya 1 bulan jika tidak cocok ada garansi uang kembali 100%.

58. Info_kelas_efektif
Q : Apakah kelasnya efektif?
A : Baik ibu, kakak paham kekhawatirannya, untuk guru-guru kami sudah melalui pelatihan selama 6 bulan sebelum mengajar murid. Di CoLearn bisa coba kelasnya 1 bulan jika tidak cocok ada garansi uang kembali 100%.

59. info_anak_ADHD
Q : Anak saya ADHD / inklusi / anak berkebutuhan khusus (ABK) lainnya
A : Baik kakak paham atas yang dihadapi, namun di CoLearn kelasnya bersama-sama dengan teman lainnya dan materi belajar menggunakan silabus kurikulum pemerintah yang sedang berjalan.60. info_mulai_belajar
Q : Mulai kelasnya kapan?
A : Setelah pembayaran akan ada proses aktivasi, kemudian bisa mulai belajar sesuai jadwal yang dipilih.

61. info_WIB
Q : Ini waktu wib ya?
A : Benar, zona waktu yang digunakan di bimbel CoLearn yaitu zona Waktu Indonesia Barat (WIB)

62. Info_tidak_bisa_hadir
Q : Jika berhalangan hadir bagaimana?
A : Jika berhalangan hadir, tersedia PDF materi yang bisa dipelajari secara mandiri

63. Info_ganti_jadwal
Q : Bisa ganti jadwal?
A : Jika nanti tidak cocok/bentrok, jadwal bisa diubah maksimal 1 kali.

64. info_waktu_belajar
Q : Waktunya flexibel bisa kapan saja ya kak?
A : Untuk jadwalnya bisa pilih salah satu dari jadwal yang tersedia, bisa dicocokkan jadwal mana yang sesuai
untuk jadwal anak dan setiap minggunya akan sama

65. info_jadwal_baru
Q : Kalau kelas baru di buka lagi kapan?
A : Kakak belum bisa memastikan kapan kelas baru akan tersedia, Ibu. Jika ada kelas baru, materinya tetap
mengikuti silabus yang sedang berjalan

66. info_jadwal_minggu
Q : Ada jadwal di hari minggu?
A : Mohon maaf Bapak/Ibu jadwal hari minggu di CoLearn tidak tersedia67. info_hari_libur
Q : Kalau hari libur ada kelas pengganti?
A : Jika ada tanggal merah / hari libur nasional maka ada kelas pengganti yang akan diinfokan sebelumnya.
68. info_jadwal_kelas_pengganti
Q : Jadwal kelas pengganti gimana?
A : Kemungkinan jam belajar kelas pengganti akan berbeda dengan jadwal sebelumnya. Informasi mengenai kelas
penganti akan diberitahukan di kelas dan dikirimkan melalui WA Kakak Siaga
69. info_hanya_coba_1bulan
Q : Klo seumpama mencoba 1 bln ternyata tidak lanjut tidak apa2 kan kak?
A : Tidak apa-apa Ibu, karena di CoLearn tidak terikat
70. info_tanya_soal
Q : Bisa tanya soal?
A : Mohon maaf, nomor ini adalah untuk pendaftaran bimbel online CoLearn.
Untuk pertanyaan soal bisa menggunakan fitur video penjelasan dengan cara:
1. Ketikkan soal di website atau foto soal dengan Google Lens
2. Pilih rujukan video penjelasan di Youtube CoLearn
71. info_tanya_pr_dikelas
Q : Bisa tanya PR di kelas?
A : Mohon maaf (Bapak/Ibu) untuk bertanya PR saat kelas berlangsung tidak bisa, dikarenakan untuk kelas di
CoLearn membahas konsep dan materi yang sedang dipelajari# FAQ Asuransi AXA SmartTravel

72. info_tanya_pr_diluar_kelas
Q : Kalau ada tugas bisa konsul ngga kak?
A : Jika ada pertanyaan tugas bisa menggunakan fitur video penjelasan (bisa akses 24 jam) dengan cara:
1. Ketikkan soal di website atau foto soal dengan Google Lens
2. Pilih rujukan video penjelasan di Youtube CoLearn

73. info_tanya_guru_jika_tidakpaham
Q : Semisal anak sy tidak paham materi yang dijelaskan apa bisa coba bertanya dengan tutornya?
A : Jika ada yang belum dipahami di dalam kelas hanya bisa bertanya sesuai dengan materi yang dipelajari saat
kelas berlangsung

74. info_tanyu_guru_pelajaran_disekolah
Q : Bisa tanya pelajaran yang di sekolah sama gurunya?
A : Mohon maaf tidak bisa Ibu. Di dalam kelas hanya bisa bertanya sesuai dengan materi yang dipelajari saat kelas
berlangsung

75. info_cara_daftar
Q : Cara daftarnya bagaimana?
A : Untuk daftar, mohon isi data berikut:
- Nama lengkap anak:
- Kelas:
- Kurikulum:
- Jadwal yang dipilih:
- No telp murid (WA & SMS):
- Email orang tua/murid (wajib):
- Nama orang tua:
- No telp orang tua (WA):- Metode pembayaran:

Untuk pembayaran, bisa pilih metode transfer antar bank (BCA, Mandiri, BRI, BSI, BNI dan bank lain), e-wallet (Gopay, OVO, Dana, Shopeepay) maupun Indomaret/Alfamart. Semua atas nama CoLearn.

76. info_daftar_semester_depan
Q : Bisa daftar untuk semester depan?
A : Baik kakak paham Ibu, sementara bisa pilih salah satu jadwalnya dahulu untuk amankan slotnya, jika nanti tidak cocok/bentrok bisa ubah jadwal maksimal 1 kali. Apakah berkenan?

77. info_biaya_daftar
Q : Biaya pendaftarannya berapa?
A : Biayanya untuk paket matematika Rp95.000/bulan dan tidak ada biaya tambahan lainnya

78. info_bayar_1semester
Q : Bisa bayar langsung 1 semester?
A : Baik, untuk daftar bulan pertama pembayarannya 1 bulan terlebih dahulu (Bapak/Ibu), pada bulan berikutnya tim perpanjangan paket akan menginfokan opsi pembayaran bulanan atau semesteran

79. info_bayar_diawal
Q : Untuk pembayarannya di awal?
A : Benar Ibu untuk pembayarannya di awal dan masa aktif periode belajar full 30 hari terhitung dari kelas pertama dimulai

80. info_cara_bayar
Q : Kirimkan no rekening aja gausah pakai virtual account bisa kak?
A : Mohon maaf, CoLearn tidak tersedia untuk transfer ke rekening🙏 Karena pembayaran CoLearn secara resmi hanya melalui link pembayaran di atas dengan metode yang telah tersedia. Apabila ibu membuka link pembayaran di atas, maka akan muncul tampilan resmi dari CoLearn ibu81. info_apakah_berbayar
Q : Apakah ini berbayar?
A : Untuk bimbelnya berbayar Ibu, untuk paket matematika Rp95.000/bulan
82. Info_bayar_perbulan
Q : Bayarnya bulanan ya?
A : Benar Ibu, untuk pembayarannya perbulan
83. Info_biaya_sama
Q : Harganya akan terus sama 95.000?
A : Untuk biayanya akan tetap Rp95.000/bulan kecuali jika menambah Fisika/Kimia
84. info_carabayar_banklain
Q : Cara pembayaran Bank Lain gimana?
A : Berikut nomor virtual account untuk (Bank ):
1. Pilih Menu Pembayaran
2. Pilih Menu transfer bank lain
3. Pilih bank BNI
4. Masukkan no VA
85. info_carabayar_Mandiri
Q : Cara pembayaran Mandiri gimana?
A : Berikut nomor virtual account Bank Mandiri:
1. Pilih Menu Pembayaran
2. Cari Xendit 88908
3. Masukkan no VA86. info_carabayar_BSI
Q : Cara pembayaran BSI gimana?
A : Berikut nomor virtual account Bank BSI:
1. Pilih Menu Pembayaran
2. Pilih Institusi - Xendit 9347
3. Masukkan no VA tanpa 9347

87. info_carabayar_BRI
Q : Cara pembayaran BRI gimana?
A : Berikut nomor virtual account Bank BRI:
1. Pilih Menu Pembayaran
2. Pilih BRIVA
3. Masukkan no VA

88. info_carabayar_BNI
Q : Cara pembayaran BNI gimana?
A : Berikut nomor virtual account Bank BNI:
1. Pilih Menu Pembayaran
2. Pilih Virtual Account Billing
3. Masukkan no VA

89. info_carabayar_BCA
Q : Cara pembayaran BCA gimana?
A : Berikut nomor virtual account Bank BCA:
1. Pilih M-Transfer
2. Pilih BCA Virtual Account
3. Masukkan no VA90. info_carabayar_Indomaret
Q : Cara pembayaran Indomaret gimana?
A : Berikut kode pembayaran melalui Indomaret, bisa langsung tunjukkan ke kasir
    """,
"""
    
91. info_carabayar_Alfamart
Q : Cara pembayaran Alfamart gimana?
A : Berikut kode pembayaran melalui Alfamart, bisa langsung tunjukkan ke kasir

92. info_carabayar_QRIS
Q : Cara pembayaran QRIS/E-wallet gimana?
A : Pembayaran melalui (e-wallet) bisa scan QR berikut ini

93. info_link_pembayaran
Q : Link pembayarannya yang mana?
A : Berikut link pembayaran untuk kelas {kelas} kurikulum {kurikulum} paket matematika semester {1} harga Rp
(harga).
{link payment}
Link/nomor Virtual Account hanya berlaku 1x transaksi hingga tanggal *{tanggal} pukul 23:59 WIB .* 

94. info_link_aktif
Q : Linknya bisa sampai besok nggak?
A : Untuk masa berlaku Link Pembayaran aktif 1 hari

95. info_nama_xendit
Q : Kenapa muncul Xendit bukan CoLearn?
A : Benar ibu, untuk pembayaran melalui Livin by Mandiri akan muncul Xendit sebagai payment gateway
pembayaran di CoLearn96. info_masa_aktif_paketbelajar
Q : Masa aktif paketnya sampai kapan?
A : Masa aktif periode belajar full 30 hari terhitung dari kelas pertama dimulai
97. info_trial
Q : Kelasnya bisa coba dahulu?
A : Mohon maaf, di CoLearn tidak ada trial. Tetapi ada Garansi Uang Kembali 100% jika tidak cocok setelah ikut
kelasnya di akhir 1 bulan pertama
98. info_persiapan_sebelum_bimbel
Q : Yang perlu dipersiapkan apa aja untuk bisa ikut Bimbelnya?
A : Murid bisa mempersiapkan alat tulis, jaringan internet yang stabil, dan HP/Laptop untuk akses kelasnya
99. info_caramasuk_kelas
Q : Cara masuk kelasnya gimana?
A : Untuk masuk kelasnya melalui Aplikasi CoLearn yang sudah terintegrasi dengan zoom, bisa diakses melalui
HP / Laptop
100. info_perangkat_belajar
Q : Belajarnya bisa pakai laptop?
A : Jika aktivasi melalui Aplikasi CoLearn di HP sudah berhasil, untuk akses kelas bisa menggunakan Laptop di
website www.colearn.id
101. info_faslitas_bimbel
Q : Fasilitas Bimbelnya Apa Aja?
A : (Reguler) Fasilitas yang didapatkan yaitu: kelas zoom interaktif, Video Review, rangkuman materi berupa PDF
dan laporan belajar untuk orangtua102. info_modul_belajar
Q : Ada Buku/Modul Belajar?
A : Untuk buku/modul tidak ada. Namun, setiap sesi kelas berakhir murid mendapat video review dan rangkuman materi berupa PDF

103. info_contoh_video_belajar
Q : Video Kelas Semua Guru ada?
A : Berikut contoh video pembelajaran di CoLearn
https://www.youtube.com/playlist?list=PLog6_k-sWUcAE4ONb3QbA1fvX9XqlIJdM

104. info_perpanjang_paket
Q : Cara perpanjang paket gimana?
A : Baik (Bapak/Ibu). Mohon ditunggu, Kakak Siaga akan segera menghubungi (Bapak/Ibu) untuk perpanjang atau upgrade paket. Terima kasih

105. info_tambah_profil_aplikasi
Q : Cara tambah Profil Baru di aplikasi gimana?
A : Terkait dengan menambah profil baru, silakan mengikuti tutorial berikut:
- Buka Aplikasi CoLearn
- Klik tombol garis tiga di pojok kiri atas
- Klik Tambah/Ganti Profil
- Klik Tambah Profil
- Isi data diri dan simpan

106. info_nomor_login
Q : Untuk masuk diaplikasi pakai nomor siapa?
A : Untuk login ke aplikasi CoLearn, gunakan nomor anak yang Ibu masukkan saat mengisi formulir pendaftaran107. info_1nomor_1akun
Q : Bisakah 1 nomor untuk 2 anak?
A : Maaf tidak bisa Ibu, satu nomor hanya dapat digunakan untuk satu akun di aplikasi CoLearn

108. info_download_aplikasi
Q : Aplikasi CoLearn bisa download dimana?
A : Aplikasi CoLearn bisa di download melalui App Store (ios) atau Play Store (android)

109. info_gender_guru
Q : Untuk gurunya perempuan kak?
A : Di CoLearn tersedia guru perempuan dan laki-laki ibu, dapat dipilih sesuai jadwal yang tersedia

110. info_guru_favorit
Q : Guru mana yang lebih bagus?
A : Untuk guru-guru kami semua sama kualitasnya karena sudah melalui pelatihan selama 6 bulan sebelum
mengajar murid, Ibu

111. info_guru_galak
Q : Gurunya engga galak kan kak?
A : CoLearn memahami kekhawatiran yang terjadi. Namun, CoLearn memastikan bahwa guru kami bisa
membangun suasana belajar di kelas jadi menyenangkan dan mudah dimengerti untuk anak

112. info_kualitas_guru
Q : Kualitas gurunya kayak gimana?
A : Untuk guru kami merupakan guru-guru yang melalui seleksi ketat dari lulusan universitas terbaik dan mereka
harus melalui pelatihan selama 6 bulan terlebih dahulu sebelum bisa mengajar murid113. info_tidak_suka_matematika
Q : Anak saya gasuka MTK gimana caranya?
A : Baik, kakak paham. CoLearn fokus membangun suasana belajar yang positif agar anak termotivasi belajar
Matematika dengan guru dan teman sekelas lainnya. Bisa dicoba daftar 1 bulan terlebih dahulu, jika anak tidak
cocok ada garansi uang kembali 100%
114. info_tidak_percaya_diri
Q : Anak saya tidak percaya diri gimana?
A : Kami paham tidak semua anak nyaman dan merasa malu berpartisipasi. Di CoLearn kami mendorong murid
untuk lebih berani bertanya di kelas supaya mereka dapat membangun kepercayaan dirinya
115. info_kerjasama
Q : Kerjasama dengan CoLearn gimana?
A : Mohon maaf nomor ini untuk pendaftaran bimbel online CoLearn. Untuk informasi kerja sama bisa
menghubungi melalui akun Instagram @peopleofcolearn atau mengirimkan email ke peopleops@colearn.id
Terima kasih
116. info_telepon_whatsapp
Q : Apakah bisa telpon?
A : Mohon maaf Ibu, WhatsApp ini diakses melalui sistem sehingga tidak bisa melakukan panggilan. Apakah ada
kendala / pertanyaan yang bisa kakak bantu jawab?
117. info_penipuan
Q : Ini bukan penipuan kan?
A : Tidak perlu khawatir, seluruh pembayaran resmi atas nama CoLearn, karna kami tidak menerima
pembayaran atas nama perorangan. Nomor ini didapatkan karena Bapak / Ibu telah mengisi formulir dari iklan
CoLearn di Instagram/Facebook, dan bisa cek melalui Instagram resmi @colearn.id118. Info_cara_klaim garansi
Q : Cara klaim Garansi Gimana?
A : Untuk klaim Garansi Uang Kembali, setelah ikut kelasnya 1 bulan pertama dengan minimal kehadiran 50% dari
total pertemuan kelasnya

119. info_data_pribadi
Q : Data pribadi saya aman?
A : Untuk kerahasiaan data dijamin aman ibu, data ini digunakan hanya untuk persyaratan aktivasi akun dan
pembuatan link pembayaran

120. info_lowongan_kerja
Q : Ada lowongan kerja?
A : Untuk info lowongan kerja bisa dicek melalui LinkedIn CoLearn atau mengirimkan lamaran pekerjaan melalui
email career@colearn.id

121. info_dampingi_anak_saat_les
Q : Orang tua boleh ikut mendampingi lesnya?
A : Orang tua boleh mendampingi saat belajar, tetapi diharapkan hanya anak yang berpartisipasi di kelas

122. info_anak_pondok
Q : Anak saya dipondok pesantren bisa ikut?
A : Bisa cek terlebih dulu kurikulum yang digunakan di sekolah anak. Pembelajaran CoLearn menggunakan
Kurikulum Pemerintah (Kurikulum Merdeka dan Kurikulum 2013). Jika anak menggunakan kurikulum sama, bisa
ikut bergabung123. info_anak_pondok
Q : Anak saya di asrama mau ikut les tapi tidak bisa pakai HP bagaimana?
A : Jika pihak asrama atau pondok memberikan izin kepada anak untuk belajar selama 1 jam (60 menit) setiap jadwal CoLearn, tidak menjadi kendala. Untuk pembelajarannya dapat di akses melalui laptop. Jika diperlukan surat izin untuk pihak sekolah, CoLearn bisa membantu menyediakan surat tersebu

124. info_kendala
Q : Kak kok audionya ngga bisa ya?
A : Untuk kendala bisa menghubungi Tim Kakak Siaga melalui:
· Chat di WA 081119103018
Jam operasional: Senin-Minggu jam 11:00-20:00 WIB (di luar hari libur nasional)

125. info_nomor_VA
Q : Nomor virtual accountnya akan sama setiap bulan ya?
A : Untuk nomor Virtual Account akan berbeda setiap bulannya

126. info_sistembayar_jika baru bergabung
Q : Jika saya mulai baru minggu ini gmn sistemnya kak, apakah tetap bayar full?
A : Masa aktif periode belajar full 30 hari terhitung dari kelas pertama anak dimulai, jadi untuk pembayarannya tetap Rp95.000

127. info_CoLearn+
Q : Kelas CoLearn+ itu apa kak?
A : Kelas CoLearn+ adalah kelas bonus yang bisa diikuti / tidak sifatnya opsional, untuk jadwalnya bisa lihat di Aplikasi CoLearn

128. info_math_club
Q : Math Club itu apa kak?# FAQ Asuransi AXA SmartTravel

A : Math Club adalah kelas bonus yang merupakan kelas pembahasan latihan soal bersama gurunya

129. info_kelas_ekstra
Q : Maksudnya kelas ekstra, gimana ya? Boleh ikut free?
A : Kelas bonus yang bisa diikuti / tidak sifatnya opsional, untuk jadwalnya bisa lihat di Aplikasi CoLearn

130. info_jadwal_diaplikasi
Q : Jadwalnya bisa dilihat diaplikasi?
A : Setelah aktivasi selesai, jadwal bimbel akan muncul di aplikasi CoLearn

131. info_reminder_kelas
Q : Ada reminder sebelum kelas di mulai?
A : Jika notifikasi di aplikasi CoLearn sudah diaktifkan, pengingat kelas akan dikirimkan melalui WhatsApp 30 menit
dan 5 menit sebelum kelas dimulai

132. info_profil_guru
Q : Bisa lihat profil guru-gurunya?
A : Untuk beberapa profil guru bisa di lihat di website ini Bapak/Ibu https://colearn.id/gurujuara

133. info_akses_pdf
Q : Cara akses rangkuman pdf materi dan video review bagaimana?
A : Untuk mengakses rangkuman pdf materi dan video review, buka aplikasi CoLearn dan masuk ke bagian
'Bimbel'

134. info_kelas_berisik
Q : Saya khawatir kalau kelasnya berisik bagaimana?# FAQ Asuransi AXA SmartTravel

A : Baik, kakak paham kekhawatirannya untuk guru-guru kami sudah melalui pelatihan untuk mengajar online dan membuat kelas berjalan kondusif. Jika berkenan, bisa daftar 1 bulan dahulu apabila tidak cocok bisa klaim garansi uang kembali 100%

135. info_anak_on_mic
Q : Kalau anak-anak di kelas pada on mic semua bagaimana?
A : Baik kakak paham, CoLearn membangun kelas yang interaktif sehingga murid diperbolehkan untuk on microphone saat proses belajar, dan guru kami akan memastikan kelas berjalan kondusif

136. info_kelas_baru
Q : Ada kelas yang baru di mulai?
A : Baik Ibu, izin infokan untuk kelas yang sudah di mulai ataupun yang akan di mulai (kelas baru) materinya akan tetap mengikuti silabus yang berjalan

137. info_sisa_kursi
Q : Sisa kursi itu apa kak?
A : Sisa kursi merupakan sisa ketersediaan jumlah murid dari jumlah maksimal di setiap kelasnya

138. Info_warna_sisa_kursi
Q : Kak bedanya yg kursi merah ijo kuning itu apa ya?
A : Baik, Ibu. Warna hijau menunjukkan bahwa masih banyak kursi tersedia, sedangkan warna kuning dan merah menandakan bahwa sisa kursi sedikit

139. info_WITA
Q : Ini waktunya WIB ya kak, kalau di makassar gimana?
A : Benar Ibu, CoLearn menggunakan zona waktu WIB. Jika zona WITA 1 jam lebih maju dari WIB

140. info_WIT
Q : Ini waktunya WIB ya kak, kalau di maluku gimana?A : Benar Ibu, CoLearn menggunakan zona waktu WIB. Jika zona WIT 2 jam lebih maju dari WIB

141. info_pembayaran_berhasil
Q : Saya sudah melakukan pembayaran ya
A : Pembayaran sudah diterima, terima kasih.
Aktivasi akun akan dikirim *ke no. WA murid dari nomor CoLearn* (*081119103010 / 081119103011).* 
*Mohon segera pilih jadwal melalui aplikasi.* Kelas sudah dapat diikuti setelah murid memilih jadwal di
aplikasi . Untuk bantuan, chat WA Kakak Siaga: 081119103018 Senin-Minggu, 11.00 - 20.00 WIB (di luar hari libur
nasional).
    """,
    """
Q: 1 kelas berapa anak
A: Di CoLearn, jumlah maksimal murid per kelas bervariasi tergantung tingkatannya. Untuk SD maksimal 30 murid, sedangkan untuk SMP dan SMA maksimal 70 murid per kelas.

Q: Adakah yg lebih sedikit kelasnya
A: Selamat pagi/siang/sore/malam, mohon maaf tidak ada Ibu

Q: Ini kelasnya 1 on 1 ato rame2 di zoomnya?
A: Untuk belajar di kelas bersama dengan teman-teman lainnya, ibu

Q: Baik nanti sy tny anaknya dl
A: Baik ibu, silahkan di diskusikan terlebih dahulu dengan anaknya

Q: Nnt d tanya sama anakny
A: Baik ibu, silahkan di diskusikan terlebih dahulu dengan anaknya

Q: Sy blm bicarakan sama anak, nanti sy info lg ya
A: Baik ibu, silahkan di diskusikan terlebih dahulu dengan anaknya

Q: Baik terimakasih ya kak ,saya kompirmsi saya anak dan papa nya anak dlu
A: Baik ibu, bisa didiskusikan terlebih dahulu

Q: Terimakasih kk infonya saya infokan ke anak saya pilihannya yng mana baru nanti saya info kk
A: Baik ibu, silahkan di diskusikan terlebih dahulu dengan anaknya

Q: Mulainya hr ini atau kapn?
A: Kelas dimulai minggu depan ibu

Q: Sabtu tidak ada jadwal ya?# FAQ Asuransi AXA SmartTravel

A: Mohon maaf ibu, untuk jadwal weekend tidak ada

Q: Bertanya apa ini hanya MTK saja ka

A: Di CoLearn fokusnya di mata pelajaran matematika dan IPA ibu

Q: Halo u zoom link apa bisa d kirim d sini juga? Karena sy mau memastikan anak saya masuk kelas
hari ini. Saya masih d kantor

A: Selamat sore Ibu, untuk link zoom diakses langsung melalui aplikasi atau bisa juga melalui web
dengan cara berikut: [Image File]

Q: Anak saya br mau masuk sma tahun ini. Bisa ikut kah?

A: Baik ibu,di colearn membuka kelas persiapan masuk SMA. Apakah berkenan kakak infokan?

Q: Ini belajarnya hanya pas zoom aj atau hr biasa tetep di kasih tugas

A: Untuk PR kami tidak ada Ibu, namun jika saat pembahasan soal soal murid belum menyelesaikan
bisa dijadikan tugas mandiri namun sifatnya tidak wajib

Q: Maaf ini suasananya menyenangkan pembawa materinya kan ya. Biar anak nyaman dan happy
belajarnya

A: Baik ibu, kakak paham. CoLearn fokus membangun suasana belajar yang positif agar anak
termotivasi belajar Matematika dengan guru dan teman sekelas lainnya. Bisa dicoba daftar 1 bulan
terlebih dahulu, jika anak tidak cocok ada garansi uang kembali 100%

Q: Kan sy minta jadwal Jumat nah, kalo sy Uda lakukan pembayaran dimulainya hari ini ya?

A: Setelah pembayaran akan ada proses aktivasi, kemudian bisa mulai belajar sesuai jadwal yang
dipilih ibu. Jadi malam ini sudah bisa ikut kelasnya


1. info_tanya_guru_dikelas
Q : Apa bisa tanya guru di kelas?
A : "Jika ada yang belum dipahami di dalam kelas hanya bisa bertanya sesuai dengan materi yang dipelajari saat kelas berlangsung"

2. info_SD_seminggu_2_kali
Q : Kalau saya mau ikut 2 kali seminggu bisa kak?
A : "Mohon maaf tidak bisa Bapak/Ibu, jika ikut dua kali dalam seminggu materinya akan sama karena tetap berjalan sesuai dengan urutan silabus"

3. info_coba_1_bulan
Q : Kalau saya mau coba 1 bulan tapi bulan selanjutnya ga lanjut itu gimana ya kak?
A : "Tidak apa-apa Ibu, karena di CoLearn tidak terikat"

4. info_IPA_saja
Q : Mau IPA saja apa bisa kak?
A : "Mohon maaf untuk paket IPA saja tidak bisa. Untuk paket tersebut pembeliannya 1 paket dengan Matematika"

5. info_ragu_jumlah_murid
Q : Murid di kelas terlalu banyak
A : "Baik bapak/ibu, kami paham kekhawatirannya, untuk guru-guru kami sudah melalui pelatihan selama 6 bulan sebelum mengajar murid.  
Di CoLearn bisa coba kelasnya 1 bulan jika tidak cocok ada garansi uang kembali 100%."

6. info_bentrok_jadwal
Q : Kalau jadwal bentrok gimana kak?
A : "Jika nanti tidak cocok/bentrok, jadwal bisa diubah maksimal 1 kali. atau Murid bisa mengubah jadwal maksimal 1 kali jika tidak cocok atau bentrok."

7. info_baru_join
Q : Kalau baru ikut sekarang apa gak ketinggalan?
A : "Di CoLearn materi yang berjalan sesuai dengan silabus (urutan) materi dari pemerintah, untuk kelas yang terlewat bisa mengakses rangkuman materi berupa PDF.
Kelas pertama dimulai sesuai dengan timeline yang ada di silabus"

8. info_kelas_lebih_tinggi
Q : Apa boleh ambil kelas diatasnya? Anak saya sudah bisa materi di kelasnya
A : "Baik bapak/ibu kami paham, untuk pembelajaran di CoLearn sebaiknya mengikuti kelas anak saat ini. Karena di Colearn materinya berjalan mengikuti silabus pemerintah. Jika tidak mengikuti sesuai kelasanak dikhawatirkan tidak terbantu sebab materinya berbeda."

9. info_promo_daftar_2_orang
Q : Ada promo gak kalau daftar 2 orang?
A : "Mohon maaf saat ini tidak ada program diskon Bapak/Ibu. Sehingga harga yang berlaku Rp 95,000/bulan untuk masing-masing murid."

10. info_tanya_tugas_di_kelas
Q : Bisa tanya tugas sekolah di kelas gak?
A : "Mohon maaf untuk bantuan mengerjakan PR tidak tersedia. Jika ada pertanyaan/tugas bisa menggunakan fitur video penjelasan (bisa akses 24 jam) dengan cara:

1. Ketikkan soal di website atau foto soal dengan Google Lens
2. Pilih rujukan video penjelasan di Youtube CoLearn"

11. info_kapan_kelas_mulai
Q : Kelasnya dimulai kapan?
A : "Setelah pembayaran akan ada proses aktivasi, kemudian bisa mulai belajar sesuai jadwal yang dipilih."

12. info_panggilan
Q : Bisa saya telfon kak?
A : "Mohon maaf Bapak/Ibu, WhatsApp ini diakses melalui sistem sehingga tidak bisa melakukan panggilan. Apakah ada kendala / pertanyaan yang bisa kakak bantu jawab?"

13. info_anak_malu
Q : Anak saya malu kalau belajarnya bareng gitu
A : "Kami paham tidak semua anak nyaman dan merasa malu berpartisipasi. Di CoLearn kami mendorong murid untuk lebih berani bertanya di kelas supaya mereka dapat membangun kepercayaan dirinya."

14. info_pilih_guru
Q : Pilihin gurunya kak yang sabar dan gak bikin tegang
A : "Untuk guru-guru kami semua sama kualitasnya karena sudah melalui pelatihan selama 6 bulan sebelum mengajar murid, Bapak/Ibu"

15. info_diskon
Q : Ada diskon gak kak?
A : "Mohon maaf saat ini tidak ada program diskon, Bapak/Ibu"

16. info_booking_slot
Q : Bisa booking dulu kak?
A : "Untuk pendaftarannya bisa kapan saja selama jadwal masih tersedia. Namun setelah pembayaran akan ada proses aktivasi dan setelah itu bisa mulai belajar sesuai jadwal yang dipilih. Apakah berkenan?"

17. info_kelas_pembahasan_soal
Q : Dikelasnya ini pembahasan soal ya kak?
A : "Di CoLearn, kelas bukan hanya pembahasan soal. Kami fokus pada pembahasan materi dengan konsep yang besar dibagi menjadi konsep-konsep kecil agar mudah dipahami. Selama kelas, ada juga pembahasan soal bersama untuk mengetahui pemahaman murid."

18. info_bantu_pr
Q : Bantu PR anak saya
A : "Mohon maaf untuk bantuan mengerjakan PR tidak tersedia. Jika ada pertanyaan/tugas bisa menggunakan fitur video penjelasan (bisa akses 24 jam) dengan cara:   

1. Ketikkan soal di website atau foto soal dengan Google Lens   
2. Pilih rujukan video penjelasan di Youtube CoLearn"

19. info_anak_solat
Q : Kalau waktu solat bagaimana kak?
A : "Di CoLearn, kami memahami pentingnya ibadah sholat bagi siswa Muslim. Meskipun tidak ada kebijakan khusus yang disebutkan, CoLearn menerapkan fleksibilitas dalam pembelajaran. Jika ada materi yang terlewat, siswa dapat mengakses video review dan rangkuman materi dalam bentuk PDF yang disediakan setelah setiap sesi kelas"

20. info_tanya_materi_sekolah
Q : Kalau nanya materi di sekolah bisa kak?
A : “Mohon maaf Bapak/Ibu murid hanya bisa bertanya sesuai dengan topik yang sedang dibahas selama kelas berlangsung
"""
]

