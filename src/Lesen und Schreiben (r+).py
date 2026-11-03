with open("system.log", "r+", encoding="utf-8") as log_file:
    inhalt = log_file.read()

    print(inhalt)

    log_file.seek(0, 2)

    log_file.write("[SUCCESS] Überprüfung abgeschlossen.\n")