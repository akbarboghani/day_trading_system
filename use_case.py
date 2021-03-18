import trading_strategy2 as ts
import market_actions_strategy2 as ma
from create_one_day_data import create_df


list1 = ['AAPL', 'MSFT', 'AMZN', 'FB', 'GOOGL', 'GOOG', 'TSLA', 'BRK-B', 'JPM', 'JNJ', 'V', 'DIS', 'NVDA', 'UNH', 'MA', 'PG', 'PYPL', 'HD', 'BAC', 'INTC', 'CMCSA', 'NFLX', 'XOM', 'VZ', 'ADBE', 'ABT', 'T', 'CRM', 'CVX', 'ABBV', 'AVGO', 'CSCO', 'KO', 'PFE', 'MRK', 'WMT', 'PEP', 'TMO', 'NKE', 'LLY', 'ACN', 'TXN', 'MDT', 'QCOM', 'MCD', 'WFC', 'COST', 'NEE', 'HON', 'DHR', 'UNP', 'BMY', 'C', 'AMGN', 'PM', 'LIN', 'SBUX', 'ORCL', 'CAT', 'LOW', 'MS', 'UPS', 'BA', 'GS', 'GE', 'DE', 'RTX', 'AMAT', 'IBM', 'NOW', 'INTU', 'MU', 'AMD', 'MMM', 'BLK', 'AMT', 'BKNG', 'SCHW', 'TGT', 'CHTR', 'CVS', 'AXP', 'ISRG', 'FIS', 'LRCX', 'LMT', 'MO', 'SYK', 'SPGI', 'TJX', 'GILD', 'TFC', 'MDLZ', 'CI', 'ANTM', 'ADP', 'ATVI', 'ZTS', 'CB', 'PLD']

list2 = ['CME', 'PNC', 'COP', 'CSX', 'TMUS', 'BDX', 'USB', 'CCI', 'FISV', 'EL', 'GM', 'CL', 'ILMN', 'NSC', 'DUK', 'ICE', 'FDX', 'TWTR', 'ADSK', 'SO', 'GPN', 'MMC', 'ITW', 'EQIX', 'ADI', 'APD', 'D', 'SHW', 'BSX', 'VRTX', 'COF', 'AON', 'ECL', 'ETN', 'EW', 'EMR', 'PGR', 'HUM', 'FCX', 'KLAC', 'REGN', 'DG', 'F', 'HCA', 'NOC', 'MCO', 'IDXX', 'MET', 'DOW', 'NEM', 'KMB', 'WM', 'TEL', 'BIIB', 'ROST', 'ALGN', 'SYY', 'APTV', 'JCI', 'CMG', 'HPQ', 'MCHP', 'BAX', 'ROP', 'MAR', 'CDNS', 'CTSH', 'SLB', 'EA', 'LHX', 'DXCM', 'GD', 'AIG', 'DD', 'EXC', 'EOG', 'APH', 'DLR', 'CMI', 'SNPS', 'A', 'AEP', 'SPG', 'IQV', 'PH', 'EBAY', 'TRV', 'TT', 'TROW', 'VIAC', 'STZ', 'PSX', 'PSA', 'MPC', 'WBA', 'BK', 'MSCI', 'PRU', 'HLT', 'LUV']

list3 = ['CNC', 'ZBH', 'IFF', 'CTVA', 'GIS', 'INFO', 'SRE', 'ALXN', 'MNST', 'ALL', 'ORLY', 'XLNX', 'PPG', 'PCAR', 'ADM', 'TDG', 'VLO', 'AFL', 'YUM', 'XEL', 'DAL', 'PXD', 'CARR', 'MSI', 'SWKS', 'ANSS', 'GLW', 'PAYX', 'DFS', 'FRC', 'KMI', 'CTAS', 'WLTW', 'SBAC', 'WELL', 'ROK', 'SWK', 'RMD', 'BLL', 'WMB', 'ETSY', 'ES', 'PEG', 'MCK', 'AME', 'AZO', 'VRSK', 'FAST', 'ZBRA', 'MTD', 'LYB', 'KEYS', 'SIVB', 'AMP', 'OTIS', 'AWK', 'STT', 'DHI', 'WEC', 'CBRE', 'VFC', 'WY', 'KR', 'MXIM', 'FITB', 'AVB', 'KHC', 'LH', 'FLT', 'BBY', 'DLTR', 'AJG', 'LEN', 'CLX', 'DTE', 'FTNT', 'CPRT', 'ED', 'CDW', 'EQR', 'OXY', 'FTV', 'VMC', 'ENPH', 'EXPE', 'HSY', 'URI', 'TER', 'TTWO', 'CERN', 'O', 'MKTX', 'SYF', 'MLM', 'MKC', 'WDC', 'WST', 'ODFL', 'LVS', 'EIX']

