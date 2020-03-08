# npb
python

■実行方法
import soup
soup.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_c.html", "C")
soup.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_g.html", "G")
soup.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_db.html", "DN")
soup.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_t.html", "T")
soup.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_s.html", "Y")
soup.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_d.html", "D")
soup.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_h.html", "H")
soup.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_f.html", "F")
soup.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_m.html", "M")
soup.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_l.html", "L")
soup.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_e.html", "E")
soup.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_bs.html", "O")
または
soup.generate_record_file_for_allteam()

■備忘録
・打撃成績の取得成功
・投手精機の取得成功
・選手のマスタデータ(ポジション等)の取得成功
→身長と体重を別項目として取得
・まだ現役選手のみ
→今後、引退後の選手データも取得する必要がある
→URLに一意の数値(8桁)があるため実装可能
→別ファイルで作成
