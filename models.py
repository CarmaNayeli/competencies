from typing import List

class Course:
    def __init__(self, code: str, name: str, prerequisites: List[str] = None):
        self.code = code
        self.name = name
        self.prerequisites = prerequisites or []

    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'prerequisites': self.prerequisites
        }

    @staticmethod
    def from_dict(data):
        return Course(data['code'], data['name'], data['prerequisites'])

    def __str__(self):
        return f"{self.code}: {self.name} (Prerequisites: {', '.join(self.prerequisites) or 'None'})"
