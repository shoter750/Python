import requests
r = requests.get('https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/MobileNetSSD_deploy.caffemodel')
r.headers['Content-Type']
with open('./Nural_Network/MobileNetSSD_deploy.caffemodel', 'wb') as output:
    output.write(r.content)
