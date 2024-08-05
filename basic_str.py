def define_str():
    """
    함수 정의 연습
    """
    # 문자열의 정의
    # 한 줄 문자열: 쌍따옴표("),홑따옴표(') 모두 가능
    s1 = "Hello Python" # 리터럴 생성
    s2 = str("Hello Python") # 타입 함수 사용
    s3 = str(3.14159) # 다른 타입을 변환 생성

    print(s1, type(s1))
    print(s2, type(s2))
    print(s3, type(s3))

    print("s1은 str?", isinstance(s1, str))

    # 여러줄 문자열: """,'''
    s4 = """Life is too short, You need Python.
            파이썬은 데이터 처리가 중요한 시대에서
            가장 널리 사용되는 언어 입니다"""
    print(s4)

    # 여러줄 문자열은 한줄 주석만 있는 파이썬에서
    # 여러줄 주석을 사용하고 할때도 사용 가능
    """여러줄 문자열 을 사용한 여러 줄 주석
    메서드 정의 바로 아래 여러 줄 주석을 추가하면
    문서화 할때 이용될 수 있고
    help 명령어로 해당 메서드의 주석을 볼수 있다
    => docstring 이라고함"""

    # f-string > 문자열 포맷팅 방식 중 하나
    name, age = "홍길동", 28
    message = f"안녕하세요,{name}님. 당신은 {age} 살입니다"
    print(message)

    width, height = 10 ,5
    message = f"사각형의 면적은 {width * height}입니다"
    print(message)

def string_oper():
    """
    문자열 연산
    """
    # 문자열 객체는 길이(len()), 인덱싱, 슬라이싱, 포함여부 판별 가능
    # imutable, 치환 불가능
    str1 = "First String"
    str2 = "Second String"
    print(len(str1),len(str2))

    # 인덱싱
    print(str1[0],str1[1], str1[2], "...",str1[9],str1[10],str1[11]) # 정방향 인덱싱
    print(str1[-12], str1[-11], str1[-10], "...", str1[-3], str1[-2], str1[-1]) # 역방향 인덱싱

    # 문자열은 imutable > 치환 불가
    # str1[0] = "f" 변경 불가

    # 슬라이싱
    # [시작경계:끝경계[:간격(옵션]]
    print(str1)
    print(str1[6:9])  # 정방향 인덱스 활용
    print(str1[-6:-3]) # 역방향 인덱스 활용

    print(str1[0:5]) # 처음 인덱스 부터 시작이면 생략가능 >
    print(str1[:5]) # 위와 아래는 결과 같음

    print(str1[6:len(str1)])
    print(str1[6:]) # 시작점부터 끝까지면 끝부분 생략가능

    print(str1[::2]) # 처음부터 끝까지 간격2
    print(str1[::-1]) # 간격 값이 음수 > 역방향 출력

def transform_methods():
    """
    대소문자 변환 관련 연습
    """
    s = "i like python"
    # 모든 문자 대문자
    print("UPPER:",s.upper())

    # 모든 문자 소문자
    print("LOWER:",s.lower())

    # 첫 글자만 대문자
    print("CAPITALIZE:", s.capitalize())

    # 각 단어의 첫글자 만 대문자
    print("TITLE:", s.title())

    # 대문자 <> 소문자 교체
    print("SWAPCASE:", s.swapcase())

    # 불변 자료 > 원본은 바뀌지 않음
    print("원본:", s)

def search_methods():
    """
    문자열 검색 관련 예제
    """
    s = "I Like Python, I Like JAVA Also"
    print("COUNT:", s.count("Like")) # 문자열 내부의 Like 갯수

    # Like 찾기
    index = s.find("Like") # 문자열 내부의 첫번째 Like
    print("1st Find:", index)
    index = s.find("Like",6) # 인덱스 6부터 검색
    print("2nd Find:", index)
    index = s.find("Like", 21) # 인덱스 21부터 검색
    print("3rd Find:", index) #찾을 검색어가 없으면 -1 반환

    # Like 찾기 : index
    """
    print("1st Index:", s.index("Like"))
    print("2nd Index:", s.index("Like",6)) 
    
    print("3rd Index:", s.index("Like", 21)) Error """
    # 방법 1: 예외처리
    # 방법 2: 먼저 검색어 포함 여부 확인 후 검색
    if"Like" in s[21:]: # 포함 여부
        print("3rd Index:", s.index("Like",21))
    else:
        print("21번 인데스 이후에 는 Like 없음")

    # 역방향 검색 : find
    print("RFIND:", s.rfind("Like")) #17 뒤에서 부터 찾지만 숫자는 앞에서부터 세어야함
    print("RFIND:", s.rfind("Like",0,17))
    
    # 문자열이 특정 문자열로 시작되는가?
    url = "http://www.naver.com"
    surl = "https://www.google.com"
    ftp = "ftp://ftp.naver.com"

    print("STARTSWITH:",url.startswith("http://"))
    print("STARTSWITH:",surl.startswith("https://"))
    print("STARTSWITH:",ftp.startswith(("http://")))
    
    # 문자열이 특정 문자열로 끝나는가?
    print("ENDSWITH:",url.endswith("naver.com"))
    print("ENDSWITH:",surl.endswith("naver.com"))
    
    # startswith, endswith에서 검색 범위를 제한
    print("STARTSWITH:",ftp.startswith("ftp.",6,len(ftp)))

