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
    "https://manusiabiasa.serv00.net/cen/epg/cubmu.php",
    "https://manusiabiasa.serv00.net/cen/epg/firstmedia.php",
    "https://manusiabiasa.serv00.net/cen/epg/starhub.php",
    "https://manusiabiasa.serv00.net/cen/epg/mewatch.php",
    "https://cindo.mra.my.id/epg/vid.php",
    "https://manusiabiasa.serv00.net/cen/epg/optus.php",
    "https://manusiabiasa.serv00.net/cen/epg/astro.php",
    "https://manusiabiasa.serv00.net/cen/epg/antik.php",
    "https://www.bevy.be/bevyfiles/malaysiapremium2.xml",
    "https://www.bevy.be/bevyfiles/germanypremium3.xml",
    "https://www.bevy.be/bevyfiles/unitedstates1.xml",
    "https://www.bevy.be/bevyfiles/italy1.xml",
    "https://www.bevy.be/bevyfiles/italy2.xml",
    "https://www.bevy.be/bevyfiles/portugal2.xml",
    "https://manusiabiasa.serv00.net/cen/epg/alkass.php",
    "https://manusiabiasa.serv00.net/cen/epg/vision.php",
    "https://cindo.mra.my.id/epg/sky.php",
    "https://cindo.mra.my.id/epg/mytv.php",
]

# Memanggil fungsi untuk mendownload semua EPGs
download_epg(urls)
