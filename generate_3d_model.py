import numpy as np
from stl import mesh
from input_handling import extract_object_from_image

# Function to create a cylinder (or any other shape)
def create_cylinder():
    # Simplified cylinder with height = 2 and radius = 1
    num_points = 20
    vertices = []
    faces = []

    # Bottom circle vertices
    for i in range(num_points):
        angle = 2 * np.pi * i / num_points
        x = np.cos(angle)
        y = np.sin(angle)
        vertices.append([x, y, -1])  # Bottom circle at z = -1

    # Top circle vertices
    for i in range(num_points):
        angle = 2 * np.pi * i / num_points
        x = np.cos(angle)
        y = np.sin(angle)
        vertices.append([x, y, 1])  # Top circle at z = 1

    # Faces of the cylinder (side faces)
    for i in range(num_points):
        next_i = (i + 1) % num_points
        faces.append([i, next_i, i + num_points])  # Side faces
        faces.append([next_i, next_i + num_points, i + num_points])

    # Bottom and top faces (optional)
    bottom_center = len(vertices)  # Center of bottom circle
    top_center = len(vertices) + 1  # Center of top circle
    for i in range(num_points):
        next_i = (i + 1) % num_points
        faces.append([i, next_i, bottom_center])  # Bottom face
        faces.append([i + num_points, next_i + num_points, top_center])  # Top face

    return np.array(vertices), np.array(faces)

# Main function to create 3D model from image (no text prompt)
def create_3d_model_from_image(image_path):
    print("Starting image preprocessing...")
    processed_image = extract_object_from_image(image_path, output_path='processed_image.jpg')

    if processed_image is None:
        print("Error: Couldn't process image.")
        return

    print("Image successfully processed.")

    # Directly create a cylinder (or another shape)
    vertices, faces = create_cylinder()
    print("Shape: cylinder")

    # Create the mesh from vertices and faces
    shape_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            shape_mesh.vectors[i][j] = vertices[f[j], :]

    print("3D mesh constructed.")

    # Save the 3D model as STL
    shape_mesh.save('output_model.stl')
    print("STL file saved as 'output_model.stl'.")

# Example usage
image_path = r'C:\Users\sanat\OneDrive\Desktop\IMG_2304.webp'
create_3d_model_from_image(image_path)
