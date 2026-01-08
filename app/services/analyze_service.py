import random

def analyze_image(image_id:str):
    skin_types = ["Oily", "Dry", "Combination", "Normal", "Bloated"]
    issues = ["Acne", "Hyperpigmentation", "Redness", "Wrinkles", "None"];

    detected_issues = random.sample(issues, k=1)
    if "None" in detected_issues and len(detected_issues) > 1:
        detected_issues.remove("None")

    result = {
        "image_id": image_id,
        "skin_type": random.choice(skin_types),
        "issues": detected_issues,
        "confidence": round(random.uniform(0.7, 0.99), 2)
    }
    return result