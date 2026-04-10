from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(...,  min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validation(self) -> "SpaceMission":

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        ranks = [member.rank for member in self.crew]
        if Rank.COMMANDER not in ranks and Rank.CAPTAIN not in ranks:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced = [m for m in self.crew if m.years_experience >= 5]
            if len(experienced) / len(self.crew) < 0.5:
                raise ValueError("Long missions need 50% experienced crew (5+ years)")

        for member in self.crew:
            if not member.is_active:
                raise ValueError(...)

        return self

        
def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)
    print("Valid mission created:")
    try:
        sarah = CrewMember(
            member_id="ID001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=37,
            specialization="Mission Command",
            years_experience=5,
            is_active=True
        )
        john = CrewMember(
            member_id="ID002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=37,
            specialization="Navigation",
            years_experience=5,
            is_active=True
        )
        alice = CrewMember(
            member_id="ID003",
            name=" Alice Johnson",
            rank=Rank.OFFICER,
            age=37,
            specialization="Engineering",
            years_experience=5,
            is_active=True
        )
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2029, 8, 10),
            duration_days=900,
            crew=[sarah, john, alice],
            mission_status="success",
            budget_millions=2500.00
        )
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}.M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value}) - {member.specialization}")
        print(f"Mission: {mission.mission_name}\n")

    except ValidationError as e:
        print(f"Error: {e}")

    print("=" * 40)
    print("Expected validation error:")
    try:
        sarah = CrewMember(
            member_id="ID001",
            name="Sarah Connor",
            rank=Rank.OFFICER,
            age=37,
            specialization="Mission Command",
            years_experience=5,
            is_active=True
        )
        john = CrewMember(
                member_id="ID002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=37,
                specialization="Navigation",
                years_experience=5,
                is_active=True
        )
        alice = CrewMember(
                member_id="ID003",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=37,
                specialization="Engineering",
                years_experience=5,
                is_active=True
        )
        mission = SpaceMission(
                mission_id="M2024_MARS",
                mission_name="Mars Colony Establishment",
                destination="Mars",
                launch_date=datetime(2029, 8, 10),
                duration_days=900,
                crew=[sarah, john, alice],
                mission_status="success",
                budget_millions=2500.00
        )
    except ValidationError as e:
        errors = e.errors()
        print(errors[0]['msg'])


if __name__ == "__main__":
    main()
