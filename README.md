# KSHRD Data Analytics Course Scraper

A Python-based web scraper that fetches course data from the KSHRD API and processes it for analysis and export.

## Overview

This project retrieves course information from the KSHRD (Khmer Software and Hardware Resource Development) API, specifically targeting the Data Analytics course curriculum. The scraped data includes course details, objectives, topics, and curriculum items, which can be saved in multiple formats for further analysis.

## Features

- **API Data Scraping**: Fetches course data from the KSHRD web API
- **JSON Export**: Automatically saves data in JSON format with UTF-8 encoding
- **Console Output**: Displays formatted course information (name, description, objectives, curriculum)
- **CSV Export**: Utility function to convert data to structured CSV format
- **Error Handling**: HTTP status validation with `raise_for_status()`

## Project Structure

```
web-scraping-kshrd-data-analysis-course/
├── data/
│   └── data_analytics_course.json    # Generated JSON output
├── venv/                             # Virtual environment
├── README.md                         # This file
├── requirements.txt                  # Python dependencies
├── save_data.py                      # Data export utilities (CSV)
└── scraper.py                        # Main scraper script
```

## Installation

1. **Clone/Navigate to the project:**
   ```bash
   cd web-scraping-kshrd-data-analysis-course
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the Scraper

```bash
python scraper.py
```

This will:
- Fetch course data from the KSHRD API
- Save the data as JSON to `data/data_analytics_course.json`
- Display formatted course information:
  - Course name and description
  - All learning objectives
  - Curriculum topics with items

### Export Data to CSV

The `save_data.py` module provides utility functions for exporting data:

```python
from scraper import data
from save_data import save_csv

save_csv(data)
```

This will export the data to `data/data_analytics_course.csv`

## Dependencies

- **requests** (2.34.2): HTTP library for making API requests

Note: `csv` and `json` are built-in Python modules and don't require installation.

## API Endpoint

The scraper targets:
```
https://kshrd-web-api.kshrd.app/curricula/course/d327c8c5-2d8f-4cc1-af70-2cc4a4284ee7
```

This endpoint returns:
- `course_name`: Name of the course
- `course_description`: Course description
- `objectives`: List of learning objectives
- `topics`: Curriculum topics with items

## Output Formats

### JSON Output (Automatic)
Saved to `data/data_analytics_course.json` automatically when running `scraper.py`.
- Pretty-printed with 4-space indentation
- UTF-8 encoding with `ensure_ascii=False` for special characters

### CSV Output (Optional)
Generated using the `save_csv()` function from `save_data.py` with columns:
- **Section**: Category type (Course, Description, Objective, Curriculum)
- **Topic**: Topic name (if applicable)
- **Content**: Actual content/text

## Requirements

- Python 3.6+
- Internet connection (to access the KSHRD API)
- Write permissions to the `data/` directory

## Error Handling

The scraper includes error checking:
- `response.raise_for_status()` - Raises an exception for HTTP errors
- File encoding is explicitly set to UTF-8 to handle special characters

## License

This project is part of the KSHRD Data Analysis Course training.

## Author

Created as part of the KSHRD web scraping and data analysis course.
