import json

class DataOptimizer:
    def __init__(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            self.data = json.load(file)
            
        all_keys = set()
        for item in self.data:
            for key in item:
                all_keys.add(key)
        
        keys_list = list(all_keys)
        print("\nДоступные колонки:")
        for index, key in enumerate(keys_list):
            print(f"[{index}] {key}")
        
        user_input = input("\nВведите номера колонок через запятую для исключения (или нажмите Enter): ")
        
        excluded_keys = set()
        if user_input.strip():
            indices = [int(item.strip()) for item in user_input.split(",") if item.strip()]
            excluded_keys = {keys_list[i] for i in indices}
        
        final_keys = all_keys - excluded_keys
        
        self.column_store = {key: [] for key in final_keys}
        for item in self.data:
            for key in final_keys:
                value = item.get(key)
                self.column_store[key].append(value)

    def update_value(self, column, index, new_value):
        self.column_store[column][index] = new_value

    def get_row(self, index):
        return {key: self.column_store[key][index] for key in self.column_store}       


optimizer = DataOptimizer("RAMS.json")

print("\nПревью колоночного хранилища:")
for column_name, values in optimizer.column_store.items():
    preview = values[:5]
    print(f"{column_name} ({len(values)} строк): {preview} ...")
