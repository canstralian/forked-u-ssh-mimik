## Advanced Usage

### CLI Arguments
The `serve.py` script supports the following CLI arguments:
- `--port`: Specify the port on which the SSH honeypot will run. Default is `22`.
- `--log-dir`: Specify the directory where log files will be stored. Default is `/var/log/ssh-honeypot/`.

### Example Commands
1. **Run on Default Port (22):**
   ```bash
   sudo python3 serve.py --port 22 --log-dir /var/log/ssh-honeypot/
   ```

2. **Run on Custom Port with Logs in a Custom Directory:**
   ```bash
   sudo python3 serve.py --port 2222 --log-dir /tmp/honeypot-logs/
   ```

3. **Display Help Message:**
   ```bash
   python3 serve.py --help
   ```

### Generating SSH Keys
To ensure the honeypot operates correctly, generate SSH keys as follows:
```bash
ssh-keygen -t rsa -b 2048 -f ssh_host_key_rsa
```
These keys should be placed in the same directory as `serve.py`.

### Docker Deployment
To deploy the honeypot using Docker, you can build and run a Docker container with the provided `Dockerfile`. For example:
```bash
docker build -t ssh-honeypot .
docker run -p 22:22 ssh-honeypot
```

### Security Disclaimer
This project is strictly for security research and educational purposes. Ensure you have the appropriate permissions before running this tool in any environment.