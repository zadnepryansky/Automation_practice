from pathlib import Path

file_name = "example.txt"

current_location = Path(__file__).parent

next_location = current_location.joinpath("resources").joinpath("text_documents").joinpath("new_folder").mkdir(
    parents=True, exist_ok=True)
# folder_path = Path("resources").join("text_documents")

print(current_location)
print(next_location)

full_filename = Path.cwd().joinpath("resources").joinpath("text_documents").joinpath(file_name)

with open(full_filename, "w+", encoding="utf-8") as file:
    file.write("our data")

with open(full_filename, "r", encoding="utf-8") as file:
    print(file.read())
