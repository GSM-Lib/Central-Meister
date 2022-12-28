# MapReduce

MapReduce는 분산처리에서 데이터를 최대한 값싸게 처리 하기 위한 알고리즘이다.

기존 데이터베이에서의 데이터 처리 방식은
1. 데이터를 가져온다.
2. 가져온 데이터를 처리한다.
3. 처리한 데이터를 저장한다.

위와 같이 진행된다.<br>
하지만 이를 데이터가 다 다른곳에 저장 돼있는 분산처리 시스템 환경에서 실행시키기에는 IO비용이 너무 많이든다.<br>

![image](https://user-images.githubusercontent.com/81360154/209764822-1c94171e-0c08-430a-a99c-dc1806a0afa6.png)

##### components : input format, partition & shuffle, sort, reduce, output format

### Input Format
<hr>
- 입력으로 사용될 파일을 정한다.
- 파일을 task로 분해할 InputSplits 을 정의한다.
- 파일을 읽어들이는 RecordReader


InputFormat은 FileInputFormat이라는 이름의abstract type으로 부터 파생된 class이다. 표준 InputFormat은 다음과 같이 3가지가 있다.<br>
TextInputFormat, KeyValueInputFormat, SequenceFileInputFormat<br>

각 format의 key/value는 아래와 같다.<br>
- TextInputFormat: 각 line의 byte offset, 각 line의 내용, default format이다<br>
- KeyValueInputFormat: 첫째 tab 문자까지의 모든 내용, line의 나머지 내용<br>
- SequenceFileInputFormat: 압축되지 않은 파일 타입, 레코드 단위 압축된 파일 타입, 블럭단위 압축된 파일 타입 중 1, 바이너리 형태로 저장해 사람이 볼순 없지만 mapreduce에선 처리하기 편한 format이다.


InputSplits:
InputSplit은 MapReduce 프로그램에서 map task를 구성하는 작업의 단위가 된다.
Dataset에 적용되는 MapReduce 프로그램은 이를 총체적으로 Job이라고 부르며 이 job은 여러 개의 (또는 수 백개의) task로 구성된다. 
Map task는 한 파일의 전체를 읽거나 일부분만을 읽을 수도도 있다.

InputFormat은 mapping 단계에서의 각각의 task의 목록을 정의한다. 
각각의 task는 각각 입력되는 split에 대응된다. 
이들 task는 입력파일의 chunk가 물리적으로 어디에 위치하고 있는지를 기준으로 각 node에 할당된다. 
개별 node마다 수십 개의 task가 할당된다.

RecordReader: 
데이터를 source에서 실제로 적재한 후 이를 Mapper가 읽기에 수월한 (key, value) pair로 변환하는 일은 RecordReader class가 담당한다. 
RecordReader instance는 InputFormat에 의해 정의된다.


### Mapper
<hr>
들어온 key-value쌍의 인풋을 reduce에서 연산하기 적절한 intermediate key-value로 매핑한다.

### OutputCollector object & Reporter object 
outputcollector는 mapper의 산출물을 reducer로 보내준다.<br>
reporters는 현재의 task에 대한 정보를 제공한다. 임의의 counter를 정의할 수도 있다

### Partition & Shuffle
<hr>
어떤 노드에서 map task가 끝나도 다른 노드에서는 아직 끝나지 않았을 수도 있다.
그런 와중에도 결과를 reduce로 전달하기 시작하는데 전달하는 과정을 shuffling한다고 한다.
산출물을 reducer로 전달할때 key에 hash함수를 적용한 값에 따라 reducer로 보내게 되는데, 해당 key space를 partition이라 한다.
key space당 reducer task를 할당하므로 partition 개수와 reduce task개수는 같다.

### Reducer
<hr>
인풋으로 (key, [value,value,value])들어오면 value를 집계해서 결과를 산출한다.

### OutputFormat:
<hr>
위 Input Format과 같은 출력 format이다.
TextOutputFormat, SequenceFileOutputFormat, NullOutputFormat 3종류가 있는데<br>

- TextOutputFormat는 일반적인 key-value쌍으로 default format이다.
- SequenceFileOutputFormat는 Input format의 sequenceFileInputFormat가 deserialize할 수있는 serialization된 형태로 저장한다.
- NullOutputFormat는 아무런 출력파일을 만들지 않으며 OutputCollector에 의해 전달받은 (key, value) pair를 무시한다. 이는 reduce() method에서 독자의 출력파일에 기록하고 Hadoop 프레임워크에 의해 추가의 빈 출력파일이 만들지 않으려는 경우 유용하다.

### RecordWriter
<hr>
InputFormat이 실제로 개별 레코드를 RecordReader 실행을 통해 읽는 것과 마찬가지로 OutputFormat class도 RecordWriter object를
OutputFormat에 지정된 대로,개별 레코드를 파일에 기록하는데 이용된다.

### Combiner
<hr>
위 그림에서 생략된 부분인데 있어도되고 없어도 된다.
combiner는 map에서 reduce로 넘어가는 단계에서 진행되는데 shuffling중에 네트워크 통신 비용을 절감하기위해<br>
map이후 local에서 진행되는 mini-reduce라고 생각하면 된다.
