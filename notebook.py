import json
import datetime

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(load_notes()) + 1,
        "title": title,
        "body": body,
        "created_at": created_at,
        "last_modified": created_at
    }
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def list_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата создания: {note['created_at']}, Дата последнего изменения: {note['last_modified']}")

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Введите новый заголовок заметки: ")
            note['body'] = input("Введите новое тело заметки: ")
            note['last_modified'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным ID не найдена")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            return
    print("Заметка с указанным ID не найдена")

def main():
    while True:
        command = input("Введите команду (add/list/edit/delete/exit): ").lower()
        if command == "add":
            add_note()
        elif command == "list":
            list_notes()
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "exit":
            break
        else:
            print("Некорректная команда")

if __name__ == "__main__":
    main()