testing = {
    "rule1": {"if": ["Ya","Tidak"], "then": "Makan Sagu"},
    "rule2": {"if": ["Ya","Ya"], "then": "Makan Sagu"},
    "rule3": {"if": ["Ya","Tidak"], "then": "Makan Sagu"}

}

testing2 = testing.copy()

testing3 = testing.copy()


print(testing)
for rule_name, rules in testing2.items():
    if rules["if"][1] == 'Ya':
        testing3.update (rule_name = testing2[rule_name])
        testing3[rule_name] = testing3.pop('rule_name')


testing2.clear()
print(testing2)
print(testing3)

print(len(testing2))