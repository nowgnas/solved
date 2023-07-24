import java.util.HashMap;
import java.util.Map;

class dot {
    boolean[] visited;

    public dot() {
        this.visited = new boolean[]{false, false, false, false};
    }
}
class Solution {
    static int[] dy = {-1, 0, 1, 0};
    static int[] dx = {0, 1, 0, -1};

    public int solution(String dirs) {
        int answer = 0;
        Map<String, Integer> map = new HashMap<>();
        map.put("U", 0);
        map.put("R", 1);
        map.put("D", 2);
        map.put("L", 3);
        dot[][] maps = new dot[11][11];
        for (int r = 0; r < maps.length; r++) {
            for (int c = 0; c < maps[0].length; c++) {
                maps[r][c] = new dot();
            }
        }
        int start_y = 11 / 2;
        int start_x = 11 / 2;

        String[] split = dirs.split("");
        for (String item :
                split) {
            int ny = start_y + dy[map.get(item)];
            int nx = start_x + dx[map.get(item)];
            if (checkRange(ny, nx, 11)) {
                if (!maps[start_y][start_x].visited[map.get(item)]) {
                    answer += 1;
                }
                maps[start_y][start_x].visited[map.get(item)] = true;
                int n_road = (map.get(item) + 2) % 4;
                maps[ny][nx].visited[n_road] = true;
                start_y = ny;
                start_x = nx;
            }
        }

        return answer;
    }

    private boolean checkRange(int ny, int nx, int i) {
        return 0 <= ny && 0 <= nx && ny < i && nx < i;
    }
}