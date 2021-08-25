from typing import List
from os import listdir, replace
from os.path import isfile, join
from pathlib import Path

class PhotoService():
    def __init__(self, photos_path: str, destination_path: str, ids: List[str]) -> None:
        self._photos_path = photos_path
        self._destination_path = destination_path
        self._ids = ids
        self._included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']

    def move_photos(self) -> None:
        photos = self._get_all_photos()
        photos_to_be_moved = self._get_photos_to_move(photos)
        self._move_to_destination(photos_to_be_moved)

    def _get_all_photos(self) -> List[str]:
        photos = [fn for fn in listdir(self._photos_path)
                    if any(fn.endswith(ext) for ext in self._included_extensions)]
        return photos

    def _get_photos_to_move(self, photos: List[str]) -> List[str]:
        photos_to_be_moved = []
        for id in self._ids:
            matching = [s for s in photos if id in s]
            photos_to_be_moved.extend(matching)
        return photos_to_be_moved


    def _move_to_destination(self, photos: List[str]) -> None:
        Path(self._destination_path).mkdir(parents=True, exist_ok=True)
        for photo in photos:
            replace(self._photos_path + '/' + photo, self._destination_path + '/' + photo)

