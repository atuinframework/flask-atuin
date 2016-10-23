#!/usr/bin/env python
# - coding: utf-8 -
import sys
import time
import datetime
import random
import csv
import re
import pprint

from handler import app
from datastore import db

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


from auth.models import *
from logs.models import *

from allegati.models import *
from convenzioni.models import *
from profiles.models import *

from clienti.models import *
from visite.models import *


@manager.command
def create_admin():
	print "Creating admin..."
	
	u = User(usertype="staff", username="admin", name="Admin", role="ADMIN")
	u.set_password('admin')
	db.session.add(u)

	db.session.commit()


@manager.command
def create_demo_users():
	print "Deleting demo users..."
	
	db.session.commit()

@manager.command
def update_policies():
	print "Updating policies..."
	
	UserPolicy.query.delete()
	
	db.session.add(UserPolicy(desc="Agent", role='AGENT', functions=','.join([
		
															])))
	
	db.session.add(UserPolicy(desc="Addetto medicina", role='ADDETTO_MEDICINA', functions=','.join([
		"VISITE_MEDICHE", "GESTIONE_VISITE_MEDICHE"
															])))
	
	db.session.add(UserPolicy(desc="User", role='USER', functions=','.join([
		
															])))
	
	db.session.commit()



@manager.command
def import_ateco():
	#map(db.session.delete, Ateco.query)

	f = open("import_data/ateco2007.csv")
	fr = csv.DictReader(f, delimiter="\t")
	
	for r in fr:
		a = Ateco.find_or_create(codice=r["codice"])
		a.log_user("SCRIPT", "0.0.0.0")
		
		a.anno = r.get("anno", 2007)
		
		a.rischio = r["rischio"]

		a.attivita = r["attivita"]
		a.categoria = r["categoria"]
		a.sotto_categoria = r["sottocategoria"]
		
		if not a.id:
			db.session.add(a)
	
	
	db.session.commit()
	



