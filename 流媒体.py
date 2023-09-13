from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import requests,base64,time,hashlib,datetime,json,re
from urllib.parse import quote
def rsa_encrypt(text):
    ts =  int(round(time.time() * 1000))

    header = {
        'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    pub_url = 'http://112.6.51.73:8281/TheNextWebApp/publicKey?nowTime=%s' %ts
    RV_url = 'http://112.6.51.73:8281/TheNextWebApp/requestVerificatioinToken?nowTime=%s' %ts
    res = requests.get(pub_url,headers=header)
    RV_token = requests.get(RV_url,headers=header).json()
    VSLcookie = res.headers['Set-Cookie']
    # print( )
    header2 = {
    'Content-Type': 'application/json; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Cookie': VSLcookie
    }
    # res2.json()
    pub_key = requests.get(pub_url,headers=header2).json()
    # 公钥
    pub_key = "-----BEGIN PUBLIC KEY-----\n %s\n-----END PUBLIC KEY-----" %pub_key
    rsakey = RSA.importKey(pub_key)
    cipher = PKCS1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(bytes(text, encoding="utf8")))
    return cipher_text.decode('utf-8'),VSLcookie,RV_token

def login(username,password):
    md5_obj = hashlib.md5(password.encode("utf-8"))
    pd_md5=md5_obj.hexdigest() #加密1次
    md5_obj2 = hashlib.md5( (username + pd_md5).encode("utf-8"))
    password_md5 = md5_obj2.hexdigest() # mima
    rsa = rsa_encrypt(password_md5)

    header = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Type": "application/json;charset=utf-8",
        "Cookie": rsa[1],
        "RV_token":rsa[2],
        "Host": "112.6.51.73:8281",
        "Proxy-Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "X-App-Name": "TheNextWebApp:112.6.51.73",
        "X-LC-RequestId": "bdddc7e9-f1d0-4bd1-87c9-24700068d6ec",
        "X-Operate-Code": "vsl_0",
        "X-Operate-Name": "common.login",
        "X-Requested-With": "XMLHttpRequest"
    }
    data = {
        'userName': username,
        'password': rsa[0]
    }

    data_str = json.dumps(data,ensure_ascii=False)
    ts =  int(round(time.time() * 1000))
    login_url = 'http://112.6.51.73:8281/TheNextWebApp/login?nowTime=%s' %ts
    res = requests.post(url=login_url,headers=header,data=data_str.encode('utf-8'))
    ress =json.loads(res.json())
    token = ress['token']
    userCode = ress['userCode']
    VSLcookie = re.split(';',  res.headers['Set-Cookie'])[0]
    return VSLcookie,token,userCode


def getdara(username,password):
    token = login(username,password)
    ts =  int(round(time.time() * 1000))
    timedate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    url = 'http://112.6.51.73:8281/TheNextWebApp/videoService/devicesManager/channel/searchChannels'
    data = {
        "nowTime":ts,
        "orgCode":"S4NbecfYB1DIST0E0KCAV4",
        "page":1,
        "pageSize":110,
        "cascading":1,
        "unitType":1

    }
    header = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Type": "application/json;charset=utf-8",
        "Cookie": "isCertificate=true;vslLang=zh;isCertLogin=false;useRetention=false;useJtlog=false;isHideCloudGroup=false;isHideVideoGroup=false;vslLastLoginIp=39.71.127.131;vslParameter=1;%s;vslUserCode=%s;subSystemHeader=%s;vslUserName=%s;vslLastLoginTime=%s;vslUserNameStr=%s;useRas=true"%(token[0],token[2],token[1],quote(username),quote(timedate),quote(username) ),
        "Host": "112.6.51.73:8281",
        "Proxy-Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "X-App-Name": "TheNextWebApp:112.6.51.73",
        "X-LC-RequestId": "bdddc7e9-f1d0-4bd1-87c9-24700068d6ec",
        "X-Operate-Code": "vsl_0",
        "X-Operate-Name": "common.login",
        "X-Requested-With": "XMLHttpRequest"
    }
    res = requests.get(url=url,headers=header,params=data)

    print(res.json())
if __name__ == "__main__":
    token = getdara("青岛西海岸新区粮食收储中心中心库","shandong@075")
    # # getdara()


