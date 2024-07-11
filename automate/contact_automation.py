import pandas as pd
import pdfplumber

pdf_path = "automate\data.pdf"
with pdfplumber.open(pdf_path) as pdf:
    first_page = pdf.pages[0]
    text = first_page.extract_text()

lines = text.split('\n')

data = []

for line in lines:
    columns = line.split()
    if len(columns) > 7:
        nomor_telp = columns[-1]
        provinsi = columns[-2]
        kota_domisili = columns[-3]
        gender = columns[-4]
        email_peserta = columns[-5]
        nama_peserta = " ".join(columns[4:-5]) 
        email_fasil = columns[3]
        nama_fasil = columns[2]
        group = columns[0]
        data.append([group, nama_fasil, email_fasil, nama_peserta, email_peserta, gender, kota_domisili, provinsi, nomor_telp])

df = pd.DataFrame(data, columns=['Group', 'Nama Fasil', 'Email Fasil', 'Nama Peserta', 'Email Peserta', 'Gender', 'Kota Domisili', 'Provinsi', 'Nomor Telp'])

df['WhatsApp Link'] = 'https://wa.me/' + df['Nomor Telp']

df.to_csv('peserta_with_wa_link.csv', index=False)


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(20)

for index, row in df.iterrows():
    driver.get(row['WhatsApp Link'])
    time.sleep(5)
    message = f"Hi {row['Nama Peserta']}, ini adalah pesan otomatis dari saya. Terima kasih sudah mendaftar workshop kami. Jika ada pertanyaan, jangan ragu untuk menghubungi saya. Terima kasih."
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    time.sleep(5)

driver.quit()

print('All messages sent!')