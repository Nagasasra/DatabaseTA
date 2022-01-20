from flask import Blueprint, render_template, jsonify, request, session, redirect, url_for
import src.logics.transLogic as transLogic
import src.logics.peopleLogic as peopleLogic
import src.logics.menuLogic as menuLogic

trans_url = Blueprint("trans", __name__)

@trans_url.route("/transactions", methods=["GET"])
def view_transactions():
	if session.get('username', None) == None:
		return redirect("/login")

	transactions = transLogic.getTransactions()
	return render_template("transactions.html", transactions = transactions)

@trans_url.route("/transactions/add", methods=["GET"])
def add_transactions():
	if session.get('username', None) == None:
		return redirect("/login")
	if len(request.args) > 0:
		is_success = transLogic.addTransactions(request.args)
		if is_success == "success":
			return redirect("/transactions")

	transactions = transLogic.getTransactions()
	staffs = peopleLogic.getStaffs()
	tables = menuLogic.getTables()
	return render_template("addTransaction.html", transactions = transactions, staffs = staffs, tables = tables)

@trans_url.route("/transactions/edit/<id_trx>", methods=["GET"])
def edit_transactions(id_trx):
	if session.get('username', None) == None:
		return redirect("/login")
	if len(request.args) > 0:
		is_success = transLogic.editTransactions(request.args)
		if is_success == "success":
			return redirect("/transactions")

	transaction = transLogic.getTransaction(id_trx)
	return render_template("editTransaction.html", transaction = transaction)


@trans_url.route("/transactionmenus/<id_trx>", methods=["GET"])
def view_transactionmenus(id_trx):
	if session.get('username', None) == None:
		return redirect("/login")

	menus = transLogic.getTransactionMenu(id_trx)
	transaction = transLogic.getTransaction(id_trx)
	return render_template("viewTransaction.html", menus = menus, transaction = transaction)

@trans_url.route("/transactionmenus/add/<id_trx>", methods=["GET"])
def add_transactionmenus(id_trx):
	if session.get('username', None) == None:
		return redirect("/login")
	is_success = ""
	if len(request.args) > 0:
		is_success = transLogic.addTransactionMenu(request.args)
		if is_success == "success":
			transLogic.updatePrices(id_trx)
			return redirect("/transactionmenus/"+str(id_trx))

	menus = menuLogic.getMenus()
	return render_template("addMenu.html", menus = menus, id_trx = id_trx, errorMessage = is_success)

@trans_url.route("/transactionmenus/delete/<id_trx>/<menuId>", methods=["GET"])
def delete_transactionmenus(id_trx, menuId):
	if session.get('username', None) == None:
		return redirect("/login")

	transLogic.deleteTransactionMenu(id_trx, menuId)
	transLogic.updatePrices(id_trx)
	return redirect("/transactionmenus/"+str(id_trx))