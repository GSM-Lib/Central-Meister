# OSI

## OSI란?

`OSI`는 `Open System Interconnection의 약자로 뜻은 **개방형 시스템간 상호 접속**입니다

OSI는 총 7계층이 존재합니다

### OSI 7계층

OSI 7계층은 프로토콜을 기능별로 나눈 것 입니다

각 계층은 `하위 계층의 기능만 이용`하고, `상위 계층에게 기능을 제공`합니다

일반적으로 `하위 계층`들은 **하드웨어**로 `상위 계층`들은 **소프트웨어**로 구현합니다

![image](https://user-images.githubusercontent.com/81547954/169839005-c6f87872-d155-49ec-afbe-ca925c78ad07.png)
> 출처: https://www.cloudflare.com/ko-kr/learning/ddos/glossary/open-systems-interconnection-model-osi/

그러면 첫번째 1계층(물리 계층)부터 알아보겠습니다

### 1계층(물리 계층)

물리 계층은(Physical layer)은 컴퓨터 네트워킹의 OSI 7계층 중 가장 낮은, 첫 번째 계층입니다

1계층의 역할은 전기적 신호를 사용하여 데이터를 전송하는 것입니다

물리 계층은 어떤 하나의 네트워크에서 기본 네트워크 하드웨어 전송기술들로 구성됩니다

네트워크의 높은 수준의 기능의 논리 데이터 구조를 기초로 하는 필수 계층입니다

* 물리적 매체를 통해 비트(Bit)의 흐름을 전송하기 위해 요구되는 기능들의 조정
* 사용되는 장비: Hub, Repeater, Cable
* 프로토콜: Ethernet.RS-232C

### 2계층(데이터 링크 계층)

데이터 링크 계층(Data link layer)은 포인트 두 포인트(Point to Point) 간 신뢰성있는 전송을 보장하기 위한 계층으로 CRC 기반의 오류 제어와 흐름 제어가 필요합니다

네트워크 위의 개체들 간 데이터를 전달하고, 물리 계층에서 발생할 수 있는 오류를 찾아 내고, 수정하는데 필요한 기능적, 절차적 수단을 제공한다

### 참고: http://www.incodom.kr/OSI
