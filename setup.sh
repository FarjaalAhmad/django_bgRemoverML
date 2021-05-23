#!/bin/bash

WORKING_DIR=$(dirname "$(readlink -f "$0")")
echo "WORKING_DIR: ${WORKING_DIR}"

declare -a urls=(
    "http://download.tensorflow.org/models/deeplabv3_mnv2_pascal_train_aug_2018_01_29.tar.gz"
    "http://download.tensorflow.org/models/deeplabv3_pascal_train_aug_2018_01_04.tar.gz"
)

for url in ${urls[@]}; do
    FILENAME=$(basename ${url})
    FILE_PATH="${WORKING_DIR}/${FILENAME}"
    if [[ ! -f "${FILE_PATH}" ]]; then
        wget ${url}
    fi

    case ${FILENAME} in
        "deeplabv3_mnv2_pascal_train_aug_2018_01_29.tar.gz" )
            EXTRACT_PATH="${WORKING_DIR}/models/mobile_net_model/model"
            ;;
        "deeplabv3_pascal_train_aug_2018_01_04.tar.gz")
            EXTRACT_PATH="${WORKING_DIR}/models/xception_model/model"
            ;;
    esac

    if [[ ! -d "${EXTRACT_PATH}" ]]; then
        mkdir -p ${EXTRACT_PATH}
    fi
    tar xvzf "${FILE_PATH}" -C ${EXTRACT_PATH} --strip=1
    rm ${FILE_PATH}
done

PYTHON_PATH="$(which python3)"
SETUP_DIR="${WORKING_DIR}/setup/"
DOWNLOAD_SCRIPT_PY="${SETUP_DIR}/download.py"

# Install gdown if not installed, without this package globaly the installation will fail
${PYTHON_PATH} -m pip install gdown

if [[ -f ${DOWNLOAD_SCRIPT_PY} ]]; then
    ${PYTHON_PATH} ${DOWNLOAD_SCRIPT_PY}
else
    echo "${DOWNLOAD_SCRIPT_PY}, not found!"
fi

declare -A files
files=(
    ["basnet.pth"]="/models/basnet/"
    ["u2net.pth"]="/models/u2net/"
    ["u2netp.pth"]="/models/u2netp/"
)

for file in ${!files[@]}; do
    FILE_PATH="${WORKING_DIR}/${file}"
    DESTINATION_DIR="${WORKING_DIR}/${files[${file}]}"
    if [[ -f ${FILE_PATH} ]]; then
        echo "Founded file: ${file}"

        if [[ ! -d "${DESTINATION_DIR}" ]]; then
            echo "Created dir: ${DESTINATION_DIR}"
            mkdir -p "${DESTINATION_DIR}"
        fi
        if mv ${FILE_PATH} ${DESTINATION_DIR}; then
            echo "${FILE_PATH} moved to ${DESTINATION_DIR}"
        else
            echo "Error while move file: ${FILE_PATH} to ${DESTINATION_DIR}"
        fi
    fi
done

rm -rf "${SETUP_DIR}"
