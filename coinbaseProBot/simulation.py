import coinbasepro as cbp
import time
from pyfcm import FCMNotification

ethPrice = 100.0
dt = 0.01

def buy():
    f = open("eur.txt", "r")
    eur = float(f.read())-0.5
    f.close()

    print(str(eur)+"€ vorhanden!")

    f = open("eur.txt", "w")
    f.write("0")
    f.close()

    eth = eur/ethPrice
    print(str(eth)+" ETH gekauft!")

    push_service = FCMNotification(api_key="AAAAOL_f7Vw:APA91bHx4r3FM3rH2RxU2JtjoMRMm8At-c9XGrUnxpp6BCHtQLup1uvjAzIifOBAMMqCDOi_Z0O6wgqYGMtVJdt4EUdVzBXiUmpP_kTJRWB_9TmJBTp2II3tELBvSBhQvxMZxxLYP_Xu")
    registration_ids = ["dSvcsDop4ek:APA91bFcfxJak8NLbyxjpXavu3RLbf28jNLRRcAcTTN7_dzg-MS8rzN3uRsPvMgpmPNvpJCaRIFMOliUDX169uf3cH2V7isYYMa0F6Hn5VZRunVhz_ZJBUot5m9V2HotGtbBxtAULUvM"]
    message_title = "ETH gekauft"
    message_body = str(eth)+" ETH vorhanden"
    result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

    f = open("eth.txt", "w")
    f.write(str(eth))
    f.close()

def sell():
    f = open("eth.txt", "r")
    eth = float(f.read())
    f.close()

    print(str(eth)+" ETH vorhanden!")

    f = open("eth.txt", "w")
    f.write("0")
    f.close()

    eur = (eth*ethPrice)-0.5
    print(str(eur)+"€ gekauft!")

    push_service = FCMNotification(api_key="AAAAOL_f7Vw:APA91bHx4r3FM3rH2RxU2JtjoMRMm8At-c9XGrUnxpp6BCHtQLup1uvjAzIifOBAMMqCDOi_Z0O6wgqYGMtVJdt4EUdVzBXiUmpP_kTJRWB_9TmJBTp2II3tELBvSBhQvxMZxxLYP_Xu")
    registration_ids = ["dSvcsDop4ek:APA91bFcfxJak8NLbyxjpXavu3RLbf28jNLRRcAcTTN7_dzg-MS8rzN3uRsPvMgpmPNvpJCaRIFMOliUDX169uf3cH2V7isYYMa0F6Hn5VZRunVhz_ZJBUot5m9V2HotGtbBxtAULUvM"]
    message_title = "ETH verkauft"
    message_body = str(eur)+"€ vorhanden"
    result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

    f = open("eur.txt", "w")
    f.write(str(eur))
    f.close()

def nextBuy():
    f = open("eur.txt", "r")
    eur = float(f.read())
    f.close()
    f = open("eth.txt", "r")
    eth = float(f.read())
    f.close()

    if(eur==0):
        return False
    if(eth==0):
        return True

def shouldBuy():
    global dt

    client = cbp.PublicClient()
    stats = client.get_product_24hr_stats("ETH-EUR")

    qt = stats["open"]/stats["last"]

    if qt > 1 and qt-1 > dt:
        dt = abs(qt-1)
        f = open("dt.txt", "w")
        f.write(str(dt))
        f.close()
        return True
    else:
        return False

def shouldSell():
    global dt

    client = cbp.PublicClient()
    stats = client.get_product_24hr_stats("ETH-EUR")

    qt = stats["open"]/stats["last"]

    if qt < 1 and abs(qt-1) > dt:
        dt = abs(qt-1)
        f = open("dt.txt", "w")
        f.write(str(dt))
        f.close()
        return True
    else:
        return False

while True:
    client = cbp.PublicClient()
    eth = client.get_product_ticker("ETH-EUR")

    ethPrice = float(eth["price"])
    f = open("dt.txt", "r")
    dt = float(f.read())
    f.close()

    if nextBuy():
        if shouldBuy():
            buy()
    else:
        if shouldSell():
            sell()

    time.sleep(120)
