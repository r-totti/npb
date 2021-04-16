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
・選手に一意(8桁)のコードが振られている
http://npb.jp/bis/players/81183848.html

・引退選手は5・6桁目が38となる
xxxx38xx

・現役選手は5・6桁目が51となる
xxxx51xx

・2017年前後で引退した選手は5・6桁目が51となっている
→引退後にコードが変わることはない
→38と51の線引きが不明
相川　亮二　https://npb.jp/bis/players/41443880.html
片岡　治大　https://npb.jp/bis/players/01305110.html

・38と51以外のコード体系が不明
集計結果から規則性を見つけたい