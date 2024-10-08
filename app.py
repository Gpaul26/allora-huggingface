from flask import Flask, Response
import requests
import json
import pandas as pd
import torch
import random

# create our Flask app
app = Flask(__name__)
        
def get_simple_price(token):
    base_url = "https://api.coingecko.com/api/v3/simple/price?ids="
    token_map = {
        'ETH': 'ethereum',
        'SOL': 'solana',
        'BTC': 'bitcoin',
        'BNB': 'binancecoin',
        'ARB': 'arbitrum'
    }
    token = token.upper()
    if token in token_map:
        url = f"{base_url}{token_map[token]}&vs_currencies=usd"
        return url
    else:
        raise ValueError("Unsupported token") 
               
# define our endpoint
@app.route("/inference/<string:token>")
def get_inference(token):

    try:
      
        url = get_simple_price(token)
        headers = {
          "accept": "application/json",
          "x-cg-demo-api-key": "CG-<your-API-coingecko>" # replace with your API key
        }
    
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
          data = response.json()
          if token == 'BTC':
            price1 = data["bitcoin"]["usd"]*1.02
            price2 = data["bitcoin"]["usd"]*0.99
          if token == 'ETH':
            price1 = data["ethereum"]["usd"]*1.02
            price2 = data["ethereum"]["usd"]*0.98
          if token == 'SOL':
            price1 = data["solana"]["usd"]*1.02
            price2 = data["solana"]["usd"]*0.98
          if token == 'BNB':
            price1 = data["binancecoin"]["usd"]*1.02
            price2 = data["binancecoin"]["usd"]*0.98
          if token == 'ARB':
            price1 = data["arbitrum"]["usd"]*1.02
            price2 = data["arbitrum"]["usd"]*0.98
          random_float = str(round(random.uniform(price1, price2), 2))
        return random_float
    except Exception as e:
       # return Response(json.dumps({"pipeline error": str(e)}), status=500, mimetype='application/json')
        url = get_simple_price(token)
        headers = {
          "accept": "application/json",
          "x-cg-demo-api-key": "CG-<your-API-coingecko>" # replace with your API key
        }
    
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
          data = response.json()
          if token == 'BTC':
            price1 = data["bitcoin"]["usd"]*1.02
            price2 = data["bitcoin"]["usd"]*0.98
          if token == 'ETH':
            price1 = data["ethereum"]["usd"]*1.02
            price2 = data["ethereum"]["usd"]*0.98
          if token == 'SOL':
            price1 = data["solana"]["usd"]*1.02
            price2 = data["solana"]["usd"]*0.98
          if token == 'BNB':
            price1 = data["binancecoin"]["usd"]*1.02
            price2 = data["binancecoin"]["usd"]*0.98
          if token == 'ARB':
            price1 = data["arbitrum"]["usd"]*1.02
            price2 = data["arbitrum"]["usd"]*0.98
          random_float = str(round(random.uniform(price1, price2), 2))
        return random_float

    
# run our Flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
