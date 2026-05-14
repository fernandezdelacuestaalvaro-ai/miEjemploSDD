from schemas import IncidentResponse


def classify_incident(incident_id: str, description: str) -> IncidentResponse:

    text = description.lower()

    if "password" in text:
        return IncidentResponse(
            incident_id=incident_id,
            category="ACCESS",
            confidence=0.95
        )

    if "network" in text:
        return IncidentResponse(
            incident_id=incident_id,
            category="NETWORK",
            confidence=0.90
        )

    return IncidentResponse(
        incident_id=incident_id,
        category="UNKNOWN",
        confidence=0.40
    )