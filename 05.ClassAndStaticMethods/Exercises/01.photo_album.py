class PhotoAlbum:
    _max_photos_on_page = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        num_of_pages = photos_count // cls._max_photos_on_page
        if photos_count % cls._max_photos_on_page:
            num_of_pages += 1
        return cls(num_of_pages)

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            filled_slots = len(self.photos[page])
            if filled_slots < PhotoAlbum._max_photos_on_page:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {filled_slots + 1}"
        return "No more free slots"

    def display(self):
        return "\n".join(self.generate_album())

    def generate_album(self):
        result = ["-----------"]
        for page in self.photos:
            tmp = ["[]"] * len(page)
            result.append(" ".join(tmp))
            result.append("-----------")
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())