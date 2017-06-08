# -*- coding: utf-8 -*- 
import lxml.html
from lxml.cssselect import CSSSelector
import requests

def makeArr(url, css):
    arr = []
    _html = requests.get(url)

    html = lxml.html.fromstring(_html.text)
    sel=CSSSelector(css)
    # Apply the selector to the DOM tree.
    nodes = sel(html)
    for i,node in enumerate(nodes):
        if i < 10 : 
            arr.append(node.text)
    return arr

innis = makeArr('http://www.innisfree.com/kr/ko/BestSellerList.do?bestClCd=RC01&catCd=ZZ',
              '#contents > div > div > div > ul > li > .listCon > .listTxt > .pdtName > a > em')
etu = makeArr('http://www.etude.co.kr/realTimeProgress.do?catId=000000&method=realTimeService',
              '#content > div.playstoreLive > div:nth-child(1) > ul > li > .prdArea > dl > dt > a')
tony = makeArr('http://www.etonymoly.com/html/corner_seller.asp?uid=166',
              '#tm-body > div > div.goods__wrap01 > ul > li > .item__cont > a > .summary')
mis = makeArr('http://missha.beautynet.co.kr/shopRank.do?rankingTpCd=06&agrgTp=10&YYYYMMDDW=undefined&check=1&brandNo=1',
            '#rightSide > div.misshainfoBox > div > div > div.tbTypeA.mt10 > table > tbody:nth-child(4) > tr > .alignL > div > a')
arita = makeArr('http://www.aritaum.com/shop/pr/shop_pr_product_list.do?i_arrPrdPopular=AC005',
               '#ul_prod_list > li > div > a > .ttl')

import re


def result(regex):
    i = 0
    while(not recommend and i < 10) :
        if re.findall(regex, innis[i]):
            recommend.append('이니스프리')
            cosmetics.append(innis[i])
        if re.findall(regex, etu[i]):
            recommend.append('에뛰드')
            cosmetics.append(etu[i])
        if re.findall(regex, tony[i]):
            recommend.append('토니모리')
            cosmetics.append(tony[i])
        if re.findall(regex, mis[i]):
            recommend.append('미샤')
            cosmetics.append(mis[i])
        if re.findall(regex, arita[i]):
            recommend.append('아리따움')
            cosmetics.append(arita[i])
        i += 1
        
    for j in range(len(recommend)):
        print recommend[j], " : ", cosmetics[j], "->", i, "위"
        
    if not recommend:
        print "순위에 해당 화장품 종류가 없습니다."

recommend =[]
cosmetics = []

regex_eye1 = u'.*?마스카라.*?'
regex_eye2 = u'.*?라이너.*?'
regex_eye3 = u'.*?브로우.*?'
regex_eye4 = u'.*?섀도우.*?'

regex_lib1 = u'.*?립스틱.*?'
regex_lib2 = u'.*?틴트.*?'

regex_face1 = u'.*?마스크.*?'
regex_face2 = u'.*?크림.*?'
regex_face3 = u'.*?토너.*?'
regex_face4 = u'.*?선.*?'
regex_face5 = u'.*?쿠션.*?'

ans = raw_input(u"1.립 2.아이 3.페이스 0.종료 중에서 추천받고 싶은 것의 숫자를 입력하세요 : ")
while (ans != '0'):
    if ans == '1':
        opt = raw_input(u"1.립스틱 2.틴트 중에서 추천받고 싶은 것의 숫자를 입력하세요 : ")
        if opt == '1':
            result(regex_lib1)
        elif opt == '2':
            result(regex_lib2)
    elif ans == '2':
        opt = raw_input(u"1.마스카라 2.아이라이너 3.아이브로우 4.아이섀도우 중에서 추천받고 싶은 것을 입력하세요 : ")
        if opt == '1':
            result(regex_eye1)
        elif opt == '2':
            result(regex_eye2)
        elif opt == '3':
            result(regex_eye3)
        elif opt == '4':
            result(regex_eye4)
    elif ans == '3':
        opt = raw_input(u"1.마스크 2.크림 3.토너 4.선크림 5.쿠션 중에서 추천받고 싶은 것을 입력하세요 : ")
        if opt == '1':
            result(regex_face1)
        elif opt == '2':
            result(regex_face2)
        elif opt == '3':
            result(regex_face3)
        elif opt == '4':
            result(regex_face4)
        elif opt == '5':
            result(regex_face4)
    else:
        print "입력 오류"
        
    ans = raw_input(u"1.립 2.아이 3.페이스 0.종료 중에서 추천받고 싶은 것의 숫자를 입력하세요 : ")