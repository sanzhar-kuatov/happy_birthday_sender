from flask import Flask, request, render_template

app = Flask(__name__)

latest_people = []

@app.route("/birthday", methods=["POST"])
def birthday():
    global latest_people

    data = request.get_json()
    latest_people = data.get("people", [])

    return {
        "message": "Birthday page generated",
        "preview_url": "http://localhost:5000/preview"
    }

@app.route("/preview")
def preview():
    return render_template(
        "birthday.html",
        people=latest_people
    )


if __name__ == "__main__":
    app.run(debug=True)