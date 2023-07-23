class dot:
    # 지도 좌표 한 점에서 상하좌우 길 지났는지 표시  
    def __init__(self):
        self.dir = [False for _ in range(4)]


# 지도 범위 체크 
def check_range(ny, nx, param):
    return ny >= 0 and nx >= 0 and ny < param and nx < param


def solution(dirs):
    answer = 0
    # 상우하좌 순서로 명령어 인덱스로 처리 
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    command = {
        'U': 0,
        'R': 1,
        'D': 2,
        'L': 3
    }
    # dot 클래스를 이용해 지도 좌표 만들기 
    maps = [[dot() for _ in range(11)] for _ in range(11)]
    # 시작 점 5,5로 만들어 주기 
    start_y = 11 // 2
    start_x = 11 // 2

    # 명령어 수행 
    for word in dirs:
        # 다음 갈 점 찾기 command 딕셔너리로 다음 좌표 한번에 찾기 
        ny = start_y + dy[command[word]]
        nx = start_x + dx[command[word]]
        # 범위 체크 
        if check_range(ny, nx, 11):
            # 다음 갈 점에서 현재 점을 바라보는 방향도 처리해 줘야 함
            n_road = (command[word] + 2) % 4
            # 현재 점에서 보는 방향이나 다음 점에서 현재 점 보는 방향 중 하나만 확인 
            if not maps[ny][nx].dir[n_road]:
                # 간 적 없으면 +1
                answer += 1
            # 방문 여부 갱신 - 방문 여부 상관 없이 지나면 True 
            maps[ny][nx].dir[n_road] = True
            maps[start_y][start_x].dir[command[word]] = True
            # 현재 점 좌표 갱신 
            start_y = ny
            start_x = nx
    return answer
