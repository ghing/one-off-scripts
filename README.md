# One-off scripts

Little scripts to solve scritable, but rare problems.

The idea is to consolidate them in one place to help make them more discoverable and to make portions more reusable.

## Installation

```
pip install git+https://github.com/ghing/one-off-scripts.git
```

## `extract_bookmarks`: Export a folder from bookmarks HTML

Extract a single folder from bookmarks HTML.

This is useful for when you want to archive some, but not all of your bookmarks, perhaps along with files for a particular job or project.

This command operates on a bookmarks HTML file which can be exported or imported from most browsers.

### Example

```
extract_bookmarks bookmarks.html "Folder Name" > bookmarks__folder_only.html
```
