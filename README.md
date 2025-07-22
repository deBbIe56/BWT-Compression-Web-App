# BWT Compression Web App

A web-based application for **compressing and decompressing genomic (DNA) data** using the **Burrows-Wheeler Transform (BWT)**, **Run-Length Encoding (RLE)**, and **Huffman Coding**. Designed for researchers, students, and institutions working with large DNA datasets who need an efficient, lossless compression solution that runs in lightweight environments.

---

## 🔬 Project Overview

This application enables:
- **Lossless compression** of DNA sequences using BWT → RLE → Huffman.
- **Decompression** from Huffman binary + code map.
- **Encryption** of compressed output (e.g. AES encryption - WIP).
- **Download support** for binary and code map files.
- **Decompression via upload or paste input.**
- **Web-based and offline desktop-ready system.**

---

## ⚙️ Features

- ✅ Upload `.txt` DNA sequence file and compress it.
- ✅ View and copy the BWT-transformed, RLE-compressed, and Huffman-encoded output.
- ✅ Paste encoded binary + Huffman map to decompress original sequence.
- ✅ Download compressed files.
- ✅ Save logs and compression metadata to SQLite (upcoming).
- ✅ Package into a **desktop executable** using PyInstaller (upcoming).
- ✅ GitHub version control support.

---

## 🧪 Technologies Used

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python (Flask)  
- **Compression Algorithms**:  
  - Burrows-Wheeler Transform (BWT)  
  - Run-Length Encoding (RLE)  
  - Huffman Coding  
- **Database (optional)**: SQLite  
- **Deployment**: GitHub, local server

---

## 🚀 Getting Started

### 🔧 Prerequisites
Ensure you have Python installed.

### 🖥️ Run Locally

```bash
git clone https://github.com/deBbIe56/BWT-Compression-Web-App.git
cd BWT-Compression-Web-App/bwt_compression_web
pip install -r requirements.txt
python app.py
