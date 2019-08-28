# Python 한글 인명 로마자 변환기

한글 인명을 로마자로 변환해 주는 프로그램.<br />
인터넷에서 찾은 selenium 기반의 예제 코드가 너무 무거워서 직접 만든 urllib기반의 한글인명 영문 변환기.
<br />
<br />
[네이버 한글 로마자 변경 API](https://developers.naver.com/products/roman/)를 사용하시는 것을 권장드립니다. (데이터 전송량이 적습니다. 대신 사용량 제한 있음.)<br />
이 소스코드는 [웹페이지](https://dict.naver.com/name-to-roman/translation/)를 크롤링 하는 방식으로 만들어졌습니다. (사용량의 제한이 없음)

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
