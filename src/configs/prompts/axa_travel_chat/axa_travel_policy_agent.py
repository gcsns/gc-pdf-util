travelPolicyDescription = """You are a knowledgeable assistant with full access to the document titled "AFI - Business Travel Policy 2024" from PT AXA Financial Indonesia. Your task is to accurately and helpfully answer any questions users may have about the document."""

travelPolicyInstructions=[
    "Refer only to the contents of the document. Do not rely on outside or assumed knowledge.",
    "Always provide clear, concise, and complete answers.",
    "Always mention your source at the end of your answers, citing the page number or section that the data was used from",
    "If the information does not exist in the document, respond honestly by saying, “This information is not available in the policy document.”",
    "Do not make up any information"
]


travelPolicyMdStrings = [
"""![AXA Logo]

# PERJALANAN DINAS KARYAWAN
# EMPLOYEE BUSINESS TRAVEL

## KEBIJAKAN SUMBER DAYA MANUSIA
## HUMAN RESOURCES POLICY

# PT AXA FINANCIAL INDONESIA
Versi 3.0

Internal""",
"""# DAFTAR ISI / TABLE OF CONTENT

| No | Content | Halaman/Page |
|---|---------|---------------|
| 1 | Latar Belakang / Introduction | 4 |
| 2 | Tujuan / Objective | 4 |
| 3 | Ruang Lingkup / Scope | 4 |
| 4 | Referensi / Reference | 4 |
| 5 | Definisi / Definition | 4 |
| 6 | Tugas dan Tanggung Jawab / Roles and Responsibility | 6 |
| 7 | Aturan Umum / General Rules | 7 |
| 8 | Prosedur Perjalanan Dinas / Business Travel Procedures | 8 |
| 9 | Perjalanan Dinas Luar Negeri / Overseas Business Travel | 14 |
| 10 | Frekuensi Peninjauan / Review Frequency | 15 |
| 11 | Lembar Persetujuan / Approval Sheet | 17 |
| 12 | Lampiran (jika ada) / Appendix (if any) | 19 |

# INFORMASI DOKUMEN / INFORMATION DOCUMENT

| Field | Value |
|-------|--------|
| Nomor Dokumen<br>Number of Document | 008/KBJ/HR/09/2024 |
| Pemilik Dokumen<br>Document Owner | Human Resources Department |
| Disiapkan oleh<br>Prepared by | Dwi Rina Paramitha |
| Ditinjau oleh<br>Review by | 1. Adrian Immanuel Jusup – Head of HRBPP HRIS Reward Strategy & Data Analytics<br>2. Anastasya Ulliwidya Salim – HR Organization & Learning Dev Talent & Services Manager<br>3. Kadek Ayu Mayang Tunjung Sari – Head of Legal<br>4. Eriza Sumarlina – Head of Compliance<br>5. Daud Ikhsan – Head of Enterprise Risk and Internal Control<br>6. Heindradi Harjanto – Head of Financial Controls and Strategy |
| Diketahui oleh<br>Acknowledge by | 1. Dian Yuwiraswati – Chief of Human Resources<br>2. Tamin Tangka – Chief Risk Officer |
| Disetujui oleh<br>Approved by | 1. Niharika Yadav – President Director<br>2. Arta Magdalena – Director<br>3. Cicilia Nina Triana Wuryanti – Director<br>4. Bukit Raharjo - Director |
| Versi Dokumen<br>Document Version | V.3.0 |
| Tanggal Revisi Terakhir<br>Date of Last Update | 1 Agustus 2023 |
| Tanggal Efektif<br>Effective Date | 9 September 2024 |

1
Internal""",
"""# HISTORI PERUBAHAN / CHANGE HISTORY

| # | Effective Date | Version | Prepared by | Part and Page | Information Changes |
|---|----------------|----------|--------------|---------------|--------------------|
| 1 | 1 Desember 2020 | V.1.0 | Kenny Immanuel | - | Dokumen Baru |
| 2 | 1 Agustus 2023 | V.2.0 | Dwi Rina Paramitha | 1. Definisi Hal. 3<br><br>2. Prosedur Perjalanan Dinas Hal. 8<br><br>3. Prosedur Perjalanan Dinas Hal. 11<br><br>4. Perjalanan Dinas Luar Negeri Hal. 13<br><br>5. Lampiran 7a dan 7b Panduan Keamanan Penerbangan Hal 17<br><br>6. Lampiran 8 Memo Penugasan Hal 17 | 1. Penambahan Chief of Function (Mancomm) dalam definisi "h"<br><br>2. Penambahan approval line pada "i" dan "ii", dan penambahan klausul "jii"<br><br>3. Perubahan klausul "vii" mengenai pembayaran Transportasi ke airport<br><br>4. Perubahan klausul "d" mengenai pembayaran Transportasi ke airport<br><br>5. Penambahan Lampiran 7a dan 7b Panduan Keamanan Penerbangan<br><br>6. Lampiran 8 Memo Penugasan sebagai prosedur pengajuan perjalanan dinas |
| 3 | 1 September 2024 | V.2.0 | Dwi Rina Paramitha | 1. Referensi Hal 4<br><br>2. Definisi Hal 5<br><br>3. Aturan Umum Hal. 8 | 1. Penambahan Delegation of Authority<br><br>2. Penambahan definisi Pengajuan Perjalanan Dinas<br><br>3. Perubahan uang saku menjadi Penggantian Biaya Perjalanan Dinas<br><br>4. Penambahan referensi Appendix terkait Travel Security<br><br>5. Penambahan aturan umum terkait non-preffered airlines. |

2
Internal""",
"""4. Prosedur Perjalanan
Dinas Hal. 8-11

5. Biaya Perjalanan
Dinas Harian Hal 11

6. Frekeuensi
Peninjauan Hal 15

7. Lampiran 2a

8. Lampiran 5, 7a, 7b,
7c, 8, dan 10, dan
11Hal 17

6. Pemisahan bagian
"Pengajuan
Perjalanan Dinas"
dengan
"Penyelesaian
Perjalanan Dinas"

7. Penambahan klausul
dan perubahan
proses dan
keterangan pada
Pengajuan
Perjalanan Dinas dan
Penyelesaian
Perjalanan Dinas

8. Perubahan judul
Biaya perjalanan
dinas harian

9. Perubahan tanggal
efektif berlakunya
peraturan

10. Perubahan pada
Business Travel
Requisition Form

11. Perubahan Lampiran
yang berkaitan
dengan Travel
Security dan
Delegation of
Authority

3
Internal""",
"""1. LATAR BELAKANG
Kebijakan sumber daya manusia untuk perjalanan dinas karyawan ini ditetapkan sebagai pedoman yang berlaku untuk semua Karyawan PT AXA Financial Indonesia ("AFI" atau "Perusahaan") dan dirancang untuk memastikan bahwa semua perjalanan dinas karyawan dikelola dengan baik dan persyaratan minimum baik dari Grup maupun dari Regulator Lokal ataupun Pemerintah terpenuhi. Persyaratan yang ditetapkan dalam dokumen ini dimasukkan untuk memenuhi persyaratan peraturan lokal maupun praktek pada umumnya.

1. INTRODUCTION
This Human Resources Policy for business travel set out the guidelines applicable to all PT AXA Financial Indonesia ("AFI" or "Company") Employees and designed to ensure that the business travel are properly managed and the minimum requirements from the Group and Local Regulators or Government are met. The requirements set out in this document supplemented in order to comply with the local regulatory requirements or best practices.

2. TUJUAN
a. Untuk menyajikan standar yang jelas tentang kelayakan tunjangan perjalanan untuk urusan pekerjaan.
b. Untuk standarisasi proses Perjalanan Dinas yang dilakukan oleh karyawan Perusahaan, dalam dan/atau luar negeri.

2. OBJECTIVE
a. To provide clear standard eligibility of travel allowances due to business matters.
b. To standardize process of Business Travel undertaken by the Company's employee, domestic and/or overseas.

3. RUANG LINGKUP
Kebijakan ini berlaku untuk karyawan tetap dengan Perjanjian Kerja Waktu Tidak Tertentu ("PKWTT"), karyawan kontrak dengan Perjanjian Kerja Waktu Tertentu ("PKWT"), selanjutnya disebut sebagai "Karyawan", dari PT AXA Financial Indonesia, selanjutnya disebut sebagai "Perusahaan", dan karyawan yang dipekerjakan melalui vendor outsource Perusahaan.

3. SCOPE
This Policy is applied to employees under indefinite employment contract (Perjanjian Kerja Waktu Tidak Tertentu/"PKWTT"), fixed term employment contract (Perjanjian Kerja Waktu Tertentu/"PKWT") of PT AXA Financial Indonesia, hereinafter referred as the "Company", and employment under outsourced vendor of the Company.

4. REFERENSI
1. AXA Security Instruction – Travel Security 2.2
2. Group Security – Travel Security Guideline
3. Airline Security Guideline (2022)
4. AXA Group Country Ratings (2024)
5. Delegation of Authority (DoA)

4. REFERENCE
1. AXA Security Instruction – Travel Security 2.2
2. Group Security – Travel Security Guideline
3. Airline Security Guideline (2022)
4. AXA Group Country Ratings (2024)
5. Delegation of Authority (DoA)

5. DEFINISI
a. Perjalanan Dinas
Perjalanan singkat ke luar tempat kerja resmi dari pemegang jabatan, dengan tujuan untuk melakukan pengamatan,

5. DEFINITION
a. Business Travel
A short trip to destinations outside the jobholder's official workplace with the purpose to conduct an observation,""",
"""pengawasan, pengadaan bisnis, monitoring, business procurement, pengendalian, diskusi, perekrutan, control, discussion, recruitment, konferensi, seminar, pelatihan, conference, seminar, training, trial, persidangan, mediasi, dan/atau tujuan mediation and/or other similar serupa lainnya, dalam kaitan purposes, for the Company's interest kepentingan Perusahaan, dan dengan and with the Company's formal instruksi formal Perusahaan. instruction.

b. Permintaan Perjalanan Dinas (BTR) b. Business Trip Requisition (BTR)
Formulir yang semua karyawan harus Form that all employees have to lengkapi untuk permintaan perjalanan complete for business trip request and dinas dan disetujui sesuai DoA (Delegasi get it approve as per DoA (Delegation of Otoritas) sebelum melakukan perjalanan Authority) before going on business trip, bisnis, sesuai dengan Lampiran 2.a yang as per the appendix 2.a attached to this melekat pada Kebijakan ini. policy.

c. Penggantian Biaya Perjalanan Dinas c. Business Trip Reimbursement (BTS)
(BTS)
Sejumlah uang yang diberikan kepada The replacement of money given to Karyawan setelah melakukan Perjalanan employees after a business trip that Dinas yang mencakup pengeluaran includes daily expenses.
sehari-hari.

d. Delegasi Otoritas (DoA) d. Delegation of Authorities (DoA)
Daftar delegasi otoritas pemberi A set of delegation authorities approval persetujuan atas pengeluaran rutin list for the routine expenditure of the operasional Perusahaan yang berlaku Company operational which is apply as sesuai parameter Perusahaan. per Company parameter.

e. Pengeluaran Rutin e. Routine Expenditure
Otorisasi batasan pengeluaran rutin A routine expense limit tier authorization terkait operasional atas Perjalanan in related to operational on Business Dinas. Travel.

f. Otorisasi Pengurangan f. Deduction Authorization
Format yang digunakan Karyawan untuk A template to be used by Employee to memberikan konfirmasi pemotongan gaji provide salary deduction confirmation terkait pembayaran di muka yang tidak due to unsettled cash advance as terselesaikan pada Lampiran 4 yang Appendix 4 attached to this Policy.
melekat pada Kebijakan ini.

g. Formulir Biaya Transportasi g. Transportation Expense Form
Format yang digunakan oleh Karyawan A template to be used by Employee as untuk mempersiapkan laporan to prepare justification report expense pertanggung jawaban penerimaan receipt related to the Business Travel pengeluaran atas transportasi dari transportation with valid original printed Perjalanan Dinas, dengan bukti receipt, or online receipt (e-receipt), as pembayaran yang sah, pada Lampiran 3 Appendix 3 attached to this Policy.
yang melekat pada Kebijakan ini.

h. Presiden Direktur h. President Director

5
Internal""",
"""Seseorang yang dalam bertindak sebagai pemberi persetujuan akhir dari setiap Perjalanan Dinas Internasional.

A person who is in act as a final approver of any International Business Travel.

i. Direktur/ Chief of Function (Mancomm)
Seorang yang bertanggung jawab sebagai pemberi persetujuan fungsional untuk Perjalanan Dinas, yang juga bertanggung jawab atas beberapa bagian dalam setiap fungsi. (pengambil keputusan tertinggi dalam setiap fungsi pada Perusahaan).

i. Director/ Chief of Function (Mancomm)
A person who responsible as functional approver in related to Business Travel approval who also responsible for several section in each function. (a highest approver within each function in the Company).

j. Atasan Langsung
Karyawan dengan tingkat jabatan 6 (enam) keatas dengan kewenangan untuk mengawasi dan memberikan instruksi kepada Karyawan lain pada garis otoritasnya.

j. Line Manager
Employee with job grade 6 (six) and above with authority to supervise and to give orders to other Employees in his/her line of authority.

k. Agen Perjalanan
Pihak ketiga yang ditunjuk oleh Perusahaan dan terdaftar dalam daftar vendor dari departemen pengadaan, untuk menyediakan jasa transportasi penerbangan dan akomodasi terkait Perjalanan Dinas Perusahaan.

k. Travel Agent
A third party that appointed by the Company and registered in the procurement department list of suppliers, to provide flight transportation and accommodation related services for the Company's Business Travel.

6. TUGAS DAN TANGGUNG JAWAB
1. Karyawan
Mengisi dan memberikan dokumen pendukung sesuai dengan daftar lampiran.

6. ROLES AND RESPONSIBILITY
1. Employee
Fill in and submit the supporting documents according to the list of appendices.

2. Departemen Human Resources "(HR)"
a. Melakukan benchmark terhadap regulasi lokal dan AXA Group mengenai Perjalanan Dinas, setidaknya setahun sekali atau apabila ada perubahan.

2. Human Resources Department "(HR)"
a. Benchmarking to the local regulations and AXA Group on the Business Travel at least once a year or if any changes.

b. Melakukan sosialisasi Perjalanan Dinas apabila ada perubahan baik melalui email blast ataupun sesi kelas sosialisasi.

b. Conduct Business Travel socialization if there is any changes, either via email blast or in a class sessions.

c. Chief of HR mengetahui setiap pengajuan perjalanan dinas dan memo penugasan luar negeri dan perjalanan dinas yang melebihi budget.

c. Chief of Human Resources acknowledging every request and assignment memo for overseas business trips and business trips that exceed the budget.

d. Melakukan Evaluasi terhadap pelaksanaan peraturan ini.

d. Conducting an evaluation of the implementation of this regulation.

6
Internal""",
"""3. Line Manager/ Head of Dept.
Proposing Assignment Memo and approving Domestic Business Travel request.

4. Respective BOD/Chief of Function (Mancomm)
Approving request for domestic business trips, overseas business trips, and business trips that exceed the budget.

5. Chief Financial Officer (CFO)
Approving every request for business trips that exceed the budget.

6. President Director/ CEO
Approving Overseas Business Travel request.

7. GENERAL RULES
a. An Employee is assumed performing Business Travel where the destination city range is more than 60 (sixty) km from his/her current official workplace. The estimate distance (in km) of the city to be visit will be mentioned in Business Travel Request form.

b. Business Travel expense is calculated based on durations (number of days) of the trip, according to Employee entitlement based on job grade applied in the Company standards as stated in Appendix 1 attached to this Policy.

c. Overtime is not applicable for Employee who performing Business Travel both domestic and overseas.

d. Employee who travels due to receiving a Company award, or Company entertainment, is not entitled to business trip reimbursement, except for Employee appointed to escort person(s) receiving a Company award or appointed to become a committee / manager / responsible person for the trip.e. Dokumen imigrasi, tiket dan pemesanan hotel dalam maupun luar negeri, atau proses administrasi lainnya dapat dilakukan oleh administrator yang ditunjuk departemennya – ini diberlakukan untuk departemen yang kerap mengadakan Perjalanan Dinas, dengan mengacu pada standar yang disediakan dan vendor resmi yang tercantum dalam Departemen Pengadaan.

f. Setiap Atasan Langsung bertanggung jawab untuk memastikan semua Perjalanan Dinas yang diminta oleh stafnya diselesaikan dalam pengaturan jadwal serta administrasi yang tepat sesuai dengan standar dan prosedur yang ada, dan semua proses yang diperlukan telah diverifikasi sebagaimana mestinya.

g. Perjalanan Dinas untuk Karyawan harus mematuhi aturan-aturan terkait dengan Travel Security yang dinyatakan dalam Panduan Keamanan Perjalanan (Lampiran 5), Panduan Keamanan Penerbangan (Lampiran 7a dan 7b), Instruksi Keamanan (Lampiran 8), dan AXA Group Country Ratings (Lampiran 10) dalam hal transportasi penerbangan, akomodasi, dan perjalanan yang melekat pada Kebijakan ini.

h. Karyawan yang akan bepergian dengan pilihan maskapai dengan kategori non-preferred harus mengisi formulir pengecualian dengan alasan yang kuat dan memperoleh persetujuan sesuai dengan matriks persetujuan yang tercantum pada formulir (Lampiran 7c)

i. Setiap Atasan Langsung wajib mensosialisasikan dan mengimplementasikan Kebijakan ini.""",
"""
8. PROSEDUR PERJALANAN DINAS
1. Pengajuan Perjalanan Dinasa. Employee may only perform Business Travel if the Business Travel Requisition (by APS for employee who have access and Business Travel Requisition Form if the employee does not have access) and to attach assignment memo and memo/invitation (if any) if you are attending external events, AFI's Agency/Telemarketing event and Training from HR. Business Travel Requisition to be approved by authorized person as stated in Delegated of Authorities Parameter (DOA) as following:

i. All Domestic Business Travels should need approval from Line Manager/Head Department, and respective BOD/ Chief of Function (Mancomm).

ii. All International Business Travels should need approval from respective BOD/ Chief of Function (Mancomm), approval from CEO, and acknowledgement from CHRO.

iii. If budget for Business Travel (include for training purposes) exceed the approved budget, the approval must be in accordance with the Delegation of Authority (DoA).

iv. In the case of Employee who has traveled for more than 15 (fifteen) calendar days consecutively in a month, then President Director's approval of the Company will be required in order to be allowed to do the next travel.

b. In situations where cash advance is required, Employee should fill out the Business Travel Requisition form (Appendix 2a) and should complete with estimated costs, to be submitted to Finance Department at least 5 (five) working days prior to departure. This travel expenses advance is only applicable for daily allowance, transportation intercity assignment and airport tax expenses. Cash advance only applicable for Employee with job grade 7tingkat jabatan 7 (tujuh) ke bawah dan persetujuan mengacu pada Delegation of Authority (DoA).
""",
"""c. Departemen Keuangan atas konfirmasi dari Atasan Langsung berhak untuk menolak lebih lanjut Permintaan Perjalanan Dinas ketika laporan pertanggung jawaban Perjalanan Dinas sebelumnya tidak dilengkapi.

d. Biaya Perjalanan Dinas yang disetujui dan dapat diproses untuk Penggantian Biaya Perjalanan Dinas mengacu pada ketentuan mengenai hak tingkat jabatan yang berlaku sesuai dengan standar jabatan (Lampiran 1).

e. Dalam hal dimana Perjalanan Dinas diajukan dengan memo acara (contoh: undangan acara dari eksternal, acara agency / telemarketing AFI, pelatihan dari HR, dan lain lain), maka penggantian biaya perjalanan harian tidak berlaku untuk biaya-biaya yang sudah termasuk dalam paket perjalanan yang tercantum dalam memo acara.

f. Tanggung jawab masing-masing departemen untuk mempersiapkan anggaran terkait tunjangan Perjalanan Dinas, termasuk namun tidak terbatas pada: penggantian biaya perjalanan dinas, transportasi dan akomodasi.

2. Penyelesaian Perjalanan Dinas
a. Karyawan diwajibkan untuk bertanggung jawab dalam menyelesaikan Perjalanan Dinas masing-masing secara mandiri dengan mengisi Formulir Penyelesaian Perjalanan Dinas (Lampiran 2b), melampirkan Formulir Permintaan Perjalanan Dinas yang sudah disetujui dan diajukan sebelumnya, bukti pembayaran asli yang dicetak, atau bukti pembayaran online (e-receipt) jika menggunakan sarana transportasi online, memo acara (jika tersedia), dan menyerahkannya kepada Departemen Keuangan paling lambat dalam 30 (tiga puluh) hari kalender setelah hari terakhir dari Perjalanan Dinas. Persetujuan Penyelesaian Perjalanan Dinas mengacu pada Delegation of Authority (DoA).b. The approval of daily business trip expense reimbursement refers to the provisions regarding the level of entitlement applied in the Company's standard (Appendix 1).
""",
"""
c. Approval for transportation expenses will refer to the Operating Expenditures approval. Business Travel Transportation Settlement must be settled by using Transportation Expense Claim Form (Appendix 3).

d. Employee who does not complete the Business Travel Settlement Form, cannot make a Request for Reimbursement of Travel Expenses, therefore Employees are required to complete the Business Travel Settlement form before they can take the next Business Travel.

e. Employees are responsible for completing the required documents if there are any document deficiencies found after the review by the Finance Department. The Finance Department has the right to reject the request for reimbursement of travel expenses if the submitted documents are incomplete.

f. In the event where the cash advance is outstanding for more than 30 (thirty) calendar days without any satisfactory explanation, the amount will be deducted from the next monthly salary. This will be the responsibility of the Employee and/or the Direct Supervisor by using the Deduction Authorization Form (Appendix 4). The Finance Department must inform the Human Resources department before the payroll cut-off date.

g. In the event that the actual travel expenses exceed the approved cash advance through a memo, the approval of the settlement will follow Routine Expenditure approval (refer to Delegation of Authority). The total of the cash advance and the settlement should not more than the entitle limit as per job grade.h. In the event where fraud or misappropriation is found, it will become the responsibility of the Line Manager and/or the respective Employee which one proven guilty and Human Resources have rights to issue a warning letter and/or ended with work dismissal.
""",
"""i. The Finance Department will process the reimbursement of Business Travel Expenses within the time limit according to the regulations in the Finance Payment Policy.

**Daily Trip Expenses**
On the day of Employee's departed from or arrived at his/her official workplace, Business Travel expenses shall be calculated as follows:

i. Departure time from the origin city* before 12.00 p.m. and/or arrival time back at the rigin city* after 12.00 p.m. shall be calculated as 1 (one) full day trip.

ii. Departure time from the origin city* after 12.00 p.m. and/or arrival time back at the origin city* before 12.00 p.m. shall be calculated as a 1/2 (half) day.

*the time indicated on the ticket of transport mode.

iii. Employee must take same day flight for training/meeting held in the afternoon, except there is no same day flight schedule to the destination city.

iv. Employee must take the same day flight home for training/meeting finished in the afternoon, except there is no same day flight home schedule.

v. Employee conducting Business Travel with categorization as 1/2 (half) day trip will only be entitled for 50% (fifty) of the standard daily business trip expense.
""",
"""**Transportation**
vi. Transportations for the Business Travel applied with following conditions:· Ke bandara / pelabuhan / stasiun kereta dari kediaman/kantor dan sebaliknya
· To airport / seaport / train station from residence/office and vice versa
· Ke kota tujuan
· To destination city
· Antar kota dan/atau daerah terpencil
· Intercity and/or remote area

vii. Ke bandara / pelabuhan / stasiun dari kediaman / kantor dan sebaliknya, Perusahaan akan memberikan pembayaran berdasarkan penggantian biaya transportasi yang sebenarnya jika Karyawan menggunakan sarana transportasi umum (misalnya anggaran taksi, kereta bandara/shuttle bus).

vii. To airport / seaport / station from residence / office and vice versa, the Company will reimburse based on actual cost for transport expenses if the Employee is using reasonable public transportation mode (e.g., budget taxi, airport train/ shuttle bus).

viii. Karyawan diperbolehkan memilih sarana transportasi untuk mencapai kota tujuan (contoh, pesawat terbang, kereta, kapal laut, bis antar kota) melalui vendor resmi departemen pengadaan setelah mendapatkan persetujuan lengkap untuk Pengajuan Perjalanan Dinas. Dalam rangka menggunakan transportasi penerbangan, Karyawan harus membeli tiket pulang pergi 21 (dua puluh satu) hari sebelum waktu keberangkatan agar memperoleh maskapai pilihan yang dikehendaki dengan tarif terendah (Tiket promosi dengan waktu, tanggal tetap dan tidak dapat dikembalikan). Pemesanan kurang dari 21 (dua puluh satu) hari hanya diijinkan untuk perjalanan yang dikarenakan kondisi yang tidak terduga. Dalam hal demikian, Agen Perjalanan akan memesan maskapai terdaftar dengan tarif terendah yang dianggarkan.

viii. Employee is allowed to choose transportation mode in order to reach the destination city (e.g., flight, train, ferry, shuttle bus) through procurement's official vendor after obtaining full approval for the Business Travel Request. In order using flight transportation Employee must booked and issued return trip flight ticket minimum 21 (twenty-one) days prior the departure time to get lowest fare of Preferred Airline (Promo Ticket with Fix Date, Fix Flight and Non-Refundable). Ticket issuance less than 21 (twenty-one) days prior only allowed for travel due to unforeseen circumstances. In such case, the Travel Agent will book the lowest fare of available airlines.

ix. Antarkota dan/atau daerah terpencil selama Perjalanan Dinas, atas persetujuan Atasan Langsung dari Karyawan dengan tingkat jabatan 7 (tujuh) kebawah dengan jumlah maksimum Rp. 300.000, - per hari / sarana transportasi lain antar kota di daerah tersebut;

ix. Intercity and/or remote area during Business Travel, subject to Line Manager's approval employee with job grade 7 (seven) and below with maximum amount IDR 300.000, - per day / other intercity transportation mode in remote area;

x. Penggantian untuk biaya transportasi Perjalanan Dinas yang meliputi: pelabuhan/pajak bandara, asuransi perjalanan jika berlaku. Rincian lebih lanjut tentang hak atas transportasi disediakan pada Lampiran 1 poin B moda transportasi, yang melekat pada Kebijakan ini.

x. Reimbursement for Business Travel transportation costs covering: seaport/airport tax, travel insurance if applicable. Further details on transportation entitlements are provided in Appendix 1 point B transportation mode, attached to this Policy.
13
Internal""",
"""Akomodasi | Accommodation

xi. Penyedia jaringan akomodasi mengacu pada vendor resmi procurement yang ditunjuk dengan tarif Perusahaan dan diberikan kepada karyawan setelah mendapatkan persetujuan lengkap, dimana kategori kamarnya sesuai ketentuan yang berlaku dari penyedia akomodasi tersebut. Rincian lebih lanjut disediakan pada Lampiran 1 yang melekat pada Kebijakan ini. | xi. The accommodation network provider refers to the appointed Travel Agent with corporate rate ceiling and will be given after obtaining full approval for the Business Travel Request, where the room category is to be defined by the accommodation provider. Further details are provided in Appendix 1 attached to this Policy.

xii. Karyawan dapat menerima peningkatan kelas kamar jika tidak menambah biaya atas tarif perusahaan. | xii. Employee may accept a room upgrade if no additional cost from corporate rate/ceiling.

xiii. Karyawan diperbolehkan untuk menggunakan lokasi akomodasi yang sama atas persetujuan Atasan Langsung, dalam kasus menghadiri acara, dengan jadwal, kerja/rapat di lokasi yang sama dengan Regulator/Pemerintah dan/atau Presiden Direktur. | xiii. Employee is allowed to use the same accommodation location with the Line Manager's approval, in the case of attending the same event, schedule, work/meeting location with Regulatory/Government and/or President Director.

xiv. Rincian dari standar Perusahaan untuk akomodasi dalam negeri dan biaya terkait lainnya disajikan pada Lampiran 1 yang melekat pada Kebijakan ini. | xiv. Details on the Company's standard for domestic accommodation and other related expenses are provided in Appendix 1 attached to this Policy.

9. PERJALANAN DINAS LUAR NEGERI | 9. OVERSEAS BUSINESS TRAVEL

a. Ke Negara tujuan, dalam rangka menggunakan transportasi penerbangan, Karyawan harus membeli tiket pulang pergi sebagai berikut agar memperoleh maskapai pilihan yang dikehendaki dengan tarif terendah (Tiket promosi dengan waktu, tanggal tetap dan tidak dapat dikembalikan): | a. To destination country, in order using flight transportation Employee must booked and issued return trip flight ticket as follow to get lowest fare of Preferred Airline (Promo Ticket with Fix Date, Fix Flight and Non-Refundable):

· Minimum 61 (enam puluh satu) hari sebelum waktu keberangkatan (untuk penerbangan antar benua). | · Minimum 61 (sixty-one) days prior the departure time (for intercontinental flights).

· Minimum 21 (dua puluh satu) hari sebelum waktu keberangkatan (untuk penerbangan dalam benua) | · Minimum 21 (twenty-one) days prior the departure time (for intra continental flights).

Pemesanan kurang dari pengaturan yang disebutkan sebelumnya hanya diperbolehkan untuk perjalanan yang dikarenakan situasi yang tidak terduga. Dalam hal demikian, Agen Perjalanan akan memesan maskapai terdaftar dengan tarif terendah yang dianggarkan. | Ticket issuance less than the beforementioned arrangement only allowed for travel due to unforeseen circumstances. In such case, the Travel Agent will book the lowest fare of available airlines.

14
Internal""",
"""b. Administration cost occurs for the Business Travel assignment will be borne by the Company, i.e. the costs for obtaining and/or extension of passport, visa, including phone bills for business purpose during business traveling.

c. Accommodation expense will be referred as per Employee job grades, and with ceiling rates based on corporate accommodation rate.

d. Residence/office to airport to residence/office transportation will be based on actual reimbursement.

e. Intercity and/or remote area during Business Travel, subject to Line Manager's approval employee with job grade 7 (seven) and below with maximum amount IDR 300.000, - per day / other intercity transportation mode in remote area.

f. Details on the Company standard for overseas accommodation, transportation, and other related expenses are provided in Appendix 1 attached to this Policy.

g. In the event of Business Travels arranged directly by the Regional or Group Office, the existing standards may be adjusted in line with Regional or Group Office guidelines.

10. REVIEW FREQUENCY
a. This Policy shall be effective as of September 9th 2024 and will be reviewed every two years. If there is any further needs or changes, the Policy shall be amended and/or supplemented accordingly.

b. With the implementation of this Policy, all prior policies and/or guidelines related to this Policy are revoked.

c. This Policy is Company' proprietary information. Any unauthorized disclosure, use or dissemination, either whole or partial of this Policy is prohibited unless for Company interest purposes and obtained prior approval from the Company.
15
Internal""",
"""d. Kebijakan ini dibuat dalam bahasa Indonesia dan bahasa Inggris. Apabila terdapat perbedaan penafsiran di antara bahasa Indonesia dan bahasa Inggris, maka bahasa Indonesia yang berlaku.

d. This Policy is made in Indonesian and English languages. If there is any discrepancy between the Indonesian and English version, the Indonesian shall prevail.# LAMPIRAN | APPENDICIES
""",
"""
a. Lampiran 1 : Hak-hak Perjalanan Dinas | a. Appendix 1 : Business Travel Entitlement

b. Lampiran 2a : Permintaan Perjalanan Dinas | b. Appendix 2a : Business Travel Requisition

c. Lampiran 2b : Formulir Penyelesaian Perjalanan Dinas | c. Appendix 2b : Business Travel Settlement Form

d. Lampiran 3 : Formulir Klaim Biaya Transportasi | d. Appendix 3 : Transportation Expense Claim Form

e. Lampiran 4 : Formulir Otorisasi Pengurangan | e. Appendix 4 : Deduction Authorization Form

f. Lampiran 5 : Group Security - Panduan Keamanan Perjalanan | f. Appendix 5 : Group Security – Travel Security Guideline

g. Lampiran 6 : Hotel Terdaftar | g. Appendix 6 : Listed Hotel

h. Lampiran 7a : Pedoman Keamanan Penerbangan | h. Appendix 7a : Airline Security Guideline

i. Lampiran 7b : Keamanan Penerbangan (preferred airlines) | i. Appendix 7b : Airline Security (preferred airlines)

j. Lampiran 7c : Formulir Pengecualian Maskapai | j. Appendix 7c : Airline Exception Form

k. Lampiran 8 : Instruksi Keamanan | k. Appendix 8 : Security Instruction

l. Lampiran 9 : Memo Penugasan | l. Appendix 9 : Assignment Memo

m. Lampiran 10 : AXA Group Country Ratings | m. Appendix 10 : AXA Group Country Ratings

n. Lampiran 11 : Delegation of Authority | n. Appendix 11 : Delegation of Authority"""
]

