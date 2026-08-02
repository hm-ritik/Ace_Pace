def get_images(files):
    return [file for file in files if file["category"] == "photo"]


def get_documents(files):
    return [file for file in files if file["category"] == "document"]