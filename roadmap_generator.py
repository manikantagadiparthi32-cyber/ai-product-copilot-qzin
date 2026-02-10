def generate_roadmap(top_issue):
    return {
        "Now": [f"Fix critical {top_issue} issues"],
        "Next": [f"Improve {top_issue} experience"],
        "Later": ["Advanced personalization", "Automation"]
    }
