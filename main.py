from datetime import datetime


class Data:
    def __init__(self, day: int, year: int, month: int, hour: int, minute: int, second: int):
        self.date_time = datetime(day=day, year=year, month=month, hour=hour, minute=minute, second=second)


class Result(Data):
    @staticmethod
    def offset():
        input_sample1 = input(
            ' Введите данные эталонных значений День/Год/Месяц/Часы/Минуты/Секунды через пробел: ').split()
        iter_input_sample1 = [int(i) for i in input_sample1]
        input_sample2 = input(' Введите данные значений День/Год/Месяц/Часы/Минуты/Секунды через пробел: ').split()
        iter_input_sample2 = [int(i) for i in input_sample2]
        sample1 = Data(iter_input_sample1[0], iter_input_sample1[1], iter_input_sample1[2], iter_input_sample1[3],
                       iter_input_sample1[4], iter_input_sample1[5]).date_time
        sample2 = Data(iter_input_sample2[0], iter_input_sample2[1], iter_input_sample2[2], iter_input_sample2[3],
                       iter_input_sample2[4], iter_input_sample2[5]).date_time
        result = sample1 - sample2
        return result


def run():
    return print(abs(round(Result.offset().total_seconds()) ))


if __name__ == '__main__':
    run()
