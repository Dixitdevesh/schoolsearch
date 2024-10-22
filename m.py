import json

# Sample Data
colleges_data = [
    {"college_id": "C001", "name": "ABC Engineering College", "stream": "Science", "subject_choice": "Engineering", "fee_structure": 50000, "location": "City A", "contact": "1234567890", "admission_process": "Entrance Exam", "eligibility": "10+2 with Physics, Chemistry, Mathematics"},
    {"college_id": "C002", "name": "XYZ Business School", "stream": "Commerce", "subject_choice": "MBA", "fee_structure": 30000, "location": "City B", "contact": "0987654321", "admission_process": "Interview", "eligibility": "Graduation in any field"},
    {"college_id": "C003", "name": "PQR Arts College", "stream": "Arts", "subject_choice": "Fine Arts", "fee_structure": 25000, "location": "City C", "contact": "1122334455", "admission_process": "Portfolio Review", "eligibility": "10+2 with any stream"},
    {"college_id": "C004", "name": "DEF Medical College", "stream": "Science", "subject_choice": "MBBS", "fee_structure": 80000, "location": "City D", "contact": "2233445566", "admission_process": "NEET Exam", "eligibility": "10+2 with Physics, Chemistry, Biology"},
    {"college_id": "C005", "name": "LMN IT College", "stream": "Science", "subject_choice": "Computer Science", "fee_structure": 60000, "location": "City E", "contact": "3344556677", "admission_process": "Entrance Exam", "eligibility": "10+2 with Mathematics"},
]

schools_data = [
    {"school_id": "S001", "name": "Greenwood High School", "stream": "Science", "subject_choice": "Biology", "fee_structure": 20000, "location": "City F", "contact": "4455667788", "admission_process": "Application Form", "eligibility": "Completion of Class 10"},
    {"school_id": "S002", "name": "Blue Ridge Academy", "stream": "Commerce", "subject_choice": "Accountancy", "fee_structure": 15000, "location": "City G", "contact": "5566778899", "admission_process": "Entrance Test", "eligibility": "Completion of Class 10"},
    {"school_id": "S003", "name": "Sunshine International School", "stream": "Arts", "subject_choice": "Literature", "fee_structure": 12000, "location": "City H", "contact": "6677889900", "admission_process": "Interview", "eligibility": "Completion of Class 10"},
    {"school_id": "S004", "name": "Riverside High School", "stream": "Science", "subject_choice": "Physics", "fee_structure": 22000, "location": "City I", "contact": "7788990011", "admission_process": "Application Form", "eligibility": "Completion of Class 10"},
    {"school_id": "S005", "name": "Mountain View School", "stream": "Commerce", "subject_choice": "Business Studies", "fee_structure": 18000, "location": "City J", "contact": "8899001122", "admission_process": "Entrance Test", "eligibility": "Completion of Class 10"},
]

feedback_data = []

# ANSI escape sequences for colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def collect_student_data():
    print(Colors.HEADER + "=== Enter Student Details ===" + Colors.ENDC)
    roll_no = input(Colors.OKCYAN + "Roll No: " + Colors.ENDC )
    name = input(Colors.OKCYAN + "Name: " + Colors.ENDC)
    father_name = input(Colors.OKCYAN + "Father's Name: " + Colors.ENDC)
    mother_name = input(Colors.OKCYAN + "Mother's Name: " + Colors.ENDC)
    class_ = input(Colors.OKCYAN + "Class: " + Colors.ENDC)
    previous_school = input(Colors.OKCYAN + "Previous School: " + Colors.ENDC)
    
    while True:
        try:
            marks = float(input(Colors.OKCYAN + "Marks: " + Colors.ENDC))
            if marks < 0 or marks > 100:
                raise ValueError("Marks should be between 0 and 100.")
            break
        except ValueError as e:
            print(Colors.FAIL + f"Invalid input: {e}. Please enter valid marks." + Colors.ENDC)
    
    stream = input(Colors.OKCYAN + "Stream (e.g., Science, Commerce, Arts): " + Colors.ENDC)
    subject_choice = input(Colors.OKCYAN + "Subject Choice: " + Colors.ENDC)

    student_data = {
        "roll_no": roll_no,
        "name": name,
        "father_name": father_name,
        "mother_name": mother_name,
        "class_": class_,
        "previous_school": previous_school,
        "marks": marks,
        "stream": stream,
        "subject_choice": subject_choice
    }

    return student_data

def store_student_data(student_data):
    with open('students.json', 'a') as file:
        json.dump(student_data, file)
        file.write("\n")
    print(Colors.OKGREEN + "Student registered successfully!" + Colors.ENDC)

