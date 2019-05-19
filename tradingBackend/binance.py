base_polo_url = 'https://api.binance.com/api/v1/ticker/24hr?symbol={}'
altcoins = ['ETH','LTC','XRP','ETC','STR','DASH','SC','XMR','XEM']

def get_crypto_data(binance_pair):
    '''Retrieve cryptocurrency data from Binance'''
    json_url = base_polo_url.format(binance_pair)
    data_df = get_json_data(json_url, binance_pair)
    data_df = data_df.set_index('date')
    return data_df

def get_altcoin_data():
    altcoin_data = {}
    for altcoin in altcoins:
        coinpair = 'BTC_{}'.format(altcoin)
        crypto_price_df = get_crypto_data(coinpair)
        altcoin_data[altcoin] = crypto_price_df
