from acdh_tei_pyutils.tei import TeiReader

def increment(numbers: list, index = None):
    if index is None:
        index = len(numbers) -1
    current = numbers[index]
    if current != 9:
        numbers[index] = current + 1
        return numbers
    else:
        numbers[index] = 0
        index -= 1
        return increment(numbers, index)

addon_doc_path = "frameworks/b-vg-addon.xml"
addon_doc = TeiReader(addon_doc_path)
version_element = addon_doc.tree.xpath(
    "//*[local-name()='version']"
)[0]
version_numbers = [
    int(n) for n in version_element.text.strip().split(".")
]
new_version_numbers = [
    str(i) for i in increment(version_numbers)
]
new_version_number  = ".".join(new_version_numbers)
print(f"old version: {version_element.text}")
print(f"new version: {new_version_number}")
version_element.text = new_version_number
addon_doc.tree_to_file(addon_doc_path)