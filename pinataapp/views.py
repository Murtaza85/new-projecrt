from django.shortcuts import render
from pathlib import Path
import requests
import os


def home(request):
    return render(request, 'Home.html')


def uploadfile(request):
    filename = request.POST['uploadfile']
    PINATA_BASE_URL = "https://api.pinata.cloud/"
    endpoint = "pinning/pinFileToIPFS"
    filepath = "static/MR Meeting Agenda.docx"
    #filename = filepath.split("/")[-1:][0]
    headers = {"pinata_api_key": os.getenv("50a8dc53de376e2527ca"), "pinata_secret_api_key": os.getenv("67dfefb7f8ba83390f57a05d8cf469944594ba2b4700201e1f6cc7e27931047a")}
    with Path(filepath).open("rb") as fp:
    #fp = open(filename, "rb")
        file_binary = fp.read()

        response = requests.post(PINATA_BASE_URL + endpoint, files={"file": (filename, file_binary)}, headers=headers,)

        #ipfs_hash = response.json()["IpfsHash"]
        # "./img/0-COOL.png" -> "0-COOL.png"
        #filename = filepath.split("/")[-1:][0]
        #image_uri = f"ipfs://{ipfs_hash}?filename={filename}"

    print(f"Successfully uploaded {filename} to pinata.")
    print(response.json())
    # return image_uri

    return render(request, 'upload.html')






