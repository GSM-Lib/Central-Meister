# Backpropagation

<hr>

> 인공지능 == 미분
<hr>
Backpropagation에 대해 알아보기전에 편미분에 대해 알아봅시다

## 편미분 partial derivative
<hr>
한줄로 설명하면 다변수 함수에서 내가 노리는 변수 하나를 제외하고 나머지는 전부 상수취급 한 이후에 미분하는것입니다.

뭐 간단한 수식하나를 예로 들어서 $h = w_1x_1 + w_2x_2$에서 
$w_1$이 $h$에 대해 끼치는 영향력을 알고 싶을때 즉
$\dfrac{\partial h}{\partial w_1}$값을 알고 싶을때
w_2는 상수 취급해서 
$h = w_1^{1-1}x_1 + w_2x_2$
$\dfrac{\partial h}{\partial w_1} = x_1$이 되는 것입니다.

<hr>

다시 원래대로 돌아와 역전파에 대해 알아보자면 
$loss = softmax(w_3*\sigma(w_2*\sigma(x*w_1+b)))$
위와 같은 깊게 얽히고설킨 수식에서 편미분을 이용해 $w_1$이 loss에 끼치는 영향력을 알아내는 것이 역전파입니다.
