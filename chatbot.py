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

    elif ("που" in user or "πού" in user or "διευθυνση" in user or "διεύθυνση" in user
          or "βρίσκεται" in user or "βρισκεται" in user
          or "location" in user or "maps" in user or "address" in user):
        print("UniChat: Το πανεπιστήμιο βρίσκεται στο Μαρούσι.")
        print("UniChat: Χάρτης Google Maps: https://maps.app.goo.gl/ad64hHNiE3wW3HUM9")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("email" in user or "μειλ" in user or "mail" in user
          or "επικοινωνια" in user or "επικοινωνία" in user):
        print("UniChat: Το email της σχολής είναι info@mitropolitiko.edu.gr")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("εξεταστικη" in user or "εξεταστική" in user
          or "exams" in user or "exam" in user
          or "εξετασεις" in user or "εξετάσεις" in user):
        print("UniChat: Η εξεταστική περίοδος ξεκινά τον Ιούνιο.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    else:
        print("UniChat: Συγγνώμη, δεν κατάλαβα την ερώτηση.")
        print("UniChat: Μπορείς να δοκιμάσεις ξανά.")