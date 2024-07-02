import math

class Restaurant:
    def __init__(self):
        self.count = 0
        self.consumers = []
        self.abilities = []
    
    def getTheInformation(self):
        self.count = int(input())
        self.consumers = list(map(int, input().split()))
        self.abilities = list(map(int, input().split()))
    
    def calculator(self):
        remain_consumers = [0] * self.count
        MBR = [0] * self.count
        Need_person = 0
        # 팀장이 검사하는 인원 (필수)
        for i in range(self.count):
            remain_consumers[i] = self.consumers[i] - self.abilities[0]
            
            if remain_consumers[i] <= 0:
                return self.count;

        for i in range(self.count):
            MBR[i] = math.ceil(remain_consumers[i] / self.abilities[1])
            Need_person += MBR[i]


        # 최종 필요인원 (팀장 + 팀원)
        return (self.count + Need_person)


if __name__ == "__main__":
    restaurant = Restaurant()
    restaurant.getTheInformation()
    print(restaurant.calculator())

    # For debugging
    # print(restaurant.count)
    
    # for consumer in restaurant.consumers:
    #     print(consumer)
    
    # for ability in restaurant.abilities:
    #     print(ability)