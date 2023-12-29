from flask import Flask, jsonify
from pycoingecko import CoinGeckoAPI
import time
import logging

app = Flask(__name__)

# Disable the Flask reloader
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

cg = CoinGeckoAPI()

def get_prices_for_ids(crypto_ids, currencies):
    current_timestamp = int(time.time())
    prices = {}

    for crypto_id in crypto_ids:
        crypto_prices = {}

        for currency in currencies:
            try:
                # Subtracting 24 hours (in seconds) to get the 'from_timestamp'
                from_timestamp = current_timestamp - 24 * 60 * 60

                data = cg.get_coin_market_chart_range_by_id(id=crypto_id, vs_currency=currency, from_timestamp=from_timestamp, to_timestamp=current_timestamp)
                price = data['prices'][-1][1]

                crypto_prices[currency] = price
            except Exception as e:
                logger.error(f"Error fetching data for {crypto_id} in {currency}: {e}")
                crypto_prices[currency] = None

        prices[crypto_id] = crypto_prices

    return prices

@app.route('/')
def crypto_prices():
    supported_crypto_ids = ['bitcoin', 'ethereum']
    supported_currencies = ['usd', 'eur']

    try:
        prices = get_prices_for_ids(supported_crypto_ids, supported_currencies)
        return jsonify(prices)
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=8080)
