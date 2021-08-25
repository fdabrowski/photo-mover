from photo_service import PhotoService

ids = ['someId']
photos_path = '/Users/filipdabrowski/Documents/playground/photo-mover'
destination_path = '/Users/filipdabrowski/Documents/playground/copied-files'

photo_service = PhotoService(photos_path, destination_path, ids);

photo_service.move_photos()