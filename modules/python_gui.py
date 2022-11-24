import PySimpleGUI as sg
import pandas as pd

def showgui():

    tab1_layout = [
        [sg.T('Denne graf viser forholdet mellem Vines specifikationer og deres bedømmelse')],
        [sg.T('data 1', key='file 1'), sg.Image("images/graf.png", size=(900, 150))],
        [sg.Text('data 2', key='file 2'), sg.Image("images/graf.png", size=(900, 150))],
        [sg.Text('data 3', key='file 3'), sg.Image("images/meme.png", size=(900, 300))],
        [sg.Multiline(
            "Som graferne overfor viser, så er der en sammenhæng mellem vinens specifikationer og dens bedømmelse. Den "
            "bedste indikator for dette er specifikation x",
            size=(900, 100))]
    ]

    tab2_layout = [[sg.T('Tab 2')],
                   [sg.Text('Vælg specifikation', size=(30, 1), font='Lucida', justification='left')],
                   [sg.Combo(
                       ["Land", "Region", "Druesort", "Vingård"],
                       key='spec', readonly=True, default_value="Land")],
                   [sg.Image("images/graf.png", key="dropdownimage")],
                   ]

    countries = ["Argentina", "Australien", "Chile", "Frankrig", "Italien", "Portugal", "Spanien", "Tyskland", "USA",
                 "Østrig"]



    grape_type = ['Müller-Thurgau', 'Malvasia', 'Moscatel de Alejandría', 'Muscadelle', 'Gaidouria', 'Viura',
                  'Weissburgunder', 'Corvinone', 'Tempranillo', 'Fernao Pires', 'Cabernet Franc',
                  'Moscatel de grano menudo', 'Grauburgunder', 'Grenache', 'Pinot Noir', 'Verdelho', 'Bourboulenc',
                  'Hárslevelű', 'Gouveio', 'Petite Sirah', 'Clairette', 'Pinotage', 'Trincadeira', 'Carignan', 'Huxelrebe',
                  'Torrontés', 'Pinot Gris', 'Malbec', "Nero d'Avola", 'Tinta Roriz', 'Mencia', 'Assyrtiko', 'Counoise',
                  'Savagnin', 'Graciano', 'Muscardin', 'Merlot', 'Cabernet Sauvignon', 'Castelao', 'Grüner Veltliner',
                  'Aligoté', 'Riesling', 'Parellada', 'Terrantez', 'Canaiolo Nero', 'Sangiovese', 'Trepat', 'Tinta Barroca',
                  'Cariñena', 'Fiano', 'Pinot Grigio', 'Sauvignon Blanc', 'Athiri', 'Zweigelt', 'Trebbiano',
                  'Pinot Meunier', 'Barbera', 'Grolleau', 'Malmsey', 'Touriga Nacional', 'Cinsaut', 'Primitivo',
                  'Montepulciano', 'Garganega', 'Xarel-lo', 'Cortese', 'Malvasia Nera', 'Tocai Friulano',
                  'Catarratto Bianco', 'Carménère', 'Pedro Ximenez', 'Krassato', 'Gamay', 'Corvina', 'Garnacha', 'Arneis',
                  'Touriga Franca', 'Xinomavro', 'Tannat', 'Verdejo', 'Viognier', 'Negroamaro', 'Vidal Blanc', 'Kerner',
                  'Pinot Blanc', 'Glera (Prosecco)', 'Chardonnay', 'Boal Branco', 'Vaccareze', 'Chasselas', 'Petit Verdot',
                  'Moscato', 'Malvasia Fina', 'Rondinella', 'Palomino', 'Loureiro', 'Chenin Blanc', 'Agiorgitiko',
                  'Arinto de Bucelas', 'Auxerrois', 'Sémillon', 'Dolcetto', 'Azal', 'Batoca', 'Silvaner', 'Marsanne',
                  'Aglianico', 'Alvarinho', 'Touriga Francesa', 'Aidani', 'Roussanne', 'Baga', 'Aragonez', 'Rabigato',
                  'Stavroto', 'Furmint', 'Gewürztraminer', 'Albariño', 'Nebbiolo', 'Bonarda', 'Shiraz/Syrah',
                  'Blaufränkisch', 'Sercial', 'Mourvedre', 'Melon de Bourgogne', 'Souzao', 'Cinsault', 'Avesso',
                  'Zinfandel', 'Grenache Blanc', 'Katsano']
    chosen_grapes = []

    regions = ["Bordeaux", "Bourgogne", "Napa Valley", "Piemonte", "Rhone Valley", "Toscana"]

    winery = ["winery1", "winery2", "winery3"]
    tab3_layout = [[sg.T('Tab 3')],
                   [sg.Combo(
                       countries
                       , default_value="Land", key="Land", readonly=True)],
                   [sg.Combo(
                       regions
                       , default_value="Region", key="Region", readonly=True)],

                   [sg.Text("Vælg op til 5 druer fra nedenstående list")],
                   [sg.Text("indtast evt druens forbogstav for at filtrere resultaterne")],
                   [sg.InputText(key="filter_grapes", size=(5, 5), enable_events=True)],
                   [sg.Listbox(
                       grape_type, key="Druesort", select_mode="extended", size=(15, 8)),
                       sg.Button("Tilføj druesort", key="add_grape"), sg.Button("Fjern valgte druer", key="clear_list"),
                       sg.Multiline(chosen_grapes, key="chosen_grapes", justification="right", size=(35, 8))],

                   [sg.Combo(
                       winery
                       , default_value="Vingård", key="Vingård", readonly=True)],
                   [sg.Button("Kør", key="Predict", enable_events=True)],
                   [sg.Text(size=(30, 1), font='Lucida', justification='left', key="tab3text")],
                   [sg.Image(key="tab3image")]

                   ]

    tab4_layout = [[sg.T('Tab 4')],
                   [sg.InputText('data 4', key='file 4')],
                   ]
    tab5_layout = [[sg.T('Tab 5')],
                   [sg.InputText('data 5', key='file 5')],
                   ]
    tab6_layout = [[sg.T('Tab 6')],
                   [sg.Image("images/meme.png", key="file 6")],
                   ]
    layout = [
        [sg.TabGroup([[sg.Tab('Om spec. og bedømmelse', tab1_layout),
                       sg.Tab('Tab 2', tab2_layout),
                       sg.Tab('Tab 3', tab3_layout),
                       sg.Tab('Tab 4', tab4_layout),
                       sg.Tab('Tab 5', tab5_layout),
                       sg.Tab('Memes-tab', tab6_layout),

                       ]])],
    ]

    window = sg.Window("window", layout, size=(800, 800), finalize=True)
    window['filter_grapes'].bind("<Return>", "_Enter")


    def modified_array(array, string):
        res = [idx for idx in array if idx[0].lower() == string.lower()]
        return res


    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        print(event)
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        if event == "filter_grapes":
            if window["filter_grapes"].get() != "":
                window["Druesort"].update(modified_array(grape_type, window["filter_grapes"].get()))
            else:
                window["Druesort"].update(grape_type)


        if event == "clear_list":
            chosen_grapes.clear()
            window["chosen_grapes"].update(chosen_grapes)
        if event == "add_grape":
            if len(chosen_grapes) <= 4 and window["Druesort"].get() not in chosen_grapes:
                chosen_grapes.append(window["Druesort"].get())
                window["chosen_grapes"].update(chosen_grapes)



        if event == "Predict":
            if window["Vingård"].get() in winery and window["Land"].get() in countries and window[
            "Region"].get() in regions and len(chosen_grapes) >= 1:
                # print("vælg ting og sager")
                print("Valgte druer:", chosen_grapes)
                print("Vingård:", window["Vingård"].get())
                print("Land:", window["Land"].get())
                print("Region:", window["Region"].get())
                # window["tab3text"].update(predict_data(grapes=chosen_grapes,winery=window["Vingård"].get(),country=window["Land"].get(),region=window["Region"].get()))
                window["tab3text"].update("result")
            else:
                window["tab3text"].update("Vælg værdier på alle felter")

    window.close()