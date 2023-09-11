# Excel Data Generator

Generate dummy employee data and export it to an Excel file.

## Overview

This Python project provides a simple tool to generate dummy employee data in an Excel spreadsheet. It's particularly useful for testing or populating databases with sample data. The generated data includes employee IDs, names, email addresses, roles, phone numbers, and more.

## Tech Stack

- Python 3.10.12
- openpyxl (for Excel file handling)
- Faker (for generating realistic dummy data)
- io (for handling input and output operations)
- pytest (for unit testing)

## Features

- Generate dummy employee data for testing and development purposes.
- Export the generated data to an Excel (.xlsx) file.
- Customize the number of rows and other data parameters.

## Prerequisites

- Python 3.10.12 installed on your system.

## InstallationClone the repository:

1. ```
   git clone https://github.com/rysamuel9/excel-data-generator.git
   cd excel-data-generator
   ```
2. Install the required packages:

   ```
   pip install openpyxl faker pytest
   ```

## Usage

1. Run the main script:

   ```
   python main.py
   ```
2. Follow the prompts to specify the number of rows and other data parameters.
3. The generated Excel file will be saved in the `generated_excel` folder.

## Folder Structure

- `core/`: Contains core entities, services, and repositories.
- `application/`: Application use cases.
- `interfaces/`: User interfaces and data generation.
- `tests/`: Unit tests for the project.
- `generated_excel/`: Directory to store generated Excel files.
