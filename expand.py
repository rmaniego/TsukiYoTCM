import os
import re
import csv
from glob import glob


def main():
    rows = list()
    for tcm in glob("*.csv"):
        with open(tcm, newline="") as file:
            rows = list(csv.reader(file))
        break

    SNAKECASE = re.compile(r"[^\w\-.]+")
    SAFE_PATH = re.compile(r"[^\w\-. ]+")

    path = []
    directory = ""
    for row in rows[1:]:
        assert len(row) == 3, "Invalid TCM file."
        
        test_case_name = row[0]
        test_case_id = row[1]
        test_case_summary = row[2]

        if not (test_case_id.strip() and test_case_summary.strip()):
            test_case_name = SAFE_PATH.sub("-", test_case_name)
            if test_case_name[0] != " ":
                path = [test_case_name.strip()]
                directory = "/".join(path).replace("\/\/", "/")
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    print(directory)
                continue
            elif test_case_name[2] != " ":
                if len(path) == 3:
                    del path[1]
                    del path[2]
                elif len(path) == 2:
                    del path[1]
                path[1].append(test_case_name.strip())
                directory = "/".join(path).replace("\/\/", "/")
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    print(directory)
                continue
            elif test_case_name[4] != " ":
                if len(path) == 3:
                    del path[2]
                path[1].append(test_case_name.strip())
                directory = "/".join(path).replace("\/\/", "/")
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    print(directory)
                continue
            
            raise Exception("Unsupported file format.")

        test_case_name = test_case_name.strip()
        filename = SNAKECASE.sub("_", test_case_name.lower())
        filepath = f"{directory}/{test_case_id}_{filename}.md".replace("\/\/", "/")

        if os.path.exists(filepath):
            continue
        
        print(filepath)

        contents = (
            f"{test_case_id}: {test_case_name}\n"
            f"Summary: {test_case_summary}\n"
            f"Preconditions: None\n"
            f"Scenario 1"
            f" | # | Step | Expected Behavior | \n"
            f" |---|------|-------------------| \n"
            f" |   |      | Verify that       | \n"
        )

        with open(filepath, "w+", encoding="utf-8") as file:
            file.write(contents)


if __name__ == "__main__":
    main()
