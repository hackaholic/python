import sys

print("stdin is TTY:", sys.stdin.isatty())
print("stdout is TTY:", sys.stdout.isatty())
print("stderr is TTY:", sys.stderr.isatty())
