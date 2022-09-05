from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
from pygoogle_image import image as pi


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(date.today())
    # извлекает изображения из изображений Google по названию.
    pi.download(keywords='cat', limit=5)
