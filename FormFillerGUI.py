#!/usr/bin/env python
#Miguel Lopez Rivera

import PySimpleGUI as sg

sg.theme("DarkBlack1")

left_column = [
  [
    sg.Combo(['26F COMPLIANCE FOR SMOKE DETECTORS AND CARBON MONOXIDE ALARMS'])
  ],
  [
    sg.InputText("Owner")
  ]

]

layout = [[sg.Column(left_column)]]
window = sg.Window("MFD FormFiller", layout)




while True:
  event, values = window.read()
  if event == "Exit" or event == sg.WIN_CLOSED:
    break

window.close()
