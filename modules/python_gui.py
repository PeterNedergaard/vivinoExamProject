import PySimpleGUI as sg
import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from modules.best_country_in_range import get_best_in_range
from modules.predict_wine_data import predict_data

def show_gui():
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
                   # [sg.Text('Vælg specifikation', size=(30, 1), font='Lucida', justification='left')],
                   # [sg.Combo(
                   #     ["Land", "Region", "Druesort", "Vingård"],
                   #     key='spec', readonly=True, default_value="Land")],
                   [sg.Image("images/top10_plot.png", key="top10_plot")],
                   ]

    countries = list(pd.read_csv("data/countries.csv")["countries"].to_numpy())
    regions = list(pd.read_csv("data/regions.csv")["regions"].to_numpy())
    grape_type = list(pd.read_csv("data/grapes.csv")["grapes"].to_numpy())
    winery = list(pd.read_csv("data/wineries.csv")["wineries"].to_numpy())

    country_region_winery = list(pd.read_csv("data/country_region_winery.csv")['country_region_winery'].to_numpy())

    chosen_grapes = []
    chosen_regions = []
    chosen_wineries = []

    tab3_layout = [[sg.T('Tab 3')],
                   [sg.Combo(
                       countries
                       , default_value="Land", key="Land", readonly=True, enable_events=True)],
                   [sg.Combo(
                       regions
                       , default_value="Region", key="Region", readonly=True, enable_events=True)],
                   [sg.Combo(
                       winery
                       , default_value="Vingård", key="Vingård", readonly=True)],

                   [sg.Text("Vælg op til 5 druer fra nedenstående list")],
                   [sg.Text("indtast evt druens forbogstav for at filtrere resultaterne")],
                   [sg.InputText(key="filter_grapes", size=(5, 5), enable_events=True)],
                   [sg.Listbox(
                       grape_type, key="Druesort", select_mode="extended", size=(15, 8)),
                       sg.Button("Tilføj druesort", key="add_grape"), sg.Button("Fjern valgte druer", key="clear_list"),
                       sg.Multiline(chosen_grapes, key="chosen_grapes", justification="right", size=(35, 8))],
                   [sg.Button("Kør", key="Predict", enable_events=True)],
                   [sg.Text(size=(30, 1), font='Lucida', justification='left', key="tab3text")],
                   [sg.Image("images/all_ratings_plot.png", key="all_ratings_plot", size=(900, 300))]

                   ]

    tab4_layout = [[sg.T('Tab 4')],
                   [sg.Text("Minimum pris:")],
                   [sg.InputText(key='Min')],
                   [sg.Text("Maximum pris (max. 2500):")],
                   [sg.InputText(key='Max')],
                   [sg.Button("Søg", key="Best_country", enable_events=True)],
                   [sg.Text(key='Tab4_result')],
                   ]
    tab5_layout = [[sg.T('Tab 5')],
                   [sg.Combo(
                       countries
                       , default_value="Land", key="Popular_land", readonly=True, enable_events=True)],
                   [sg.Image(key="popular_top5_plot")]
                   ]
    tab6_layout = [[sg.T('Tab 6')],
                   [sg.Image("images/meme.png", key="file 6")],
                   ]
    layout = [
        [sg.TabGroup([[sg.Tab('Om spec. og bedømmelse', tab1_layout),
                       sg.Tab('Top 10 lande', tab2_layout),
                       sg.Tab('Forudsig bedømmelse', tab3_layout),
                       sg.Tab('Bedste land for prisen', tab4_layout),
                       sg.Tab('Top 5 populære vine', tab5_layout),
                       sg.Tab('Memes-tab', tab6_layout),

                       ]])],
    ]

    window = sg.Window("window", layout, size=(800, 800), finalize=True)
    window['filter_grapes'].bind("<Return>", "_Enter")

    def modified_array(array, string):
        res = [idx for idx in array if idx[0].lower() == string.lower()]
        return res

    def get_regions_from_country(country):
        region_list = []

        for row in country_region_winery:
            str_row = str(row)
            if str_row.startswith(country):
                region_list.append(str_row.split(',')[1])

        return list(numpy.unique(region_list))

    def get_wineries_from_region(region):
        winery_list = []

        for row in country_region_winery:
            str_row = str(row)
            str_split = str_row.split(',')
            if str_split[1] == region:
                winery_list.append(str_split[2])

        return list(numpy.unique(winery_list))

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        print(event)
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        if event == "Land":
            chosen_regions = get_regions_from_country(window["Land"].get())
            window["Region"].update(values=chosen_regions)

        if event == "Region":
            chosen_wineries = get_wineries_from_region(window["Region"].get())
            window["Vingård"].update(values=chosen_wineries)

        if event == "filter_grapes":
            if window["filter_grapes"].get() != "":
                window["Druesort"].update(modified_array(grape_type, window["filter_grapes"].get()))
            else:
                window["Druesort"].update(grape_type)

        if event == "Best_country":
            max_price = window["Max"].get()
            min_price = window["Min"].get()

            if not window["Min"].get().isnumeric() or not window["Max"].get().isnumeric():
                result = "Pris skal være mellem 0 og 2500 kr."
            else:
                result = get_best_in_range(int(min_price), int(max_price))

            window["Tab4_result"].update(result)

        if event == "Popular_land":
            window["popular_top5_plot"].update("images/popular_top5_plots/top5_" + window['Popular_land'].get() + ".png")

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
                window["tab3text"].update("Vurderet bedømmelse: " + str(
                    predict_data(grapes=chosen_grapes, winery=window["Vingård"].get(), country=window["Land"].get(),
                                 region=window["Region"].get())))
                # window["tab3text"].update("result")
            else:
                window["tab3text"].update("Vælg værdier på alle felter")

    window.close()
