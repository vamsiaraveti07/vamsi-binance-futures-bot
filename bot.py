from binance import Client
from orders import (
    place_market_order,
    place_limit_order,
    place_stop_limit_order
)
API_KEY="mBe6XgO9HZiV96bjEqhi27OoJdEMQ1I1YulBOz3Le1Ll9YpAYpdaSYQ3l6THHFem"
API_SECRET="uFvlca91GHmKnPES2O0r6X1KrztUe6zlDn0Gv4DQBqqRZfu686LtPBMHn9tTXdCv"


client = Client(API_KEY, API_SECRET, testnet=True)
client.FUTURES_URL = "https://testnet.binancefuture.com"


def show_balance():
    balances = client.futures_account_balance()
    for b in balances:
        if b["asset"] == "USDT":
            print("USDT Balance:", b["balance"])


def show_positions():
    positions = client.futures_position_information()
    active = False
    for p in positions:
        if float(p["positionAmt"]) != 0:
            active = True
            print(
                f"{p['symbol']} | Qty: {p['positionAmt']} | "
                f"PnL: {p['unRealizedProfit']}"
            )
    if not active:
        print("No open positions.")


def menu():
    print("\n==============================")
    print(" Binance Futures Testnet Bot ")
    print("==============================")
    print("1. Place Market Order")
    print("2. Place Limit Order")
    print("3. Place Stop-Limit Order")
    print("4. View USDT Balance")
    print("5. View Open Positions")
    print("6. Exit")


def main():
    while True:
        menu()
        choice = input("Choose option (1-6): ")

        if choice == "1":
            symbol = input("Symbol (BTCUSDT): ").upper()
            side = input("Side (BUY/SELL): ").upper()
            qty = float(input("Quantity: "))
            order = place_market_order(client, symbol, side, qty)
            print("Order:", order["status"] if order else "FAILED")

        elif choice == "2":
            symbol = input("Symbol (BTCUSDT): ").upper()
            side = input("Side (BUY/SELL): ").upper()
            qty = float(input("Quantity: "))
            price = float(input("Limit Price: "))
            order = place_limit_order(client, symbol, side, qty, price)
            print("Order:", order["status"] if order else "FAILED")
        
        elif choice == "3":
            symbol = input("Symbol (BTCUSDT): ").upper()
            side = input("Side (BUY/SELL): ").upper()
            qty = float(input("Quantity: "))
            stop_price = float(input("Stop Price: "))
            limit_price = float(input("Limit Price: "))

            order = place_stop_limit_order(
                client, symbol, side, qty, stop_price, limit_price
            )

            print("Order:", order["status"] if order else "FAILED")


        elif choice == "4":
            show_balance()

        elif choice == "5":
            show_positions()

        elif choice == "6":
            print("Exiting bot. Bye 👋")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