@manager.command
def import_convenzioni():
	map(db.session.delete, Convenzione.query)
	map(db.session.delete, ServizioConvenzione.query)
	db.session.commit()
	
	servizi_import = (
		("SICUREZZA", "Sicurezza", ()),
		("RSPP", "RSPP", ()),
		("MEDICINA_LAVORO", "Medicina del lavoro", (
												("ESAMI_LABORATORIO", "Esami di laboratorio"),
											)),
		("AMBIENTE", "Ambiente", ()),
		("MACCHINE", "Macchine", ()),
		("ADR", "ADR", ()),
		("DATORE_LAVORO", "Datore Lavoro", ()),
		("RESP_TECNICO", "Responsabile Tecnico", ()),
		("RESP_PRIVACY", "Responsabile Privacy", ()),
		("RESP_AMIANTO", "Responsabile Amianto", ()),
		("ASPP", "ASPP", ()),
		("TELESISTRI", "Telesistri", ()),
		("SICUREZZA_CANTIERI_POS", "Sicurezza Cantieri Pos", ()),
		("AGGIORNAMENTO_PRIVACY", "Aggiornamenti Privacy", ()),
		("ASSISTENZA_OHSAS", "Assistenza OHSAS", ())

		#Sicurezza+RSPP
		#Sicurezza+Ambiente
		#Sicurezza+Ambiente+RSPP
		#Sicurezza + Macchine
		#Sicurezza +Ambiente +Assistenza OHSAS
		#Sicurezza + Ambiente + Macchine

	)

	for (servizio, desc, sub_services) in servizi_import:
		s = ServizioConvenzione.find_or_create(servizio=servizio, parent_id=0)
		
		if not s.id:
			db.session.add(s)
			db.session.flush()

		s.descrizione = desc
		s.log_user("SCRIPT", "0.0.0.0")
		
		for (sub_servizio, sub_desc) in sub_services:
			sub_serv = ServizioConvenzione.find_or_create(servizio=sub_servizio, parent_id=s.id)
			
			sub_serv.descrizione = sub_desc
			sub_serv.log_user("SCRIPT", "0.0.0.0")

			if not sub_serv.id:
				db.session.add(sub_serv)
				
	db.session.commit()
	
	conversione_servizi = {
		'ADR' : "ADR",
		'ASPP' : "ASPP",
		'Aggiornamenti Privacy' : "AGGIORNAMENTO_PRIVACY",
		'Ambiente' : "AMBIENTE",
		'Datore Lavoro' : "DATORE_LAVORO",
		'Macchine' : "MACCHINE",
		'Medicina del lavoro' : "MEDICINA_LAVORO",
		'RSPP' : "RSPP",
		'Resp. Amianto' : "RESP_AMIANTO",
		'Resp.Tecnico' : "RESP_TECNICO",
		'Responsabile Privacy' : "RESP_PRIVACY",
		'Sicurezza Cantieri Pos' : "SICUREZZA_CANTIERI_POS",
	
		'Sicurezza' : "SICUREZZA",
		'Telesistri' : "TELESISTRI",
		'Assistenza OHSAS' : "ASSISTENZA_OHSAS",
		#'Sicurezza + Ambiente + Macchine' : [""],
		#
		#'Sicurezza + Macchine' : [],
		#'Sicurezza +Ambiente +Assistenza OHSAS' : [""],
		#'Sicurezza+Ambiente' : [],
		#'Sicurezza+Ambiente+RSPP': [],
		#'Sicurezza+RSPP' : [],
	}
	
	f = open("import_data/convenzioni.csv")
	fr = csv.DictReader(f, delimiter="\t")
	
	#with db.session.no_autoflush:
	if 1:
		for (idx, conv) in enumerate(fr):
			
			cliente = Cliente.query.filter_by(id=conv["ditta"]).first()
			
			if not cliente:
				continue
			
			servizi_list = filter(None, [conversione_servizi.get(s.strip(), "") for s in conv["servizi_conv"].split("+")])
			
			c = Convenzione.filter_servizi(servizi_list).filter_by(cliente_id=conv["ditta"]).first()
			
			if not c:
				c = Convenzione()
				c.cliente = cliente
				c.set_servizi(servizi_list)
				db.session.add(c)

			c.responsabile = User.query.filter_by(username=conv["responsabile"]).first()
			c.status = conv["stato_conv"]		
			c.note = conv["note"]
	
			c.gennaio = float(conv["gennaio"])
			c.febbraio = float(conv["febbraio"])
			c.marzo = float(conv["marzo"])
			c.aprile = float(conv["aprile"])
			c.maggio = float(conv["maggio"])
			c.giugno = float(conv["giugno"])
			c.luglio = float(conv["luglio"])
			c.agosto = float(conv["agosto"])
			c.settembre = float(conv["settembre"])
			c.ottobre = float(conv["ottobre"])
			c.novembre = float(conv["novembre"])
			c.dicembre = float(conv["dicembre"])
	
			c.log_user("SCRIPT", "0.0.0.0")

	db.session.commit()




