# chatbot.py — Terminal version of UniChat
# This is the original command-line chatbot before the GUI was added.
# It reads user input in a loop and prints the matching response.


def greet():
    # Print the welcome message when the chatbot starts
    print("UniChat: Γεια σου! Είμαι το UniChat. Πώς μπορώ να σε βοηθήσω;")


def get_response(user):
    # Match the user's message against known keywords.
    # Each block covers a different topic a student might ask about.

    if ("τηλέφωνο" in user or "τηλεφωνο" in user):
        # User asked about the secretary's phone number
        print("UniChat: Το τηλέφωνο της γραμματείας είναι 210XXXXXXX.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("ωρες" in user or "ώρες" in user) and "γραμματ" in user:
        # User asked about the secretary's office hours
        print("UniChat: Η γραμματεία λειτουργεί από 09:00 έως 15:00.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("που" in user or "πού" in user or "διευθυνση" in user or "διεύθυνση" in user
          or "βρίσκεται" in user or "βρισκεται" in user
          or "location" in user or "maps" in user or "address" in user):
        # User asked for the university's location or address
        print("UniChat: Το πανεπιστήμιο βρίσκεται στο Μαρούσι.")
        print("UniChat: Χάρτης Google Maps: https://maps.app.goo.gl/ad64hHNiE3wW3HUM9")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("email" in user or "μειλ" in user or "mail" in user
          or "επικοινωνια" in user or "επικοινωνία" in user):
        # User asked for the school's contact email
        print("UniChat: Το email της σχολής είναι info@mitropolitiko.edu.gr")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("εξεταστικη" in user or "εξεταστική" in user
          or "exams" in user or "exam" in user
          or "εξετασεις" in user or "εξετάσεις" in user):
        # User asked about the exam period
        print("UniChat: Η εξεταστική περίοδος ξεκινά τον Ιούνιο.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("βαθμοι" in user or "βαθμοί" in user
          or "grades" in user or "results" in user
          or "αποτελεσματα" in user or "αποτελέσματα" in user
          or "moodle" in user):
        # User asked about grades or the Moodle platform
        print("UniChat: Οι βαθμοί ανακοινώνονται μέσω της εφαρμογής Moodle, στο section INFORMATION & ANNOUNCEMENTS.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("εγγραφες" in user or "εγγραφές" in user
          or "registration" in user or "registrations" in user
          or "enroll" in user or "enrollment" in user):
        # User asked about student enrollment or registrations
        print("UniChat: Οι εγγραφές πραγματοποιούνται έως τα τέλη Σεπτεμβρίου.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("βιβλιοθηκη" in user or "βιβλιοθήκη" in user
          or "library" in user
          or "βιβλια" in user or "βιβλία" in user):
        # User asked about the campus library
        print("UniChat: Η βιβλιοθήκη του Μητροπολιτικού Κολλεγίου διαθέτει χιλιάδες τίτλους βιβλίων, υπολογιστές και δωρεάν WiFi.")
        print("UniChat: Email Campus Αμαρουσίου: amclibrary@mitropolitiko.edu.gr")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("isic" in user or "card" in user
          or "καρτα" in user or "κάρτα" in user
          or "student card" in user):
        # User asked about the ISIC student card
        print("UniChat: Η κάρτα ISIC εκδίδεται ηλεκτρονικά μέσω του Κολλεγίου.")
        print("UniChat: Απαιτούνται βεβαίωση σπουδών, στοιχεία φοιτητή και κόστος 15€.")
        print("UniChat: Η ενεργοποίηση ολοκληρώνεται σε 1-3 ημέρες μέσω εφαρμογής.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("χειμερινα" in user or "χειμερινά" in user
          or "μαθηματα" in user or "μαθήματα" in user
          or "winter" in user or "courses" in user):
        # User asked about winter semester courses
        print("UniChat: Τα χειμερινά μαθήματα ξεκινούν στα μέσα Οκτωβρίου.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    elif ("εκπτωση" in user or "έκπτωση" in user
          or "discount" in user
          or "προσφορα" in user or "προσφορά" in user
          or "διδακτρα" in user or "δίδακτρα" in user):
        # User asked about tuition fees or available discounts
        print("UniChat: Υπάρχει έκπτωση 20% στα δίδακτρα για εγγραφές έως τα τέλη Φεβρουαρίου.")
        print("UniChat: Πώς αλλιώς μπορώ να σε βοηθήσω;")

    else:
        # No keyword matched — ask the user to try again
        print("UniChat: Συγγνώμη, δεν κατάλαβα την ερώτηση.")
        print("UniChat: Μπορείς να δοκιμάσεις ξανά.")


def main():
    # Start the chatbot: show the greeting and keep reading user input
    greet()

    while True:
        user = input("Εσύ: ").lower()

        # Stop the loop if the user types a goodbye keyword
        if user == "exit" or user == "τελος" or user == "αντιο":
            print("UniChat: Ευχαριστώ! Καλή συνέχεια.")
            break

        get_response(user)


# Run the terminal chatbot when this file is executed directly
if __name__ == "__main__":
    main()
