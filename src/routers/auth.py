from flask import Blueprint, render_template, jsonify, request, session, redirect, url_for
import src.logics.authLogic as authLogic
from werkzeug.utils import secure_filename


auth_url = Blueprint("auth", __name__)

@auth_url.route("/register", methods=["GET"])
def register_user():
	print(request.args)
	if request.args.get("email"):
		is_success = authLogic.register(request.args)
		if is_success == "success":
			return redirect("/login")
		else:
			return render_template("register.html", errorMessage=is_success)

	return render_template("register.html")

@auth_url.route("/login", methods=["GET"])
@auth_url.route("/", methods=["GET"])
def login_user():
	print(request.args)
	if request.args.get("username"):
		is_success = authLogic.login(request.args)
		if is_success == "success":
			return redirect("/home")
		else:
			return render_template("login.html", errorMessage=is_success)

	return render_template("login.html")

@auth_url.route("/logout", methods=["GET"])
def logout_user():
	session.clear()
	return redirect("/login")

@auth_url.route("/home", methods=["GET"])
@auth_url.route("/profile", methods=["GET"])
def profile():
	if session.get('username', None) == None:
		return redirect("/login")

	user = authLogic.getUser(session["username"])
	return render_template("profile.html", user = user)

@auth_url.route("/profile/edit", methods=["GET"])
def edit_profile():
	if session.get('username', None) == None:
		return redirect("/login")

	user = authLogic.getUser(session["username"])
	return render_template("editProfile.html", user = user)

@auth_url.route("/profile/edit", methods=["POST"])
def edit_profile_post():
	if session.get('username', None) == None:
		return redirect("/login")
	print(request.files)
	file = request.files['profile']
	if file.filename != '':
		filename = session["username"] + "." + file.filename.split(".")[-1].lower()
		file.save("static/profiles/" + filename)
		authLogic.editPicture(session["username"], filename)

	is_success = ""
	if request.form.get("employeeId"):
		is_success = authLogic.editUser(request.form)
		if is_success == "success":
			return redirect("/profile")

	user = authLogic.getUser(session["username"])
	return render_template("editProfile.html", user = user, errorMessage=is_success)