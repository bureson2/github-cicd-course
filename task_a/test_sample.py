def test_example():
    assert 1 + 1 == 2

def test_generate_html():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test Report</title>
    </head>
    <body>
        <h1>Výsledek testu</h1>
        <p>Test proběhl úspěšně!</p>
    </body>
    </html>
    """
    with open("report.html", "w") as f:
        f.write(html_content)

    assert "Test" in html_content
