import PySimpleGUI as sg
import subprocess

layout = [
    [sg.Input(key="-INPUT-", size=(45, 1)), sg.Button("Run"), sg.Button("Exit")],
    [sg.Output(size=(60, 20))]
]

window = sg.Window("Mterm", layout, resizable=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    if event == "Run":
        command = values["-INPUT-"]
        try:
            result = subprocess.run(
                command, shell=True, capture_output=True, text=True
            )
            print(result.stdout)
            if result.stderr:
                print(result.stderr)
        except Exception as e:
            print(f"Error: {e}")

window.close()
