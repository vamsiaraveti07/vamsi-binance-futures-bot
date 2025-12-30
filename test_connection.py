from binance import Client

API_KEY="mBe6XgO9HZiV96bjEqhi27OoJdEMQ1I1YulBOz3Le1Ll9YpAYpdaSYQ3l6THHFem"
API_SECRET="uFvlca91GHmKnPES2O0r6X1KrztUe6zlDn0Gv4DQBqqRZfu686LtPBMHn9tTXdCv"

client = Client(
    api_key=API_KEY,
    api_secret=API_SECRET,
    testnet=True
)

client.FUTURES_URL = "https://testnet.binancefuture.com"

try:
    balances = client.futures_account_balance()
    print("✅ CONNECTED TO BINANCE FUTURES TESTNET")

    for b in balances:
        if b["asset"] == "USDT":
            print("USDT Balance:", b["balance"])

except Exception as e:
    print("❌ ERROR:", e)
