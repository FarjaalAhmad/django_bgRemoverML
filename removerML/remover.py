import argparse
import os
import gc
import tqdm
import logging
from libs.strings import *
from libs.networks import model_detect
import libs.preprocessing as preprocessing
import libs.postprocessing as postprocessing

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


def __work_mode__(path: str):
    """Determines the desired mode of operation"""
    if os.path.isfile(path):  # Input is file
        return "file"
    if os.path.isdir(path):  # Input is dir
        return "dir"
    else:
        return "no"


def __save_image_file__(img, file_name, output_path, wmode):
    """
    Saves the PIL image to a file
    :param img: PIL image
    :param file_name: File name
    :param output_path: Output path
    :param wmode: Work mode
    """
    # create output directory if it doesn't exist
    folder = os.path.dirname(output_path)
    if folder != '':
        os.makedirs(folder, exist_ok=True)
    if wmode == "file":
        file_name_out = os.path.basename(output_path)
        if file_name_out == '':
            # Change file extension to png
            file_name = os.path.splitext(file_name)[0] + '.png'
            # Save image
            img.save(os.path.join(output_path, file_name))
            gc.collect()
        else:
            try:
                # Save image
                img.save(output_path)
                gc.collect()
            except OSError as e:
                if str(e) == "cannot write mode RGBA as JPEG":
                    raise OSError("Error! "
                                  "Please indicate the correct extension of the final file, for example: .png")
                else:
                    raise e
    else:
        # Change file extension to png
        file_name = os.path.splitext(file_name)[0] + '.png'
        # Save image
        img.save(os.path.join(output_path, file_name))
        gc.collect()


def process(input_path, output_path, model_name="u2net",
            preprocessing_method_name="bbd-fastrcnn", postprocessing_method_name="rtb-bnb"):
    """
    Processes the file.
    :param input_path: The path to the image / folder with the images to be processed.
    :param output_path: The path to the save location.
    :param model_name: Model to use.
    :param postprocessing_method_name: Method for image preprocessing
    :param preprocessing_method_name: Method for image post-processing
    """
    if input_path is None or output_path is None:
        raise Exception(
            "Bad parameters! Please specify input path and output path.")

    model = model_detect(model_name)  # Load model
    if not model:
        logger.warning("Warning! You specified an invalid model type. "
                       "For image processing, the model with the best processing quality will be used. "
                       "(u2net)")
        # If the model line is wrong, select the model with better quality.
        model_name = "u2net"
        model = model_detect(model_name)  # Load model
    preprocessing_method = preprocessing.method_detect(
        preprocessing_method_name)
    postprocessing_method = postprocessing.method_detect(
        postprocessing_method_name)
    wmode = __work_mode__(input_path)  # Get work mode
    if wmode == "file":  # File work mode
        image = model.process_image(
            input_path, preprocessing_method, postprocessing_method)
        __save_image_file__(image, os.path.basename(
            input_path), output_path, wmode)
    elif wmode == "dir":  # Dir work mode
        # Start process
        files = os.listdir(input_path)
        for file in tqdm.tqdm(files, ascii=True, desc='Remove Background', unit='image'):
            file_path = os.path.join(input_path, file)
            image = model.process_image(
                file_path, preprocessing_method, postprocessing_method)
            __save_image_file__(image, file, output_path, wmode)
    else:
        raise Exception(
            "Bad input parameter! Please indicate the correct path to the file or folder.")
