import random
import time

class rainsensor:
    def init(self):
        self.max_range = 1023
        self.min_range = 188
        self.set_value = None
        n = None


    def start(self):
        x = self.getValue()
        self.update(x)
    

    def update(self,x):
        self.value = x
        self.rain_measure(x)


    def getValue(self):
        n = random.randint(188,1023)
        return n


    def rain_measure(self,set_value): 
        print(f'the measurement of rain is:{set_value} mm')
        if(set_value>187 and set_value<201):
             print("more rain")
        elif(set_value>202 and set_value<350):
            print("normal rain") 
        else:
            print("no rain")


    def stop(self):
        pass

    if __name__ == '__main__':
        rain =  rainsensor()
        for i in range(10):
            print(time.ctime())
            rain.start()
            time.sleep(7)