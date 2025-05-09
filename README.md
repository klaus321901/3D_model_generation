# 3D Model Generator

## Project Description

The **3D Model Generator** is a Python-based application that converts 2D images into 3D models. Using a combination of computer vision techniques and 3D modeling libraries, the program extracts an object from a given image, processes it, and generates a 3D mesh. The generated model is saved as an STL file, which is a widely used format for 3D printing and visualization.

This project leverages several Python libraries, including OpenCV for image processing, NumPy for numerical computations, and numpy-stl for 3D model generation.

## Key Features

- **Image Processing**: Uses OpenCV to extract contours and objects from 2D images.
- **3D Model Generation**: Constructs a simple 3D mesh based on the extracted contours.
- **STL File Output**: Saves the generated 3D model as an STL file for 3D printing or further use in 3D visualization tools.
- **Virtual Environment**: A virtual environment to manage dependencies and avoid conflicts with other projects.

## Project Structure




Setup Instructions
Follow the steps below to set up and run the project:

1. Clone the repository:
```bash
git clone https://github.com/klaus321901/3d_model_generation.git
cd 3d_model_generator
```



2. Create a virtual environment:
On Windows:

```bash
python -m venv venv
```
On macOS/Linux:

```bash
python -m venv venv
```
3. Activate the Virtual Environment:
On Windows:

```bash
.\venv\Scripts\activate
```
On macOS/Linux:

```bash
source venv/bin/activate
```

4. Install the dependencies:
```bash
pip install -r requirements.txt
```
Running the Project
After setting up the environment, run the following command to generate the 3D model:

```bash
python generate_3d_model.py
```

Once the script executes successfully, a file named output_model.stl will be generated in the project directory. This file contains the 3D model in STL format.

## Output

After execution, a file named `output_model.stl` will be generated in the project directory.

## Thought Process

The idea behind this project was to build a basic pipeline that translates 2D visual data into a tangible 3D form using Python libraries. The process involves:

- **Image Input**: Using OpenCV to capture contours from the input image, identifying the shapes and objects.
- **3D Mesh Construction**: Using NumPy to convert the extracted contours into a 3D mesh structure.
- **STL Conversion**: Leveraging the numpy-stl library to create an STL file that can be used in 3D printing or visualization applications.

This project helped me explore the integration of computer vision with 3D modeling techniques, building a simple pipeline from image processing to 3D model creation.


## Libraries Used

- **numpy**: Used for numerical computations and handling 3D data.
- **opencv-python**: Used for image processing and object extraction from the input image.
- **matplotlib**: Used for visualizing the contours and 3D objects during the processing stage.
- **numpy-stl**: Used for creating and saving the 3D model as an STL file for printing or visualization.


