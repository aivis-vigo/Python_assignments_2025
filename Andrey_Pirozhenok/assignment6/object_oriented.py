import random
from abc import ABC, abstractmethod

with open("name_list_generator/names.txt", encoding="utf8") as f:
    data = f.read().splitlines()
    first_names = data[::2]
    last_names = data[1::2]  # Pretend those are surnames


class NameManager:
    def __init__(self, names: list[str]):
        self.names = names

    def pick_name(self) -> str:
        return random.choice(self.names)


class NameGenerator:
    def __init__(self, first_name_manager: NameManager, last_name_manager: NameManager):
        self.first_name_manager = first_name_manager
        self.last_name_manager = last_name_manager

    def generate_name(self):
        first = self.first_name_manager.pick_name()
        last = self.last_name_manager.pick_name()
        return f"{first} {last}"


class StatisticEvaluator(ABC):
    @abstractmethod
    def record(self, x: float): ...

    @abstractmethod
    def finish(self) -> float: ...


class AverageStatistic(StatisticEvaluator):
    def __init__(self):
        self.count = 0.0
        self.sum = 0.0

    def record(self, x: float):
        self.count += 1
        self.sum += x

    def finish(self) -> float:
        return self.sum / self.count


class StatisticEvaluatorFactory(ABC):
    @abstractmethod
    def new(self) -> StatisticEvaluator: ...


class AverageStatisticFactory(StatisticEvaluatorFactory):
    def new(self) -> AverageStatistic:
        return AverageStatistic()


class GradeAggregator:
    def __init__(self, statistic: StatisticEvaluatorFactory):
        self.statistic = statistic

    def aggregate(self, grades) -> float:
        s = self.statistic.new()

        for grade in grades.values():
            s.record(grade)

        return s.finish()


# example usage

first_name_manager = NameManager(first_names)
last_name_manager = NameManager(last_names)
gen = NameGenerator(first_name_manager, last_name_manager)


print(gen.generate_name())
grades = {
    gen.generate_name(): 1,
    gen.generate_name(): 2,
    gen.generate_name(): 3,
    gen.generate_name(): 4,
    gen.generate_name(): 5,
    gen.generate_name(): 6,
    gen.generate_name(): 7,
    gen.generate_name(): 8,
    gen.generate_name(): 9,
    gen.generate_name(): 10,
}
print(grades)


aggregator = GradeAggregator(AverageStatisticFactory())

print(aggregator.aggregate(grades))
