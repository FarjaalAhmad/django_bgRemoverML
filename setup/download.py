import gdown

url = 'https://drive.google.com/uc?id=1s52ek_4YTDRt_EOkx1FS53u-vJa0c4nu'
output = 'basnet.pth'
gdown.download(url, output, quiet=False)
gdown.cached_download(url, output, postprocess=gdown.extractall)

url = 'https://drive.google.com/uc?id=1rbSTGKAE-MTxBYHd-51l2hMOQPT_7EPy'
output = 'u2netp.pth'
gdown.download(url, output, quiet=False)
gdown.cached_download(url, output, postprocess=gdown.extractall)

url = 'https://drive.google.com/uc?id=1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ'
output = 'u2net.pth'
gdown.download(url, output, quiet=False)
gdown.cached_download(url, output, postprocess=gdown.extractall)
