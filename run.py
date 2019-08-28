from urllib_korean_to_roman import korean_to_roman


def main():
    result = korean_to_roman("배수지")
    print(result)

    result = korean_to_roman("이지은")
    print(result)

    result = korean_to_roman("말도 안되는 이름")
    print(result)


if __name__ == '__main__':
    main()
