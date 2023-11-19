import rasterio
import numpy as np
import os


def tif_to_xyz(input_path, output_path):
    # Open the raster dataset
    with rasterio.open(input_path) as src:
        # Create a file for writing XYZ coordinates
        with open(output_path, 'w') as xyz_file:
            # Loop through all rows and columns of the raster
            for row in range(src.height):
                for col in range(src.width):
                    # Read the elevation value (z) at the current pixel
                    z_value = src.read(1)[row, col]
                    # Get the (x, y) coordinates of the current pixel
                    x, y = src.xy(row, col)

                    # Write the (x, y, z) coordinates to the XYZ file
                    xyz_file.write("{:.2f} {:.2f} {: .2f}\r\n".format(x, y, z_value))

    print("XYZ coordinates have been written to 'roi.xyz'.")


def main():
    tif_cropped = './data/Terrain/LIDAR-DTM-1m-2022-TQ38sw/roi_dtm.tif'
    roi_xyz = './data/Terrain/LIDAR-DTM-1m-2022-TQ38sw/roi.xyz'
    it_tif = 'C:/Users/cooki/Downloads/Italy/mini_DTM_cropped.tif'
    roi_it_xyz = 'C:/Users/cooki/Downloads/Italy/roi_it.xyz'
    # tif_to_xyz(tif_cropped, roi_xyz)
    tif_to_xyz(it_tif, roi_it_xyz)


if __name__ == '__main__':
    main()
