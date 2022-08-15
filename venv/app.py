from flask import Flask, Response, request

import json

from yahoo import search_in_yahoo_finance
import pprint
app = Flask(__name__)


@app.route("/")
def main():
    return "Hola Mundo"

@app.route("/api/search/")
def search():
    ticker = request.args.get("params")
    financial_info = search_in_yahoo_finance(ticker=ticker)
    return Response(json.dumps({
        "ticker": ticker,
        "longname": financial_info["quotes"][0]["longname"],
        "name": financial_info["quotes"][0]["shortname"],
        "shortname": financial_info["quotes"][0]["shortname"],
        "symbol": financial_info["quotes"][0]["symbol"],
        "exchange": financial_info["quotes"][0]["exchange"],
        "score": financial_info["quotes"][0]["score"],
        "exchDisp": financial_info["quotes"][0]["exchDisp"],
        "sector": financial_info["quotes"][0]["sector"],
        "industry": financial_info["quotes"][0]["industry"],
        "isYahooFinance": financial_info["quotes"][0]["isYahooFinance"],
        "typeDisp": financial_info["quotes"][0]["typeDisp"],
    }), status=200, mimetype="application/json")
    #app.run(host='0.0.0.0') //esta linea nos ayudaria que la applicacion funcione con ip del equipo como servidor


    #http://127.0.0.1:5000/api/search/?params=ko
    #carlos_guerrero
    #Walter
    
@app.route ("/api/current-price")
def current_price():
    return "<p>Hello, current price!</p>"