@manager.command
def create_demo_data():
	print("Deleting demo data...")
	
	map(db.session.delete, Nominativo.query)
	map(db.session.delete, Cliente.query)
	map(db.session.delete, Persona.query)
	
	#map(db.session.delete, Visita.query)
	#map(db.session.delete, Idoneita.query)
	db.session.commit()


	print("Clienti...")
	c = Cliente()
	c.ragione_sociale = "Scalebox"	
	c.partita_iva = "761754543"	
	c.citta = "S. Ilario"
	c.comune = "S. Ilario"
	c.provincia = "RE"
	c.indirizzo= "Via Salvador Allende"
	c.cap = 42029
	c.pec = "scalebox@pec.it"

	db.session.add(c)
	db.session.flush()
	id_scalebox = c.id

	c = Cliente()
	c.ragione_sociale = "Rivi"	
	c.partita_iva = "123893"	
	c.citta = "Reggio Emilia"
	c.comune = "Reggio Emilia"
	c.provincia = "RE"
	c.indirizzo= "Via Ferravilla"
	c.cap = 42124
	c.pec = "rivi@pec.it"

	db.session.add(c)
	db.session.flush()

	c = Cliente()
	c.ragione_sociale = "Caldaie Rotte snc"	
	c.partita_iva = "86513489"	
	c.citta = "Montecavolo"
	c.comune = "Quattro Castella"
	c.provincia = "RE"
	c.indirizzo= "Via Vattelapesca"
	c.cap = 42124
	c.pec = "latuacaldaiasnc@pec.it"

	db.session.add(c)
	db.session.flush()
	id_caldaia = c.id


	print("Persone...")
	p = Persona()
	p.nominativo = "Luca Zarotti"	
	p.codice_fiscale = "zrtlcuh82h223t"
	p.email = {"lavoro":"luca.zarotti@scalebox.it"}
	p.citta = "Reggio Emilia"
	p.comune = "Reggio Emilia"
	p.provincia = "RE"
	p.indirizzo= "Via caffè"
	p.cap = 42100
	p.data_nascita = "1982-06-01"
	p.citta_nascita = "Reggio Emilia"
	p.comune_nascita = "Reggio Emilia"
	p.provincia_nascita = "RE"
	p.cap_nascita = 42100

	db.session.add(p)
	db.session.flush()
	id_luca = p.id
	
	p = Persona()
	p.nominativo = "Casciello Paolo"	
	p.codice_fiscale = "csfe4231524qew"
	p.email = {"lavoro":"paolo.casciello@scalebox.it"}
	p.citta = "Reggio Emilia"
	p.comune = "Reggio Emilia"
	p.provincia = "RE"
	p.indirizzo= "Via di qui"
	p.cap = 42124
	p.data_nascita = "1982-06-01"
	p.citta_nascita = "S. Ilario"
	p.comune_nascita = "S.Ilario"
	p.provincia_nascita = "RE"
	p.cap_nascita = 42121

	db.session.add(p)
	db.session.flush()
	id_paolo = p.id

	print("Nominativi...")
	n = Nominativo()
	n.persona_id = id_luca
	n.cliente_id = id_scalebox
	n.mansione = "Videoterminalista"
	n.status = "ACTIVE"

	db.session.add(n)
	db.session.flush()
	
	n = Nominativo()
	n.persona_id = id_paolo
	n.cliente_id = id_caldaia
	n.mansione = "Impiegato"
	db.session.add(n)
	nn = n.transfer(id_scalebox, "Videoterminalista")
	nn.status = "ACTIVE"
	db.session.add(nn)
	
	db.session.commit()



@manager.command
def import_persone_csv():
	f = open("import_data/nominativi_norm.csv")
	vm = csv.DictReader(f, delimiter="\t")

	records = list(vm)
	f.close()

	map(db.session.delete, Nominativo.query)
	db.session.commit()

	map(db.session.delete, Persona.query)
	db.session.commit()

	errors_found = []

	for (idx, p) in enumerate(records):
		
		print("=" * 80)
		print("NUOVO RECORD = {}".format(idx))
		print("-" * 80)
		pprint.pprint(p)
		print("=" * 80)

		p = {k:(v and v.strip() or "") for (k,v) in p.iteritems()}
		
		luogo = re.split(r"(?:\((\w+)\))?\s*$", p["luogo_nascita"])

		provincia = ""
		if len(luogo) > 1:
			provincia = luogo[1].strip()
		
		luogo = luogo[0].strip()

		p_search = {
			"nominativo" : p["nominativo"],

			"nazione_nascita" : "Italia",
			"comune_nascita" : luogo,
		}
		
		try:
			p_search["data_nascita"] = datetime.datetime.strptime(p["data_nascita"], "%d-%m-%Y"),

		except:
			#month / day / Year   
			try:
				
				p_search["data_nascita"] = datetime.datetime.strptime(p["data_nascita"], "%m/%d/%Y"),
			except:

				errors_found.append((idx, p))
				continue

		persona = Persona.find_or_create(**p_search)
		persona.log_user("SCRIPT", "0.0.0.0")
		
		if not persona.id:
			db.session.add(persona)

			persona.nominativi=[Nominativo(cliente_id=p["id_ditta"])]

		persona.status = "ACTIVE"

		#fields to update
		persona.citta_nascita = luogo				
	

	f = open("last_import.log", "w")

	if errors_found:
		f.close()

		print("\n\nERRORI RISCONTATI: esaminare il file last_import.log")

		with open('last_import.log', 'a') as fout:
			for (idx, p) in errors_found:
				fout.write("\n")

				d = {"row" : idx+1, "data":p}
				pprint.pprint(d, stream=fout)

				fout.write("\n|" + ("=-=" * 26) + "|\n")
	else:
		f.write("NO_ERRORS")
		f.close()
	
	db.session.commit()



