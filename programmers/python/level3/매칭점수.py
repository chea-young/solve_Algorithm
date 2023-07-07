"""
매칭점수 계산
- 기본점수, 외부 링크수, 링크점수, 매칭점수
    - 기본점수 - 검색어가 등장하는 횟수(대소문자 무시)
    - 외부 링크수 - 다른 외부 페이지로 연결된 링크 수
    - 링크 점수 - 링크가 걸린 다른 웹 페이지의 기본점수 / 외부 링크 수
    - 매칭 점수 - 기본점수 + 링크 점수

"""
import heapq

def solution(word, pages):
    answer = 0
    # 페이지 데이터 정렬
    """
    자신: <meta property="og:url" content="https://a.com"/>
    링크: <a href="https://c.com">
    """
    data = [] # (자신, [링크 URL, ..], 페이지 내용)
    for p in pages:
        p_data = p.split('\n')
        print(p_data)

    # 매칭 점수 계산

    ## 기본 점수 계산 -> "".count(word)
    basic = []

    ## 외부 링크수 계산
    outer_link = []

    ## 링크 점수
    link = []

    ## 매칭 점수
    data = []

    return answer
p1 = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print(solution("blind", p1))