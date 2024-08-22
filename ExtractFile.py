import openpyxl
import os
import re

# Define the root directory where you want to search for text files
root_directory = 'E:\\Computer Architecture\\Group Project-2\\Output\\456.hmmer'

# Define a list of regex patterns you want to search for in each line
regex_patterns = [r'system\.cpu\.dcache\.overall_miss_rate::total\s+(\d+\.\d+)\s+#\s+miss rate for overall accesses',
                  r'system\.cpu\.dcache\.overall_misses::total\s+(\d+)\s+#\s+number of overall misses',
                  r'system\.cpu\.icache\.overall_miss_rate::total\s+(\d+\.\d+)\s+#\s+miss rate for overall accesses', 
                  r'system\.cpu\.icache\.overall_misses::total\s+(\d+)\s+#\s+number of overall misses',
                  r'system\.l2\.overall_miss_rate::total\s+(\d+\.\d+)\s+#\s+miss rate for overall accesses', 
                  r'system\.l2\.overall_misses::total\s+(\d+)\s+#\s+number of overall misses']  # Add your regex patterns to this list

# Create a new Excel workbook
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = 'Cache1 Stats Output Data'

# Walk through the root directory and its subdirectories
for root, _, files in os.walk(root_directory):
    for filename in files:
        if filename.endswith('stats.txt'):
            file_path = os.path.join(root, filename)
            folder_name = os.path.basename(os.path.normpath(root))
            extracted_lines = []

            # Open and read the file
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if any(re.search(pattern, line) for pattern in regex_patterns):
                        extracted_lines.append(line.strip())

            if extracted_lines:
                # Write the file path and extracted lines to the Excel worksheet
                worksheet.append([file_path, folder_name] + extracted_lines)

# Save the Excel workbook to a file
workbook.save('E:\\Computer Architecture\\Group Project-2\\Output\\Data1.xlsx')
