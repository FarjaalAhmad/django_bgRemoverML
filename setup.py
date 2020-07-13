import sys
import os
import gdown
import tarfile
from libs.strings import MODELS_NAMES


class Config:
    """Config object"""
    # general
    arc_name = "model.tar.gz"
    # mobile_net_model
    mn_url = "https://github.com/OPHoperHPO/image-background-remove-tool/releases/download/3.2/deeplabv3_mnv2_pascal_train_aug_2018_01_29.tar.gz"
    mn_dir = os.path.join("models", "mobile_net_model")
    # xception_model
    xc_url = "https://github.com/OPHoperHPO/image-background-remove-tool/releases/download/3.2/deeplabv3_pascal_train_aug_2018_01_04.tar.gz"
    xc_dir = os.path.join("models", "xception_model")
    # u2net
    u2_url = "https://github.com/OPHoperHPO/image-background-remove-tool/releases/download/3.2/u2net.pth"
    u2_dir = os.path.join("models", "u2net")
    # basnet
    bn_url = "https://github.com/OPHoperHPO/image-background-remove-tool/releases/download/3.2/basnet.pth"
    bn_dir = os.path.join("models", "basnet")
    # u2netp
    u2p_url = "https://github.com/OPHoperHPO/image-background-remove-tool/releases/download/3.2/u2netp.pth"
    u2p_dir = os.path.join("models", "u2netp")


def prepare():
    """Creates folders"""
    print("Create folders")
    try:
        if not os.path.exists(Config.mn_dir):
            os.makedirs(Config.mn_dir)
        if not os.path.exists(Config.xc_dir):
            os.makedirs(Config.xc_dir)
        if not os.path.exists(Config.u2_dir):
            os.makedirs(Config.u2_dir)
        if not os.path.exists(Config.u2p_dir):
            os.makedirs(Config.u2p_dir)
        if not os.path.exists(Config.bn_dir):
            os.makedirs(Config.bn_dir)
    except BaseException as e:
        print("Error creating model folders! Error:", e)
        exit(1)
    return True


def download():
    """Loads model archives"""
    path_mn = os.path.join(Config.mn_dir, Config.arc_name)
    path_xc = os.path.join(Config.xc_dir, Config.arc_name)
    try:
        if os.path.exists(path_mn):  # Clean old files
            os.remove(path_mn)
        if os.path.exists(path_xc):
            os.remove(path_xc)
        print("Start download model archives!")
        gdown.download(Config.mn_url, path_mn, quiet=False)
        gdown.download(Config.xc_url, path_xc, quiet=False)
        gdown.download(Config.u2_url, os.path.join(
            Config.u2_dir, "u2net.pth"), quiet=False)
        gdown.download(Config.u2p_url, os.path.join(
            Config.u2p_dir, "u2netp.pth"), quiet=False)
        gdown.download(Config.bn_url, os.path.join(
            Config.bn_dir, "basnet.pth"), quiet=False)
        print("Download finished!")
    except BaseException as e:
        print("Error download model archives! Error:", e)
        exit(1)
    return True


def untar():
    """Untar archives"""
    path_mn = os.path.join(Config.mn_dir, Config.arc_name)
    path_xc = os.path.join(Config.xc_dir, Config.arc_name)
    try:
        print("Start unpacking")
        if path_mn.endswith("tar.gz"):
            tar = tarfile.open(path_mn, "r:gz")
            tar.extractall(path=Config.mn_dir)
            tar.close()
            os.rename(os.path.join(Config.mn_dir, "deeplabv3_mnv2_pascal_train_aug"),
                      os.path.join(Config.mn_dir, "model"))
            print("Unpacking 1 archive finished!")
        if path_xc.endswith("tar.gz"):
            tar = tarfile.open(path_xc, "r:gz")
            tar.extractall(path=Config.xc_dir)
            tar.close()
            os.rename(os.path.join(Config.xc_dir, "deeplabv3_pascal_train_aug"),
                      os.path.join(Config.xc_dir, "model"))
            print("Unpacking 2 archive finished!")
    except BaseException as e:
        print("Unpacking error! Error:", e)
        exit(1)
    return True


def clean():
    """Cleans temp files"""
    path_mn = os.path.join(Config.mn_dir, Config.arc_name)
    path_xc = os.path.join(Config.xc_dir, Config.arc_name)
    try:
        if os.path.exists(path_mn):  # Clean old files
            os.remove(path_mn)
        if os.path.exists(path_xc):
            os.remove(path_xc)
    except BaseException as e:
        print("Cleaning error! Error:", e)
    return True


def setup():
    """Performs program setup before use"""
    if prepare():
        if download():
            if untar():
                if clean():
                    pass


def cli():
    model_name = "all"
    if model_name == "all":
        setup()
    elif model_name == "u2net":
        if not os.path.exists(Config.u2_dir):
            os.makedirs(Config.u2_dir)
        gdown.download(Config.u2_url, os.path.join(Config.u2_dir, "u2net.pth"), quiet=False)
    elif model_name == "basnet":
        if not os.path.exists(Config.bn_dir):
            os.makedirs(Config.bn_dir)
        gdown.download(Config.bn_url, os.path.join(Config.bn_dir, "basnet.pth"), quiet=False)
    elif model_name == "u2netp":
        if not os.path.exists(Config.u2p_dir):
            os.makedirs(Config.u2p_dir)
        gdown.download(Config.u2p_url, os.path.join(Config.u2p_dir, "u2netp.pth"), quiet=False)
    elif model_name == "xception_model":
        if not os.path.exists(Config.xc_dir):
            os.makedirs(Config.xc_dir)
        path_xc = os.path.join(Config.xc_dir, Config.arc_name)
        gdown.download(Config.xc_url, path_xc, quiet=False)
        if path_xc.endswith("tar.gz"):
            tar = tarfile.open(path_xc, "r:gz")
            tar.extractall(path=Config.xc_dir)
            tar.close()
            os.rename(os.path.join(Config.xc_dir, "deeplabv3_pascal_train_aug"),
                      os.path.join(Config.xc_dir, "model"))
            print("Unpacking archive finished!")
        if os.path.exists(path_xc):
            os.remove(path_xc)
    elif model_name == "mobile_net_model":
        if not os.path.exists(Config.mn_dir):
            os.makedirs(Config.mn_dir)
        path_mn = os.path.join(Config.mn_dir, Config.arc_name)
        if os.path.exists(path_mn):  # Clean old files
            os.remove(path_mn)
        gdown.download(Config.mn_url, path_mn, quiet=False)
        if path_mn.endswith("tar.gz"):
            tar = tarfile.open(path_mn, "r:gz")
            tar.extractall(path=Config.mn_dir)
            tar.close()
            os.rename(os.path.join(Config.mn_dir, "deeplabv3_mnv2_pascal_train_aug"),
                      os.path.join(Config.mn_dir, "model"))
            print("Unpacking archive finished!")
        if os.path.exists(path_mn):  # Clean old files
            os.remove(path_mn)
    else:
        print("ERROR! You specified an invalid model type! EXIT!")
        exit(1)
    print("Setup finished! :)")


cli()
