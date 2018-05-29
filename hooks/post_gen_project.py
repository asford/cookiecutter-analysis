import subprocess
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
)

def check_call(cmd):
    logging.info(cmd)
    subprocess.check_call(cmd, shell=True)

origin = "{{ cookiecutter.origin_url }}"

check_call("git init")

if origin.strip():
    check_call("git remote add origin " + origin)
else:
    logging.info("No origin url specified.")
