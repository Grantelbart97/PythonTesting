from testing_course.exploration.calculator import Calculator
from src.testing_course.exploration.person_repository import InMemoryPersonRepository

calc = Calculator()
calc.add("1", 2)
calc.add(1)
total: str = calc.multiply(2, 3)

repo = InMemoryPersonRepository()
print(repo.read_person_by_id(0).name)

class HalfRepository:
    def create_person():
        return None
    service = PersonService(HalfRepository())
    service.register("Alice")