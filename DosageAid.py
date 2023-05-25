# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 23:37:01 2023

@author: Hajar
"""


import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px

# Liste von Benutzername-Passwort-Paaren
USERS = [
    {"username": "zhaw", "password": "123"},
]

 

def login():
    st.title("Login")
    username = st.text_input("Benutzername")
    password = st.text_input("Passwort", type="password")
    login_button = st.button("Einloggen")

 

    if login_button:
        for user in USERS:
            if username == user["username"] and password == user["password"]:
                st.success("Erfolgreich eingeloggt!")
                st.session_state.authenticated = True
                main()
                return

 

        st.error("Ungültiger Benutzername oder Passwort!")
    
    

def page_home():
    image_url = "https://media.istockphoto.com/id/949119664/vector/cute-white-doctor-robot-modern-health-care-flat-editable-vector-illustration-clip-art.jpg?s=170667a&w=0&k=20&c=EMq4RjpMf12KPNpp7hbyU8i663LaYbcooGQpbvRuXSI="
    st.markdown("<h1 style='color: skyblue; font-weight: bold; font-family: Wide;'>DosageAid 💊</h1>", unsafe_allow_html=True)
    st.write('Herzlich Willkommen zur Medikamentendosierungs-App! Hier finden Sie alle Werkzeuge, die Sie benötigen, um Ihre Medikamentendosierung genau zu planen und im Blick zu behalten.')
    st.write('Wir hoffen, dass Ihnen unsere App dabei helfen wird, Ihre Medikamentendosierung auf einfache und effektive Weise zu optimieren. Vielen Dank, dass Sie sich für unsere App entschieden haben!')
    st.image(image_url, width=500)
    st.write('Vielen Dank, dass Sie uns Vertrauen.')
    st.caption(':Blue[Herzlichst: Vinitha Yogathas, Anashai Anandaruban, Hajar Maanaoui]')
    
    st.balloons()
    

    
def page_medlist():
    st.header(':orange[Medikamentenliste]')
    st.write('Sie können hier Ihre Einnahmezeiten auswählen und die App erkennt automatisch, welches Medikament zu welcher Zeit eingenommen wurde. Nur mit ein paar Klicks kann eine Übersicht erschaffen werden!.')
    # Erstellen des DataFrames mit 4 Spalten und 4 Zeilen
    data = {
    'Medikamente 💊': ['Aspirin Cardio 100 mg', 'Metformin 500 mg', 'Atorvastatin 20 mg', 'Zolpidem 5 mg'],
    'Einnahme ⏳': ['Morgens', 'Morgens/Abends', 'Abends', 'Nachts'],
    'Dosierung': ['1 Tablette', 'Je 1 Tablette', '1 Tablette', '1/2 - max. 1 Tablette'],
    'Kontrolle': [False, False, False, False]
}
    df = pd.DataFrame(data)


# Checkbox-Menü für die Spalte "Kontrolle" erstellen
    selected_rows = st.multiselect('Kontrolle', df["Medikamente 💊"].tolist())

 

# Markiere ausgewählte Einnahmen in der DataFrame als "done"
    for einnahme in selected_rows:
        df.loc[df["Einnahme ⏳"] == einnahme, 'Kontrolle'] = True

 

    st.write(df)

    st.subheader('Information ℹ️')
    st.write('Nun können sie bei "Choose an Option" ihre Einnahmezeit anwählen, somit wird das eingenommene Medikament mit ☑️ angezeigt.')

def page_meds():

    st.header("Hier finden Sie weitere Informationen zu den Medikamenten")
    st.write('Das Compendium ist einen umfassende Online-Datenbank für medizinische Informationen. Es bietet detaillierte Informationen zu Medikamenten, Krankheiten und Therapien für Fachleute und Patienten. Das Compendium wird regelmässig aktualisiert und ermöglicht gezielte Suche nach relevanten Informationen. Es unterstützt fundierte Entscheidungen und informierte Diskussionen im Gesundheitswesen. Nebenbei finden Sie auch den SL-Preis, der für die Krankenkasse relevant ist. Dieser Preis kann Ihnen dabei helfen, die Kosten des Medikaments abzuschätzen.')
    st.write('Klicken Sie auf den Link „compendium.ch", um das entsprechende Verzeichnis zu öffnen.')
    url = "https://compendium.ch"
    link_name = "Compendium"
    st.markdown(f"[{link_name}]({url})")
    
   
def page_numbers():
    st.header("☎️ Wichtige Telefonnummern!")
    st.write("Haben Sie Beschwerden? Wurde ein Medikament vergessen oder falsch eingenommen? Zögern Sie nicht anzurufen!")
    st.write("Speichern Sie diese Telefonnummern für den Fall von Notfällen, Vergiftungen und medizinischen Notfällen in Ihrem Mobiltelefon, um schnelle Hilfe zu erhalten. Diese Nummern bieten rasche Unterstützung und sind besonders wichtig in dringenden Situationen.")
    data = {'Kategorie': ['Allgemeiner Notruf', 'Vergiftungen', 'Ärztlicher Notfalldienst', 'Psychiatrischer Notfalldienst'],
            'Telefonnummer': ['112', '145', '0800 33 66 55', '0800 333 444']}
    df = pd.DataFrame(data) 

    st.table(df)
    

# Funktion zum Anzeigen der Symptome auf der Seite
def page_symptoms():
        # Daten für die Tabelle
    data = {'Beschwerden': ['Kopfschmerzen', 'Bauchschmerzen', 'Übelkeit', 'Schwindel', 'Husten', 'Fieber'],
            'Zeitpunkt/Häufigkeit': ['1x täglich', '2x täglich', '3x täglich', 'Mehr als 3x täglich', '2x täglich', '1x täglich']}
    
    # DataFrame erstellen
    df = pd.DataFrame(data)
    
    # Titel und Beschreibung
    st.write('# ⚠️ Sind Besondere Symptome aufgetreten?')
    st.write('Haben Sie Veränderungen bemerkt? Treten Häufiger Symptome auf? Bitte tragen sie es ein und nehmen sie es mit für Ihre nächste Arztkonsultation.')
    
    # Tabelle anzeigen
    st.write(df)
        
    

    selected_symptoms = st.multiselect('Symptome', data['Beschwerden'])
    if len(selected_symptoms) > 0:
        df = pd.DataFrame({
            'Symptome': selected_symptoms,
            'Zeitpunkt/Häufigkeit': [data['Zeitpunkt/Häufigkeit'][data['Beschwerden'].index(symptom)] for symptom in selected_symptoms]
        })
        st.write(df)
    else:
        st.write('Keine Symptome ausgewählt.')

# Funktion zum Erstellen eines Plots auf der Seite
def page_plot():

#Daten Aus Excel-Tabelle

    # Datenstruktur erstellen
    data = {
        'Kategorie': ['Randomisiert', 'Keine Daten für primäre Endpunkte', 'Intention-to-treat Gruppe',
                      'Aus der Studie ausgeschieden', 'Wegen Nebenwirkungen', 'Fehlende Wirksamkeit',
                      'Andere Gründe'],
        'Kontinuierliche Zolpidem Einnahme': [388, 2, 386, 22, 13, 1, 8,],
        'Diskontinuierliche Zolpidem Einnahme': [408, 5, 403, 26, 16, 2, 8,]
    }
    
    # DataFrame erstellen
    df = pd.DataFrame(data)
    
    # Titel und Beschreibung
    st.headers('Information über Zolpidem ℹ️')
    st.write('Einnahme von Zolpidem')
    st.write('Diese Tabelle zeigt die Anzahl der Studienteilnehmer und welche aus unterschiedlichen Gründen ausgeschieden wurden. Studie aus Tellmed.ch')
    
    # Tabelle anzeigen
    st.table(df)
    
    # Horizontaler Balkendiagramm-Plot der Studienabbrüche
    fig = px.bar(df, x='Kategorie', y=['Kontinuierliche Zolpidem Einnahme'], 
                 title='Studie von Tellmed.ch',)
    fig.update_layout(barmode='stack')
    fig.update_yaxes(title="Persons")
    st.plotly_chart(fig)

    fig2 = px.bar(df, x='Kategorie', y=['Diskontinuierliche Zolpidem Einnahme'], 
                 title='Studie von Tellmed.ch',)
    fig2.update_layout(barmode='stack')
    fig2.update_yaxes(title="Persons")
    st.plotly_chart(fig)

    st.write('Tabelle aus Tellmed.ch')
    image_url ="https://www.tellmed.ch/show_image.php?file_id=576"
    st.image(image_url, width=500)
  
    #https://www.tellmed.ch/modules_end/printthis/?uniqueid=uniqueid&tip=2&popup=yes&mode=content_db&contentId=4854&lng=Lng1&thisMode=&clas_css=0&level_0=0   

def main():
    st.sidebar.title("Navigation")
    pages = {
        "Startseite": page_home,
        "Medikamentenliste": page_medlist,
        "Compendium": page_meds,
        "Wichtige Telefonnummern": page_numbers,
        "Ihre Symptome": page_symptoms,
        "Studie: Zolpidem": page_plot
    }

 

    if "authenticated" not in st.session_state:
        login()
    else:
        selection = st.sidebar.radio("Gehe zu", list(pages.keys()))
        page = pages[selection]
        page()

 

if __name__ == "__main__":
    main()










  