@manager.command
def import_visite_csv():
	f = open("import_data/visite_mediche.csv")
	vm = csv.DictReader(f)

	# truncate `visite`; truncate `idoneita`; truncate `nominativi`; truncate `clienti`; truncate `persone`; truncate `allegati`;

	records = list(vm)
	f.close()

	map(db.session.delete, Visita.query)
	db.session.commit()
	

	giudizio_conversion = {
		"IDONEO" : "IDONEO",
		"IDONEO CON NOTE" : "IDONEO_NOTE",
		"PRESCRIZIONE/LIMITAZIONE" : "PRESCRIZIONE_LIMITAZIONE",
		"NON IDONEO" : "NON_IDONEO"
	}

	tipologia_conversion = {
		"ALCOOL TEST" : "ALCOOL_TEST",
		"AUDIOMETRIA" : "AUDIOMETRIA",
		"ELETTROCARDIOGRAMMA": "ELETTROCARDIOGRAMMA",
		"ESAMI BIOUMORALI" : "ESAMI_TOSSICOLOGICI",
		"ESAMI DEL SANGUE" : "ESAMI_LABORATORIO",
		"ESAMI EMATOSIERICI" : "ESAMI_BIOUMORALI",
		"ESAMI TOSSICOLOGICI" : "ESAMI_EMATOSIERICI",
		"PIOMBEMIA" : "PIOMBEMIA",
		"PRIMA VISITA" : "PRIMA_VISITA",
		"SPIROMETRIA" : "SPIROMETRIA",
		"STIRENE" : "STIRENE",
		"VISIOTEST" : "VISIOTEST",
		"VISITA PERIODICA" : "VISITA_PERIODICA",
	}

	lost_and_found = []

	for v in records:
		cliente_id = int(v["ID"])

		nominativo = Nominativo.query.filter_by(
			cliente_id=cliente_id).filter(
				Nominativo.persona_id.in_(
					[i[0] for i in Persona.query.with_entities(Persona.id).filter(Persona.nominativo.like(v["nominativo"])).all()]
				)).first()

		#Nominativo.query.filter_by(cliente_id=cliente_id).filter(Nominativo.persona_id.in_([i[0] for i in Persona.query.with_entities(Persona.id).filter(Persona.nominativo.like(nstring)).all()])).first()

		if not nominativo:
			p = Persona(nominativo=v["nominativo"],
					status="ACTIVE",
					ins_username="SCRIPT",
					upd_username="SCRIPT",
					ins_address="0.0.0.0",
					upd_address="0.0.0.0"
				)
			db.session.add(p)
			db.session.flush()
			
			nominativo = Nominativo(persona_id=p.id, cliente_id=cliente_id,
					ins_username="SCRIPT",
					upd_username="SCRIPT",
					ins_address="0.0.0.0",
					upd_address="0.0.0.0"
			)
			db.session.add(nominativo)
			db.session.flush()
		
		db.session.add(Visita(
			status="ACTIVE",
			id=v["key"],
			tipologia=tipologia_conversion.get(v["tipovisita"], v["tipovisita"]),
			nominativo_id=nominativo.id,
	
			data_visita=datetime.datetime.strptime(v["datavisita"].replace("0000-00-00", "1970-01-01"), "%Y-%m-%d") if v["datavisita"].replace("NULL", "") else "1970-01-01",
			scadenza_visita=datetime.datetime.strptime(v["scadenzavisita"].replace("0000-00-00", "1970-01-01"), "%Y-%m-%d") if v["scadenzavisita"].replace("NULL", "") else "1970-01-01",

			ins_username="SCRIPT",
			upd_username="SCRIPT",
			ins_address="0.0.0.0",
			upd_address="0.0.0.0"
		))
		
		
		if v["tipovisita"] in ("VISITA PERIODICA", "PRIMA VISITA"):
			idoneita = Idoneita(
				status="ACTIVE",
				nominativo_id=nominativo.id,
				giudizio=giudizio_conversion.get(v["giudizio"], v["giudizio"]),
				
				data_idoneita=datetime.datetime.strptime(v["datavisita"].replace("0000-00-00", "1970-01-01"), "%Y-%m-%d") if v["datavisita"].replace("NULL", "") else "1970-01-01",
				scadenza_idoneita=datetime.datetime.strptime(v["scadenzavisita"].replace("0000-00-00", "1970-01-01"), "%Y-%m-%d") if v["scadenzavisita"].replace("NULL", "") else "1970-01-01",

				note=v["note"],

				ins_username="SCRIPT",
				upd_username="SCRIPT",
				ins_address="0.0.0.0",
				upd_address="0.0.0.0"
				
			)
			db.session.add(idoneita)
			db.session.flush()
			
			allegato_fname = v.get("idoneita", "")
			if allegato_fname:
				a = Allegato(
					attach_id = idoneita.id,
					tipologia="IDONEITA",
					ins_username="SCRIPT",
					upd_username="SCRIPT",
					ins_address="0.0.0.0",
					upd_address="0.0.0.0"
				)
				a.set_path("documents/idoneita/" + allegato_fname)
				db.session.add(a)			


	

	db.session.commit()

