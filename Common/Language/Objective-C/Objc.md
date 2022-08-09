# 개요
Objc는 .h 파일와 .m 파일이 있다. 
.h 파일은 헤더파일이다. 선언하는 용도이며, 해당 파일에서 선언된 부분은 헤더를 추가한 곳에서 전체 공개 된다. (`#import <헤더파일>`)
.m 파일은 구편파일이다. 구련하는 용도이며, 해당 파일에서 선언된 부분은 내부에서만 공개 된다.

# 변수 선언
`type` name = `value`;
```objc
NSString *name = @"name";
```
자료형이 클래스일 경우 변수명 앞에 *이 붙어야 한다.

# Method 정의
+ or - (`return type`) method name:(`parameter type`) parameter name;

+는 class method이고 -는 instance method이다.

# Method 호출
[class method];
```objc
[array addObject:object]
```

# 객체 선언
```objc 
Object *o = [[Object alloc] init];
```

# 문자열
objc는 문자열을 `@" " ` 형식으로 사용한다.
문자열 안에 값을 넣으려면 `@"%@", 2` 같은 방식으로 넣어야 된다

# 로그
```objc
NSLog(@"Log");
NSLog(@"%@", 2);
```

# Class 선언
선언부
```objc
@interface Object : Parent class
...
@end
```

구현부
```objc
@implementation Object
...
@end
```

클래스 안에 매서드 정의할때 공개하고 싶다면 선언부에, 내부적으로만 사용한다면 구현부에서만 작성할 수 있다.
클래스에서 변수를 선언한다면 `@property`를 사용해서 선언한다.
```objc
@interface Object: NSObject
@property (nonatomic) NSString *name;
@end
```

# protocol confirm
```objc
@interface Object: Parent <Protocol>

@end
```
위처럼 부모 클래스 옆에 <>안에 confirm할 프로토콜을 넣는다. (다중 confirm 가능)j
