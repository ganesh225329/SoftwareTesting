from faker import Faker
import random

fake = Faker()

departments = [
    "HR",
    "Finance",
    "IT",
    "Marketing",
    "Sales"
]

html = """

<!DOCTYPE html>

<html>

<head>

<title>Employee Table</title>

<style>

table{

border-collapse:collapse;
width:70%;

}

th,td{

border:1px solid black;
padding:10px;
text-align:center;

}

th{

background:lightblue;

}

</style>

</head>

<body>

<h2>Employee Records</h2>

<table id="employeeTable">

<tr>

<th>ID</th>

<th>Name</th>

<th>Department</th>

<th>Salary</th>

</tr>

"""

# Generate 9 random employees
for i in range(1,10):

    html += f"""

<tr>

<td>{i}</td>

<td>{fake.name()}</td>

<td>{random.choice(departments)}</td>

<td>{random.randint(25000,90000)}</td>

</tr>

"""

# Add John Deo
html += """

<tr>

<td>10</td>

<td>John Deo</td>

<td>IT</td>

<td>85000</td>

</tr>

"""

html += """

</table>

</body>

</html>

"""

with open("employee.html","w") as file:

    file.write(html)

print("Employee Table Created Successfully")