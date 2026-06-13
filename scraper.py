import requests

# API endpoint for the Data Analytics
url = "https://kshrd-web-api.kshrd.app/curricula/course/d327c8c5-2d8f-4cc1-af70-2cc4a4284ee7"

response = requests.get(url)

response.raise_for_status()

data = response.json()

# Display course information
print("=== COURSE ===")
print("Course:", data["course_name"])
print("Description:", data["course_description"])

# Display course objective
print("\n=== OBJECTIVES ===")
for objective in data["objectives"]:
    print("-", objective["objective"])

# Display curriculum topics
print("\n=== CURRICULUM ===")
for topic in data["topics"]:
    print(f"\n{topic['topic_name']}")

    for item in topic["items"]:
        print(f"  - {item['item_content']}")