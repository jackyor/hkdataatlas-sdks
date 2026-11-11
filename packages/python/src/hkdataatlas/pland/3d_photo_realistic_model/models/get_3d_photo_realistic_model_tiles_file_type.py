from typing import Literal

Get3DPhotoRealisticModelTilesFileType = Literal["CESIUM", "OBJ", "OSGB"]

GET_3D_PHOTO_REALISTIC_MODEL_TILES_FILE_TYPE_VALUES: set[
    Get3DPhotoRealisticModelTilesFileType
] = {
    "CESIUM",
    "OBJ",
    "OSGB",
}


def check_get_3d_photo_realistic_model_tiles_file_type(
    value: str,
) -> Get3DPhotoRealisticModelTilesFileType:
    if value in GET_3D_PHOTO_REALISTIC_MODEL_TILES_FILE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_3D_PHOTO_REALISTIC_MODEL_TILES_FILE_TYPE_VALUES!r}"
    )
