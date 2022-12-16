# trait

* Scala 는 interface 가 없으며 대신  trait 을 사용한다.
* Scala 의 trait 는 자바의 interface 와 달리 구현 가능하다. (자바8 부터는 자바인터페이스도 디폴트메소드등 구현)
* 하나의 부모클래스를 갖는 클래스의 상속과 달리 트레이트는 몇개라도 조합해 사용 가능하다.
* Scala 의 trait 는 자바의  인터페이스와 추상클래스의 장점을 섞었다.
* 트레이트를 믹스인 할때는 extends 키워드를 이용한다.
* extends를 사용하면 trait 의 슈퍼클래스를 암시적으로 상속하고 , 본래 trait 를 믹스인한다.
* trait 는 어떤 슈퍼클래스를 명시적으로 상속한 클래스에 혼합할 수 있다.
   그때 슈퍼클래스는 extends 를 사용하고, trait 는 with 로 믹스인한다.

```
trait Philosophical {
    def philosophize() {
        println("I consume memory, therefore I am!")
    }
}
class Frog extends Philosophical {
    override def toString = "green"
}
```

위와 같이 trait안의 메소드를 함수를 trait안에서 구현 할 수 있단거 빼고는 자바의 interface와 크게 다르지 않는
trait의 중요한점은 믹스인시 순서와 trait선언시 어떤 클래스를 상속 받았을 경우 해당 trait은 해당 클래스를 상속한 클래스에만 사용 할 수 있단거다.
```
abstract class Manager { // 트레이트가아닌 추상클래스임에 주의

  def lookup(): Unit = {
    println("Base lookup")
  }
}

// 슈퍼클래스로 Manager를 선언하였다. 이 선언은 TaskManager 트레이트가 Manager를 상속한 클래스에만 Mixin될 수 있다는 것이다.
trait TaskManager extends Manager {

  override def lookup(): Unit = {
    println("TaskManager task lookup")
    super.lookup()
  }
}

trait JobManager extends Manager {

  override def lookup(): Unit = {
    println("JobManager job lookup")
    super.lookup()
  }
}

// Manager가 아닌 이외의 클래스를 상속할 경우 컴파일 에러가 난다
class ManagerImpl extends Manager with TaskManager with JobManager {

  override def lookup(): Unit = {
    println("Impl lookup")
    super.lookup()
  }
}

object Test {

  def main(args: Array[String]): Unit = {
    val manager = new ManagerImpl
    manager.lookup()
  }
}
```
위 main을 실행하면 아래와 같이 결과가 나오는데
Impl lookup<br>
JobManager job lookup<br>
TaskManager task lookup<br>
Base lookup<br>

순서가 extends Manager with TaskManager with JobManager에서 오른쪽부터 실행됨을 확인할 수 있다.
