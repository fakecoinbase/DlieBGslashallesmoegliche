import coinbasepro as cbp
import time

ethPrice = 100.0
dt = 0.05

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
        return True
    else:
        return False

while True:
    client = cbp.PublicClient()
    eth = client.get_product_ticker("ETH-EUR")

    ethPrice = float(eth["price"])

    if nextBuy():
        if shouldBuy():
            buy()
    else:
        if shouldSell():
            sell()

    time.sleep(60*60)