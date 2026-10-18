import json
def classify_score(data):

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

    return data

class DataClassifier():
    def __init__(self, json_string):
        try:
            self.data = json.loads(json_string)
            print("Data is accepted!")


        except json.JSONDecodeError as e:
            print("Error. Invalid JSON", e)
            self.data = []

    def save_to_file(self, filename="scores.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)
        print(f"Results with categories are saved in {filename}")

    def classify_all(self):
        for student in self.data:
            classify_score(student)



user_input = """[ {"name": "Alex", "subject": "Maths", "score": "91"}, 
                  {"name": "John", "subject": "Physics", "score": "47"}, 
                  {"name": "Kate", "subject": "Computer Science", "score": "76"}, 
                  {"name": "Max", "subject": "Maths", "score": "28"}, 
                  {"name": "Emma", "subject": "Physics", "score": "63"} ]"""


classifier = DataClassifier(user_input)
classifier.classify_all()
classifier.save_to_file()