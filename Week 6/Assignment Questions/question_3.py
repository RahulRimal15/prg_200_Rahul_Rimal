exam_date = "August 20, 2026"


def schedule_exam():
    subject = "Python Programming"

    def update_date():
        nonlocal subject
        subject = subject + " - Final Exam"

        # By Rahul Rimal

    update_date()

    print("Exam Subject:", subject)
    print("Exam Date:", exam_date)


schedule_exam()

