# zookeeper

분산 시스템에선 메세지를 전송 하고 네트워크가 끊키면 송신자는 수신지가 메세지를 성공적으로 수신했는지 알 수 없다.
메세지를 받고 응답을 못준 건지 메세지 전송 자체가 실패된 것인지 알 수 없다.
zookeeper는 hadoop에서 클러스터를 관리하기 위해 사용된다.


![image](https://user-images.githubusercontent.com/81360154/208442846-3bc909b3-cfbd-4327-b601-c2c06e905678.png)

### quorum
<hr>
위 사진에서 보이 듯이 leader서버 하나와 follower서버 둘이 있다, 즉 zookeeper에서 서버는 여러개 일반 적으로 홀수개가 있다.<br>
leader 서버는 트랜잭션을 수행할때 모든 follower서버에게 proposal을 보내고 설정한 quorum수 이상의 서버로부터 ack메세지를 받아야 트랜잭션을 수행한다.<br>
만약 leader서버에서 이상이 생겼을 경우 follower서버들의 내부 알고리즘을 통해 leader 서버를 election합니다.

### znode
<hr>

![image](https://user-images.githubusercontent.com/81360154/208812769-9cde976b-bd3c-49d3-9231-d127ceecad5d.png)
zookeepr에서 데이터 저장은 일반적인 hierarchical구조를 사용한다.<br>
각 znode에는 상태정보, config,위치정보등이 담겨있다. 그래서 각 노드에 저장된 데이터의 크기는 작다(1mb미만)
위 사진을 보면 znode에 종류가 3가지 있는데, 
 - Persistence Node : 노드에 데이터를 저장하면 일부러 삭제하지 않는 이상 삭제되지 않고 영구히 저장된다. 
 - Ephemeral Node : 노드를 생성한 클라이언트의 세션이 연결되어 있을 경우에만 유효하다.
                                          클라이언트 연결이 끊어지는 순간 삭제된다.
                                          이를 통해서 클라이언트가 연결이 되어 있는지 아닌지를 판단하는데 사용 할 수 있음.
 - Sequence Node : 노드를 생성할 때 자동으로 sequence 번호가 붙는 노드이다. 주로 분산 락을 구현하는데 이용된다.

### watch
<hr>
zookeeper에선 znode에 변화를 감지하기위해 폴링방식을 사용하는것은 설계와는 맞지 않는다.<br>
주키퍼에서는 변화를 감지하기 위해 watcher라는 것을 사용하는데, 어떤 znode에 watcher를 걸어 놓으면 설정한 callback함수가 실행된다.<br>
watcher는 1회성이라 한번 실행되면 삭제되므로 다시 등록을 해주어야한다.<br>

### ACL (Access Control List)
<hr>
znode의 권한은 일반적인 유닉스 계열의 os에서 사용하는 rwx와는 조금 다른 방식을 사용한다.

- CREATE : 해당 znode의 자식 node를 만들 수 있는 권한.
- READ : 해당 znode에서 data를 읽고 와 그 자식들의 목록을 읽을 수 있는 권한.
- WRITE : 해당 znode에 값을 쓸 수 있는 권한.
- DELETE : 해당 znode의 자식들을 지울 수 있는 권한.
- ADMIN : 해당 znode에 권한을 설정할 수 있는 권한.

### stat
<hr>
zxid는 주키퍼의 transaction id로 znode에는 아래와 같은 상태 변화 정보가 기록된다.
zxid는 sequence node라서 b의 zxid가 a의 zxid작다면 b의 transaction이 더 빨리 일어난것이다.

- czxid : znode를 생성한 트랜잭션의 id
- mzxid : znode를 마지막으로 수정 트랜잭션의 id
- ctime : znode가 생성됐을 때의 시스템 시간
- mtime : znode가 마지막으로 변경되었을 때의 시스템 시간
- version : znode가 변경된 횟수
- cversion : znode의 자식 node를 수정한 횟수
- aversion : ACL 정책을 수정한 횟수
- ephemeralOwner : 임시 노드인지에 대한 flag
- dataLength : data의 길이
- numChildren : 자식 node의 수