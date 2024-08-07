import pandas as pd
from pydriller import Repository
import re

# Initialize empty list to store commit data
project_data = []
developer_data = []
commits_data = []
class_data = []
method_data = []

# Specify the path to your repository
repo_path = 'https://github.com/khurramirshad/FoodDeliveryProject'
class_regex = re.compile(r'class\s+(\w+)\s*')
method_regex = re.compile(r'(public|protected|private|static|\s)+[\w<>\[\]]+\s+(\w+)\s*\(.*?\)\s*\{')

# Traverse through commits
for commit in Repository(repo_path).traverse_commits():
    # Projectid,ProjectName,Date
    project_data.append({
        'ProjectId': commit.project_name,
        'ProjectName': commit.project_name,
        'Date': commit.author_date
    })
    # DeveloperId,Name,Projectid,
    developer_data.append({
        'DeveloperId': commit.author.name,
        'Name': commit.author.name,
        'ProjectId': commit.project_name
    })

    # CommitId,ProjectID,Date,DeveloperId,Branch
    commits_data.append({
        'CommitId': commit.hash,
        'ProjectID': commit.project_name,
        'date': commit.author_date,
        'DeveloperId': commit.author.name,
        'Branch': commit.branches 
    })

    for modified_file in commit.modified_files:
        if modified_file.filename.endswith('.java') and modified_file.source_code:
            # Find all class id,Name,CommitId
            found_classes = class_regex.findall(modified_file.source_code)
            if found_classes:
                class_data.append({
                    'ClassId': found_classes[0],
                    'Name': found_classes[0],
                    'CommitId': commit.hash               
                })
            # Find all method names
            found_methods = method_regex.findall(modified_file.source_code)
            for method in found_methods:
                method_data.append({
                    'MethodId': method[1],
                    'Name': method[1],
                    'ClassId': found_classes[0]
                })

# Create DataFrames from the lists
df_project = pd.DataFrame(project_data)
df_developer = pd.DataFrame(developer_data)
df_commits = pd.DataFrame(commits_data)
df_classes = pd.DataFrame(class_data)
df_methods = pd.DataFrame(method_data)

# Save the DataFrames to CSV files
df_project.to_csv('D:\\MS\\Dissertation\\Python_Neo4j\\output\\project.csv', index=False)
df_developer.to_csv('D:\\MS\\Dissertation\\Python_Neo4j\\output\\developer.csv', index=False)
df_commits.to_csv('D:\\MS\\Dissertation\\Python_Neo4j\\output\\commits.csv', index=False)
df_classes.to_csv('D:\\MS\\Dissertation\\Python_Neo4j\\output\\class.csv', index=False)
df_methods.to_csv('D:\\MS\\Dissertation\\Python_Neo4j\\output\\methods.csv', index=False)