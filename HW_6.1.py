import time

class TrafficLight:
    color =  ["Red", "Yellow", "Green"]


    def running(self):
        while True:
            for i in TrafficLight.color:
                if i == TrafficLight.color[2]:
                    TrafficLight.color.reverse()

                elif i == "Yellow":
                    print(i)
                    time.sleep(2)
                else:
                    print(i)
                    time.sleep(7)

trafic = TrafficLight()
trafic.running()