@manager.command
def import_clienti_csv():
	f = open("import_data/clienti.csv")
	cc = csv.DictReader(f)
	records = list(cc)
	f.close()

	map(db.session.delete, Cliente.query.filter(Cliente.id.in_(c["ID"] for c in records)).all())
	db.session.commit()

	
	map(db.session.add, [Cliente(
		status="ACTIVE",
		id=c["ID"],
		ragione_sociale=c["Ditta"],
		partita_iva=c["PartitaIva"],
		pec=c["pec"],
		citta="",
		provincia=c["Provincia"].rsplit("(", 1)[0].strip(),
		comune=c["Comune"],
		cap=c["CAP"],
		indirizzo=c["Indirizzo"],
		ins_username="SCRIPT",
		upd_username="SCRIPT",
		ins_address="0.0.0.0",
		upd_address="0.0.0.0"
	) for c in records])
	
	db.session.commit()




@manager.command
def populate_mansioni():
	mansioni_tuple = (
		("ACTIVE", "IMPIEGATO", "Impiegato"),
		("ACTIVE", "OPERAIO", "Operaio"),
	)

	attivita_tuple = (
		("ACTIVE", "SALDATURA", "Saldatura"),
		("ACTIVE", "TAGLIO", "Taglio"),
		("ACTIVE", "VERNICIATURA", "Verniciatura"),
		("ACTIVE", "VIDEOTERMINALE", "VideoTerminale"),
	)

	for (status, name, desc) in mansioni_tuple:
		
		m = Mansione.find_or_create(nome=name)
		if not m.id:
			db.session.add(m)

		m.descrizione = desc
		m.status = status
		
	
	for (status, name, desc) in attivita_tuple:
		
		a = Attivita.find_or_create(nome=name)
		if not a.id:
			db.session.add(a)

		a.descrizione = desc
		a.status = status
	

	db.session.commit()











if __name__ == '__main__':
	manager.run()
	

	


