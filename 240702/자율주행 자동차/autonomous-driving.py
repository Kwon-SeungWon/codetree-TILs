import math
import sys

class AutoCAR:
    def __init__(self):
        self.size_x = 0
        self.size_y = 0
        self.init_x = 0
        self.init_y = 0
        self.init_direction = 0
        self.maps = []
        self.moving_count = 1

    def input_function(self):
        input_str = input()
        inputs = input_str.split()
        self.inputs = list(map(int, inputs))

    def input_value(self):
        self.input_function()
        self.size_x = self.inputs[0]
        self.size_y = self.inputs[1]

        self.input_function()
        self.init_x = self.inputs[0]
        self.init_y = self.inputs[1]
        self.init_direction = self.inputs[2]
        
        # 방문 여부
        self.visited = [[False] * self.size_y for _ in range(self.size_x)]

        # 현재 방향
        self.current_direction = self.init_direction
        self.current_position_x = self.init_x
        self.current_position_y = self.init_y

    def input_map(self):
        for i in range(self.size_x):
            self.input_function()
            row = self.inputs
            self.maps.append(row)
        
    
    def turning_around(self):
        dp_x = [-1, 0, 1, 0]
        dp_y = [0, 1, 0, -1] 

        self.visited[self.current_position_x][self.current_position_y] = True

        while True:
            state = False

            for _ in range(4):
                # 왼쪽으로 회전
                self.current_direction = (self.current_direction - 1) % 4

                # 새로운 위치 계산
                new_x = self.current_position_x + dp_x[self.current_direction]
                new_y = self.current_position_y + dp_y[self.current_direction]

                # 맵의 범위를 벗어나지 않고, 방문하지 않은 곳이라면 이동
                if 0 <= new_x < self.size_x and 0 <= new_y < self.size_y:
                    if not self.visited[new_x][new_y] and self.maps[new_x][new_y] == 0:
                        self.current_position_x = new_x
                        self.current_position_y = new_y
                        self.visited[new_x][new_y] = True
                        self.moving_count += 1
                        state = True
                        break

            if not state:
                back_direction = (self.current_direction + 2) % 4

                # 새로운 위치 계산
                new_x = self.current_position_x + dp_x[back_direction]
                new_y = self.current_position_y + dp_y[back_direction]

                if self.maps[new_x][new_y] == 1:
                    break

                self.current_position_x = new_x
                self.current_position_y = new_y

        return self.moving_count
        
    
if __name__ == "__main__":
    autocar = AutoCAR()
    autocar.input_value()
    autocar.input_map()

    result = autocar.turning_around()
    print(result)