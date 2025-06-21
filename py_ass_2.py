import csv
def load_scores(path: str) -> list[tuple[str,int]]:
    record = []
    # if not path.exists(path):
    #     return record
    try:
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) != 2:
                    continue
                name, score = row
                record.append((name, int(score)))
    except:
        print(f"Error Reading in {path}")
    return record


def add_score(record: list[tuple[str,int]], name: str, score: int) -> None:
    record.append((name, score))


def save_scores(path: str, record: list[tuple[str,int]]) -> None:
    try:
        with open(path, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            for name, score  in record:
                writer.writerow([name, score])
    except:
        print(f"Error Writing To {path}")



def top_n(record: list[tuple[str,int]], n: int) -> list[tuple[str,int]]:
    sorted_records = sorted(record, key=lambda x: x[1], reverse=True)
    return sorted_records[:n]


def main():
    path = "score.csv"
    record = load_scores(path)
    while True:
        print("\n--- Score Keeper Menu ---")
        print("1. Show Top N Scores")
        print("2. Add New Score")
        print("3. Exit")
        try:
            choice = int(input("Enetr your choice b/w 1-4 : "))
        except:
            print("input wrong choice")
            continue
        if choice == 1:
            try:
                n = int(input("How many top score you want to display ? "))
                top_scores = top_n(record, n)
                print("Top score : \n")
                for name, score in top_scores:
                    print(f"{name} : {score}")
            except:
                print("please enter a valid number.")
        elif choice == 2:
            name = input("Enter name : ")
            try:
                score = int(input("Enetr the score : "))
                add_score(record, name, score)
                save_scores(path, record)
                print("score added successfully")
            except:
                print("score must be a valid integer")
        elif choice == 3:
            print("Exiting, Goodbye!")
            break
        else:
            print("Enetr a valid choice.")



if __name__ == "__main__":
    main()