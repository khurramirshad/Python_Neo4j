
import git 


# Execute from the repository root directory
#repo = git.Repo('https://github.com/khurramirshad/FoodDeliveryProject')
repo = git.Repo('.')
remote_refs = repo.remote().refs

for ref in remote_refs:
    print(ref.name)