from faker import Faker
fake_data =Faker()
for i in range(1,11):
  print(fake_data.name())
  print(fake_data.email())
  print(fake_data.phone_number())