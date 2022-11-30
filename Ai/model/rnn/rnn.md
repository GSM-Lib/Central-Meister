# RNN
Recurrent Neural Network
<hr>


> 이전 출력도 입력으로 받는 FC layer
<hr>
여러 한계점이 많지만 분명히 한떄 자연어처리에서 유용하게 쓰였던 rnn.

그 rnn의 구조에 대해 알아봅시다.

위 나의 생각 한줄에도 말했듯이 근본적으론 FC layer인데

![fc_layer](https://user-images.githubusercontent.com/81360154/202978893-86370cac-a791-4857-a19e-a439838e1fdf.png)

이제 거기에 이전 레이어의 출력을 입력으로 받는 식입니다.

보통 rnn을 설명하는 글에서 사진을 아래 좌항(folded)과 우항(unfolded)으로 자주하는데 개인적으로 우항이 좀더 이해하는데 편한거 같습니다.
하지만 헷갈리면 안될 것 우항의 각 타임스텝에서의 레이어들의 weight는 전부 같습니다.(shared weights)

여기서 나는 어? 레이어마다 가중치가 다 다르면 성능이 더 좋게 나오지 않을까? 라고 생각했지만 shared weights를 사용하는 이유를 찾아보니
1. 문장이 다른 문장들에 대해 좀더 general한 성능을 뽑기위해
2. "On Monday it was snowing","It was snowing on Monday" 두 문장은 같은 문장인데 각 타임스텝마다 weight가 다르면 다른 출력을 뽑기때문

이라고 한다 ref=https://stats.stackexchange.com/questions/221513/why-are-the-weights-of-rnn-lstm-networks-shared-across-time


![rnn](https://user-images.githubusercontent.com/81360154/202978913-10f6b4d8-88ab-430c-9c91-ed695d080e4e.png)
그래서 우항의 사진으로 설명하자면 첫번째 A레이어에서 나오는 출력이 각각 출력층과 다음 A레이어로 들어가는데 둘이 같은 값입니다.

rnn의 수식은 $h_t = \sigma(x_tW^T_{i} + b_{i} + h_{t-1}W^T_{h} + b_{h})$입니다.
$x$는 입력, $w$는 학습될 가중치, $h_{t-1}$는 이전 레이어의 출력입니다.

이러한 출력을 다음 레이어로 넘기는 특성때문에 생기는 문제가 있는데 바로 long term dependencies입니다.

# long-term dependencies
<hr>
<img width="1581" alt="Screenshot 2022-11-23 at 11 32 10 PM" src="https://user-images.githubusercontent.com/81360154/203572766-4d0501ad-e610-450c-875e-1d00bc0e75de.png">

문장의 감정분석, 생성등 nlp task를 진행할때 감정 분석은 rnn맨 마지막 레이어의 출력을 generator에 보내주고 생성에서는 똑같이 rnn으로 이루어진 encoder의 맨 마지막출력을 decoder로 보내주는 식으로 진행되므로 마지막 레이어의 출력이 얼마나 해당 문장들의 정보를 잘 담고 있냐가 중요한데,
torch에서 쓰이는 rnn의 default activation 함수인 tanh를 보시면 아래와 같은데

![tanh](https://user-images.githubusercontent.com/81360154/203571705-af8da3fe-4bed-456e-b549-105479f2a585.png)

사진에서 보이듯이 tanh의 치역은 (-1,1)입니다.

따라서 문장의 머리 부분, 예시로 "학습이 잘 안되는 문제 발생" 이라는 문장을 들자면
"학습" 부분의 정보는 encoder 마지막 hidden state에 거의 담겨 있지 않은 것 이죠. 위의 예시 문장은 그나마 짧아서 다행이지
만약, 입력 문장이 현재 이글의 전부 라면 맨 첫 단어인 "RNN"의 정보는 거의 0에 수렴할 것 입니다.

이를 해결 하기 위해 나온 것이 LSTM입니다.
