"""
Scraping Ulasan Aplikasi Melalui Google Play Store
"""

# Mengimpor pustaka google_play_scraper untuk mengakses ulasan dan informasi aplikasi dari Google Play Store.
from google_play_scraper import app, reviews, Sort, reviews_all

# Mengambil semua ulasan dari aplikasi whatsapp
scrapreview = reviews_all(
    'com.whatsapp',        # ID paket aplikasi
    lang='id',             # Bahasa ulasan (default: 'en')
    country='id',          # Negara (default: 'us')
    sort=Sort.MOST_RELEVANT, # Urutan ulasan (default: Sort.MOST_RELEVANT)
    count=1000             # Jumlah maksimum ulasan yang ingin diambil
)

# Menyimpan hasil scraping ke dalam file 'whatsapp_review.csv'
import csv
with open('whatsapp_review.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Review", "Rating"])
    for review in scrapreview:
        writer.writerow([review['content'], review['score']])
print("Scraping selesai. Data tersimpan dalam file 'whatsapp_review.csv'")
