rules = {
    ("fever", "cough"): "flu",
    ("flu",): "visit doctor",
    ("headache", "fever"): "viral infection"
}

facts = set()

symptoms = input("Enter symptoms separated by comma: ")
facts.update(sym.strip() for sym in symptoms.split(","))

changed = True

while changed:
    changed = False

    for condition, result in rules.items():
        if all(c in facts for c in condition):
            if result not in facts:
                facts.add(result)
                print(f"Rule Applied: {condition} -> {result}")
                changed = True

print("\nFinal Conclusions:")
for fact in facts:
    print("-", fact)