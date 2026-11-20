import subprocess

result = subprocess.run(["npm","run","build"],capture_output=True, text=True)

if result.returncode != 0 :
    print(result.stderr)
print(result.returncode)
print(result.stdout)
