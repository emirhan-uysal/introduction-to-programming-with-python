def generate_html_report(summary: dict, output_file: str = "report.html"):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{summary['title']}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                color: #333;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 600px;
                margin: auto;
                background: white;
                padding: 30px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
            }}
            h1 {{
                color: #2c3e50;
                text-align: center;
                margin-bottom: 30px;
            }}
            .result {{
                display: flex;
                justify-content: space-between;
                margin: 10px 0;
                font-size: 1.1em;
            }}
            .result span {{
                font-weight: bold;
            }}
            .status {{
                text-align: center;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
                color: white;
                background-color: {"#2ecc71" if summary['all_passed'] else "#e74c3c"};
                margin-top: 30px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{summary['title']}</h1>
            <div class="result"><span>Total Tests:</span> {summary['total']}</div>
            <div class="result"><span>Passed:</span> {summary['passed']}</div>
            <div class="result"><span>Failed:</span> {summary['failed']}</div>
            <div class="result"><span>Duration:</span> {summary['duration_seconds']} seconds</div>
            <div class="result"><span>Pass Percentage:</span> {summary['pass_percentage']}%</div>
            <div class="status">
                {"All tests passed!" if summary['all_passed'] else "Some tests failed."}
            </div>
        </div>
    </body>
    </html>
    """

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Report written to {output_file}")
