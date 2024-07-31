import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker('ko_KR')

# Define the number of rows to generate
num_rows = 10000

# Generate fake data
data = {
    '기준': [fake.date_this_century() for _ in range(num_rows)],
    '이름': [fake.name() for _ in range(num_rows)],
    '휴대폰번호': [fake.phone_number() for _ in range(num_rows)],
    '이메일': [fake.email() for _ in range(num_rows)],
    '집주소': [fake.address() for _ in range(num_rows)],
    '주민번호': [fake.ssn() for _ in range(num_rows)],
    '생년월일': [fake.date_of_birth() for _ in range(num_rows)],
    '직업': [fake.job() for _ in range(num_rows)],
    '카드번호': [fake.credit_card_number() for _ in range(num_rows)],
    '종교': [fake.random_element(elements=('불교', '기독교', '천주교', '무교', '기타')) for _ in range(num_rows)],
    '정치정당': [fake.random_element(elements=('민주당', '국민의힘', '정의당', '기타')) for _ in range(num_rows)],
    '운전면허번호': [fake.license_plate() for _ in range(num_rows)],
    'IP주소': [fake.ipv4() for _ in range(num_rows)],
    '은행계좌번호': [fake.bban() for _ in range(num_rows)],
    '신용카드번호': [fake.credit_card_number() for _ in range(num_rows)],
    '병명(질환)': [fake.random_element(elements=('고혈압', '당뇨병', '천식', '암', '없음')) for _ in range(num_rows)],
    'sns계정': [fake.user_name() for _ in range(num_rows)]
}

# Create DataFrame
df_fake = pd.DataFrame(data)

# Save to CSV
output_path = 'fake_data.csv'
df_fake.to_csv(output_path, index=False, encoding='utf-8-sig')
