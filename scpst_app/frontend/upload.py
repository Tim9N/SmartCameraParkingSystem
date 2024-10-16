import bucketAPI


image_path1 = "./static/images/Cars1.png"
image_path2 = "./static/images/Cars2.png"
image_path3 = "./static/images/Cars3.png"

destination_path = "./downloads/Cars3.png"

# Download Image 3
bucketAPI.download_from_bucket("Cars3.png", destination_path)

# bucketAPI.upload_to_bucket(image_path1, "Cars1.png")
# bucketAPI.list_bucket()

# bucketAPI.upload_to_bucket(image_path2, "Cars2.png")
# bucketAPI.list_bucket()

# bucketAPI.upload_to_bucket(image_path3, "Cars3.png")
# bucketAPI.list_bucket()

# bucketAPI.download_from_bucket("Cars1.png")

# bucketAPI.delete_from_bucket("Cars2.png")
# bucketAPI.list_bucket()