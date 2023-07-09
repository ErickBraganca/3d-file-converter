from tkinter import Tk, Button, filedialog, messagebox, Label
from os import path

from main import file_converter

# Defining global variables
root = Tk()
root.title("3D File Converter")
root.geometry("250x300")
root.config(bg="#37474f")

ui_components = []

input_extensions = (
    ("Autodesk FBX", ".fbx"),
    ("Wavefront", ".obj"),
    ("STereoLithography", ".stl"),
    ("Collada", ".dae"),
    ("AutoCAD", ".apts"),
    ("ASCII Scene", ".asc"),
    ("Brickadia", ".bre"),
    ("OpenCTM", ".ctm"),
    ("ASTM E57", ".e57"),
    ("Evolve Surface", ".es"),
    ("GL Transmission Format", ".gltf"),
    ("GL Transmission Format", ".glb"),
    ("GL Transmission", ".pdb"),
    ("Polygon File Format", ".ply"),
    ("PTS Format", ".pts"),
    ("Pointools", ".ptx"),
    ("Quake", ".qobj"),
    ("Triangle", ".tri"),
    ("Texto", ".txt"),
    ("VMD", ".vmi"),
    ("VRML", ".wrl"),
    ("X3D", ".x3d"),
)
output_extensions = (
    ("3Ds Max", ".3ds"),
    ("OpenCTM", ".ctm"),
    ("Collada", ".dae"),
    ("AutoCAD", ".dxf"),
    ("Wavefront", ".obj"),
    ("STereoLithography", ".stl"),
)


def init():
    converter_config = {"input_path": "", "input_name": "", "output_path": ""}

    def import_file():
        import_path = filedialog.askopenfilename(filetypes=input_extensions)
        if import_path:
            input_name = path.basename(import_path)
            converter_config["input_path"] = import_path
            converter_config["input_name"] = input_name.split(".")[0]

            btn_instance = ui_components[0]
            btn_instance.config(state="active")

    # ----------------------#
    def export_file():
        export_path = filedialog.asksaveasfilename(
            filetypes=output_extensions, initialfile=converter_config["input_name"]
        )
        if export_path:
            converter_config["output_path"] = export_path
            file_converter(converter_config)
            messagebox.showinfo(title="3D Exporter", message="Export was concluded")

    # ----------------------#
    def build_interface():
        btn_import = Button(
            root, text="Import",
            command=import_file,
            font="Roboto",
            bg="#009879",
            fg="#fff",
            borderwidth=0,
            relief="flat"
        )
        btn_export = Button(
            root,
            text="Export",
            command=export_file,
            state="disabled",
            font="Roboto",
            bg="#ff5100",
            fg="#fff",
            borderwidth=0,
            relief="flat"
        )

        btn_import.pack(pady="50", ipadx="25", ipady="10")
        btn_export.pack(pady="10", ipadx="25", ipady="10")

        ui_components.append(btn_export)

        root.mainloop()

    # ----------------------#
    build_interface()


# ----------------------#
init()
