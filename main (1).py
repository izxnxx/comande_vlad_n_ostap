from scanner import load_rules, scan_file

rules_path = "rules.txt"
file_to_scan = "rules.txt"  

rules = load_rules(rules_path)

found = scan_file(file_to_scan, rules)

if found:
    print(f"УВАГА! У файлі {file_to_scan} знайдено загрози: {found}")
else:
    print(f"Файл {file_to_scan} чистий.")


