from alpha_vantage.timeseries import TimeSeries


def main():
    ts = TimeSeries()
    # Get json object with the intraday data and another with  the call's metadata
    data, meta_data = ts.get_intraday('GOOGL')
    print(data)


if __name__ == '__main__':
    main()
