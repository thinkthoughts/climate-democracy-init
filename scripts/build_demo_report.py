from climate_democracy.report import LocalClimateReport

report = LocalClimateReport(
    title="Climate Democracy Init Report",
    watershed="Replace with local watershed",
    school_district="Replace with local school district",
    initiative="Replace with official climate democracy initiative name",
    actionable_summary="Draft a local reading/writing workflow that connects climate action to shared public geography.",
)

report.save()
print("Wrote demo report to docs/reports/")
