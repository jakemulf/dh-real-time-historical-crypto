"""
real_time_crypto.py

A Deephaven Python script that reads real-time crypto data
"""
from deephaven import time_table

import requests

import json

COIN = "btc"
EXCHANGE = "bitfinex"
CURRENCY = "usd"

def report_usage_metrics(allowance):
    """
    Logs the remaining credits for the API

    Parameters:
        allowance (dict): The JSON API response as a dictionary
    Returns:
        None
    """
    cost = allowance["cost"]
    remaining = allowance["remaining"]
    print(f"Used {cost} CryptoWatch credits, {remaining} remaining.")

def retrieve_coin_current_price(coin, exchange, currency):
    """
    Retrieves the real-time price for the given coin, exchange, and currency

    Parameters:
        coin (str): The coin whose price to retrieve
        exchange (str): The exchange to access
        currency (str): The currency to evaluate the price in
    Returns:
        float: The current price of the coin as a float
    """
    url = f"https://api.cryptowat.ch/markets/{exchange}/{coin}{currency}/price"
    response = requests.get(url)

    if not(response.status_code == 200):
        print(f"Request for {coin}-{currency} on {exchange} failed")
        return None

    json_data = response.json()
    report_usage_metrics(json_data["allowance"])

    try:
        return float(json_data["result"]["price"])
    except:
        print(f"Failed to parse data for {coin}-{currency} on {exchange}")
        return None

real_time_data = (time_table("00:01:00")
            .update([
                "Price = (double)retrieve_coin_current_price(COIN, EXCHANGE, CURRENCY)",
                "Coin = COIN",
                "Exchange = EXCHANGE",
                "Currency = CURRENCY",
            ])
)
