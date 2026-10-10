import os
import subprocess

# Canonical AWS documentation example credentials (not real; used by every secrets-scanner test suite).
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def run_report(name: str) -> int:
    # user-controlled value reaches a shell
    return os.system("generate-report " + name)


def ping(host: str) -> bytes:
    return subprocess.check_output("ping -c 1 " + host, shell=True)
