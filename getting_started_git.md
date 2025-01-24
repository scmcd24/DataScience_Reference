
# Git Commands

 - Terms
    - git:      Version control system
    - Github:   Wrapper around git, online git tracking system
    - origin:   Link to your remote repository (Github)

 - Creating a new repo
    - Create new repo on Github
    - Create new local directory for your git repo: 
        - $ mkdir <git_repo>
        - $ cd <git_repo>
    - Create git repo: $ git init
    - Rename default branch: $ git branch -M "main"
    - Make sure your username / password are set up: 
        - $ nano ~/.gitconfig       # Add user.name and user.email
        - OR $ git config --global --edit
        - OR $ git config --global user.name "username"
    - Link git repo to github repo: git remote add origin <URL>
        - If asked for your username/password, enter gitconfig username and GitHub TOKEN (Add link)

 - Logging Changes
    - Before making changes, update local directory with current Github version:
        - $ git pull origin main
    - Check out working branch: $ git checkout -b main
    - After making local changes, stage/add them and commit:
        - Add file to be tracked: $ git add <any files you want updated>
        - $ git commit -m "Comment what changes you made" 
        - OR $ git commit -am "Comment what changes you made"   # Stage all TRACKED files
    - When you're finished, push the commit to upload to remote repo:
        - $ git push -u origin main     # Upload changed files to Github
    - Pull request


- Other Useful
    - Change last commit: $ git commit --amend
    - Find who made last changes to a file: $ git blame
    - View summary of commits: $ git log
    - See what files are staged for next commit: $ git status
    - See what branch you're working in: $ git branch
    - Remove last commit, but keep changes: $ git reset --soft HEAD~1
    - Revert repo to an older version: $ git revert <hash#>

 - Using git in the terminal
    - vim is the default git text editor: :q to quit, etc

 - References
    - [https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
    - [Authenticating git](https://dev.to/shafia/support-for-password-authentication-was-removed-please-use-a-personal-access-token-instead-4nbk)