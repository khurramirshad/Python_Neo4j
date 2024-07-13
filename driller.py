from pydriller import Repository
import csv,json

# Replace 'path_to_repo' with the path to your repository
repo = Repository('https://github.com/khurramirshad/FoodDeliveryProject')
repo_details = []


# Loop through all commits
for commit in repo.traverse_commits():
    # print(f'Commit {commit.hash} by {commit.author.name} on {commit.author_date} in {commit.project_name}')
    file_list = []
    class_list = []
    method_list = []
    
    for modified_file in commit.modified_files:
            file_list.append(modified_file.filename)
            # print(modified_file.source_code)
            if modified_file.source_code:
                 for line in modified_file.source_code.split('\n'):
                    if 'class' in line.split():
                        class_list.append(line)

    commit_details = {"id": commit.hash , "ProjectName":commit.project_name , "Date":commit.author_date,"Author": commit.author.name,"Branch":commit.branches,"Files" : file_list, "Class":class_list} 
    repo_details.append(commit_details)

 
    # Write data into the CSV file 
with open('D:\MS\Dissertation\Python_Neo4j\output\commits_details.csv', 'w', newline='') as file:
    writer=csv.writer(file)
    writer.writerow(repo_details)
   