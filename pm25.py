import pandas as pd

url = 'https://data.epa.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=CSV'

df = pd.read_csv(url).dropna()['county site pm25	datacreationdate'.split()]


def get_pm25(sort=False):
    global df
    if sort:
        df = df.sort_values('pm25', ascending=False)

    return df.columns.tolist(), df.values.tolist()


def get_six_pm25():
    global df
    if df is None:
        df = pd.read_csv(url).dropna()[
            'county site pm25	datacreationdate'.split()]

    six_countys = ['臺北市', '新北市', '桃園市', '臺中市', '臺南市', '高雄市']

    datas = []
    for county in six_countys:
        pm25 = round(df.groupby('county').get_group(county)['pm25'].mean(), 2)
        datas.append([county, pm25])

    return datas


def get_countys():
    global df

    return sorted(set(df['county']))


def get_county_pm25(county):
    global df

    datas = df.groupby('county').get_group(county)[
        ["site", "pm25"]].values.tolist()

    return datas


if __name__ == '__main__':

    print(get_pm25(True))
    # print(get_countys())
