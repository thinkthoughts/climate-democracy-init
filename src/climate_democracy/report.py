from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json


@dataclass
class LocalClimateReport:
    title: str
    watershed: str
    school_district: str
    initiative: str
    actionable_summary: str

    def to_markdown(self) -> str:
        return f"""# {self.title}

## Local geography

- Watershed: {self.watershed}
- School district: {self.school_district}
- Initiative: {self.initiative}

## Actionable summary

{self.actionable_summary}
"""

    def save(self, outdir: str | Path = "docs/reports") -> None:
        out = Path(outdir)
        out.mkdir(parents=True, exist_ok=True)
        slug = self.title.lower().replace(" ", "-")
        (out / f"{slug}.md").write_text(self.to_markdown(), encoding="utf-8")
        (out / f"{slug}.json").write_text(json.dumps(asdict(self), indent=2), encoding="utf-8")
