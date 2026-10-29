def interactive_menu():
    print("=" * 60)
    print("Try it yourself (press Enter with nothing typed to quit anytime)")
    print("=" * 60)
    print("Pick an automaton to test:")
    for key, (label, _) in EXAMPLES.items():
        print(f"  {key}) {label}")

    choice = input("Choice (blank to quit): ").strip()
    if choice not in EXAMPLES:
        return
    _, builder = EXAMPLES[choice]
    automaton = builder()

    while True:
        s = input("Enter a string to test (blank to go back): ").strip()
        if not s:
            break
        show_result(automaton, s)
