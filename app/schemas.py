from dataclasses import dataclass


@dataclass
class IncidentRequest:
    incident_id: str
    description: str


@dataclass
class IncidentResponse:
    incident_id: str
    category: str
    confidence: float