from binance.client import Client as binance_Client 
from twilio.rest import Client as twil_Client
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY_SECRET = os.getenv('SECRET_KEY')
API_KEY = os.getenv('API_KEY')

# Your Account SID from twilio.com/console
account_sid = os.getenv('ACCOUNT_SID')
# Your Auth Token from twilio.com/console
auth_token  = os.getenv('AUTH_TOKEN')

to = os.getenv('TO')

#Binance auth
binance = binance_Client(API_KEY, API_KEY_SECRET)
#print(client)

#Twillio Auth
twil = twil_Client(account_sid, auth_token)



# balance = client.get_asset_balance(asset='USDT')
# print(balance)


def dcaIn():
    buy = binance.create_order(symbol="BNBUSDT", side="buy", type="MARKET",
                                                     quoteOrderQty=10)
    #print(f"You just spent {buy['cummulativeQuoteQty']} USDT to buy {buy['executedQty']} BNB")
    #send notification to twil
    message = twil.messages.create(to=to, from_="+19853324576",body=f"You just spent {buy['cummulativeQuoteQty']} USDT to buy {buy['executedQty']} BNB")
    print(message.sid)

dcaIn()
