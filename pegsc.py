import requests
import xml.etree.ElementTree as ET

def download_and_merge_epg(urls, output_file="merged_epg.xml"):
    # Buat elemen root baru untuk hasil gabungan
    root = ET.Element("tv")
    root.set("generator-info-name", "CendolCen")

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            try:
                # Parsing XML dari konten
                tree = ET.ElementTree(ET.fromstring(response.content))
                epg_root = tree.getroot()

                for programme in epg_root.findall("programme"):
                    root.append(programme)
                print(f"Berhasil menambahkan data dari {url}")
            except ET.ParseError:
                print(f"Gagal mem-parsing XML dari {url}")
        else:
            print(f"Gagal mengunduh {url}. Status code: {response.status_code}")

    # Menulis hasil gabungan ke file
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"File EPG gabungan berhasil disimpan sebagai {output_file}")

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
    "https://astvstreamingpro.my.id/epg/vision.php",
    "https://cindo.mra.my.id/epg/sky.php",
    "https://cindo.mra.my.id/epg/mytv.php",
]

# Jalankan fungsi EPG
download_and_merge_epg(urls)
