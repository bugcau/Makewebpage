import pandas as pd
from faker import Faker
import random

class PersonalData:
    def __init__(self, name, id_number, birth_date, other_info=None):
        self.name = name
        self.id_number = id_number
        self.birth_date = birth_date
        self.other_info = other_info if other_info is not None else {}

    def __repr__(self):
        return f"PersonalData(name={self.name}, id_number={self.id_number}, birth_date={self.birth_date}, other_info={self.other_info})"

    def add_other_info(self, key, value):
        self.other_info[key] = value

    def get_info(self):
        info = {
            "name": self.name,
            "id_number": self.id_number,
            "birth_date": self.birth_date,
        }
        info.update(self.other_info)
        return info

def calculate_check_digit(rrn):
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    sum_val = sum(int(a) * b for a, b in zip(rrn, weights))
    remainder = (11 - (sum_val % 11)) % 10
    return remainder

def generate_rrn(birth_date, gender_code):
    rrn = birth_date.strftime('%y%m%d') + str(gender_code)
    rrn += ''.join(str(random.randint(0, 9)) for _ in range(5))
    check_digit = calculate_check_digit(rrn)
    return rrn + str(check_digit)

def generate_fake_personal_data(fake):
    name = fake.name()
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90)
    gender_code = random.choice([1, 2]) if birth_date.year < 2000 else random.choice([3, 4])
    id_number = generate_rrn(birth_date, gender_code)
    birth_date_str = birth_date.strftime('%Y-%m-%d')
    other_info = {
        "address": fake.address(),
        "phone": fake.phone_number(),
        "email": fake.email()
    }
    return {
        "name": name,
        "id_number": id_number,
        "birth_date": birth_date_str,
        "address": other_info["address"],
        "phone": other_info["phone"],
        "email": other_info["email"]
    }

# Faker 객체 생성
fake = Faker('ko_KR')

# 100,000개의 무작위 개인정보 데이터 생성
data = [generate_fake_personal_data(fake) for _ in range(100000)]

# 데이터프레임으로 변환
df = pd.DataFrame(data)

# CSV 파일로 저장
csv_path = "개인정보생성.csv"
df.to_csv(csv_path,encoding="euc-kr" ,index=False)
