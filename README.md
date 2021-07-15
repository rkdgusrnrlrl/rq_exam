# python redis 라이브러리 테스트(feat, pytest)
- incr 명렁어를 사용 하면 해당 키의 값의 숫자를 +1 해 준다.
  - 카운터를 넣을때 유용하게 썼음(예: 알람 갯수, 방문자 수 등)
- redis 의 set collection 을 쓰면 중복값 패스해서 중복 없는 리스트 만들 떄 유용
  - python set 과 비슷할 줄 알았는데, python set 의 경우 입력의 순서를 보장 하지 않음
    ```python
    ss = set()
    ss.add(50) # => {50}
    ss.add(150) # => {50, 150} 
    ss.add(70) # => {70, 50, 150} 
    ```
- pytest 의 경우 setup/teardown 을 fixture 를 사용해 구현 할 수 있음
  - python generator 에서 세팅 한 값을  yield 로 넘겨고 후처리 한다.
    
