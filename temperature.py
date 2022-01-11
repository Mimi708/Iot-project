import random
import time


class temp:
    def _init_(self,max_value,min_value,duration,eq={}):
        self.max_value = max_value
        self.min_value = min_value
        self.char_eq  = eq
        self.duration = duration

    def start(self):
        while self.duration:
            yield self.get_output()
            self.duration = self.duration - 1
            time.sleep(1)


    def get_output(self):
        x = random.randint(0,5)
        y =  self.calculate(self.char_eq.get("a"), x, 2) + self.calculate(self.char_eq.get("b"), x, 1) + self.char_eq.get("c")

        if self.__is_low_temp(y) is not None:
            return self.__is_low_temp()
        if self.__is_high_temp(y) is not None:
            return self.__is_high_temp(y)
        return y

    @staticmethod
        
    def calculate(a,x,p):
        return a * (x ** p)
    def __is_low_temp(self,val):
        if val < self.min_value:
            return self.min_value
    def __is_high_temp(self,val):
        if val > self.max_value:
            return self.max_value
        return None


if __name__ == '__main__':
    eq = {
        "a": 2,
        "b": 1,
        "c" : 2,
    }

    sensor = temp(max_value=80,min_value=-80,duration=10,eq=eq)

    get = sensor.start()

    for i in get:
        print(i)