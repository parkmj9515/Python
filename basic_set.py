evens = { 0, 2, 4, 6, 8, 10} # 짝수집합
odds = { 1, 3, 5, 7, 9} # 홀수집합
numbers = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9} # 전체집합
mthree = { 0, 3, 6, 9} # 3의배수집합

def define_set():
    """
    집합 정의 연습
    set : 순서가 없고, 중복 허용 하지 않음
        len, in, not in 길이와 포함여부 확인
    """
    empty = set() # 빈 set
    print(type(empty), type({}))

    # 길이, 포함 여부 확인
    print(numbers,"Length:",len(numbers))
    print(2 in numbers, 2 in evens, 2 in odds, 2 in mthree)

    # 다른 순차형으로 set 만들기 
    s = "Python Programming"
    chars = set(s.upper())
    print(s, chars)

    # list 등 순차자료형의 중복값을 제거할 때 유용
    lst = "Python Programming Java Programming HTML Programming".split()
    print(lst)
    
    # 리스트에서 중복 요소를 제거한 요소 갯수는?
    s = set(lst)
    print("set:",s,len(s))
    lst2 = list(s)
    print("lst2:",lst2)


def set_methods():
    """
    set 메서드들
    """
    print("numbers:",numbers,len(numbers))
    numbers.add(10)
    print("numbers:",numbers,len(numbers))
    
    numbers.add(10) # 중복을 허용하지 않음
    print("numbers:",numbers,len(numbers))

    print("evens:",evens)
    evens.add(3)  # 추가
    print("evens:",evens)
    evens.discard(3) # 3삭제
    print("evens:",evens)
    evens.discard(3) # 삭제
    print("evens:",evens)
    # discard는 없어도 오류없이 무시
    if 3 in evens:
        evens.remove(3) # remove는 데이터가 없으면 keyError 발생
    evens.update({10})
    print("evens:",evens)


def set_oper():
    """
    set의 집합 연산
    """
    # 합집합: |, union
    numbers.add(10)
    print(evens | odds == numbers) # 짝수 집합 합집합 홀수 집합 == 전체 집합
    print(evens.union(odds) == numbers)

    # 교집합: &, intersection
    print(evens & mthree == {0, 6}) # 짝수 집합 교집합 3의 배수 집합 == {0, 6} 집합
    print(evens.intersection(mthree) == {0,6})

    # 차집합: -, difference
    print(numbers - odds == evens) # 전체집합 - 홀수집합 = 짝수집합
    print(numbers.difference(odds) == evens)

    # 판별함수: issuperset, issubset
    print(numbers.issuperset(evens), numbers.issuperset(odds)) # 부모 집합 여부 판별
    print(evens.issubset(numbers), odds.issubset(numbers)) # 부분 집합 여부 판별
    

def loop():
    for num in numbers:
        print(num, end="\t")
    else:
        print()



if __name__ == "__main__":
    # define_set()
    # set_methods()
    # set_oper()
    loop()