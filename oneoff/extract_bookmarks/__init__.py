"""Extract a folder of bookmarks from an HTML file exported from a browser."""

from bs4 import BeautifulSoup, NavigableString
import fire


def extract_bookmarks(bookmarks_html, folder_path):
    """
    Extract a folder of bookmarks from an HTML file exported from a browser.

    """
    folder_paths = folder_path.split("/")
    with open(bookmarks_html) as bookmarks_f:
        soup = BeautifulSoup(bookmarks_f, "html.parser")

    # Bookmark folders correspond to <dl> elements in the bookmarks HTML
    folder_el = soup.find("dl")

    # Find the header element matching the specified folder name.
    bookmark = None
    for folder in folder_paths:
        for bookmark in folder_el.find_all("dt"):
            heading = bookmark.find("h3", text=folder)
            if heading is not None:
                break

        folder_el = bookmark.find("dl")

    # Find the next element that's a tag. This should be the
    # <dl> element for the bookmark folder.
    sibling = None
    for sibling in heading.next_siblings:
        if not isinstance(sibling, NavigableString):
            break

    folder_list = sibling

    output_html = (
        "<!DOCTYPE NETSCAPE-Bookmark-file-1>\n"
        "<!-- This is an automatically generated file.\n"
        "     It will be read and overwritten.\n"
        "     DO NOT EDIT! -->\n"
        '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n'
        "<TITLE>Bookmarks</TITLE>\n"
        "<H1>Bookmarks</H1>\n"
        f"<DT>{str(heading)}"
        f"{str(folder_list)}"
    )
    print(output_html)


def main():
    """Entry point for command"""
    fire.Fire(extract_bookmarks)
