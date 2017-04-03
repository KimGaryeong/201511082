# coding: utf-8
import requests
import lxml.etree

def getkbreport():
    kbrep = requests.get('http://www.kbreport.com/main')
    _htmlTree = lxml.etree.HTML(kbrep.text)
    nodes = _htmlTree.xpath("//div[@class='team-rank-box']//table[@class='team-rank']//tr")
    print "���̺� �� ����: ", len(nodes)
    counter=0
    for teams in nodes:
        for cols in teams:
            if cols.xpath('.//a/text()'):
                print cols.xpath('.//a/text()')[0],
            else:
                print cols.text.strip(),
        print

def main():
    getkbreport()

if __name__ == "__main__":
    main()