def suggest_colleges_or_schools(student_data):
    stream = student_data["stream"]
    subject_choice = student_data["subject_choice"]

    print(Colors.HEADER + "\nSuggested Colleges:" + Colors.ENDC)
    found_college = False
    for college in colleges_data:
        if college["stream"] == stream and college["subject_choice"] == subject_choice:
            found_college = True
            print(Colors.OKBLUE + f"Name: {college['name']}, Fee: {college['fee_structure']}, Admission Process: {college['admission_process']}, Location: {college['location']}, Contact: {college['contact']}, Eligibility: {college['eligibility']}" + Colors.ENDC)

    if not found_college:
        print(Colors.FAIL + "No colleges found matching your preferences." + Colors.ENDC)

    print(Colors.HEADER + "\nSuggested Schools:" + Colors.ENDC)
    found_school = False
    for school in schools_data:
        if school["stream"] == stream and school["subject_choice"] == subject_choice:
            found_school = True
            print(Colors.OKBLUE + f"Name: {school['name']}, Fee: {school['fee_structure']}, Admission Process: {school['admission_process']}, Location: {school['location']}, Contact: {school['contact']}, Eligibility: {school['eligibility']}" + Colors.ENDC)

    if not found_school:
        print(Colors.FAIL + "No schools found matching your preferences." + Colors.ENDC)

def apply_to_institution(institution_name, student_roll):
    # Storing application data to file
    with open('applications.json', 'a') as file:
        json.dump({"student_roll": student_roll, "institution_name": institution_name}, file)
        file.write("\n")
    print(Colors.OKGREEN + f"You have applied to {institution_name}. Please follow the admission process." + Colors.ENDC)

def check_application_status(student_roll):
    print(Colors.HEADER + "Checking application status..." + Colors.ENDC)
    found = False
    with open('applications.json', 'r') as file:
        applications = file.readlines()
        for application in applications:
            application_data = json.loads(application.strip())
            if application_data["student_roll"] == student_roll:
                found = True
                print(Colors.OKBLUE + f"Application for Roll No {student_roll} found." + Colors.ENDC)
                return
    if not found:
        print(Colors.FAIL + f"No applications found for Roll No {student_roll}." + Colors.ENDC)

def search_institutions():
    print(Colors.HEADER + "Search for Colleges/Schools" + Colors.ENDC)
    criteria = input(Colors.OKCYAN + "Enter stream or subject choice to search (e.g., Science, MBA): " + Colors.ENDC)
    
    print(Colors.HEADER + "\nSearch Results for Colleges:" + Colors.ENDC)
    found_college = False
    for college in colleges_data:
        if criteria.lower() in college["stream"].lower() or criteria .lower() in college["subject_choice"].lower():
            found_college = True
            print(Colors.OKBLUE + f"Name: {college['name']}, Fee: {college['fee_structure']}, Admission Process: {college['admission_process']}, Location: {college['location']}, Contact: {college['contact']}, Eligibility: {college['eligibility']}" + Colors.ENDC)

    if not found_college:
        print(Colors.FAIL + "No colleges found matching your search." + Colors.ENDC)

    print(Colors.HEADER + "\nSearch Results for Schools:" + Colors.ENDC)
    found_school = False
    for school in schools_data:
        if criteria.lower() in school["stream"].lower() or criteria.lower() in school["subject_choice"].lower():
            found_school = True
            print(Colors.OKBLUE + f"Name: {school['name']}, Fee: {school['fee_structure']}, Admission Process: {school['admission_process']}, Location: {school['location']}, Contact: {school['contact']}, Eligibility: {school['eligibility']}" + Colors.ENDC)

    if not found_school:
        print(Colors.FAIL + "No schools found matching your search." + Colors.ENDC)

def view_all_institutions():
    print(Colors.HEADER + "View All Colleges:" + Colors.ENDC)
    for college in colleges_data:
        print(Colors.OKBLUE + f"Name: {college['name']}, Fee: {college['fee_structure']}, Admission Process: {college['admission_process']}, Location: {college['location']}, Contact: {college['contact']}, Eligibility: {college['eligibility']}" + Colors.ENDC)

    print(Colors.HEADER + "\nView All Schools:" + Colors.ENDC)
    for school in schools_data:
        print(Colors.OKBLUE + f"Name: {school['name']}, Fee: {school['fee_structure']}, Admission Process: {school['admission_process']}, Location: {school['location']}, Contact: {school['contact']}, Eligibility: {school['eligibility']}" + Colors.ENDC)

