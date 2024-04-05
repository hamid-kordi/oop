from abc import abstractmethod, ABC
import random
import string


class abstract(ABC):
    @abstractmethod
    def generate(self):
        pass


class RandomInt(abstract):

    def generate(self):
        count = ""
        for i in range(20):
            temp = random.randint(0, 9)
            count = str(temp) + count
        return int(count)


class RandomStr(abstract):

    def generate(self):
        length = 20
        generated_string = "".join(
            random.choice(string.ascii_uppercase) for _ in range(length)
        )

        return generated_string


class RandomStrInt(abstract):

    def generate(self):
        length = 10
        generated_string = "".join(
            random.choice(string.ascii_uppercase) for _ in range(length)
        )

        for i in range(10):
            temp = str(random.randint(0, 9))
            generated_string = str(temp) + generated_string
            ls_generate = list(generated_string)

        indices = list(range(len(ls_generate)))
        random.shuffle(indices)
        ls_generate = [ls_generate[i] for i in indices]
        generated_string = "".join(ls_generate)
        return generated_string


obj1 = RandomInt()
print(obj1.generate())

obj2 = RandomStr()
print(obj2.generate())


obj3 = RandomStrInt()
print(obj3.generate())
