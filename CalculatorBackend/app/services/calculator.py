"""
main calculator
"""
import requests


def get_btc_price():
    """
    Gets the BTC price from public domain
    :return: btc_price
    """
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    result = requests.get(url).json()
    # print(result)
    btc_price = result['bpi']['USD']['rate_float']
    print(f"BTC Price is {btc_price}")
    return btc_price


def get_network_hash_rate():
    """
    Gets the Network Hash Rate from public domain
    :return: network_hash_rate
    """
    url = 'https://2ff50fee-4d9b-4870-88cc-9417959b5f60.mock.pstmn.io/network-info'
    result = requests.get(url).json()
    # print(result)
    network_hash_rate = result['networkHashRate'] * 1000
    print(f"Network Hash Rate is {network_hash_rate}")
    return network_hash_rate


def crypto_profit_calculator(input):
    """
    Main Crypto Profit Calculator 
    
    :return: dictionary of CryptoCalcResult
    """
    # conver pc to kW
    power_consumption_kw = input.power_consumption / 1000
    initial_investment = input.initial_investment

    # costs
    cost_daily = power_consumption_kw * input.electricity_cost * 24
    cost_monthly = cost_daily * 30
    cost_yearly = cost_daily * 365

    # default values from public domain
    block_reward_btc = 3.125
    blocks_per_day = 144
    btc_price = get_btc_price()
    network_hash_rate = get_network_hash_rate()

    # revenue in usd and btc
    btc_revenue_daily = (input.hash_rate / network_hash_rate) * block_reward_btc * blocks_per_day
    revenue_daily = btc_revenue_daily * btc_price
    revenue_monthly = revenue_daily * 30
    revenue_yearly = revenue_daily * 365

    btc_revenue_monthly = btc_revenue_daily * 30
    btc_revenue_yearly = btc_revenue_daily * 365

    # profits
    daily_profit = revenue_daily - cost_daily
    monthly_profit = revenue_monthly - cost_monthly
    yearly_profit = revenue_yearly - cost_yearly

    if monthly_profit > 0:
        breakeven_timeline = initial_investment / monthly_profit
    else:
        breakeven_timeline = initial_investment

    cost_to_mine = initial_investment / revenue_yearly

    return {
        "dailyCost": cost_daily,
        "monthlyCost": cost_monthly,
        "yearlyCost": cost_yearly,
        "dailyRevenueUSD": revenue_daily,
        "monthlyRevenueUSD": revenue_monthly,
        "yearlyRevenueUSD": revenue_yearly,
        "dailyRevenueBTC": btc_revenue_daily,
        "monthlyRevenueBTC": btc_revenue_monthly,
        "yearlyRevenueBTC": btc_revenue_yearly,
        "dailyProfitUSD": daily_profit,
        "monthlyProfitUSD": monthly_profit,
        "yearlyProfitUSD": yearly_profit,
        "breakevenTimeline": breakeven_timeline,
        "costToMine": cost_to_mine
    }
