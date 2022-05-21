# SOLID
객체 설계에 필요한 5가지 원칙으로써 유지보수가 쉽고, 유연하고, 확장이 쉬운 소프트웨어를 만들기 위한 수단으로 본다.

- S: SPR(Single Responsibility Principle) - 단일 책임 원칙
- O: OCP(Open-Closed Principle) - 개방-폐쇠 원칙
- L: LSP(Liskov Substitution Principle) - 리스코프 치환 원칙
- I: ISP(Interface Segregation Principle) - 인터페이스 분리 원칙
- D: DIP(Dependency Inversion Principle) - 의존관계 역전 원칙

## S: SPR(Single Responsibility Principle) - 단일 책임 원칙
- 클래스 수정이유는 단 하나여야 한다.
- 클래스 하나는 단 하나의 책임(Knowing, Doing)만 가져야 한다.
- 하나의 책임이 여려 개의 클래스에 나뉘어 있어도 안된다.
- 하나의 클래스 안에 협력관계가 여러개 있는 것은 괜찮다.

SRP 적용 전
```Swift
class Handler {
  func handle() {
    let data = requestDataToAPI()
    let array = parse(data: data)
    saveToDB(array: array)
  }
    
  private func requestDataToAPI() -> Data {
    // send API request and wait the response
  }
    
  private func parse(data: Data) -> [String] {
    // parse the data and create the array
  }
    
  private func saveToDB(array: [String]) {
    // save the array in a database
  }
}
```
- `Handler`란 클래스가 여러 개의 책임을 가지고 있다. (API, Parsing, DB)

<br>

SRP 적용 후
```Swift
class Handler {
 
    let apiHandler: APIHandler
    let parseHandler: ParseHandler
    let dbHandler: DBHandler
 
    init(apiHandler: APIHandler, parseHandler: ParseHandler, dbHandler: DBHandler) {
        self.apiHandler = apiHandler
        self.parseHandler = parseHandler
        self.dbHandler = dbHandler
    }
 
    func handle() {
        let data = apiHandler.requestDataToAPI()
        let array = parseHandler.parse(data: data)
        dbHandler.saveToDB(array: array)
    }
}
 
class APIHandler {
 
    func requestDataToAPI() -> Data {
        // send API request and wait the response
    }
}
 
class ParseHandler {
 
    func parse(data: Data) -> [String] {
        // parse the data and create the array
    }
}
 
class DBHandler {
 
    func saveToDB(array: [String]) {
        // save the array in a database 
    }
}
```
- 기존 `Handler`클래스가 3개의 책임을 가지고 있었으나,
- `APIHandler`, `ParseHandler`, `DBHandler` 클래스가 각각 하나의 책임을 가지고 있고 `Handler` 클래스 안에 협력관계로 있다.

<br>

## O: OCP(Open-Closed Principle) - 개방-폐쇄 원칙
- 확장에는 열려있으나 변경에는 닫혀있어야 한다. (기능 케이스를 추가할때 기존 코드를 변경하지 않고 추가해야 한다.)
- 객체가 변경될 때는 해당 객체만 바꿔도 동작이 잘 되면 OCP가 잘 지켜진거고, 바꿔야할 것이 많다면 OCP를 잘 안지킨것이다.
- 모듈이 주변환경에 지나치게 의존해서는 안된다.

OCP 적용 전
```Swift
enum Country {
  case korea
  case japan
  case china
}

class Flag {
  let country: Country
  
  init(country: Country) {
    self.country = country
  }
}

func printNameOfCountry(flag: Flag) {
  switch flag.country {
    case .china:
      print("중국")
    case .korea:
      print("한국")
    case .japan:
      print("일본")
  }
}
```
- Country enum에 USA case를 추가하면 printNameOfCountry() 함수도 수정해야 한다. 결합도와 의존성이 높고, 유지보수가 힘들다.

<br>

