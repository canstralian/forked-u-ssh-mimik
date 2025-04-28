# ssh-mimik

SSH honeypot utilizing ephemeral Docker containers.

# Usage

`git clone https://github.com/1d8/ssh-mimik`

`pip3 install -r requirements.txt`

Now we must generate the SSH keys that our mock SSH server will use:

`ssh-keygen -t rsa -b 2048 -f ssh_host_key_rsa`

`python3 serve.py --help` to display available options (This is subject to change when new features are introduced)

`python3 serve.py -p 22` to serve the SSH server on port 22

## Todo

- [ ] Update readme to include usage information
- [ ] Clean up `serve.py` code
- [ ] Update `serve.py` code to auto generate the necessary SSH keys
- Add CLI args for: 
	- [ x ] Specifying the port SSH will run on
	- [ ] Specify the location log files will be saved to
