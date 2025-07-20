#Jeremy Durdel
#Chapter 14 Lab 2
#07/20/2025

from dataclasses import dataclass

@dataclass
class Computer:
    __cpu_speed: int
    __ram_size: int
    __drive_size: int

    @property
    def cpu_speed(self):
        return self.__cpu_speed

    @cpu_speed.setter
    def cpu_speed(self, value):
        self.__cpu_speed = value

    @property
    def ram_size(self):
        return self.__ram_size

    @ram_size.setter
    def ram_size(self, value):
        self.__ram_size = value

    @property
    def drive_size(self):
        return self.__drive_size

    @drive_size.setter
    def drive_size(self, value):
        self.__drive_size = value

def main():
    computer1 = Computer(20, 16, 2000)
    computer2 = Computer(50, 32, 5000)

    print(computer1)
    print(computer2)

if __name__ == "__main__":
    main()