def filter_institutions():
    print(Colors.HEADER + "Filter Institutions by Fee Structure or Location" + Colors.ENDC)
    criteria = input(Colors.OKCYAN + "Enter fee structure or location to filter (e.g., 50000, City A): " + Colors.ENDC)
    
    print(Colors.HEADER + "\nFiltered Results for Colleges:" + Colors.ENDC)
    found_college = False
    for college in colleges_data:
        if str(college["fee_structure"]) == criteria or college["location"] == criteria:
            found_college = True
            print(Colors.OKBLUE + f"Name: {college['name']}, Fee: {college['fee_structure']}, Admission Process: {college['admission_process']}, Location: {college['location']}, Contact: {college['contact']}, Eligibility: {college['eligibility']}" + Colors.ENDC)

    if not found_college:
        print(Colors.FAIL + "No colleges found matching your filter." + Colors.ENDC)

    print(Colors.HEADER + "\nFiltered Results for Schools:" + Colors.ENDC)
    found_school = False
    for school in schools_data:
        if str(school["fee_structure"]) == criteria or school["location"] == criteria:
            found_school = True
            print(Colors.OKBLUE + f"Name: {school['name']}, Fee: {school['fee_structure']}, Admission Process: {school['admission_process']}, Location: {school['location']}, Contact: {school['contact']}, Eligibility: {school['eligibility']}" + Colors.ENDC)

    if not found_school:
        print(Colors.FAIL + "No schools found matching your filter." + Colors.ENDC)

def leave_feedback(institution_name, feedback):
    feedback_data.append({"institution_name": institution_name, "feedback": feedback})
    with open('feedback.json', 'w') as file:
        json.dump(feedback_data, file)
    print(Colors.OKGREEN + f"Feedback for {institution_name} submitted successfully!" + Colors.ENDC)

def view_feedback(institution_name):
    print(Colors.HEADER + "Viewing Feedback for", institution_name + Colors.ENDC)
    found = False
    for feedback in feedback_data:
        if feedback["institution_name"] == institution_name:
            found = True
            print(Colors.OKBLUE + feedback["feedback"] + Colors.ENDC)
    if not found:
        print(Colors.FAIL + "No feedback found for", institution_name + Colors.ENDC)

def main():
    while True:
        print(Colors.HEADER + "\nWelcome to the College/School Finder System!" + Colors.ENDC)
        print(Colors.OKCYAN + "1. Register Student" + Colors.ENDC)
        print(Colors.OKCYAN + "2. Search for Colleges/Schools" + Colors.ENDC)
        print(Colors.OKCYAN + "3. Suggest Colleges/Schools" + Colors.ENDC)
        print(Colors.OKCYAN + "4. Apply to College/School" + Colors.ENDC)
        print(Colors.OKCYAN + "5. Check Application Status" + Colors.ENDC)
        print(Colors.OKCYAN + "6. View All Institutions" + Colors.ENDC)
        print(Colors.OKCYAN + "7. Filter Institutions" + Colors.ENDC)
        print(Colors.OKCYAN + "8. Leave Feedback" + Colors.ENDC)
        print(Colors.OKCYAN + "9. View Feedback" + Colors.ENDC)
        print(Colors.OKCYAN + "10. Exit" + Colors.ENDC)
        
        choice = input(Colors.OKCYAN + "Choose an option: " + Colors.ENDC)
        
        if choice == '1':
            student_data = collect_student_data()
            store_student_data(student_data)
            print(Colors.OKGREEN + "Student registered successfully!" + Colors.ENDC)
        elif choice == '2':
            search_institutions()
        elif choice == '3':
            roll_no = input(Colors.OKCYAN + "Enter your Roll No: " + Colors.ENDC)
            found = False
            with open('students.json', 'r') as file:
                students = file.readlines()
                for student in students:
                    student_data = json.loads(student.strip())
                    if student_data["roll_no"] == roll_no:
                        found = True
                        suggest_colleges_or_schools(student_data)
                        break
            if not found:
                print(Colors.FAIL + "Student not found." + Colors.ENDC)
        elif choice == '4':
            institution_name = input(Colors.OKCYAN + "Enter the College/School Name you want to apply to: " + Colors.ENDC)
            roll_no = input(Colors.OKCYAN + "Enter your Roll No: " + Colors.ENDC)
            apply_to_institution(institution_name, roll_no)
        elif choice == '5':
            roll_no = input(Colors.OKCYAN + "Enter your Roll No to check application status: " + Colors.ENDC)
            check_application_status(roll_no)
        elif choice == '6':
            view_all_institutions()
        elif choice == '7':
            filter_institutions()
        elif choice == '8':
            institution_name = input(Colors.OKCYAN + "Enter the College/School Name to leave feedback for: " + Colors.ENDC)
            feedback = input(Colors.OKCYAN + "Enter your feedback: " + Colors.ENDC)
            leave_feedback(institution_name, feedback)
        elif choice == '9':
            institution_name = input(Colors.OKCYAN + "Enter the College/School Name to view feedback for: " + Colors.ENDC)
            view_feedback(institution_name)
        elif choice == '10':
            print(Colors.OKGREEN + "Exiting... Thank you for using the system!" + Colors.ENDC)
            break
        else:
            print(Colors.FAIL + "Invalid choice. Please try again." + Colors.ENDC)

if __name__ == "__main__":
    main()