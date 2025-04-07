def vigenere_encrypt(plaintext, key):
    # Konversi plaintext dan key ke huruf besar dan buang non-alphabet
    plaintext = ''.join([c for c in plaintext.upper() if c.isalpha()])
    key = key.upper()

    ciphertext = ''
    key_length = len(key)
    
    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord('A')
        k = ord(key[i % key_length]) - ord('A')
        c = (p + k) % 26
        ciphertext += chr(c + ord('A'))
    
    return ciphertext

# Contoh penggunaan
plaintext = """
Di sebuah perpustakaan tua, rak-rak buku berjejer rapi, menyimpan ribuan pengetahuan.
Seorang mahasiswa duduk di sudut ruangan, tenggelam dalam buku tebal yang ia baca. Lampu
redup menerangi meja kayu yang penuh dengan catatan dan referensi. Suara lembaran buku
yang dibalik terdengar pelan, berpadu dengan ketukan pena di atas kertas. Seorang pustakawan
berjalan perlahan, memastikan semua buku tersusun rapi. Di luar jendela, hujan rintik-rintik
turun, menambah suasana tenang di dalam ruangan. Waktu terasa berjalan lambat di tempat ini,
memberi kesempatan bagi siapa pun untuk mendalami ilmu tanpa gangguan.
"""

key = "DELVIAHIVAKARISMA"
ciphertext = vigenere_encrypt(plaintext, key)
print("Ciphertext:\n", ciphertext)
