from tkinter import Tk, Button, filedialog
from os import path

# Defining global variables
root = Tk()
root.title("3D File Converter")


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
            converter_config["input_name"] = input_name.path.splitext(path.basename(import_path))[0]
    # ----------------------#
    def export_file():
        export_path = filedialog.asksaveasfilename(
            filetypes=output_extensions, initialfile=converter_config["input_name"]
        )
        if export_path:
            converter_config["output_path"] = export_path

    # ----------------------#
    def build_interface():
        btn_import = Button(root, text="Import", command=import_file)
        btn_export = Button(root, text="Export", command=export_file)

        btn_import.pack()
        btn_export.pack()

        root.mainloop()

    # ----------------------#
    build_interface()
# ----------------------#
init()
