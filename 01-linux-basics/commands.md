## 🛠️ Linux Command Reference (Levels 1-12)

### 📁 File Exploration 
• `ls -l`: List files with details (permissions, owner, size).
• `ls -a`: List all files, including hidden ones (starting with `.`).
- `file [name]`: Identify file type.
- `pwd`: Print working directory.
• `mkdir -p`: Create a directory and any missing parent directories.

### 🔍 Searching & Filtering 
- `grep "[text]" [file]`: Find specific words.
- `sort | uniq -u`: Find unique lines in a list.
- `base64 -d`: Decode base64 strings.
- `wc` : word count (note with -l means counting file by file)
- `tail -f`: Follow logs in real-time.

### 📍 Finding Files 
- `find [path] -size [size]`: Locate files by exact size (e.g., 1033c for 1033 bytes) 

### 🔐 Permissions & Ownership 
- `chmod`: Change permissions (e.g., 600, 700).
- `chown`: Change owner and group.

### 🚀 Redirection & System Admin 
- `>, >>, 2>`: Output and error redirection.
- ``top` / `htop`: System dashboard to see running processes and CPU/RAM.
- `kill -9`: Forcefully stop a process using its ID (PID).
- `df -h`: Check disk space in human-readable format.
- `free -h`: Check RAM/Memory usage.

### 🐳 Docker Fundamentals 
• `docker version`: Verify Docker is running and connected.
• `docker ps -a`: List all containers (running and stopped).
• `docker run -it`: Run a container and enter its interactive terminal.
• `docker run -d`: Run a container in the background (detached).
• `docker stop`: Stop a running container.
• `docker exec -it`: Run a command (like opening a shell) inside a container that is already running.
• `docker logs`: View the output/logs of a container.
• `docker build -t`: Build a custom image from a Dockerfile.
• `docker rm [CONTAINER_ID or NAME]`: To remove a specific container 
• `docker container prune`: To remove ALL stopped containers at once (DevOps shortcut)

### 🛠️ Git Config
• `git init`: Init repo
• `git remote add origin [URL]`: Link to GitHub
• `git remote -v`: Check URL
• `ssh -T git@github.com`: Verify SSH

### 🔄 Daily Workflow
• `git status`: See changes
• `git add .` / `[file]`: Stage changes
• `git commit -m "message"`: Save
• `git push` / `pull`: Sync with GitHub

### 🕵️ Investigation
• `git log --oneline`: History
• `git diff`: Show changes
• `git checkout [file]`: Revert file

### 🛡️ Safety
• `.gitignore`: Ignore files
• `git rm --cached [file]`: Untrack file