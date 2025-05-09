from stl import mesh
from input_handling import extract_object_from_image
import numpy as np

def create_3d_model_from_image(image_path):
    print("Starting to process image...")
    processed_image = extract_object_from_image(image_path, output_path='processed_image.jpg')  # Adjust if needed

    if processed_image is None:
        print("Error in processing image!")
        return

    print("Image processed successfully.")

    # Step 2: Convert processed image data into 3D data (This could involve 3D reconstruction logic)
    vertices = np.array([[-1, -1, -1],
                         [ 1, -1, -1],
                         [ 1,  1, -1],
                         [-1,  1, -1],
                         [-1, -1,  1],
                         [ 1, -1,  1],
                         [ 1,  1,  1],
                         [-1,  1,  1]])

    faces = np.array([[0, 3, 1],
                      [1, 3, 2],
                      [2, 3, 7],
                      [7, 3, 6],
                      [6, 3, 5],
                      [5, 3, 1],
                      [4, 7, 6],
                      [4, 6, 5],
                      [0, 4, 5],
                      [0, 5, 1],
                      [0, 7, 4],
                      [7, 0, 3]])

    print("Vertices and faces defined.")

    cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = vertices[f[j], :]

    print("3D mesh created.")

    # Step 3: Save the 3D model as .stl or .obj
    cube.save('output_model.stl')
    print("STL file saved as output_model.stl")

# Run the model generation
image_path = r'C:\Users\sanat\OneDrive\Desktop\IMG_2304.webp'  # Path to the input image
create_3d_model_from_image(image_path)
