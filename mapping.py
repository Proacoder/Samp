employees = [
    {"name": "A", "salary": 30000},
    {"name": "B", "salary": 50000},
    {"name": "C", "salary": 40000},
    {"name": "D", "salary": 60000}
]

# 1️⃣ Extract salaries using map
salaries = list(map(lambda e: e["salary"], employees))

# 2️⃣ Find minimum and maximum salary
min_salary = min(salaries)
max_salary = max(salaries)

# 3️⃣ Remove employees with min and max salary using filter
filtered_employees = list(
    filter(lambda e: e["salary"] != min_salary and e["salary"] != max_salary, employees)
)

# 4️⃣ Calculate average salary
remaining_salaries = list(map(lambda e: e["salary"], filtered_employees))
average_salary = sum(remaining_salaries) / len(remaining_salaries)

print("Average Salary:", average_salary)
