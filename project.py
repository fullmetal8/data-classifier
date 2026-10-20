import json
def classify_score(data):
    try:
        score = int(data["score"])
        if score <= 39:
            data["category"] = "poor"
            data["status"] = "failed"
        elif score <= 59:
            data["category"] = "satisfactory"
            data["status"] = "passed"
        elif score <= 79:
            data["category"] = "good"
            data["status"] = "passed"
        else :
            data["category"] = "excellent"
            data["status"] = "passed"

    except (ValueError, TypeError, KeyError):
        print(f"Student {data.get('name', 'No name')} has empty or nonint value for score!")
        data["status"] = "error"
        data["category"] = "Empty or invalid score"

    return data

class DataClassifier():
    def __init__(self, file_path):

        clean_path = file_path.strip().strip("'\"")
        try:
            with open(clean_path, "r", encoding="utf-8") as file:
                self.data = json.load(file)
                print(f"File '{clean_path}' is successfully uploaded!")

        except FileNotFoundError:
            print(f"Error: '{clean_path} is not found!'")
            self.data = []

        except json.JSONDecodeError as e:
            print("Error. Invalid JSON", e)
            self.data = []
            return

        required_fields = ["name", "subject", "score"]
        if isinstance(self.data, list):
            for student in self.data:
                if isinstance(student, dict):
                    missing_fields = [field for field in required_fields if field not in student]
                    if missing_fields:
                        student_name = student.get("name", "No name")
                        print(f"{missing_fields} is required in '{student_name}'")
                        student["status"] = "error"
                        student["category"] = f"Missing: {','.join(missing_fields)}"


        


        
    def save_to_file(self, output_filename="processed_scores.json"):
        with open(output_filename, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)
        print(f"Results with categories are saved in {output_filename}")

    def classify_all(self):
        for student in self.data:
            classify_score(student)



user_input = """[ {"name": "Alim", "subject": "Maths", "score": ""}, 
                  {"name": "John", "subject": "Physics", "score": "47"}, 
                  {"name": "Kate", "subject": "Computer Science", "score": "76"}, 
                  {"name": "Max", "subject": "Maths", "score": "28"}, 
                  {"name": "Emma", "subject": "Physics", "score": "63"} ]"""


user_file_path = input("Enter path to JSON-file:")
classifier = DataClassifier(user_file_path)
if classifier.data:
    classifier.classify_all()
    classifier.save_to_file()
