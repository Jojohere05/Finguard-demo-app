import os
import re

print("🔍 FinGuard Demo Scan Running...\n")

violations = []

patterns = {
    "API_KEY": r"sk_test_[0-9a-zA-Z]+",
    "JWT_SECRET": r"JWT_SECRET\s*=\s*['\"].+['\"]",
    "PASSWORD": r"password\s*=\s*['\"].+['\"]"
}

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in {".git", "__pycache__", "node_modules","scripts"}]

    for file in files:
        if file.endswith((".py", ".yaml", ".yml")):
            path = os.path.join(root, file)

            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                    for name, pattern in patterns.items():
                        if re.search(pattern, content):
                            violations.append((name, path))
            except:
                pass

print(f"Files scanned: {len(violations)} issues found\n")

if violations:
    print("❌ Violations detected:\n")
    for v in violations:
        print(f"- {v[0]} in {v[1]}")

    print("\n🚫 Decision: REVIEW")
    exit(1)
else:
    print("✅ No issues found")
    print("Decision: ALLOW")