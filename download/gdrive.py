from sys import platform
import requests

def get(id):
    URL = "https://docs.google.com/uc?export=download"
    sess = requests.session()
    r = sess.get(URL, params={"id": id}, stream=True)
    return r

def download_from_gdrive(id, destination):
    URL = "https://docs.google.com/uc?export=download"
    sess = requests.session()
    response = sess.get(URL, params={"id": id}, stream=True)
    token = get_confirm_token(response)
    if token:
        params = {"id": id, "confirm": token}
        response = sess.get(URL, params=params, stream=True)
    save_response_content(response, destination)

def save_response_content(response, destination, chunk_size=32768):
    chunk_size = chunk_size
    with open(destination, "wb") as f:
        for chunk in response.iter_content(chunk_size):
            if chunk:
                f.write(chunk)
                
def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            return value
    return None

def download_from_gdrive_with_id(id, file_name=""):
    if not file_name.strip():
        r = get(id)
        file_name = r.headers.get("Content-Disposition").split(";")[1].split("=")[1]
    
    if platform == "linux":
        from os import system as system_prot
        wget = r'wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://docs.google.com/uc?export=download&id='+str(id)+'" -O- | sed -rn "s/.*confirm=([0-9A-Za-z_]+).*/\\1\\n/p")&id='+str(id)+'" -O '+str(file_name)+' && rm -rf /tmp/cookies.txt'
        system_prot(wget)
    elif platform == "win32":
        download_from_gdrive(id, file_name)

