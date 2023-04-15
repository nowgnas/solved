
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, m, answer, zero, copyZero;
    static int[][] map, copyMap;
    static BufferedReader br;
    static StringTokenizer st;
    static int[] dy = {-1, 0, 1, 0};
    static int[] dx = {0, 1, 0, -1};
    static List<Node> list;
    static int[] matrixIdx;


    static class Node {
        int y, x;

        public Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 0) {
                    list.add(new Node(i, j));
                    zero++;
                }
            }
        } // 입력 끝

        matrixIdx = new int[3];
        answer = Integer.MIN_VALUE;

        comb(0, 0, list);
        System.out.println(answer);
    }

    static void comb(int start, int cnt, List<Node> list) {
        if (cnt == 3) {
            copyMap = new int[n][m];
            copyZero = zero;
            copy(); // 초기 맵 복사
            madeWall(matrixIdx); // 벽 3개 세우기
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (copyMap[i][j] == 2) {
                        bfs(i, j);
                    }
                }
            }
            answer = Math.max(copyZero, answer);
            return;
        }

        for (int i = start; i < list.size(); i++) {
            matrixIdx[cnt] = i;
            comb(i + 1, cnt + 1, list);

        }
    }

    static void madeWall(int[] wall) {
        for (int i = 0; i < 3; i++) {
            Node n = list.get(wall[i]);
            int y = n.y;
            int x = n.x;
            copyMap[y][x] = 1;
            copyZero--;
        }
    }

    static void copy() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                copyMap[i][j] = map[i][j];
            }
        }
    }


    static void bfs(int startY, int startJ) {
        Queue<Node> queue = new ArrayDeque<>();
        queue.offer(new Node(startY, startJ));
        boolean[][] visited = new boolean[n][m];
        visited[startY][startJ] = true;

        while (!queue.isEmpty()) {
            Node cur = queue.poll();
            int cy = cur.y;
            int cx = cur.x;
            for (int i = 0; i < 4; i++) {
                int ny = cy + dy[i];
                int nx = cx + dx[i];
                if (checkRange(ny, nx) && !visited[ny][nx] && copyMap[ny][nx] == 0) {
                    queue.add(new Node(ny, nx));
                    visited[ny][nx] = true;
                    copyMap[ny][nx] = 2;
                    copyZero--;
                }
            }
        }
    }

    static boolean checkRange(int ny, int nx) {
        return ny >= 0 && nx >= 0 && ny < n && nx < m;
    }
}
