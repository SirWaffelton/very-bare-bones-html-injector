from flask import Flask, request, render_template_string

app = Flask(__name__)

# A basic template with a form and injected content placeholder
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Simple HTML Injector</title>
</head>
<body>
    <h1>Simple HTML Injector Demo</h1>
    <form method="POST">
        <label for="html_input">Enter HTML to inject:</label><br>
        <textarea id="html_input" name="html_input" rows="5" cols="60"></textarea><br><br>
        <input type="submit" value="Inject HTML">
    </form>
    <hr>
    <h2>Injected Content:</h2>
    <div style="border: 1px solid #ccc; padding: 10px;">
        {{ injected_html | safe }}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    injected_html = ""
    if request.method == "POST":
        # Get user HTML input
        injected_html = request.form.get("html_input", "")
    # Render the template with the injected HTML
    return render_template_string(HTML_TEMPLATE, injected_html=injected_html)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
