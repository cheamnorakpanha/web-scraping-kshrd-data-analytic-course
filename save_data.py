import csv
import json
import os

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)


def save_json(data):
    with open("data/data_analytics_course.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("JSON file saved successfully!")


def save_csv(data):
    with open(
        "data/data_analytics_course.csv", "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)

        writer.writerow(["Section", "Topic", "Content"])

        writer.writerow(["Course", "", data["course_name"]])

        writer.writerow(["Description", "", data["course_description"]])

        for objective in data["objectives"]:
            writer.writerow(["Objective", "", objective["objective"]])

        for topic in data["topics"]:
            for item in topic["items"]:
                writer.writerow(
                    ["Curriculum", topic["topic_name"], item["item_content"]]
                )

    print("CSV file saved successfully!")