def modify_replace_methods():
    """
    문자열 수정, 치환 관련 메서드 연습
    """
    s = "            Alice and the Heart Queen             "
    print("STRIP:[",s.strip(),"]",sep="") # 앞뒤 공백 제거
    print("LSTRIP:[",s.lstrip(),"]",sep="") # 왼쪽 공백 제거
    print("RSTRIP:[",s.rstrip(),"]",sep="") # 오른쪽 공백 제거

    s="------------------Alice and the Heart Queen------------------"
    print("STRIP:[",s.strip("-"),"]",sep="") # 앞뒤 공백 제거

    s="I Like Java"
    # JAVA -> Python
    print("REPLACE:",s.replace("Java","Python"))
    print("원본:",s) # str은 immutable > 변경x 즉, 원본 변경x

def align_methods():
    """
    문자열 정렬 관련 메서드
    """
    s = "Alice and the Heart Queen"
    print("CENTER:[",s.center(60),"]",sep="") # 중앙 정렬
    print("CENTER:[",s.center(60,"*"),"]",sep="")
    
    print("LJUST:[",s.ljust(60,"*"),"]",sep="")
    print("RJUST:[",s.rjust(60,"*"),"]",sep="")

    print("ZFILL:","1234".zfill(5)) # 5자리 확보, 내용을 채운 후 빈 공간에 0으로 채움
    print("ZFILL:","123456".zfill(5)) # 확보한 5자리는 최소 공간, 넘쳐도 잘리지는 않음

def split_join_methods():
    """
    문자열 분할과 합치기 관련 메서드
    """
    s = "Ham and Cheese and Breads and Ketchup"
    print("SPLIT:",s.split()) # 공백 문자를 기준으로 분리
    
    ingr = s.split(" and ") #' and '을 기준으로 분리
    print("SPLIT:",ingr)
    print("JOIN:[",",".join(ingr),"]") # ingr리스트를 , 를 중심으로 합침
    print(s.split(" and ",2)) # 앞에서 두개만 분리
    print(s.rsplit(" and ",2)) # 뒤에서 두개만 분리

    # 줄 단위 구분: split("\n")과 동일

    lines = """"\
        Java Programming
        Python Programming
        HTML Coding
        """
    print("split:",lines.split())
    print("split:",lines.split("\n"))

    print("splitlines",lines.splitlines(True)) # 개행 문자 유지
    print("splitlines:",lines.splitlines(False)) # 개행 문자 유지하지않음 기본값:false

def check_methods():
    """
    str 데이터의 형태 판별
    """
    print("1234".isdigit()) # 숫자로만 구성?
    print("abcd".isalpha()) # 알파벳 형태?
    print("python3".isalnum()) # 알파벳과 숫자로?
    print("python 3".isalnum()) # 공백 포함? > 공백은 포함x False반환
    print("\r\n\t".isspace()) # 공백 문자 형태?  스페이스, 개행문자, 탭 등 모두 공백 문자
    print("".isspace()) # 공백 문자 > 공백x False반환

    print("PYTHON".isupper()) # 모두 대문자?
    print("python".islower()) # 모두 소문자?
    print("Python Programming".istitle()) # 타이틀 형태? 즉, 각 단어의 첫글자가 대문자인 형태

def string_format():
    """
    문자열 포맷팅 연습
    """
    # c 스타일 문자열 포맷
    # %s(문자열), %c(문자 1개), %d(정수), %f(실수), %o(8진수), %x(16진수), %%(Literal %)
    fmt = "%d개의 %s 중에서 %d개를 먹었다"
    print(fmt %(10,"사과",3))

    print("현재 이자율은 %f%%입니다"% 3.4) 
    print("현재 이자율은 %.2f%%입니다" %3.4) # 소수점 이하 2자리까지 출력

    # named formatting
    fmt = "%(total)d개의 %(fruit)s 중에서 %(eat)d개를 먹었다"
    print(fmt %{"total":10, "fruit":"자두", "eat":3})
    print(fmt %{"fruit":"자두", "eat":3, "total":10}) # 순서 상관없음

    # format 메서드
    fmt = "{}개의 {} 중에서 {}개를 먹었다"
    print(fmt.format(10, "포도", 3))
    print("{0}개의 {1} 중에서 {2}개를 먹었다".format(10, "포도", 3)) # 인덱스 지정 가능

    # placeholder의 named parameter를 이용
    fmt = "{total}개의 {fruit}중에서 {eat}개를 먹었다"
    print(fmt.format(eat=3, total=10, fruit="수박"))

    # dict 작성된 데이터가 있을 경우 : format_map
    data = {"total": 10, "eat": 3, "fruit": "자몽"}
    print(fmt.format_map(data))


    # f-string
    # 포맷팅 문자열 앞에 f
    # {}내부에 데이터, 변수명, 표현식 > 해당 결과 바인딩 > 최종 출력물
    total, fruit, eat = 10, "애플망고", 3
    print(f"{total}개의 {fruit}중에서 {eat}개를 먹었다")
    # placeholder 내부에 연산식 활용 가능
    total,fruit,eat = 10,"apple",3
    print(f"{total}개의 {fruit.upper()}중에서 {eat}개를 먹어서 {total - eat}개가 남았다")


if __name__ == "__main__":
    
    # define_str()
    # string_oper()
    # transform_methods()
    # search_methods()
    # modify_replace_methods()
    # align_methods()
    # split_join_methods()
    # check_methods()
    string_format()