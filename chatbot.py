print("UniChat: Γεια σου! Είμαι το UniChat. Πώς μπορώ να σε βοηθήσω;")

while True:
    user = input("Εσύ: ").lower()

    if user == "exit" or user == "τελος" or user == "αντιο":
        print("UniChat: Ευχαριστώ! Καλή συνέχεια.")
        break

    elif "τηλέφωνο" in user or "τηλεφωνο" in user:
        print("UniChat: Το τηλέφωνο της γραμματείας είναι 210XXXXXXX.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("ωρες" in user or "ώρες" in user) and "γραμματ" in user:
        print("UniChat: Η γραμματεία λειτουργεί από 09:00 έως 15:00.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    else:
        print("UniChat: Συγγνώμη, δεν κατάλαβα την ερώτηση.")
        print("UniChat: Μπορείς να δοκιμάσεις ξανά.")