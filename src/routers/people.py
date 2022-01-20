from flask import Blueprint, render_template, jsonify, request, session, redirect, url_for
import src.logics.peopleLogic as peopleLogic

people_url = Blueprint("staff", __name__)

@people_url.route("/staffs", methods=["GET"])
def view_staffs():
	if session.get('username', None) == None:
		return redirect("/login")

	staffs = peopleLogic.getStaffs()
	return render_template("staffs.html", staffs = staffs)

@people_url.route("/staffs/add", methods=["GET"])
def add_staffs():
	if session.get('username', None) == None:
		return redirect("/login")
	if request.args.get("email"):
		is_success = peopleLogic.addStaffs(request.args)
		if is_success == "success":
			return redirect("/staffs")

	staffs = peopleLogic.getStaffs()
	return render_template("addStaff.html", staffs = staffs)
