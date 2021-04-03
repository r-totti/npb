# npb
python

■実行方法
-- python
import Active
Active.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_c.html", "C")
Active.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_g.html", "G")
Active.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_db.html", "DN")
Active.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_t.html", "T")
Active.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_s.html", "Y")
Active.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_d.html", "D")
Active.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_h.html", "H")
Active.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_f.html", "F")
Active.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_m.html", "M")
Active.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_l.html", "L")
Active.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_e.html", "E")
Active.generate_record_file_for_1team("http://npb.jp/bis/teams/rst_bs.html", "O")
または
Active.generate_record_file_for_allteam()

■備忘録
・打撃成績の取得成功
・投手精機の取得成功
・選手のマスタデータ(ポジション等)の取得成功
→身長と体重を別項目として取得
・まだ現役選手のみ
→今後、引退後の選手データも取得する必要がある
→URLに一意の数値(8桁)があるため実装可能
http://npb.jp/bis/players/81183848.html
→別ファイルで作成
・Common.pyを作成して現役、引退選手の共通処理を外だしにする

