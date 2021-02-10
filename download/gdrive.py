from sys import platform
import requests

def get(id):
    URL = "https://docs.google.com/uc?export=download"
    sess = requests.session()
    r = sess.get(URL, params={"id": id}, stream=True)
    return r

def download_from_gdrive_with_id(id, file_name=" ", linux=True):
    if not file_name.strip():
        r = get(id)
        file_name = r.headers.get("Content-Disposition").split(";")[1].split("=")[1]
    
    if platform == "linux" and linux:
        from os import system as system_prot
        wget = r'wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://docs.google.com/uc?export=download&id='+str(id)+'" -O- | sed -rn "s/.*confirm=([0-9A-Za-z_]+).*/\\1\\n/p")&id='+str(id)+'" -O '+str(file_name)+' && rm -rf /tmp/cookies.txt'
        system_prot(wget)

