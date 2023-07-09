import pymeshlab

def file_converter(config):

    # Extract file i/o parameters from
    input_file = config["input_path"]
    output_file = config["output_path"]

    # Create a MeshSet object
    mesh = pymeshlab.MeshSet()

    # Load the input FBX file
    mesh.load_new_mesh(input_file)

    # Export the mesh to SAT format
    mesh.save_current_mesh(output_file)
