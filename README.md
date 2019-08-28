# Python 한글 인명 로마자 변환

## 설명

한글 인명을 로마자로 변환해 주는 프로그램.<br />
인터넷에서 찾은 예제 소스가 selenium을 사용하는 것 밖에 없어서 너무 무거워서 urllib 버전으로 내가 직접 만들었음.
<br />
<br />
[네이버 한글 로마자 변경 API](https://developers.naver.com/products/roman/)를 사용하시는 것을 권장드립니다.<br />
웹페이지를 크롤링 하는 방식으로 만들어서 API보다 데이터의 전송량이 많음. (기능은 동일) 

## Dependency

- python3 (3.6에서 테스트 되었습니다.)
- bs4 (0.0.1)

## 사용방법

```python
from urllib_korean_to_roman import korean_to_roman

result = korean_to_roman("배수지")
print(result)

result = korean_to_roman("이지은")
print(result)

result = korean_to_roman("말도 안되는 이름")
print(result)
```

- 결과
```
['Bae Sooji', 'Bae Suji', 'Bae Soojee', 'Bae Sujee']
['Lee Jieun', 'Lee Jeeeun', 'Lee Jien', 'Lee Jeeen']
[]
```