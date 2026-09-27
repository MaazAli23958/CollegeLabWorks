import collections

def write_data():
    # Write department data
    num_depts = int(input("Enter number of departments: "))
    with open("departments.txt", "w") as dept_file:
        for _ in range(num_depts):
            did = input("Enter Department ID: ").strip()
            dname = input("Enter Department Name: ").strip()
            dloc = input("Enter Department Location: ").strip()
            dept_file.write(f"{did},{dname},{dloc}\n")

    # Write employee data
    num_emps = int(input("\nEnter number of employees: "))
    with open("employees.txt", "w") as emp_file:
        for _ in range(num_emps):
            name = input("Enter Employee Name: ").strip()
            eid = input("Enter Employee ID: ").strip()
            salary = input("Enter Employee Salary: ").strip()
            did = input("Enter Department ID: ").strip()
            emp_file.write(f"{name},{eid},{salary},{did}\n")

    print("\nData has been saved to 'departments.txt' and 'employees.txt'.")

def calculate_avg_salary():
    try:
        # Load departments into a dictionary
        dept_names = {}
        with open("departments.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 2:
                    dept_id = parts[0]
                    dept_names[dept_id] = parts[1]

        # totals --> Keeps sum of all salaries for each department
        totals = {}
        #counts --> Keeps number of employees in each department
        counts = {}

        with open("employees.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 4:
                    salary = int(parts[2])
                    dept_id = parts[3]

                    totals[dept_id] = totals.get(dept_id, 0) + salary
                    counts[dept_id] = counts.get(dept_id, 0) + 1

        # Print average salary per department
        print("\nAverage Salary Report:")
        for dept_id in totals:
            avg = totals[dept_id] / counts[dept_id]
            name = dept_names.get(dept_id, "Unknown Department")
            print(f"{name} (ID {dept_id}): ₹{avg:.2f}")

    except FileNotFoundError:
        print("Missing file: Please run the data input first.")
    except Exception as e:
        print("Error:", e)


# Run the program
write_data()
calculate_avg_salary()