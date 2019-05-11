# 参考にさせていただいたソース
# https://qiita.com/shunyooo/items/b408b8d61f9f73b21da7

# import [ライブラリ名]でライブラリを読み込む
import requests  # httpリクエストを飛ばせる
import json  # json形式で取得するため使う。
import pandas as pd  # DataFrame用
import os


def output_weather_forecast_information(CITYNAMES, APIKEY, APIURL, DIR_NAME):
    """

    Overview
    --------
    Apiから天気の情報を抽出して、json形式で出力を行う。

    Parameters
    ----------
    CITYNAMES       :   list
        取得したい地域名
    APIKEY          :   str
        事前に取得したApikey
    APIURL          :   str
        ApiにアクセスするためのURL
    DIR_NAME        :   str
        出力する際のフォルダ名

    Returns
    -------
    all_fullpath    :   list
        DataFrameで表示するために出力したファイルパスを返す。

    """
    all_fullpath = []
    # 配列に格納されている数の天気の情報を得る。
    for cityname in CITYNAMES:
        # urlを取得する。
        # 対象の地域を1地域づつ見ていく。
        weather_apiurl = APIURL.format(city=cityname, key=APIKEY)
        # apiにリクエストを送る。requests.get(url)で取得可能
        url_request = requests.get(weather_apiurl)
        # print(url_request.text)
        # 結果はjson形式で取得になるので、データの変換を行う。json.load(対象のjsonファイル→今回だったら'url_request')
        weather_result = json.loads(url_request.text, encoding="utf-8")
        # ディレクトリ作る。　exist_ok=Trueで省略可能。
        os.makedirs(DIR_NAME, exist_ok=True)
        # dirpath＋filepath作成
        full_filePath = os.path.join(
            DIR_NAME, cityname + '_Weather_Result.json')
        all_fullpath = all_fullpath + [full_filePath]

        # json形式でファイル出力
        with open(full_filePath, 'w') as result_json:
            json.dump(weather_result, result_json,
                      indent=2, ensure_ascii=False)
            print('出力完了', cityname)
    return all_fullpath


def dataframe_make_json(ALL_FILEPATH):
    """

    Overview
    --------
    json形式のファイルをDataFrameの形式でコンソールに表示する。

    Parameters
    ----------
    ALL_FILEPATH    : list
        json形式のファイルが格納されているファイルパス

    """
    for file_name in ALL_FILEPATH:
        json_load_file = json.load(open(file_name))
        df = pd.DataFrame(json_load_file["表示したいkey"])
        print(df)


if __name__ == "__main__":

    # WebAPIで天気を調べる。
    # apikeyを設定
    apikey = '取得したapikey'

    # 調べたい地域を配列に入れる
    areas = ['調べたい地域']

    # apiの雛形を格納する
    # @argument city:調べたい地域が入る
    # @argument key:apikeyが入る

    api = 'http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={key}'

    dir_pathname = 'result_in_dir_path'

    file_path = output_weather_forecast_information(
        areas, apikey, api, dir_pathname)

    dataframe_make_json(file_path)
