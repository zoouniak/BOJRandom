import random

import requests
from bs4 import BeautifulSoup
def solve(username):
    # 내가 푼 문제들 리스트 받아오기
    myurl = 'https://www.acmicpc.net/user/' + username
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(myurl, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    trs = soup.select(
        'body > div.wrapper > div.container.content > div.row > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > '
        'div.panel-body > div > a')
    solved = []
    for tr in trs:
        solved.append(tr.text)
    return solved


def get_problem(algo, tier):
    #각 알고리즘 별 티어 문제 받아오기
    problems = {}
    for num in algo:
        problemurl = 'https://www.acmicpc.net/problemset?sort=ac_desc&' + 'tier=' + str(tier) + '&algo=' + str(num)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(problemurl, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        trs = soup.select('#problemset > tbody > tr')
        for tr in trs:
            num = tr.select_one('td:nth-child(1)').text
            title = tr.select_one('td:nth-child(2) > a').text
            problems[num] = title

    return problems


### 실행하기
print('백준 아이디 입력>>', end=' ')
username = input()
solved = solve(username)
print('풀고자 하는 알고리즘 선택{그리디(33),브루트포스(125),그래프탐색(11),정렬(97),재귀(62),dp(25)} >>', end=' ')
# 백준 알고리즘 별 번호
# 그리디 33 #구현 102 #브루트포스 125 #그래프탐색 11
# 정렬 97 #너비우선탐색 126  #깊이우선탐색 127
# 데이크스트라 22 #백트래킹 5 #재귀 62 #dp 25 #분할정복 24
algo = list(map(int, input().split()))
print('티어를 선택하세요(실버5부터 숫자 6으로 시작 ++)골드5(11),실버1(10) ...>>', end=' ')
tier = input()
problems = get_problem(algo, tier)
while True:
    choice = random.choice(list(problems.keys()))
    if choice not in solved:
        print('오늘 풀 문제는!!!', choice, '번', problems[choice], '입니다.', end='')
        exit()
