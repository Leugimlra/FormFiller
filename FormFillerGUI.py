#!/usr/bin/env python
#Miguel Lopez Rivera

import PySimpleGUI as sg

sg.theme("DarkAmber")

layout = [[ sg.Combo(['choice1', 'choice2', 'choice3'])]]

window = sg.Window("MFD FormFiller", layout)



while True:
  event, values = window.read()
  if event == "Exit" or event == sg.WIN_CLOSED:
    break

window.close()
