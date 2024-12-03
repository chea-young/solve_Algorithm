import java.io.*;
import java.util.StringTokenizer;

/**
 *  N개 도시
 *  M개 노선 수
 *
 *  A 시작도시
 *  B 도착도시
 *  C 버스를 타고 이동하는데 걸리는 시간
 *  - C = 0 순간이동을 하는 경우
 *  - C < 0 타임머신으로 시간을 되돌아가는 경우
 *
 *  결과: 1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간
 *  - 어떤 도시로 가는 과정에 무한히 오래 전으로 되돌리수 있는 경우 -1
 *  - N-1걸려 1번도시에서 가느 가장 빠른 시간
 *  - 해당 도시로 가는 경로가 없다면 -1
 *
 * 1. 최단 거리 테이블을 초기화 시킨다.
 * 2. 1번 도시를 출발 노드로 설정하고 N-1번의 반복을 돌려 벨만포드 알고리즘을 이용하여 각 도시로 가는 최단 거리를 갱신한다.
 * 3. 마지막으로 N번쩨 탐색에서 음수 순환의 존재 여부를 파악한다.
 *  1. 값이 작아진 경로가 있다면 해당 경로는 음수 간선이 포함된 싸이클로 음수 무한대로 수렴하기 때문에 경로가 없다고 간주한다.
 *  2. 음수 순환이 없으면, 최단 거리 테이블을 조회하여 초기값이 갱신되지 않은 도시는 경로가 없으므로 -1, 그 외에는 최단거리를 출력해준다.
 */

class City {
    int startCity;
    int endCity;
    int time;

    public City(int startCity, int endCity, int time) {
        this.startCity = startCity;
        this.endCity = endCity;
        this.time = time;
    }
}

class BellmanfordResult {
    boolean result; // 순환 여부
    long[] dist;

    public BellmanfordResult(boolean result, long[] dist) {
        this.result = result;
        this.dist = dist;
    }
}

public class Main {
    private static final int INF = Integer.MAX_VALUE;
    private static final int START_BUS_NUM = 1;

    static int N; // 도시의 개수
    static int M; // 버스 노선의 개수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        City[] information = new City[M]; // 인접 리스트

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int startCity = Integer.parseInt(st.nextToken());
            int endCity = Integer.parseInt(st.nextToken());
            int time = Integer.parseInt(st.nextToken());

            information[i] = new City(startCity, endCity, time);
        }

        // 밸만포드 확인
        BellmanfordResult bellmanfordResult = bellmanford(information);
        long[] dist = bellmanfordResult.dist;
        if(bellmanfordResult.result) { // 음수 순환 존재하면 -1 출력
            System.out.println(-1);
        }
        else { // 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단거리 출력
            for(int i=2; i<N+1; i++) {
                if(dist[i] == INF) { // 도달할 수 없으면 -1
                    System.out.println("-1");
                }
                else { // 최단 거리 출력
                    System.out.println(dist[i]);
                }
            }
        }

    }

    public static BellmanfordResult bellmanford(City[] information) {
        // 최단 거리 테이블 초기화
        long[] dist = initializeDist();

        dist[START_BUS_NUM] = 0; dist[1] = 0;

        // 매 반복마다 모든 간선을 확인
        for(int i=1; i<N+1; i++) {
            for(int j=0; j<M; j++) {
                int cur = information[j].startCity; 1
                int next = information[j].endCity; 3
                int cost = information[j].time; 4

                if(dist[cur] == INF) { // 아직 탐색해본 적이 없는 위치
                    continue;
                }

                // 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 짧은 경우
                if(dist[next] > (dist[cur] + cost)) {
                    dist[next] = dist[cur] + cost;

                    // N번째 값이 갱신된다면 음수 순환 존재
                    if (i == N) {
                        return new BellmanfordResult(true, dist);
                    }
                }
            }
        }

        return new BellmanfordResult(false, dist);
    }

    /**
     * 최단 거리 리스트 생성 함수
     * @return 초기화된 최단 거리 리스트
     */
    public static long[] initializeDist() {
        long[] dist = new long[N+1]; // 최단 거리 테이블
        for (int i = 0; i < N+1; i++) {
            dist[i] = INF;
        }

        return dist;
    }
}
