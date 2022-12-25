# Hive
hive는 기존 java로 mr을 구현해 업무를 하는 것이 복잡하고 귀찮아서 익숙한 sql을 빅데이터에서 사용할 수 있게 하기위해 시작한 프로젝트이다.<br>
현재 오픈소스 프로젝트이며 빅데이터의 가장 대표적인 SQL on Hadoop이다.<br>
![image](https://user-images.githubusercontent.com/81360154/209296926-0625f2c7-e3ec-416b-b038-8f176ac92ed4.png)

### UI
<hr>
CLI, JDBC와 같은 UI들로 사용자가 작업을 수행 할수 있는 인터페이스를 제공한다.

### Driver
<hr>
세션을 생성해 쿼리문을 실행하고 progress와 라이프사이클을 모니터링한다.<br>
쿼리문에 의해 생성되는 메타데이터를 저장하고, 

### Compiler
<hr>
metastore를 참고해 쿼리 구문을 abstract syntax tree(AST)로 변환하고, 호환성과 컴파일 타임 에러 확인 후 directed acyclic graph(DAG)로 변환한다.<br>
논리적, 물리적 플랜을 기반으로 최적화를 진행한다.

### Metastore
<hr>
각 테이블의 스키마, 위와 같은 메타데이터를 관리한다.<br>
파티션 메타데이터를 통해 드라이버가 클러스터에 분산된 다양한 데이터 셋의 progress를 트래킹하도록 돕는다.

### Execution Engine
<hr>
컴파일러에 의해 생성된 실행 계획을 실행한다.
