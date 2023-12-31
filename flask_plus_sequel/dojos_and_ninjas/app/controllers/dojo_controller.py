from app import app
from flask import Flask, render_template, redirect, request, session
from app.models.dojo_model import Dojo


@app.route('/dojos')          
def get_all_dojos():
    dojos=Dojo.get_all_users()
    #print (dojos)
    return render_template("show_all_dojos.html", dojos=dojos )

@app.route('/add_dojo', methods=['POST'])
def add_dojo():
    data=request.form
    Dojo.save(data)
    return redirect("/dojos")

@app.route('/dojo/<int:id>')
def dojo_ninjas(id):
    data={
        "id":id
    }
    one_dojo=Dojo.get_ninjas_from_dojo(data)
    print("!!!!!!", one_dojo.id)
    session['id']=one_dojo.id
    print('?????', session['id'])
    return render_template("dojo_show.html", one_dojo=one_dojo)

@app.route('/ninja/delete/<int:id>')
def delete_ninja(id):
    data={
        "id":id
    }
    Dojo.delete_ninja(data)
    return redirect(f'/dojo/{session["id"]}')





