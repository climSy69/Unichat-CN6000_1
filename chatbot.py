def greet():
    print("UniChat: Γεια σου! Είμαι το UniChat. Πώς μπορώ να σε βοηθήσω;")


def get_response(user):
    if ("τηλέφωνο" in user or "τηλεφωνο" in user):
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

    elif ("βαθμοι" in user or "βαθμοί" in user
          or "grades" in user or "results" in user
          or "αποτελεσματα" in user or "αποτελέσματα" in user
          or "moodle" in user):
        print("UniChat: Οι βαθμοί ανακοινώνονται μέσω της εφαρμογής Moodle, στο section INFORMATION & ANNOUNCEMENTS.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("εγγραφες" in user or "εγγραφές" in user
          or "registration" in user or "registrations" in user
          or "enroll" in user or "enrollment" in user):
        print("UniChat: Οι εγγραφές πραγματοποιούνται έως τα τέλη Σεπτεμβρίου.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("βιβλιοθηκη" in user or "βιβλιοθήκη" in user
          or "library" in user
          or "βιβλια" in user or "βιβλία" in user):
        print("UniChat: Η βιβλιοθήκη του Μητροπολιτικού Κολλεγίου διαθέτει χιλιάδες τίτλους βιβλίων, υπολογιστές και δωρεάν WiFi.")
        print("UniChat: Email Campus Αμαρουσίου: amclibrary@mitropolitiko.edu.gr")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("isic" in user or "card" in user
          or "καρτα" in user or "κάρτα" in user
          or "student card" in user):
        print("UniChat: Η κάρτα ISIC εκδίδεται ηλεκτρονικά μέσω του Κολλεγίου.")
        print("UniChat: Απαιτούνται βεβαίωση σπουδών, στοιχεία φοιτητή και κόστος 15€.")
        print("UniChat: Η ενεργοποίηση ολοκληρώνεται σε 1-3 ημέρες μέσω εφαρμογής.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("χειμερινα" in user or "χειμερινά" in user
          or "μαθηματα" in user or "μαθήματα" in user
          or "winter" in user or "courses" in user):
        print("UniChat: Τα χειμερινά μαθήματα ξεκινούν στα μέσα Οκτωβρίου.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("εκπτωση" in user or "έκπτωση" in user
          or "discount" in user
          or "προσφορα" in user or "προσφορά" in user
          or "διδακτρα" in user or "δίδακτρα" in user):
        print("UniChat: Υπάρχει έκπτωση 20% στα δίδακτρα για εγγραφές έως τα τέλη Φεβρουαρίου.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    else:
        print("UniChat: Συγγνώμη, δεν κατάλαβα την ερώτηση.")
        print("UniChat: Μπορείς να δοκιμάσεις ξανά.")


def main():
    greet()

    while True:
        user = input("Εσύ: ").lower()

        if user == "exit" or user == "τελος" or user == "αντιο":
            print("UniChat: Ευχαριστώ! Καλή συνέχεια.")
            break

        get_response(user)


if __name__ == "__main__":
    main()
