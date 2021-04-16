import urllib.request
import requests
from bs4 import BeautifulSoup
import csv

# ////////////////////////////////////////////////////////////////
class NpbPlayer:
    # ------------------------------------------------------------
    def __init__(self, url):
        # self.name = name
        self.url = url
        self.filename = url.replace('http://npb.jp/bis/players/', '').replace('.html', '')
        self.ary_record_pitch = []  # 投手記録
        self.ary_record_bat = []  # 打者記録
        self.ary_ma = []    # マスタデータ

    # ------------------------------------------------------------
    # 1選手の投手記録をCSVファイルに出力
    def output_record_to_csv_file_pitch(self, fname):
        if len(self.ary_record_pitch) > 0:
            with open(fname, "w") as fh:
                writer = csv.writer(fh, lineterminator="\n")
                writer.writerows(self.ary_record_pitch)

    # ------------------------------------------------------------
    # 1選手の打者記録をCSVファイルに出力
    def output_record_to_csv_file_bat(self, fname):
        if len(self.ary_record_bat) > 0:
            with open(fname, "w") as fh:
                writer = csv.writer(fh, lineterminator="\n")
                writer.writerows(self.ary_record_bat)

    # ------------------------------------------------------------
    # 1選手のマスタデータをCSVファイルに出力
    def output_record_to_csv_file_ma(self, fname):
        if len(self.ary_ma) > 0:
            with open(fname, "w", encoding="utf-8_sig") as fh:
                writer = csv.writer(fh, lineterminator="\n")
                writer.writerows(self.ary_ma)

    # ------------------------------------------------------------
    # 1選手の記録を収集
    def get_record(self):
        try:
            resp = urllib.request.urlopen(self.url)
        except urllib.error.HTTPError as e:
            print("HTTP-Error : ", e.code)
            return False
        except urllib.error.URLError as e:
            print("URL-Error : ", e.reason)
            return False
        else:
            self.ary_record_pitch = []
            self.ary_record_bat = []
            self.ary_ma = []
            bs = BeautifulSoup(resp.read(), "html.parser")
            # 打者記録取得
            for div in bs.find_all("table",id="tablefix_b"):
                for tr in div.find_all("tr", class_="registerStats"):
                    ary_1_record = []
                    for td in tr.find_all("td"):
                        ary_1_record.append(td.get_text().strip())
                    self.ary_record_bat.append(ary_1_record)
            # 投手記録取得
            for pit in bs.find_all("table",{"id":"tablefix_p"}):
                for ptr in pit.find_all("tr", class_="registerStats"):
                    ary_1_record = []
                    for index, ptd in enumerate(ptr.find_all("td")):
                        if index == 14: continue
                        table_inning = ptd.find_all("tr")
                        for data in table_inning:
                            inning_th = data.find("th")
                            inning_td = data.find("td")
                        if len(table_inning) == 0:
                            ary_1_record.append(ptd.get_text().strip())
                        elif len(inning_td) == 0:
                            ary_1_record.append(inning_th.get_text())
                        elif len(inning_th) != 0:
                            ary_1_record.append(inning_th.get_text() + inning_td.get_text())
                    self.ary_record_pitch.append(ary_1_record)
            # マスタデータ取得
            ary_ma_record = []
            # 名前取得
            for pc_v_name in bs.find_all("div",id="pc_v_name"):
                for mli in pc_v_name.find_all("li",id={"pc_v_no", "pc_v_name", "pc_v_kana"}):
                    ary_ma_record.append(mli.get_text().strip())
            # 登録情報
            for pc_bio in bs.find_all("section",id="pc_bio"):
                for mtr in pc_bio.find_all("tr"):
                    mth = mtr.find("th").string
                    mtd = mtr.find("td")
                    if mth.find("身長／体重") != -1:
                        for thlist in mtd.get_text().split('／'):
                            ary_ma_record.append(thlist.strip())
                    else:
                        ary_ma_record.append(mtd.get_text().strip())
            self.ary_ma.append(ary_ma_record)
            return True

# ////////////////////////////////////////////////////////////////
def get_retired_player_list():
    ary_cPlayer = []
    # http://npb.jp/bis/players/81183848.html
    with open('npb.txt', 'r') as f:
        for line in f:
            try:
                url = line.replace('\n','')
                response = requests.get(url)
                print(url)
                # print(response.status_code)   # HTTPのステータスコード取得
            except requests.exceptions.HTTPError as e:
                print("URL_Error : ", e.response)
            if response.status_code == 200:
                cPlayer = NpbPlayer(url)
                ary_cPlayer.append(cPlayer)
            else:
                pass
    return ary_cPlayer

# ////////////////////////////////////////////////////////////////
def generate_record_file_for_1player(team_url, prefix):
    pass

# ////////////////////////////////////////////////////////////////
def generate_record_file_for_allplayer():
    ary_cPlayer = get_retired_player_list()
    for cPlayer in ary_cPlayer:
        if True == cPlayer.get_record():
            print("now generating %s" % cPlayer.filename)
            cPlayer.output_record_to_csv_file_bat("../retired/da/%s_da.txt" % (cPlayer.filename))
            cPlayer.output_record_to_csv_file_pitch("../retired/pt/%s_pt.txt" % (cPlayer.filename))
            cPlayer.output_record_to_csv_file_ma("../retired/ma/%s_ma.txt" % (cPlayer.filename))
