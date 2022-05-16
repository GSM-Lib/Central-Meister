# Declarations(선언)

### Constant Declaration(상수 선언)

상수 선언은 프로그램에 명명된 상수값을 도입합니다 

상수 선언은 `let` 키워드를 사용하여 선언되고 다음과 같은 형식을 가집니다

![image](https://user-images.githubusercontent.com/81547954/168509231-4d6dcf75-3472-4bbd-907e-1f28abdcda4b.png)
> 출처: https://bbiguduk.gitbook.io/swift/language-reference/declarations#constant-declaration

상수는 **값이 설정된 후에 변경할 수 없습니다**

왜냐하면 **상수가 클래스 객체로 초기화되면 이 객체 자체는 변경할 수 있지만** 이 **상수 이름과 참조하는 객체 간의 바인딩은 변경할 수 없기** 때문입니다

상수가 전역 범위로 선언되면 값으로 반드시 초기화 되어야 합니다

### Variable Declaration(변수 선언)

변수 선언은 프로그램에 명명된 변수 값을 도입하고 `var` 키워드를 사용하여 선언합니다

변수 선언은 
* 명명된 값
* 변경 가능한 값
* 저장된 값
* 계산된 변수와 프로퍼티
* 저장된 변수와 프로퍼티 관찰자
* 정적변수 프로퍼티

다양한 종류의 선언 형식을 가집니다

사용할 적절한 형식은 변수가 선언되는 범위와 선언되는 변수의 종류에 따라 다릅니다

변수는 **값이 설정된 후에도 값을 변경할 수 있습니다**

### 저장된 변수와 저장된 변수 프로퍼티 (Stored Variables and Stored Variable Properties)

다음의 형식으로 저장된 변수 또는 저장된 변수 프로퍼티를 선언할 수 있습니다

![image](https://user-images.githubusercontent.com/81547954/168514402-459d2bb1-b42b-40fb-8f76-814606e47d64.png)

이러한 형식의 변수 선언은 전역 범위, 함수의 지역 범위, 또는 클래스나 구조체 선언의 컨텍스트에서 정의합니다

### 참고: https://bbiguduk.gitbook.io/swift/language-reference/declarations#constant-declaration
