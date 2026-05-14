from classifier import classify_incident


def main():

    incident_id = "INC-001"

    description = "Voy a cambiarsourceTree"

    response = classify_incident(
        incident_id=incident_id,
        description=description
    )

    print("=== RESULT ===")
    print(f"Incident: {response.incident_id}")
    print(f"Category: {response.category}")
    print(f"Confidence: {response.confidence}")


if __name__ == "__main__":
    main()