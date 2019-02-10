# 参考にさせていただいたソース
# https://qiita.com/shunyooo/items/b408b8d61f9f73b21da7

# import [ライブラリ名]でライブラリを読み込む
import requests  # httpリクエストを飛ばせる
import json  # json形式で取得するため使う。

# WebAPIで天気を調べる。
# apikeyを設定
apikey = '取得したapi'

# 調べたい地域を配列に入れる
areas = ['調べたい地域名']

# apiの雛形を格納する
# @argument city:調べたい地域が入る
# @argument key:apikeyが入る
api = 'http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={key}'

# 配列に格納されている数の天気の情報を得る。

for cityname in areas:
    # urlを取得する。
    # 対象の地域を1地域づつ見ていく。
    weather_apiurl = api.format(city=cityname, key=apikey)
    # 確認用　print(weather_apiurl)
    # apiにリクエストを送る。requests.get(url)で取得可能
    url_request = requests.get(weather_apiurl)
    # print(url_request.text)
    # 結果はjson形式で取得になるので、データの変換を行う。json.load(対象のjsonファイル→今回だったら'url_request')
    weather_result = json.loads(url_request.text, encoding="utf-8")
    # json形式でファイル出力
    with open(cityname + '_Weather_Result.json', 'w') as result_json:
        json.dump(weather_result, result_json, indent=2, ensure_ascii=False)
    print('出力完了')
