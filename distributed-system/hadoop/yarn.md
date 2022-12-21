# yarn (Yet Another Resouce Negotiator)

Hadoop은 분산처리를 위한 오픈소스 프레임워크이다.<br>
분산처리 컴퓨터 여러대를 클러스터화 하여 데이터를 병렬적으로 처리하는 것이다.<br>
클러스터의 사전적 의미는 무리인데, 그냥 컴퓨터 여러대를 한묶음으로 보는 개념으로 보면 된다.<br>

![image](https://user-images.githubusercontent.com/81360154/207621783-e1f7dc9f-79b9-411d-80b2-122c650fe951.png)
Hadoop 2.0 이상의 아키텍쳐는(YARN) 위와 같은데, resource manager, node manager, application master, container로 이루어져 있다.

### resource manager
<hr>
resource manager는 scheduler와 application manager라는 두 components를 가지고 있다.

Scheduler는 client가 요청한 작업을 수행하는데 필요한 자원을 application master를 통해 container에게 할당해준다.
Scheduler는 그저 scheduler이기 때문에 application을 모니터링하거나 상태를 추적하지 않는다.
또한 application이나 하드웨어의 결함 때문에 실패한 작업을 재시작하는 것을 보증하지 않는다.

### node manager
<hr>
resource manager가 전체적인 클러스터를 관리 할 수있게 현재 노드의 상태(heartbeats)를 resource manager에게 전달한다.
Container의 상태를 계속해서 추적하고 만약 문제가 발생한 경우 resource manager로 부터 container를 kill하라는 명령을 받아 수행하기도 한다.

### application master
<hr>
application master는 들어온 application이 요구하는 resource가 얼마인지 계산해서 resource manager에게 resource를 요청한다.
이후 node manager들 한 container를 만들라고 지시한다.(실직적으로 container는 node manager가 생성)
application master또한 현재 노드를 모니터링 한다.
작업이 완료되면 client에 결과를 보내고 resource manager에게 작업이 끝났다는 메세지를 보낸다.


### container
<hr>
resource manager가 할당해준 cpu,ram,disk 공간이다.
그저 application이 돌아가는 자원공간이다.

