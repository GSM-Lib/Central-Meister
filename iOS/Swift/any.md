# existential any
Swift 5.6에서 `any`가 생겼습니다.

## existential type?
protocol이 type으로 사용될 때 이를 existential type이라고 합니다.


기존에는 protocol을 Type으로 받으면 아래처럼 됩니다. 
```swift
protocol Ex {}
struct ExStruct: Ex {}

let ex: Ex = ExStruct()
```

그리고 Swift 5.6 이상부터는 아래처럼 사용할 수 있습니다.
```swift
protocol Ex {}
struct ExStruct: Ex {}

let ex: any Ex = ExStruct()
```

# 왜 any를 써야하는지?
1. protocol(existential type)과 struct, class의 타입(concrete type)을 구분하기 위해서.
2. Swift 5.7 이상부터는 warning을 띄우고 6.0 이상부터는 Compile 에러를 띄운다고 한다.
3. existential type 은 concrete type 보다 더 많은 비용이 드는데, 개발자가 이 퍼포먼스 비용을 나타내는 명확한 구분이 없었다.
  
