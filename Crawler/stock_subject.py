# -*- coding:utf-8 -*-
import requests
from lxml import etree
import json

url = "https://www.twse.com.tw/zh/api/codeFilters?filter={num}"

content = u"""<div class="outer"><div class="win code-browse-win"><label class="close"></label><div class="content"><div class="code-browse-popup"><div class="outer"><h1>股票代碼查詢</h1><div class="body"><div class="view v1"><div class="group">證券分類：<div class="category stk"><a data-val="0049">封閉式基金</a><a data-val="0099P">ETF</a><a data-val="019919T">受益證券</a><a data-val="0999GA">附認股權特別股</a><a data-val="0999GD">附認股權公司債</a><a data-val="0999G9">認股權憑證</a><a data-val="0999">認購權證 (國內標的)</a><a data-val="0999P">認售權證 (國內標的)</a><a data-val="0999F">認購權證 (外國標的)</a><a data-val="0999Q">認售權證 (外國標的)</a><a data-val="http://mops.twse.com.tw/mops/web/t150sb02">標的證券查詢 (國內)</a><a data-val="http://mops.twse.com.tw/mops/web/t33sb01">標的證券查詢 (外國)</a><a data-val="CB">可轉換公司債</a><a data-val="0999C">牛證</a><a data-val="0999B">熊證</a><a data-val="0999X">可展延牛證</a><a data-val="0999Y">可展延熊證</a><a data-val="9299">存託憑證</a><a data-val="01">水泥工業</a><a data-val="02">食品工業</a><a data-val="03">塑膠工業</a><a data-val="04">紡織纖維</a><a data-val="05">電機機械</a><a data-val="06">電器電纜</a><a data-val="07">化學生技醫療</a><a data-val="21">化學工業</a><a data-val="22">生技醫療業</a><a data-val="08">玻璃陶瓷</a><a data-val="09">造紙工業</a><a data-val="10">鋼鐵工業</a><a data-val="11">橡膠工業</a><a data-val="12">汽車工業</a><a data-val="13">電子工業</a><a data-val="24">半導體業</a><a data-val="25">電腦及週邊設備業</a><a data-val="26">光電業</a><a data-val="27">通信網路業</a><a data-val="28">電子零組件業</a><a data-val="29">電子通路業</a><a data-val="30">資訊服務業</a><a data-val="31">其他電子業</a><a data-val="14">建材營造</a><a data-val="15">航運業</a><a data-val="16">觀光事業</a><a data-val="17">金融保險</a><a data-val="18">貿易百貨</a><a data-val="23">油電燃氣業</a><a data-val="19">綜合</a><a data-val="20">其他</a></div></div><div class="group">指數查詢：<div class="category idx"><a data-val="IX0001">發行量加權股價指數</a><a data-val="IX0002">臺灣50指數</a><a data-val="IX0003">臺灣中型100指數</a><a data-val="IX0004">臺灣資訊科技指數</a><a data-val="IX0005">臺灣發達指數</a><a data-val="IX0006">臺灣高股息指數</a><a data-val="IX0007">未含金融指數</a><a data-val="IX0008">未含電子指數</a><a data-val="IX0009">未含金融電子指數</a><a data-val="IX0010">水泥類指數</a><a data-val="IX0011">食品類指數</a><a data-val="IX0012">塑膠類指數</a><a data-val="IX0013">水泥窯製類指數</a><a data-val="IX0014">塑膠化工類指數</a><a data-val="IX0015">機電類指數</a><a data-val="IX0016">紡織纖維類指數</a><a data-val="IX0017">電機機械類指數</a><a data-val="IX0018">電器電纜類指數</a><a data-val="IX0019">化學生技醫療類指數</a><a data-val="IX0020">化學類指數</a><a data-val="IX0021">生技醫療類指數</a><a data-val="IX0022">玻璃陶瓷類指數</a><a data-val="IX0023">造紙類指數</a><a data-val="IX0024">鋼鐵類指數</a><a data-val="IX0025">橡樛類指數</a><a data-val="IX0026">汔車類指數</a><a data-val="IX0027">電子工業類指數</a><a data-val="IX0028">半導體類指數</a><a data-val="IX0029">電腦及週邊設備類指數</a><a data-val="IX0030">光電類指數</a><a data-val="IX0031">通信網路類指數</a><a data-val="IX0032">電子零組件類指數</a><a data-val="IX0033">電子通路類指數</a><a data-val="IX0034">資訊服務類指數</a><a data-val="IX0035">其他電子類指數</a><a data-val="IX0036">建材營造類指數</a><a data-val="IX0037">航運類指數</a><a data-val="IX0038">觀光類指數</a><a data-val="IX0039">金融保險類指數</a><a data-val="IX0040">貿易百貨類指數</a><a data-val="IX0041">油電燃氣類指數</a><a data-val="IX0042">其他類指數</a><a data-val="IX0061">臺灣證券交易所銳聯臺灣就業創造99指數</a><a data-val="IX0078">寶島股價指數</a><a data-val="IX0080">臺灣證券交易所銳聯臺灣高薪酬100指數</a><a data-val="IX0082">臺灣證券交易所公司治理100指數</a><a data-val="IX0088">臺灣證券交易所小型股300發行量加權股價指數</a><a data-val="IX0091">臺灣指數公司漲升股利150指數</a><a data-val="IX0092">臺灣指數公司漲升股利100指數</a><a data-val="IX0093">臺灣指數公司藍籌30指數</a><a data-val="IX0094">臺灣指數公司工業菁英30指數</a><a data-val="IX0095">臺灣指數公司電子菁英30指數</a><a data-val="IX0096">臺灣指數公司低波動股利精選30指數</a><a data-val="IX0097">臺灣指數公司低貝塔100指數</a><a data-val="IX0101">臺灣指數公司中小型精選50指數</a><a data-val="IX0102">臺灣指數公司中小型A級動能50指數</a><a data-val="IX0103">臺灣指數公司臺灣上市上櫃生技醫療股價指數</a><a data-val="IX0104">臺灣指數公司特選高股息低波動股價指數</a><a data-val="IX0105">FTSE4Good臺灣指數公司臺灣永續指數</a><a data-val="IX0107">臺灣指數公司特選內需高收益股價指數</a><a data-val="IX0108">臺灣指數公司臺灣上市上櫃中小型公司治理股價指數</a><a data-val="IX0109">臺灣指數公司臺灣上市上櫃IPO股價指數</a><a data-val="IX0110">臺灣指數公司價值投資股價指數</a></div></div><div class="group">期貨型權證查詢：<div class="category fwt"></div></div></div><div class="view v2"><a class="back">&lt; 返回分類</a>請選擇股票：<div class="stocks"><div class="items"></div><div class="pagination"></div></div></div></div></div></div></div></div></div>"""
xtree = etree.HTML(content)

target_content = xtree.xpath('//div[@class="group"]/div/a')
dict_stock = {i.get('data-val'):i.text for i in target_content}
# print(dict_stock)
stock_all_code = ["%.2d" % num for num in range(1,32,1)]


stock_detail = {}
for num in stock_all_code:
	response = requests.request("GET", url.format(num=num))
	content = {data.split('\t')[0]:data.split('\t')[1] for data in response.json()['resualt']}
	stock_detail[dict_stock[num]] = content
print(stock_detail)

exit()