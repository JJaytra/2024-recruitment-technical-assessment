from dataclasses import dataclass

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    result = []
    parent_files = []
    for file in files:
        if file.parent != -1:
            parent_files.append(file.parent)
    for file in files:
        if file.id not in parent_files:
            result.append(file.name)
    return result


"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:
    categories = {}
    for file in files:
        for category in file.categories:
            if category in categories:
                categories[category] += 1
            else:
                categories[category] = 1

    sorted_categories = sorted(categories.keys(), key=lambda x: (-categories[x], x))
    
    return sorted_categories[:k]


"""
Task 3
"""



def largestFileSize(files: list[File]) -> int:
    # contains files and their sizes
    file_sizes = {}
    # result dict with total size
    result = {}
    # populate dict first
    for file in files:
        file_sizes[file.id] = file.size

    def dfs_sizes(id):
        total_size = file_sizes.get(id, 0)
        for file in files:
            if file.parent == id:
                total_size += dfs_sizes(file.id)
        result[id] = total_size
        return total_size

    # iterate parent files
    for file in files:
        if file.parent == -1:
            dfs_sizes(file.id)

    # get max
    largest = max(result.values())

    return largest


if __name__ == '__main__':
    testFiles = [
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(3, "Folder", ["Folder"], -1, 0),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
    ]


    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]

    assert kLargestCategories(testFiles, 3) == [
        "Documents", "Folder", "Media"
    ]

    assert largestFileSize(testFiles) == 20992

