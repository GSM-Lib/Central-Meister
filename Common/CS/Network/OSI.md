# OSI

## OSI란?

`OSI`는 `Open System Interconnection의 약자로 뜻은 **개방형 시스템간 상호 접속**입니다

OSI는 총 7계층이 존재합니다

### OSI 개념

* OSI는 개방형 시스템 상호 연결 모델의 표준입니다

* 실제 인터넷에서 사용되는 TCP/IP 는 OSI 참조 모델을 기반으로 상업적이고 실무적으로 이용될 수 있도록 단순화한 것입니다

### OSI 탄생배경

* 초기 여러 정보 통신 업체 장비들은 자신의 업체 장비들끼리만 연결이 되어 호환성이 없었음
* 모든 시스템들의 상호 연결에 있어 문제없도록 표준을 정한것이 OSI 7계층
* 표준(호환성)과 학습도구에 의미로 제작

### OSI 7계층

OSI 7계층은 프로토콜을 기능별로 나눈 것 입니다

#### 작동원리
1. OSI 7계층은 응용, 표현, 세션, 전송, 네트워크, 데이터링크, 물리계층으로 나뉩니다
2. 전송 시 7계층에서 1계층으로 각각의 층마다 인식할 수 있어야 하는 헤더를 붙입니다(캡슐화)
3. 수신 시 1계층에서 7계층으로 헤더를 떼어냅니다(디캡슐화)
4. 출발지에서 데이터가 전송될 때 헤더가 추가되는데 2계층에서만 오류제어를 위해 꼬리부분에 추가됩니다
5. 물리계층에서 1, 0 의 신호가 되어 전송매체 (동축케이블, 광섬유 등)을 통해 전송합니다

각 계층은 `하위 계층의 기능만 이용`하고, `상위 계층에게 기능을 제공`합니다

일반적으로 `하위 계층`들은 **하드웨어**로 `상위 계층`들은 **소프트웨어**로 구현합니다

![image](https://velog.velcdn.com/images/cgotjh/post/52907c8c-c149-4943-ad21-3996f44f912f/995EFF355B74179035.jpg)
> 출처: https://shlee0882.tistory.com/110

그러면 첫번째 1계층(물리 계층)부터 알아보겠습니다

### 1계층(물리 계층)

물리 계층은(Physical layer)은 컴퓨터 네트워킹의 OSI 7계층 중 가장 낮은, 첫 번째 계층입니다

1계층의 역할은 **전기적 신호**를 사용하여 **데이터를 전송**하는 것입니다

물리 계층은 어떤 하나의 네트워크에서 기본 네트워크 하드웨어 전송기술들로 구성됩니다

네트워크의 높은 수준의 기능의 논리 데이터 구조를 기초로 하는 필수 계층입니다

* 물리적 매체를 통해 비트(Bit)의 흐름을 전송하기 위해 요구되는 기능들의 조정
* 사용되는 장비: Hub, Repeater, Cable
* 프로토콜: Ethernet.RS-232C

### 2계층(데이터 링크 계층)

데이터 링크 계층(Data link layer)은 `포인트 두 포인트(Point to Point)` 간 **신뢰성있는 전송을 보장하기 위한 계층**으로 **CRC 기반의 오류 제어와 흐름 제어**가 필요합니다

**네트워크 위의 개체들 간 데이터를 전달**하고, **물리 계층에서 발생할 수 있는 오류를 찾아 내고**, **수정하는데 필요한 기능적, 절차적 수단을 제공**합니다

* 오류없이 한 장치에서 다른 장치로 프레임(Frame, 비트의 모음)을 전달하는 역할
* 사용되는 장비: Bridge, Switch
* 프로토콜: MAC, PPP, HDLC, Frame-Relay, FDDI, ATM, etc...

### 3계층(네트워크 계층)
네트워크 계층(Network layer)은 **여러개의 노드를 거칠때마다 경로를 찾아주는 역할**을 하는 계층으로 **다양한 길이의 데이터**를 네트워크들을 통해 전달합니다

그 과정에서 **전송 계층이 요구하는 서비스 품질(QoS)을 제공하기 위한 기능적, 절차적 수단을 제공**합니다

네트워크 계층은 `라우팅, 흐름 제어`, `세그맨테이션(segmentation/desegmentation)`, `오류 제어`, `인터네트워킹(Internetworking)`등을 수행합니다

* 다중 네트워크 링크에서 패킷(Packet)을 발신지로부터 목적지로 전달할 책임을 갖습니다
* 사용되는 장비: Route
* 프로토콜: IP, ICMP, IGMP

### 4계층(전송 계층)

전송 계층(Transport layer)은 `양 끝단(End to end)`의 **사용자들이 신뢰성 있는 데이터를 주고 받을 수 있도록** 하여, **상위 계층들이 데이터 전달의 유효성이나 효율성을 생각하지 않도록 해줍니다**

또한 **시퀀스 넘버 기반의 오류 제어 방식을 사용합니다** 특정 연결의 유효성을 제어하고, 일부 프로토콜은 `상태 개념(stateful)`이 있고, `연결 기반(connection oriented)`입니다

* 전체 메시지를 발신지 대 목적지(End to end)간 제어와 에러를 관리합니다
* 사용되는 장비: Gateway
* 프로토콜: TCP, UDP, ARP

### 5계층(세션 계층)
세션 계층(Session layer)은 양 끝단의 응용 프로세스가 **통신을 관리하기 위한 방법을 제공**합니다

`동시 송수신방식(duplex)`, `반이중 방식(half-duplex)`, `전이중 방식(Full Duplex)`의 통신과 함께, `체크 포인팅`과 `유휴`, `종료`, `다시 시작 과정` 등을 수행합니다

* 통신 세션을 구성하는 계층으로, 포트(port)연결이라고도 할 수 있습니다
* 응용간의 질서 제어
* 프로토콜: SSH, TLS

> 세션(Session)이란?
>>  \* 네트워크 환경에서 사용자 간 또는 컴퓨터 간의 대화를 위한 논리적 연결
>>
>> \* 프로세스들 사이에 통신을 수행하기 위해서 메시지 교환을 통해 서로를 인식 한 이후부터 통신을 마칠 때가지의 기간

### 6계층(표현 계층)

표현 계층(Presentation layer)은 **코드 간의 번역을 담당**하여 사용자 시스템에서 데이터의 형식상 차이를 다루는 부담을 응용 계층으로부터 덜어 줍니다

**MIME 인코딩이나 암호화 등의 동작이 이 계층에서 이루어집니다**

> 예를 들면, EBCDIC로 인코딩된 문서 파일을 ASCII로 인코딩된 파일로 바꿔 주는 것이 표현 계층의 몫입니다

* 운영체계의 한 부분으로 입력 또는 출력되는 데이터를 하나의 표현 형태로 변환합니다
* 이해할 수 있는 포멧 변환
* 포로토콜: JPEG, MPEG, SMB, AFP

### 7계층(응용 계층)

응용 계층(Application layer)은 **응용 프로세스와 직접 관계하여 일반적인 응용 서비스를 수행**합니다

일반적인 응용 서비스는 **관련된 응용 프로세스들 사이의 전환을 제공**합니다

> 응용 서비스의 예로 `Telnet`, `SSH`, `HTTP`, `SMTP`, `FTP` 등이 있습니다

* 사용자가 네트워크에 접근할 수 있도록 해주는 계층입니다
* 서비스 제공
* 프토로콜: DHCP, DNS, FTP, HTTP

### 참고: http://www.incodom.kr/OSI, https://velog.io/@cgotjh/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-OSI-7-%EA%B3%84%EC%B8%B5-OSI-7-LAYER-%EA%B8%B0%EB%B3%B8-%EA%B0%9C%EB%85%90-%EA%B0%81-%EA%B3%84%EC%B8%B5-%EC%84%A4%EB%AA%85