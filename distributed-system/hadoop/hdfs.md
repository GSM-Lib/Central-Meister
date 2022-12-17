# HDFS (Hadoop Distributed File System)

- 하드웨어 결함을 exception이 아닌 norm으로 본다.
- 한번 적히면 append나 truncate를 제외하고는 파일 수정이 불가능하다 appending을 지원하긴 하나 임의로 append할순 없다. 이 덕분에 높은 데이터 처리량을 가질 수 있다.
- 데이터노드를 클러스터에 추가하기만 하면 파일시스템 용량이 늘어난다.
- 데이터를 블록으로 나눠 저정한다. (default = 128MB)
- fault tolerance를 위해데이터를 복제하여 저장한다. (default = 3)

##### components : namenode, secondary namenode, datanode

### namenode
<hr>
데이터의 메타정보를 저장한다. fsimage(파일명, 디렉토리, 파일 크기, 권한) (블럭정보 mapping )<br>
지속적으로 데이터노드의 상태를 모니터링하고 관리한다.

- 데이터 노드는 3초단위로 상태정보와 블록정보를 담은 Heartbeat(default per 3초) 시그널을 네임노드로 전송하며, 이 시그널이 오지않으면 장애노드로 판단하여 데이터를 새 노드로 복제한다.
- 용량이 부족한 노드 발견시 데이터 블록을 다른 노드로 이동.
- 네임노드는 블록의 복제본 수도 관리하게 되며 복제본 수가 일치 하지 않는 블록이 발견될 경우 블록을 복제하거나 삭제한다.

클라이언트의 요청을 처리한다
- HDFS에 파일저장시 네임노드에서 요청을 받아 권한승인을 하거나, 조회시 어떤 블럭을 조회해야 하는지 알려줍니다.
- 단 실제 파일 저장은 Client가 직접 데이터 노드로 전송합니다.

![image](https://user-images.githubusercontent.com/81360154/208253112-3ce09d75-7727-4e1c-a0d2-d994dc0c8172.png)

hdfs 시작될때 namenode의 구동 순서는 다음과 같다.

- fsimage를 디스크에서 읽어 메모리에 로딩한다.
- 메모리에 editslog 중에 반영되지 않은 것을 찾아 반영한다.
- 로드된 메모리의 정보로 다시 fsimage 파일 갱신한다.
- 데이터노드와 네임노드가 통신하며 데이터노드가 등록된다.
- 데이터노드가 네임노드에게 블록리포트를 보내준다.
- safemode에 진입하며 데이터노드가 보내준 블록리포트를 바탕으로 블록복제가 일정수준이상을 만족때 까지 safemode에 머무른다.
- 블록복제가 일정수준을 만족하면 자동으로 safemode에서 빠져나온다.
- 네임노드는 주기적으로(약 1시간) 데이터노드에게 블록리포트를 받아 블록매핑정보(어떤 데이터노드에 어떤 블록이 있는지)를 만들어내서 메모리에 저장해놓는다.
- editslog를 초기화 한다.

### secondary datanode
<hr>
위 namenode 구동 순서에서 만약 파일시스템을 지속적으로 사용할 경 메모리에 editlog를 반영하는 작업의 시간이 오래 걸리게 된다.
이를 방지하기 위해 보조네임노드는 주기적으로 editlog를 fsimage에 적용해 주어 editlog의 크기를 줄이는 작업을 수행한다.

![image](https://user-images.githubusercontent.com/81360154/208254053-3e04bab6-40ec-44da-8cda-3271c6cc5c5a.png)

- namenode한테 editlog랑 fsimage를 달라한다.
- namenode가 파일을 보내주고 기존editlog파일을 초기화한다.
- secondart namenode에서 fsimage에 editlog를 적용시켜 fsimage.ckpt를 만든다.
- fsimage.ckpt를 namenode에게 보내준다.
- namenode는 받은 fsimaeg.ckpt를 fsimage에 적용한다.


### datanode
<hr>
실제로 데이터가 저장되는 곳이다.
client가 namenode에 요청을 하지만 실제로 데이터를 주고받는 작업은 datanode와 한다.

