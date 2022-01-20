from flask import Blueprint, render_template, jsonify, request, session, redirect, url_for
import src.logics.menuLogic as menuLogic

menu_url = Blueprint("menu", __name__)

@menu_url.route("/menus", methods=["GET"])
def view_menus():
	if session.get('username', None) == None:
		return redirect("/login")

	menus = menuLogic.getMenus()
	return render_template("menus.html", menus = menus)

@menu_url.route("/menus/add", methods=["GET"])
def add_menus():
	if session.get('username', None) == None:
		return redirect("/login")
	if len(request.args) > 0:
		is_success = menuLogic.addMenus(request.args)
		if is_success == "success":
			return redirect("/menus")

	menus = menuLogic.getMenus()
	return render_template("addMenu.html", menus = menus)

@menu_url.route("/categories", methods=["GET"])
def view_categories():
	if session.get('username', None) == None:
		return redirect("/login")

	categories = menuLogic.getMenuCategories()
	return render_template("categories.html", categories = categories)

@menu_url.route("/categories/add", methods=["GET"])
def add_categories():
	if session.get('username', None) == None:
		return redirect("/login")
	if len(request.args) > 0:
		is_success = menuLogic.addMenuCategories(request.args)
		if is_success == "success":
			return redirect("/categories")

	categories = menuLogic.getMenuCategories()
	return render_template("addCategories.html", categories = categories)

@menu_url.route("/tables", methods=["GET"])
def view_tables():
	if session.get('username', None) == None:
		return redirect("/login")

	tables = menuLogic.getTables()
	return render_template("tables.html", tables = tables)