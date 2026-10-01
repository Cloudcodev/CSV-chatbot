import sys

print("=" * 50)
print("environment check")
print("=" * 50)

print(f"Python Version: {sys.version} \n")
print(f"Python Executable: {sys.executable}")

try:
    import pip
    print(f"pip (package manager): installed")
except ImportError:
    print(f"pip: not found!")

print("\n" + "=" * 50)
print("if all checks passed, done!")
print("=" * 50)