list4 = ['PPL', 'QRVO', 'TSN', 'CCL', 'KSU', 'VTR', 'RF', 'NTRS', 'EFX', 'OKE', 'KEY', 'KMX', 'CHD', 'IP', 'VRSN', 'ARE', 'MTB', 'HAL', 'COO', 'HPE', 'RSG', 'CTLT', 'TYL', 'CFG', 'TRMB', 'TSCO', 'TFX', 'HOLX', 'GRMN', 'PAYC', 'ULTA', 'HIG', 'NUE', 'FE', 'XYL', 'HES', 'VTRS', 'DRI', 'DOV', 'AES', 'AEE', 'ETR', 'IR', 'RCL', 'AMCR', 'WAT', 'GWW', 'ALB', 'ESS', 'CAG', 'BKR', 'BR', 'CTXS', 'STX', 'EXR', 'CE', 'VAR', 'IT', 'NDAQ', 'MPWR', 'NVR', 'PEAK', 'HBAN', 'DGX', 'EXPD', 'CMS', 'MGM', 'UAL', 'MAA', 'AKAM', 'ANET', 'GPC', 'CAH', 'J', 'STE', 'ABC', 'EMN', 'OMC', 'IEX', 'K', 'ABMD', 'CINF', 'INCY', 'AVY', 'DRE', 'PFG', 'RJF', 'PKI', 'BXP', 'NTAP', 'MAS', 'TDY', 'DPZ', 'POOL', 'DISCK', 'FMC', 'BF-B', 'HRL', 'WAB', 'WYNN']

list5 = ['AAL', 'SJM', 'LB', 'DVN', 'LYV', 'BIO', 'PKG', 'CHRW', 'JBHT', 'EVRG', 'LUMN', 'UDR', 'PHM', 'HAS', 'WHR', 'LDOS', 'HST', 'FFIV', 'TPR', 'LW', 'PWR', 'XRAY', 'FBHS', 'NLOK', 'TXT', 'LNT', 'WRK', 'JKHY', 'FOXA', 'L', 'LKQ', 'SNA', 'BWA', 'HWM', 'FANG', 'AAP', 'CBOE', 'CNP', 'ATO', 'MHK', 'LNC', 'IPG', 'MOS', 'IRM', 'ALLE', 'WRB', 'UHS', 'CF', 'RE', 'WU', 'CMA', 'NCLH', 'PNR', 'CPB', 'NWSA', 'GL', 'NRG', 'RHI', 'HSIC', 'MRO', 'NWL', 'ZION', 'REG', 'DISCA', 'IVZ', 'TAP', 'NI', 'IPGP', 'ALK', 'AOS', 'NLSN', 'KIM', 'PNW', 'DISH', 'JNPR', 'PBCT', 'DVA', 'APA', 'COG', 'ROL', 'AIZ', 'BEN', 'HII', 'PVH', 'FLIR', 'FRT', 'VNO', 'SEE', 'DXC', 'HBI', 'NOV', 'LEG', 'RL', 'HFC', 'PRGO', 'UNM', 'GPS', 'SLG', 'FOX', 'FLS']

lst_days = ['2021-03-18', '2021-03-17', '2021-03-16', '2021-03-15', '2021-03-14', '2021-03-13', '2021-03-12']
lst_stocks = list1[:20]
for i in list2[:20]:
    lst_stocks.append(i)
for i in list3[:20]:
    lst_stocks.append(i)
for i in list4[:20]:
    lst_stocks.append(i)
for i in list5[:20]:
    lst_stocks.append(i)


if __name__ == '__main__':

    for day in lst_days:
        reader = create_df(day)
        average_price = (reader.mean(axis=0, numeric_only=True))['Close']
        print('The mean price of the stocks on', day, 'is', average_price)

        strategy_dic = {}
        market_dic = {}
        dic = {}
        total = {}
        holdings = {}
        cash = {}
        news = {}
        symbols = lst_stocks
        num_to_select = 100
        list_of_random_items = symbols
        counter = 0

        length = []
        for i in range(num_to_select):
            N = len(reader[reader['Symbol'] == list_of_random_items[i]])
            length.append(N)

        N = min(length)

        for j in range(N):
            for i in range(num_to_select):
                send = reader[reader['Symbol'] == list_of_random_items[i]]
                send = send.iloc[j]
                send = send.to_dict()

                counter += 1
                if counter < (num_to_select + 1):
                    strategy_dic['strategy' + str(send["Symbol"])] = ts.Strategy()
                    market_dic['market' + str(send["Symbol"])] = ma.MarketActions(
                        strategy_dic['strategy' + str(send["Symbol"])])

                dic['_action' + str(send["Symbol"])] =\
                    market_dic['market' + str(send["Symbol"])].received_market_data(send)
                total[str(send["Symbol"])], holdings[str(send["Symbol"])], \
                    cash[str(send["Symbol"])], news[str(send["Symbol"])] = \
                    market_dic['market' + str(send["Symbol"])].action_buy_sell_hold(
                        send, dic['_action' + str(send["Symbol"])])

            if list(news.values()) == [None] * num_to_select:
                pass
            else:
                sum_total = sum(total.values())
                sum_cash = sum(cash.values())
                sum_holdings = sum(holdings.values())

        print('You made:', sum(total.values()) - num_to_select * 100000)