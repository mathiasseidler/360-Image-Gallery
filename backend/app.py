from flask import Flask, send_from_directory, request, redirect, Response
from data_controller import Image360DataController

app = Flask(__name__)
data_ctrl = Image360DataController()
# Path for our main Svelte page

@app.route("/")
def base():
    return send_from_directory('../frontend/public', 'index.html')


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('../frontend/public', path)


@app.route("/images/<path:path>")
def images(path):
    return send_from_directory('../data/images', path)





@app.route('/upload', methods=['POST'])
def upload_file():
    # print(request.form.to_dict(flat=False))
    for uploaded_file in request.files.getlist('360photos'):
        if uploaded_file.filename != '':
            uploaded_file.save('../data/images/' + uploaded_file.filename)
    return Response('Hello World!')

# A route to return all of the available entries in our catalog.


@app.route('/api/v1/projects', methods=['GET'])
def return_all_projects():
    all_projects = data_ctrl.get_projects_df()
    return all_projects.to_json()


if __name__ == "__main__":
    app.run(debug=True, port=4000)
