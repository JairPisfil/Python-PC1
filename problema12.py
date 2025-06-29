MIMES = {
    'gif':'image/gif',
    'jpg':'image/jpeg',
    'zip':'application/zip',
    'jpeg':'image/jpeg',
    'png':'image/png',
    'pdf':'application/pdf',
    'txt':'text/plain'
    }

response = input('ext name: ')
response = response.lower().strip()

_, ext = response.split('.')


if ext.lower() in MIMES.keys():
    x = MIMES.get(ext)
    print(x)
else:
    print('application/octet-stream')