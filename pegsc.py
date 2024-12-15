import requests

def download_epg(urls):
    for url in urls:
        # Mendapatkan nama file dari URL
        file_name = url.split('/')[-1]
        
        # Mengirim permintaan GET ke URL
        response = requests.get(url)
        
        # Memeriksa apakah permintaan berhasil
        if response.status_code == 200:
            # Menyimpan konten ke file
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"File {file_name} berhasil didownload.")
        else:
            print(f"Gagal mendownload file {file_name}. Status code: {response.status_code}")

# Daftar URL EPG
urls = [
    "https://astvstreamingpro.my.id/epg/cubmu.php",
    "https://astvstreamingpro.my.id/epg/firstmedia.php",
    "https://astvstreamingpro.my.id/epg/starhub.php",
    "https://astvstreamingpro.my.id/epg/mewatch.php",
    "https://astvstreamingpro.my.id/epg/vid.php",
    "https://astvstreamingpro.my.id/epg/optus.php",
    "https://www.bevy.be/bevyfiles/malaysiapremium2.xml",
    "https://www.bevy.be/bevyfiles/germanypremium3.xml",
    "https://www.bevy.be/bevyfiles/unitedstates1.xml",
    "https://www.bevy.be/bevyfiles/italy1.xml",
    "https://www.bevy.be/bevyfiles/italy2.xml",
    "https://www.bevy.be/bevyfiles/portugal2.xml",
]

# Memanggil fungsi untuk mendownload semua EPGs
download_epg(urls)
