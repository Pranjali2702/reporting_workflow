from src.extract import extract_data
from src.transform import transform
from src.report import build_report
from src.notify import send_report

df = extract_data('sql/queries.sql')
summary = transform(df)
build_report(summary, 'output/report.xlsx')

send_report(
    recipients=['pranjalibisht5@gmail.com'],  # send to yourself for testing
    subject='Test Report - Reporting Workflow',
    body='This is a test of the automated reporting pipeline.',
    attachment_path='output/report.xlsx'
)

print("Report generated and emailed successfully.")