# Implicit

x.method()에서 타입오류가 나면 컴파일러는 convert(x).method()로 실행하게 된다.
여기서 convert()가 implicit이다

### 암시적 변환
<hr>
어떤 객체 button이 있고 그 button의 메소드들중 특정 인터페이스를 상속하는 클래스를 파라미터로 받는 메소드가 있다 하면

```
val button = new Button 

button.addLButtonDownAction(
    new ActionListener {
        def actionPerformed ( event : ActionEvent ) {
            println("스칼라 어려워")
        }
    }
}
```
이런식으로 파라미터를 넘겨줄 수 있을것이다.
하지만 println 하나 넘겨 주려고 저렇게 쓰는건 너무 길다.

```
button.addLButtonDownAction((_: ActionEvent) => printn("스칼라 어려워"))
```
이런식으로 간결하고 코드 가독성이 높게 쓰고 싶지만 addLButtonDownAction메소드는 클래스를 파라미터로 받기 때문에 위에 호출은 오류가난다.
이럴때 사용하는 것이 implicit conversion이다.

```
implicit def functionToActionClass(f : ActionEvent => Unit ) = 
    new ActionListener {
        def actionPerformed (event : ActionEvent) = f(event)
    }
```
위는 함수를 파라미터로 받아 클래스를 리턴 해주는 함수이다.
```
button.addLButtonDownAction(
    functionToActionClass( 
        (_: ActionEvent) => println (" 삐약 ") 
    ) 
)
```
implicit덕분에 코드가 한줄 짧아졌다 하지만 이것만으론 아쉽다.
```
button.addLButtonDownAction( (_: ActionEvent) => println(" 삐약 ") )
```
근데 짜잔, 사실 이렇게만 써도 작동을한다. 이것이 implicit의 힘이다.

일단 저 코드가 컴파일되면 처음엔 타입오류가 발생하긴 한다. 그럼 컴파일러는 implicit conversion을 통해서 해결 할 수 있지 않나 살펴봅니다.
살펴보다가 implicit 로 선언된 함수 functionToActionClass를 찾았습니다. 이걸 가지고 시도해보니 잘 된다.

암시적 변환이란 컴파일러가 열심히 일해서 개발자가 성가신 일들을 하지 않게 도와주는 녀석이었습니다.
이제 클래스를 넣어도 잘되고 저렇게 람다식으로 넣어도 잘 될 것입니다. 

 

### 암시적 파라미터
<hr>

```
def greet (name : String )(implicit prompt : MyPrompt) = {
    println (name)
    println (prompt.preference)
  }
```
위와 같은 함수가 하나 있다고 하자 위 함수를 호출하려면 일반적으로
```
val prompt = new MyPrompt(" ubuntu> ")
greet("linux")(prompt)
```
이런 식으로 해야할 것이다.
하지만 함수 선언에서 두번째 파라미터 필드가 Implicit으로 돼있기 때문에



```
greet("linux")
```
이런 식으로 호출해도 암시적으로 파라미터에 값을 넣어준다. 물론 그냥 이렇게해서 되는건아니고

```
object HamaPrefs{
  implicit val prompt: MyPrompt = new MyPrompt(" ubuntu> ")
}

class MyPrompt(greet: String) {
  val preference = greet
}
```
어디 이런식으로 선언해 놔야한다.

따라서 프레임워크등을 사용하다가 implicit 가 나오면 해당 프레임워크에서 그 인자에 대해서는 미리 만들어 뒀구나 라고 생각하면 편하다.


