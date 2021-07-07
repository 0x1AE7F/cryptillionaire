import time
import os
import os.path
import requests
from bs4 import BeautifulSoup
import time
from crypto_prices import crypto
# import html2text


main_run_path = os.path.dirname(os.path.abspath(__file__))

print("Debug Info:")
print(main_run_path)

saves_path_main = main_run_path + "/saves/"

def tutorial():
    print("Welcome to Cryptillionaire")
    time.sleep(0.5)
    print("In this game you need to invest into Crypto to get MONEY (§)\nby trading it")
    time.sleep(0.5)
    print("You are starting with 1000$ and work your way up to be the next millionaire")
    time.sleep(0.5)
    tutorial_answer = input("Have you read the Text above? \n Hint: type YES to procede: ")
    if tutorial_answer == "YES":
        f = open("./saves/tutorial.txt", 'a')
        f.write("Tutorial is Done")
        f.close()
        print("Please Restart your Game to let it finish setting up")



def show_cypto():


    #Bitcoin Stats
    url_btc = "https://coinmarketcap.com/currencies/bitcoin/markets/"
    req = requests.get(url_btc)
    soup = BeautifulSoup(req.content, 'html.parser')
    price_btc = soup.find("div", {"class": "priceValue___11gHJ"})

    print("Bitcoin: ")
    print(crypto.bitcoin_price + "\n")


    #Ethereum Stats
    url_eth = "https://coinmarketcap.com/currencies/ethereum/"
    req = requests.get(url_eth)
    soup = BeautifulSoup(req.content, 'html.parser')
    price_eth = soup.find("div", {"class": "priceValue___11gHJ"})

    print("Ethereum: ")
    print(cypto.ethereum_price + "\n")


    #Binance Coin Stats
    url_bnb = "https://coinmarketcap.com/currencies/binance-coin/"
    req = requests.get(url_bnb)
    soup = BeautifulSoup(req.content, 'html.parser')
    price_bnb = soup.find("div", {"class": "priceValue___11gHJ"})

    print("Binance Coin: ")
    print(crypto.binance_price + "\n")


    #Tether Stats
    url_usdt = "https://coinmarketcap.com/currencies/tether/"
    req = requests.get(url_usdt)
    soup = BeautifulSoup(req.content, 'html.parser')
    price_usdt = soup.find("div", {"class": "priceValue___11gHJ"})

    print("Tether: ")
    print(price_usdt.text + "\n")


def sell_crypto():
    print("What Crypto do you want to sell?")
    time.sleep(1)

    f_btc = open(saves_path_main + "bitcoin.txt", 'r+')
    btc_owned = f_btc.read()
    f_btc.close()


    f_eth = open(saves_path_main + "ethereum.txt", 'r+')
    eth_owned = f_eth.read()
    f_eth.close()


    f_binance = open(saves_path_main + "binance.txt", 'r+')
    binance_owned = f_binance.read()

    f_tether = open(saves_path_main + "tether.txt", 'r+')
    tether_owned = f_tether.read()

    print("1. Bitcoin:")
    print("Owned: " + btc_owned  + "\n")

    print("2. Ethereum:")
    print("Owned: " + eth_owned  + "\n")

    print("3. Binance Coin:")
    print("Owned: " + binance_owned  + "\n")

    print("4. Tether:")
    print("Owned: " + tether_owned  + "\n")

    sell_choice = input(": ")

    if sell_choice == "1":
        selling_name = str("Bitcoin")
        selling = btc_owned
        save_file_sell = saves_path_main + "bitcoin.txt"
    if sell_choice == "2":
        selling_name = str("Ethereum")
        selling = eth_owned
        save_file_sell = saves_path_main + "ethereum.txt"
    if sell_choice == "3":
        selling_name = str("Binance")
        selling = binance_owned
        save_file_sell = saves_path_main + "binance.txt"
    if sell_choice == "4":
        selling_name = str("Tether")
        selling = tether_owned
        save_file_sell = saves_path_main + "tether.txt"

    time.sleep(2)
    print("Selected: " + selling_name + "\n" + "Owned: " + selling)
    print("How much to sell of crypto?")
    sell_amount = input(": ")

    #Removing Crypto from Account

    selling = float(selling) - float(sell_amount)
    if float(selling) < 0:
        print("Not enough Crypto!")
        selling = float(selling) + float(sell_amount)
    elif float(selling) > 0:
            time.sleep(1)
            input("Press ENTER to confirm sell...")
            f_confirm_sell_save = open(save_file_sell, 'w')
            f_confirm_sell_save.write(str(selling))

    def add_money():
        if sell_choice == "1":
            url_btc = "https://coinmarketcap.com/currencies/bitcoin/markets/"
            req = requests.get(url_btc)
            soup = BeautifulSoup(req.content, 'html.parser')
            price_btc = soup.find("div", {"class": "priceValue___11gHJ"})
            price_current_sell = price_btc
        elif sell_choice == "2":
            url_eth = "https://coinmarketcap.com/currencies/ethereum/"
            req = requests.get(url_eth)
            soup = BeautifulSoup(req.content, 'html.parser')
            price_eth = soup.find("div", {"class": "priceValue___11gHJ"})
            price_current_sell = price_eth
        elif sell_choice == "3":
            url_bnb = "https://coinmarketcap.com/currencies/binance-coin/"
            req = requests.get(url_bnb)
            soup = BeautifulSoup(req.content, 'html.parser')
            price_bnb = soup.find("div", {"class": "priceValue___11gHJ"})
            price_current_sell = price_bnb
        elif sell_choice == "4":
            url_usdt = "https://coinmarketcap.com/currencies/tether/"
            req = requests.get(url_usdt)
            soup = BeautifulSoup(req.content, 'html.parser')
            price_usdt = soup.find("div", {"class": "priceValue___11gHJ"})
            price_current_sell = price_usdt
          

            money_adding_sell = price_current_sell * sell_amount

            f_money_sell = open(saves_path_main + "money.txt", 'r')
            money_sell_bank = f_money_sell.read()
            f_money_sell.close()

            f_money_sell = open(saves_path_main + "money.txt", 'w')
            f_money_sell.write(money_sell_bank + money_adding_sell)
            f_money_sell.close()
            print("You got: " + str(money_adding_sell + money_sell_bank) + "\n" + "from selling: " + sell_amount + " " + selling_name)
        add_money()
        

def main_menu():
    print("Welcome to Cryptillionaire")
    time.sleep(0.4)
    print("Available Choices:")
    time.sleep(0.4)
    print("1:  Show Crypto Prices")
    time.sleep(0.3)
    print("2: Sell Crpto")
    time.sleep(0.3)
    print("3: Buy Crypto")
    time.sleep(0.3)
    print("4: View History")
    time.sleep(0.3)
    print("5: Exit")

    menu_choice = input("\n : ")
    if menu_choice == "1":
        show_cypto()

    if menu_choice == "2":
        sell_crypto()

    if menu_choice == "3":
        print("Work in progress")

    if menu_choice == "4":
        print("Work in progress")
    
    if menu_choice == "5":
        print("Exiting...")
        time.sleep(3)
        exit()


if os.path.isfile(saves_path_main + "tutorial.txt"):
    main_menu()
else:
    tutorial()





    #Tasks: Check selling for errors