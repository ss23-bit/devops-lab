### Image is a read-only blueprint.

### 🚢 Docker commands
`docker pull [image]` : Download a "pre-made" computer environment (like ubuntu or python).
`docker images` : List all the environments you have downloaded.
`docker run -it [image] bash` : Create a container and "jump inside" its terminal.
`docker ps` : See which containers are currently "alive" and running. `ps -a`: Show me All containers, including the ones that are exited, dead, or crashed."
`docker stop [container_id]` : Shut down a running container.
`docker rm [container_id]` : Delete a container to save disk space.
`docker inspect [container_id]` : The "God Mode" command. Use this to find a container's IP address and networking setup without even going inside it.
`172.17.0.x` : The default IP range for Docker containers.
`Avoid Internal IPs` : Do not rely on `172.17.x.x` in WSL2; it is unstable and often blocked by the virtual switch.
`docker run -p [HostPort]:[ContainerPort]` : Maps a host port to a container port (The standard way to access apps).

### 🕵️ Run `ip addr` inside the container: What just happened?
- When you started container, Docker acted like a "Mini-Router." It created a virtual network bridge (usually called docker0) and gave your container its own private IP address.

### `docker run -it -p 8080:8000 ubuntu bash`: haven't put anything on the "Internet" yet.
- What does `-p 8080:8000` mean?
`It tells Docker`: "If someone knocks on my WSL Host at Port 8080, send them inside the container to Port 8000."

- `The Image`: You downloaded a "package" (Ubuntu) from the internet to your house.

- `The Container`: You opened that package and started a tiny "virtual computer" inside your real computer.

- `The Docker "Database" (Registry)`: When people talk about Docker Hub, that's where the empty packages live. Your specific container with your specific files is private and only exists on your hard drive right now.

### Container Lifecycle :
`docker run` = Create a fresh instance from the Image.
`exit (or docker stop)` = The instance dies.

`docker start -ai my-web-server`: f you want to go back into the exact same container you used before (The -ai stands for Interactive and Attach, so you can get back to the bash prompt.)

`docker run -it --rm --name my-web-server -p 8080:8000 ubuntu bash`: With --rm: When you type exit, the container is deleted automatically. No more "Conflict" errors next time!

`docker run -it --rm -v $(pwd):/app -p 8080:8000 ubuntu bash`
`-v` : Stands for Volume. How we persist data outside the container.
`$(pwd)` : This is a Linux shortcut for "My Current Directory."
`:/app` : This tells Docker: "Inside the container, create a folder called /app and mirror my current WSL folder there."

`-d` (Docker Detached): Even if you close your terminal or restart your computer, Docker keeps that container running `docker run -d`

`docker exec -it [name] [command]` : Run a command inside a container that is already running.

`-e` : Pass configuration (like passwords) into a container.

`docker logs [name]` : See what’s happening inside a background container (very important for debugging!).