OCP 적용 후
```Swift
enum Country {
  case korea
  case japan
  case china
    
  var name: String {
    switch self {
      case .china:
        return "중국"
      case .korea:
        return "한국"
      case .japan:
        return "일본"
    }
  }
}

class Flag {
  let country: Country
    
  init(country: Country) {
    self.country = country
  }
}

func printNameOfCountry(flag: Flag) {
  print(flag.country.name)
}
```

```Swift
protocol Country {
  var name: String { get }
}

struct Korea: Country {
  let name: String = "한국"
}

struct Japan: Country {
  let name: String = "일본"
}

struct China: Country {
  let name: String = "중국"
}

class Flag {
  let country: Country
  
  init(country: Country) {
    self.country = country
  }
}

func printNameOfCountry(flag: Flag) {
  print(flag.country.name)
}
```
- USA를 추가하고 싶다면 Country를 confirm하는 구조체를 만들기만 하면 된다. 결합도가 낮고, 응집도가 높아 유지보수에 용이하다.

<br>
  
## L: LSP(Liskov Substitution Principle) - 리스코프 치환 법칙
- 서브 타입은 (상속받은)기본 타입으로 대체 가능해야 한다.
- 자식 클래스는 부모 클래스의 동작(의미)를 바꾸지 않는다.
- 상속을 사용했을 때 서브클래스는 자신의 슈퍼클래스 대신 사용돼도 같은 동작을 해야한다.

LSP 적용전
```Swift
class 직사각형 {
  var 너비: Float = 0
  var 높이: Float = 0
  var 넓이: Float {
    return 너비 * 높이
  }
}

class 정사각형: 직사각형 {
  override var 너비: Float {
    didSet {
      높이 = 너비
    }
  }
}

func printArea(of 직사각형: 직사각형) {
  직사각형.높이 = 5
  직사각형.너비 = 2
  print(직사각형.넓이)
}

let rectangle = 직사각형()
printArea(of: rectangle)
let square = 정사각형()
printArea(of: square)
```

<br>

LSP 적용후
```Swift
protocol 사각형 {
  var 넓이: Float { get }
}

class 직사각형: 사각형 {
  private let 너비: Float
  private let 높이: Float
  
  init(너비: Float, 높이: Float) {
    self.너비 = 너비
    self.높이 = 높이
  }
  
  var 넓이: Float {
    return 너비 * 높이
  }
}

class 정사각형: 사각형 {
  private let 변의길이: Float
  
  init(변의길이: Float) {
    self.변의길이 = 변의길이
  }
  
  var 넓이: Float {
    return 변의길이 * 변의길이
  }
}
```

## I: ISP(Interface Segregation Principle) - 인터페이스 분리 원칙
- 인터페이스를 일반화하여 구현하지 않는 인터페이스를 confirm하는 것보다
- 구체적인 인터페이스를 confirm하는 것이 더 좋다는 원칙.
- 인터페이스를 설계할 때, 굳이 사용하지 않는 인터페이스는 confirm해 구현하지 말고
- 오히려 한 가지의 기능을 가지더라도 정말 사용하는 인터페이스로 분리하는 것이 좋다.

ISP 적용 전
```Swift
protocol Shape {
    var area: Float { get }
    var length: Float { get }
}

class Square: Shape {
    var width: Float
    var height: Float
    
    var area: Float {
        return width * height
    }
    
    var length: Float {
        return 0
    }
    
    init(
        width: Float,
        height: Float
    ) {
        self.width = width
        self.height = height
    }
}

class Line: Shape {
    var pointA: Float
    var pointB: Float
    
    var area: Float {
        return 0
    }
    
    var length: Float {
        return pointA - pointB
    }
    
    init(
        pointA: Float,
        pointB: Float
    ) {
        self.pointA = pointA
        self.pointB = pointB
    }
}
```
- Line, Square 모두 Shape를 상속받는 객체지만 실제로 Square는 length라는 변수가 필요가 없고
- Line은 area란 변수가 필요없다.
- 하지만 예제에서는 단지 Shape라는 프로토콜을 채택한다는 이유만으로 필요없는 기능을 구현하고 있다.
- 이 경우 ISP를 지키지 않고 있다고 할 수 있다.

