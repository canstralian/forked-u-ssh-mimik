# forked-u-ssh-mimik

![GitHub Repo stars](https://img.shields.io/github/stars/canstralian/forked-u-ssh-mimik?style=social)
![GitHub forks](https://img.shields.io/github/forks/canstralian/forked-u-ssh-mimik?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/canstralian/forked-u-ssh-mimik?style=social)
![GitHub license](https://img.shields.io/github/license/canstralian/forked-u-ssh-mimik)
![GitHub last commit](https://img.shields.io/github/last-commit/canstralian/forked-u-ssh-mimik)
![GitHub issues](https://img.shields.io/github/issues/canstralian/forked-u-ssh-mimik)
![GitHub closed issues](https://img.shields.io/github/issues-closed/canstralian/forked-u-ssh-mimik)
![GitHub pull requests](https://img.shields.io/github/issues-pr/canstralian/forked-u-ssh-mimik)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/canstralian/forked-u-ssh-mimik)

![Python versions](https://img.shields.io/pypi/pyversions/forked-u-ssh-mimik)
![PyPI version](https://img.shields.io/pypi/v/forked-u-ssh-mimik?label=pypi%20release)
![Build Status](https://github.com/canstralian/forked-u-ssh-mimik/actions/workflows/main.yml/badge.svg)
![CodeQL Analysis](https://github.com/canstralian/forked-u-ssh-mimik/actions/workflows/codeql-analysis.yml/badge.svg)
![Bandit Scan](https://img.shields.io/badge/security-bandit-yellow)
![Dependencies Safe](https://img.shields.io/badge/dependencies-safe-brightgreen)

![Repo size](https://img.shields.io/github/repo-size/canstralian/forked-u-ssh-mimik)
![Contributors](https://img.shields.io/github/contributors/canstralian/forked-u-ssh-mimik)
![Top language](https://img.shields.io/github/languages/top/canstralian/forked-u-ssh-mimik)

---

## ⚠️ Disclaimer

This repository is a **fork of [redveil-security/ssh-mimik](https://github.com/redveil-security/ssh-mimik)**. It is intended for:

- **Security auditing**  
- **Static and dynamic analysis**  
- **Educational use in isolated lab environments**  

**Not intended for offensive use.**  

---

## 🔒 Purpose of this Fork

This fork focuses on **safe research and responsible testing**:

- Hardened deployment practices (isolated containers/VMs, no host mounts).  
- Pre-launch dependency and security scans (`Bandit`, `Safety`).  
- Documentation of security risks and safe usage guidelines.  

All testing should be done in **isolated environments**; do not run on production systems or networks.

# ssh-mimik

SSH honeypot utilizing ephemeral Docker containers.

# Usage

`git clone https://github.com/1d8/ssh-mimik`

`pip3 install -r requirements.txt`

Now we must generate the SSH keys that our mock SSH server will use:

`ssh-keygen -t rsa -b 2048 -f ssh_host_key_rsa`

`python3 serve.py --help` to display available options (This is subject to change when new features are introduced)

`sudo python3 serve.py -p 22 -l /splunk/log/folder` to serve the SSH server on port 22 & place log file within specified directory

* If you choose to run on a different port, you still need to run as `sudo`. Otherwise the docker containers will not be able to spawn & each time you try SSHing in, you will get the following error: `shell request failed on channel 0`


Once the server is up & running the default creds are: `user:password`

## Todo

- [ ] Update readme to include usage information
- [ ] Clean up `serve.py` code
- [ ] Update `serve.py` code to auto generate the necessary SSH keys
- Add CLI args for: 
	- [ x ] Specifying the port SSH will run on
	- [ x ] Specify the location log files will be saved to
- [ ] Add example usage of utilizing Dockerfiles to deploy more realistic honeypots (EX: Deploying additional directories & files)
- [ ] Add automated python script that'll auto attack SSH honeypots on specified subnet to simulate attacker. CTF-style questions will then be asked based on these commands ran.
- [ ] Possible web interface for viewing active SSH sessions & logs?
- [ ] Implement check to ensure running with root privileges, otherwise exit to avoid causing errors


## Common Issues

Script immediately exiting without starting server:

![](https://i.ibb.co/qLTCPHjv/2025-05-26-08-59.png)

**Fix: Ensure you've generated your SSH keys & they're placed in the same directory you're running the script from.**
