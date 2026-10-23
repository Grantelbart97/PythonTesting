from testing_course.exploration.calculator import Calculator
from testing_course.exploration.person_repository import InMemoryPersonRepository
from testing_course.exploration.person_service import PersonService

calc = Calculator()
calc.add(1, 2)
total: float = calc.multiply(2, 3)

repo = InMemoryPersonRepository()
service = PersonService(repo)
service.register("Alice", 30)

person = repo.read_person_by_id(0)
if person is not None:
    print(person.name)
