# BTree

### B-Tree
<hr>
B-Tree란 이진트리와 다르게 자식노드가 2개 이상 일 수 있고 모든 leaf노드의 level이 같은 자료구조이다.<br>
모든 leaf노드의 level이 같은 덕에 최악의상황에 O(N)이 나오는 이진트리와 달리 최악의상황에서도 O(logN)의 성능을 보여준다.

B-Tree에는 N차 B-Tree라는 말이 나오는데 최대 자식노드수가 N인 B-Tree를 N차 B-Tree라고 부릅니다.<br>
![image](https://user-images.githubusercontent.com/81360154/210086548-4287eb09-d1be-473b-b4a7-c9c0ae5a0730.png)
위 사진의 B-Tree는 3차 B-Tree인 것이죠 또한 사진에서 보이듯이 자식 노드의 개수는 부모 노드 key개수에 1을 더한 값이다.

### B-Tree 검색
1. root node에서 시작
2. 현재 노드의 key를 순회해 찾는 key가 있으면 탐색 종료
3. else 어떤 이웃한 두 key사이에 key가 들어가는 경우 해당 포인터를 통해 자식 Node로 내려간다
4. 찾는 key가 나올때 까지 2,3 반복

![image](https://user-images.githubusercontent.com/81360154/210087498-0cb29118-27d3-497d-bcf3-1ce43983dc2e.png)
root node의 key들을 전부 순회하고 찾는 key인 14가 7과 15사이에 들어가므로 사이에 있는 포인터로 이동

![image](https://user-images.githubusercontent.com/81360154/210087589-41c61ead-c815-4bd4-a14d-9edc074958e2.png)
포인터가 가리킨 노드의 key인 9,11을 전부 순회하고 찾는 키가 11보다 크므로 11오른쪽의 포인터로 이동

![image](https://user-images.githubusercontent.com/81360154/210087690-df6e7b7f-927e-42fe-9b91-1f51ad0a7bdd.png)
포인터가 가리킨 노드로 내려가 key순회중 찾는 key검색 완료

실제 데이터베이스에선 한 노드에 많은 key가 존재할 수 있으므로 binary serach등의 알고리즘을 이용해 효율적으로 찾을 수 있다.

### B-Tree 삽입
B-Tree는 오름차순과 자식 노드의 개수가 본인 노드 key개수의 +1 인것, 모든 leaf 노드의 level이 같음을 유지해야한다.<br>
이를 고려해 데이터를 삽입하는 과정은 다음과 같다.<br>


1. 빈 트리인경우 입력데이터를 root node로 한다.
2. root node가 가득찼을 경우 분할해 Leaf node를 생성 *eg) 3차 B-Tree에서 [8,9,10]가 입력으로 들어올경우 [8]-[9]-[10]로 분할 leaf:8,10 root:9
3. 데이터가 들어갈 자리를 검색을 통해 구한다.
4. 데이터가 들어갈 leaf node에 자리가 남아있다면 정렬을 유지하도록 데이터를 삽입한다.
5. 데이터가 들어갈 leaf node에 자리가 없다면 데이터를 삽입후 해당 node를 분할한다.
6. 분할은 해당 node의 중앙값을 기준으로 중앙값은 부모 node로합쳐지거나 해당 노드가 root노드인경우 새로운 root node로 생성된다.
7. 중앙값을 기준으로 분할전 중앙값의 왼쪽 데이터는 분할후의 왼쪽 포인터가 오른쪽 데이터는 오른쪽 포인터가 가리키게 된다.
8. 균형을 유지할 때까지 6,7 반복

![image](https://user-images.githubusercontent.com/81360154/210090311-bf41c6e6-dbf8-46ab-a546-d6900506de81.png)
검색을 통해 데이터가 들어갈 노드를 찾는다.
![image](https://user-images.githubusercontent.com/81360154/210090320-32a55f1a-0f71-4bf3-8fe0-7255ca9eef9b.png)
정렬을 유지하도록 적절한 자리에 데이터를 넣는다.
![image](https://user-images.githubusercontent.com/81360154/210090330-063b7f61-8ab6-467d-9fd0-f637b8ec9369.png)
데이터를 넣은 노드가 꽉차있으므로 분할한다.
![image](https://user-images.githubusercontent.com/81360154/210090335-519700e5-4562-4b33-8ad8-1c1176fbf4f7.png)
분할후 중앙값이였던 13의 왼쪽포인터는 분할전 왼쪽 데이터였던 12를 오른쪽 포인터는 14를 가리킨다.
![image](https://user-images.githubusercontent.com/81360154/210090516-19c90762-93e7-49dc-956f-27c9f60b7279.png)
분할후에도 부모노드의 균형이 맞지않으므로 한번더 분할
![image](https://user-images.githubusercontent.com/81360154/210090531-ab7028bf-acc7-4abd-8aa9-0cdf14c26485.png)
한번더 분할후에도 균형이 맞지않으므로 한번더 분할
![image](https://user-images.githubusercontent.com/81360154/210090538-9fe5e333-52d7-4898-977e-fea4cb4e7a26.png)
분할한 노드가 root node였으므로 중앙값은 부모노드에 합쳐지는 것이 아닌 새로운 root node로 생성

### B-Tree 삭제
<hr>
M차 B-Tree에서 노드의 key의 최소 개수는 floor(M/2)개 이다

1. 삭제할 key가 leaf node에 있는 경우
   1. 현재 node의 key개수가 최소보다 큰 경우
   2. 현재 node의 key개수가 최소이고 왼쪽 또는 오른쪽에 있는 형제 node의 key수가 최소보다 큰 경우
   3. 현재 node와 왼쪽, 오른쪽 형제 node의 key수가 최소이고, 부모 node의 key수가 최소보다 큰 경우
   4. 현재 node와 왼쪽,오른쪽,부모 node의 key수가 전부 최소인 경우
2. 삭제할 Key가 leaf node를 제외한 node에 있는 경우
    1. 현재 node또는 자식 node의 key수가 최소보다 큰 경우
    2. 현재 node와 자식 node 모두 key 수가 최소인 경우

설명을 위해 몇가지 용어를 임의로 정하겠다.
Lmax := 현재 node의 왼쪽 자손 중 가장 큰 key<br>
Rmin := 현재 node의 오른쪽 자손 중 가장 작은 key<br>
par := 현재 node를 가리키는 부모 node의 포인터의 오른쪽에 있는 key. 가장 우측에 있는 포인터인 경우 왼쪽에 있는 key<br>
K := 삭제할 key<br>

1-i) 해당 key를 단순히 삭제해도 균형에 문제가 없다.

1-ii) K를 par로 바꾸고, par를 K의 왼쪽 형제 node의 key수가 최소보다 크면 Lmax로 오른쪽 형제의 node의 key수가 최소보다 크면 Rmin으로 바꿔준다.
e.g) K=10 
![image](https://user-images.githubusercontent.com/81360154/210092704-3e34d6cd-1a8b-4109-a543-9d1848bb9cb3.png)

![image](https://user-images.githubusercontent.com/81360154/210092730-3e305a71-9b92-4f52-8e49-6699952489ee.png)
K인 10을 par인 11로 대체
![image](https://user-images.githubusercontent.com/81360154/210092740-38229de0-2a49-43a7-af49-fb7d449dc247.png)
K의 왼쪽 형제노드인 [8]은 최소이므로 오른쪽 형제노드인 [12,14]중 최소값인 12(Rmin)으로 대체
![image](https://user-images.githubusercontent.com/81360154/210092749-44668538-8fd4-41c0-8cbb-b8e511ee6b78.png)
대체해준 Rmin은 삭제

1-iii)
K를 삭제하고, par를 부모 node에서 분할해 오른쪽형제 node와 합쳐준다. 삭제할 key의 포인터가 가장 우측에 있는 포인터였을 경우 왼쪽 형제노드와 합쳐준다.
e.g) K=16
![image](https://user-images.githubusercontent.com/81360154/210093728-8d2b2389-6af5-4565-b3c0-f5586421de93.png)
16삭제
![image](https://user-images.githubusercontent.com/81360154/210093734-9fe8c481-fd6b-4b0f-8a7e-4a758532f101.png)
par인 17을 분할한다. K의 포인터가 가장 우측의 포인터가 아니므로 오른쪽 형제 노드인 19와 par을 합친다.
![image](https://user-images.githubusercontent.com/81360154/210093741-608b70bb-73ae-4c39-93eb-35ef415a88cc.png)
삭제 완료

1-iiii) 2-ii에서 설명

2-i) K의 Lmax또는 Rmin과 바꿔준후 K를 삭제한다
e.g) K=15
![image](https://user-images.githubusercontent.com/81360154/210094099-396b7979-26d5-4a90-8c31-72cdfb75ce53.png)

![image](https://user-images.githubusercontent.com/81360154/210094110-b572bbc7-8684-477c-a82d-e990e3f7337d.png)
K의 Lmax인 14와 교환한다. 이후 K인 15를 삭제한다.

2-ii) 

1. K를 삭제하고 K의 양쪽 자식을 하나로 합친다. 이를 n1이라 하자 
2. K의 par를 K의 형제 노드에 합쳐준다. 이를 n2라 하자. 
3. n2를 k의 형제 노드에 합친다.
4. n1을 n2의 자식으로 둔다.
5. 이후 균형을 맞추기위해 분할을 하거나 n2의 부모 노드를 기준으로 2번으로 돌아가 반복한다.

1-iiii의 경우 아래 사진기준K가 14가아닌 12또는 15일 것
![image](https://user-images.githubusercontent.com/81360154/210102965-a6149403-a747-410a-98b9-3aec32c90fb5.png)

![image](https://user-images.githubusercontent.com/81360154/210102976-df27cbf2-0d40-472b-a0e6-75772a871738.png)

