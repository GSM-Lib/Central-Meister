# Gradient Descent
<hr>

> 인공지능이 학습하는 방법
<hr>

deep learning의 가장 근간이 되는 gradient descent에 대해 알아봅시다.

딥러닝에 대해 공부하게 된다면 가장 먼저 공부하게 될 부분이 이 gradient descent라 생각하는데 그만큼 딥러닝에서 중요한 부분입니다.

하지만 이해하는데 그렇게 어렵지는 않습니다.

모델에서 쭉 forwarding되다가 이제 loss를 구하고 역전파를 통해 어떤 t번째 레이어에서 가중치 매트릭스의 변수하나 $\theta$가 loss에 끼치는 영향력 크기인 gradient $\dfrac{\partial loss}{\partial \theta}$를 구했을텐데
![image](https://user-images.githubusercontent.com/81360154/203344308-3cd9c5d9-5575-4f8d-9369-1f54fff8b2f1.png)

위 사진에서 보이듯이 gradient가 양수일때는 저 공이 왼쪽으로 굴러야하므로 gradient만큼 빼줍니다 vice versa

따라서 gradient descent의 수식은 $w = w - \alpha\dfrac{\partial loss}{\partial \theta}$가 됩니다.
수식에서 alpha는 learning rate라는 것인데 식에서 보듯이 learning rate가 클수록 학습속도가 빨라지고 작을수록 느려집니다 하지만 learning rate가 크면 gradient exploding이 일어날 수 있습니다.
그렇다고 또 learning rate가 너무 작으면 학습 속도가 느리고 local minimum에 빠질 수 있다.

이제 저 공이 구르는거에 물리현상을 더한 momentum과 공이 크게 굴러야할곳엔 크게 구르고 작게 굴러야할곳엔 작게 구르는 adagrad같은 방법(수식)들이 있는데
이는 optimizer파트에서 더 자세하게 다루겟습니다.




