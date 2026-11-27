# Belajar Python Bareng
 
Repo belajar Python yang dibuat **bersama-sama**, gratis, dan terbuka untuk siapa saja. Mau pemula yang baru kenal `print()`, atau yang sudah jago dan pengen berbagi ilmu, semuanya boleh ikut.
 
![License](https://img.shields.io/badge/license-MIT-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
 
---
 
## Tentang Repo Ini
 
Repo ini berisi catatan, contoh kode, dan latihan Python dari dasar sampai lanjut. Bedanya dengan repo belajar biasa: **setiap orang belajar di branch-nya sendiri, lalu hasilnya digabung ke `main`** lewat Pull Request. Jadi sambil belajar Python, kamu sekaligus belajar Git dan kerja kolaborasi.
 
## Tujuan
 
- Belajar Python dengan bahasa yang santai dan mudah dipahami
- Belajar Git & GitHub lewat praktik langsung
- Membangun kumpulan materi yang bisa dipakai siapa saja
- Saling review kode dan saling koreksi
---
 
## Struktur Repo
 
```
belajar-python/
├── 01-dasar/
│   ├── README.md          # penjelasan materi
│   ├── contoh/            # contoh kode
│   └── latihan/           # soal latihan
├── 02-tipe-data/
├── 03-percabangan-perulangan/
├── 04-fungsi/
├── 05-oop/
├── catatan-pribadi/       # jurnal belajar tiap kontributor
│   └── <username>/
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```
 
> Struktur ini bisa berkembang. Kalau kamu mau tambah topik baru, buat foldernya dengan nomor urut berikutnya.
 
---
 
## Model Belajar: Satu Orang, Satu Branch
 
**Wajib menggunakan branch.** Semua kontribusi, sekecil apa pun (termasuk typo), harus dikerjakan di branch sendiri dan masuk lewat Pull Request. Push langsung ke `main` tidak diperbolehkan, dan Pull Request yang berasal dari `main` akan ditolak.
 
Aturan mainnya sederhana:
 
| Branch | Fungsi |
|---|---|
| `main` | Isi final yang sudah direview. **Dilarang push langsung ke sini.** |
| `<namakamu >`| ini branch untuk kamu mengerjakan pembelajaran kalian  |
 
### Alurnya
 
```
 belajar materi → tulis catatan/kode di branch kamu → buka Pull Request → direview → validasi admin (dapa) -> yang progress terbanyak akan di push ke master
```
 
---
 
## Cara Mulai
 
### 1. Fork & clone repo
catatan : sudah meminta request bergabung melalui WA chat untuk kolabolator akses
 
Klik tombol **Fork** di kanan atas halaman GitHub, lalu:
 
```bash
git clone https://github.com/Dapalagingoding/python_learn.git
cd python_learn
```
 
Tambahkan repo asli sebagai `upstream` supaya bisa sinkron:
 
```bash
git remote add upstream https://github.com/Dapalagingoding/python_learn.git
```
 
### 2. Sinkronkan dengan `main` terbaru
 
```bash
git checkout main
git pull upstream main
```
 
### 3. Buat branch baru
 
```bash
git checkout -b materi/tipe-data
```
 
### 4. Kerjakan, lalu commit
 
```bash
git add .
git commit -m "materi: tambah penjelasan mutable vs immutable"
```
 
### 5. Push dan buka Pull Request
 
```bash
git push origin materi/tipe-data
```
 
Buka GitHub, klik **Compare & pull request**, isi deskripsi singkat, lalu kirim.
 
### 6. Review & merge
 
Maintainer atau kontributor lain akan memberi komentar. Perbaiki kalau diminta, lalu setelah disetujui PR kamu di-merge ke `main`.
 
---
 
## Aturan Commit
 
Pakai format `jenis: deskripsi singkat`:
 
| Jenis | Kapan dipakai |
|---|---|
| `materi` | Menambah atau mengubah penjelasan |
| `latihan` | Menambah soal atau jawaban |
| `fix` | Memperbaiki typo atau bug |
| `docs` | Mengubah dokumentasi (README, dll.) |
| `refactor` | Merapikan tanpa mengubah isi |
 
Contoh:
 
```
materi: tambah bab dictionary
latihan: jawaban soal perulangan nomor 1-5
fix: perbaiki typo di bab fungsi
```
 
---
 
## Cara Berkontribusi
 
Kamu bisa ikut membantu dengan cara:
 
- Menulis materi baru
- Membuat soal latihan
- Melaporkan atau memperbaiki kesalahan
- Menerjemahkan atau memperjelas penjelasan
- Mereview Pull Request orang lain
**Baru pertama kali kontribusi?** Cari issue berlabel [`good first issue`](../../labels/good%20first%20issue). Itu tugas ringan yang cocok untuk pemula.
 
Panduan lengkap ada di [CONTRIBUTING.md](CONTRIBUTING.md).
 
### Checklist sebelum buka Pull Request
 
- [ ] Saya bekerja di branch sendiri, bukan di `main`
- [ ] Branch dibuat dari `main` terbaru
- [ ] Nama branch sesuai aturan
- [ ] Kode sudah dicoba dan bisa jalan
- [ ] Penjelasan mudah dipahami pemula
- [ ] Tidak ada file yang tidak perlu (`__pycache__`, `.env`, dll.)
---
 
## Tata Krama
 
- Hargai semua level kemampuan. Tidak ada pertanyaan bodoh.
- Beri feedback yang membangun, bukan menjatuhkan.
- Jelaskan alasan, bukan cuma bilang "salah".
- Pakai bahasa yang sopan dan inklusif.
Pelanggaran berulang bisa berujung pada penghapusan akses kontribusi.
 
---
 
## Kebutuhan
 
- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- Akun [GitHub](https://github.com/)
- Code editor (VS Code, PyCharm, dll.)
Cek instalasi:
 
```bash
python --version
git --version
```
 
---
 
## Roadmap
 
- [x] Dasar Python & tipe data
- [ ] Percabangan & perulangan
- [ ] Fungsi
- [ ] Struktur data (list, dict, set, tuple)
- [ ] OOP
- [ ] File handling & error handling
- [ ] Modul & package
- [ ] Mini project bersama
Punya ide topik lain? [Buat issue baru](../../issues/new).
 
---
 
## Lisensi
 
Proyek ini memakai lisensi [MIT](LICENSE). Kamu bebas memakai, mengubah, dan membagikan ulang, asalkan mencantumkan atribusi.
 
---
 
## Dukung Proyek Ini
 
Kalau repo ini bermanfaat:
 
- Kasih bintang di GitHub
- Bagikan ke teman yang lagi belajar Python
- Ikut berkontribusi
Selamat belajar!
 