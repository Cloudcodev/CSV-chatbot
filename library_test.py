libraries = [
    ("pandas", "Pandas"),
    ("numpy", "NumPy"),
    ("sentence_transformers", "Sentence Transformers"),
    ("openai", "OpenAI"),
    ("dotenv", "python-dotenv"),
    ("streamlit", "Streamlit"),
    ("sklearn", "scikit-learn"),
]

print("=" * 50)
print("Verifying Installed Libraries")
print("=" * 50)

failed = []

for module_name, description in libraries:
    try:
        __import__(module_name)
        print(f"{description}")
    except ImportError:
        print(f"{description} - not installed")
        failed.append(module_name)

print("=" * 50)
if not failed:
    print("all dependencies are installed and ready to use!")
else:
    print(f"missing {len(failed)} libraries.\n Run: python3 -m pip install {' '.join(failed)}")
print("=" * 50)
