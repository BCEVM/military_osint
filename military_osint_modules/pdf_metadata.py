from PyPDF2 import PdfReader

def run():
    print("\n=== PDF Metadata Extractor ===")
    path = input("Path ke file PDF >> ")
    try:
        reader = PdfReader(path)
        metadata = reader.metadata
        for key, value in metadata.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"[!] Gagal membaca metadata: {e}")
