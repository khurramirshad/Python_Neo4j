import pandas as pd
from pydriller import Repository
from tqdm import tqdm

# Initialize empty lists to store commit data
project_data = []
developer_data = []
file_data = []

# Specify the path to your repository
#repo_path = 'https://github.com/LibrePDF/OpenPDF'
repo_path = 'https://github.com/JodaOrg/joda-time.git'

# Traverse through commits with a progress bar
try:
    for commit in tqdm(Repository(repo_path).traverse_commits(), desc="Processing commits"):
        # Check if the commit has any modified files
        if commit.modified_files:
            # Projectid, ProjectName, Date
            if not any(d['ProjectId'] == commit.project_name for d in project_data):
                project_data.append({
                    'ProjectId': commit.project_name,
                    'ProjectName': commit.project_name,
                    'Date': commit.author_date
                })

            # DeveloperId, Name, Projectid
            if not any(d['DeveloperId'] == commit.author.name for d in developer_data):
                developer_data.append({
                    'DeveloperId': commit.author.name,
                    'Name': commit.author.name,
                    'ProjectId': commit.project_name
                })

            for modified_file in commit.modified_files:
                if modified_file.filename.endswith('.java') and modified_file.source_code:
                    # Collect file information with developer info
                    file_data.append({
                        'FileName': modified_file.filename,
                        'DeveloperId': commit.author.name,
                        'DeveloperName': commit.author.name,
                        'ProjectId': commit.project_name,
                        'ChangeType': modified_file.change_type.name
                    })
except Exception as e:
    print(f"An error occurred: {e}")

# Create DataFrames from the lists
df_project = pd.DataFrame(project_data)
df_developer = pd.DataFrame(developer_data)
df_files = pd.DataFrame(file_data)

# Save the DataFrames to CSV files
output_path = 'D:\\MS\\Dissertation\\Python_Neo4j\\output\\Joda\\'
df_project.to_csv(f'{output_path}project.csv', index=False)
df_developer.to_csv(f'{output_path}developer.csv', index=False)
df_files.to_csv(f'{output_path}files.csv', index=False)