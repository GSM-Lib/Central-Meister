# RNN
Recurrent Neural Network
<hr>


> 이전 출력도 입력으로 받는 FC layer
<hr>
여러 한계점이 많지만 분명히 한떄 자연어처리에서 유용하게 쓰였던 rnn.

그 rnn의 구조에 대해 알아보자.

위 나의 생각 한줄에도 말했듯이 근본적으론 FC layer인데
![fc_layer](https://user-images.githubusercontent.com/81360154/202978893-86370cac-a791-4857-a19e-a439838e1fdf.png)

이제 거기에 이전 레이어의 출력을 입력으로 받는 식이다.
레이어는 다음 사진의 A하나를 레이어 하나라 생각하면 된다

보통 rnn을 설명하는 글에서 사진을 아래 좌항(folded)과 우항(unfolded)으로 자주하는데 개인적으로 우항이 좀더 이해하는데 편한거 같다
![rnn](https://user-images.githubusercontent.com/81360154/202978913-10f6b4d8-88ab-430c-9c91-ed695d080e4e.png)
그래서 우항의 사진으로 설명하자면 첫번째 A레이어에서 나오는 출력이 각각 출력층과 다음 A레이어로 들어가는데 둘이 같은 값이다.

rnn의 수식은 $h_t = tanh(x_tW^T_{ih} + b_{ih} + h_{t-1}W^T_{hh} + b_{hh})$이다.
$x$는 입력, $w$는 학습될 가중치, $h_{t-1}$는 이전 레이어의 출력이다.

이러한 출력을 다음 레이어로 넘기는 특성때문에 생기는 문제가 있는데 바로 gradient vanishing이다.

# Gradient vanishing
문장의 감정분석, 생성등 nlp task를 진행할때 감정 분석은 rnn맨 마지막 레이어의 출력을 generator에 보내주고 생성에서는 똑같이 rnn으로 이루어진 encoder의 맨 마지막출력을 decoder로 보내주는 식으로 진행되므로 마지막 레이어의 출력이 얼마나 해당 문장들의 정보를 잘 담고 있냐가 중요한데,
torch에서 쓰이는 rnn의 default activation 함수인 tanh만 봐도 미분했을때 그래프가 아래와 같은데
![tanhDerivation](https://user-images.githubusercontent.com/81360154/202978926-a12e154e-73e7-48a0-952e-dfaa8af18d17.png)
보면 출력값이 전부 1이하이다.

따라서 loss함수가 뱉은 loss가 backpropagation을 거듭하면 거듭할수록 점점 작아지면서 0에 수렴하게 된다.

이를 해결하기 위해 나온것이 LSTM이다.
