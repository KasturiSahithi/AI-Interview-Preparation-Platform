from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf(
    filename,
    resume_score,
    detected_skills,
    career_paths,
    resume_analysis,
    questions,
    feedback
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Interview Preparation Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"Resume Score: {resume_score}/100",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Detected Skills",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            ", ".join(detected_skills),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Career Recommendations",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            ", ".join(career_paths),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Resume Analysis",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            str(resume_analysis),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Interview Questions",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            str(questions),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Interview Feedback",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            str(feedback),
            styles["BodyText"]
        )
    )

    doc.build(content)

    return filename