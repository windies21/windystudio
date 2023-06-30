Automatically prefix JIRA issue numbers to Git commit messages

Edit.
~~~
$ vi .git/hooks/prepare-commit-msg
~~~

Copy and paste this code
~~~
#!/bin/sh

# Get the branch name
branch_name=$(git symbolic-ref --short HEAD)

# Extract JIRA issue number from branch name
issue_number=$(echo "$branch_name" | sed -n 's/.*\/\([A-Z]*-[0-9]*\).*/\1/p')

# If an issue number is found, prefix it to the commit message
if [ -n "$issue_number" ]; then
    sed -i.bak -e "1s/^/[$issue_number] /" "$1"
fi
~~~

[Make It Global](https://coderwall.com/p/jp7d5q/create-a-global-git-commit-hook)
