import sqlite3
from flask import Flask, redirect, render_template, request, url_for
from asyncio.windows_events import NULL
from pickle import TRUE
from tkinter import *
from pyfirmata import Arduino, SERVO
from test import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	coneccao = sqlite3.connect("automSQL.db")
	cursor = coneccao.cursor()
	if (request.method == 'POST'):
		if 'controle' in request.form.to_dict():
			task_content = request.form.to_dict()

			aux = "select * from automacao WHERE ambiente = " + "'" + task_content['controle'] + "'"
			cursor.execute(aux)
			status = cursor.fetchall()

			if(task_content['val'] == 'ON'):
				if(task_content['controle'] == 'Sala'):
					ledon(2)
				elif(task_content['controle'] == 'Cozinha'):
					ledon(7)
				elif(task_content['controle'] == 'Quarto'):
					ledon(8)
				elif(task_content['controle'] == 'Suite'):
					ledon(12)
				elif(task_content['controle'] == 'Banheiro'):
					ledon(13)
				elif(task_content['controle'] == 'Alarme'):
					Blink()

					
			elif(task_content['val'] == 'Alterar'):
				task_content = request.form['content']
				servoctrl(task_content)
			else:
				if(task_content['controle'] == 'Sala'):
					ledoff(2)	
				elif(task_content['controle'] == 'Cozinha'):
					ledoff(7)
				elif(task_content['controle'] == 'Quarto'):
					ledoff(8)
				elif(task_content['controle'] == 'Suite'):
					ledoff(12)
				elif(task_content['controle'] == 'Banheiro'):
					ledoff(13)
				elif(task_content['controle']== 'Alarme'):
					Blinkoff()


			cursor.execute("select * from automacao")
			status = cursor.fetchall()
			coneccao.commit()
			coneccao.close()

			return render_template('index.html', contents=status)
	else:
		cursor.execute("select * from automacao")
		status = cursor.fetchall()
		return render_template('index.html', contents=status)

listaAmbientes = [
	("Sala","Lampada","", "OFF", 0,"18/08/2022 08:00:00", "18/08/2022 18:00:00"),
	("Sala","Alarme", "Seg Ter Qua Qui Sex Sab Dom", "ON", 24,"",""),
	("Sala","Temperatura", "Seg Ter Qua Qui Sex Sab Dom", "ON", 24,"",""),
	("Cozinha","Lampada", "Seg Ter Qua Qui Sex Sab Dom", "OFF", 0, "08:00:00", "18:00:00"),
	("Quarto","Lampada", "", "OFF", 4, "18/08/2022 08:00:00", ""),
	("Suite","Lampada", "", "OFF", 2,"", "18/08/2022 18:00:00"),
	("Banheiro","Lampada", "Seg Ter Qua Qui Sex Sab Dom", "OFF", 24,"", "")
]

if __name__ == "__main__":
    app.run(host = '10.15.112.55')