<br>

ISP 적용 후

```Swift
protocol AreaCalculatableShape {
    var area: Float { get }
}

protocol LenghtCalculatableShape {
    var length: Float { get }
}

class Square: AreaCalculatableShape {
    var width: Float
    var height: Float
    
    var area: Float {
        return width * height
    }
    
    init(
        width: Float,
        height: Float
    ) {
        self.width = width
        self.height = height
    }
}

class Line: LenghtCalculatableShape {
    var pointA: Float
    var pointB: Float
    
    var length: Float {
        return pointA - pointB
    }
    
    init(
        pointA: Float,
        pointB: Float
    ) {
        self.pointA = pointA
        self.pointB = pointB
    }
}
```
- 기존의 필요없는 기능들을 구현하고 있던 인터페이스들(프로토콜들)을 더욱 세분화하여 나누었다.

## D: DIP(Dependency Inversion Principle) - 의존관계 역전 원칙
- 상위레벨 모듈은 하위레벨 모듈에 의존하면 안된다.
- 두 모듈은 추상화된 인터페이스(protocol)에 의존해야 한다.
- 추상화된 것은 구체적인 것에 의존하면 안되고, 구체적인 것이 추상화된 것에 의존해야 한다.
- 의존관계를 맺을 때, 변화하기 쉬운 것 또는 자주 변화화는 것(클래스)보다는 변화하기 어렵거나 거의 변화가 없는것(인터페이스)에 의존해야 한다
- 하위레벨 모듈이 상위레벨 모듈을 참조하는 것은 되지만 상위레벨 모듈이 하위레벨 모듈을 참조하는 것은 안하는게 좋다. 그런 경우는 제네릭이나 Associate를 사용하는 것이 좋다.
- DIP를 만족하면 의존성 주입(Dependency Injection)이라는 기술로 변화를 쉽게 수용할 수 있다.

DIP 적용전
```Swift
class 맥북13인치 {
  func 전원켜기() {}
}

class 개발자 {
  let 노트북: 맥북13인치 = 맥북13인치()
  
  func 개발시작() {
    노트북.전원켜기()
  }
}
```

- DI(의존성 주입): 외부에서 객체를 생성해서 내부에 넣는 것을 말함
```Swift
class 맥북13인치 {
  func 전원켜기() {}
}

class 개발자 {
  let 노트북: 맥북13인치
  
  init(노트북: 맥북13인치) {
    self.노트북 = 노트북
  }
  
  func 개발시작() {
    노트북.전원켜기()
  }
}
```
- 객체생성을 외부에서 한 경우를 DI라고 부름
- 그럼 DIP는 뭐인가?

<br>

DIP 적용후
```Swift
protocol 노트북 {
  func 전원켜기()
}

class 개발자 {
  let 노트북: 노트북
  
  init(맥북: 노트북) {
    self.노트북 = 맥북
  }
  
  func 개발시작() {
    노트북.전원켜기()
  }
}

class 맥북13인치: 노트북 {
  func 전원켜기() {}
}

class 맥북15인치: 노트북 {
  func 전원켜기() {}
}

class 레노버: 노트북 {
  func 전원켜기() {}
}
```
- 객체를 외부에서 생성해서 주입할 뿐만 아니라, 프로토콜이라는 추상화시킨 객체를 의존시키게 만들어야한다
- DIP는 더 중요한 모듈이 덜 중요한 모듈에 의존하면 안되며
- 추상화에 의존해야 되는 원칙으로 실체에 의존할 것인가, 추상화에 의존할 것인가가 포인트다