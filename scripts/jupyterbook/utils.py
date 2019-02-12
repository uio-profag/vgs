"""Utility functions for Jupyter Book.

This is a mini-module to make testing easier."""

import string
import nbformat as nbf
import os

ALLOWED_CHARACTERS = string.ascii_letters + '-_/.' + string.digits


def _split_yaml(lines):
    yaml0 = None
    for ii, iline in enumerate(lines):
        iline = iline.strip()
        if yaml0 is None:
            if iline == '---':
                yaml0 = ii
            elif iline:
                break
        elif iline == '---':
            return lines[yaml0 + 1:ii], lines[ii + 1:]
    return [], lines


def _check_url_page(url_page, content_folder_name):
    """Check that the page URL matches certain conditions."""
    if not all(ii in ALLOWED_CHARACTERS for ii in url_page):
        raise ValueError("Found unsupported character in filename: {}".format(url_page))
    if '.' in os.path.splitext(url_page)[-1]:
        raise _error("A toc.yml entry links to a file directly. You should strip the file suffix.\n"
                        "Please change {} to {}".format(url_page, os.path.splitext(url_page)[0]))
    if any(url_page.startswith(ii) for ii in [content_folder_name, os.sep+content_folder_name]):
        raise ValueError("It looks like you have a page URL that starts with your content folder's name."
                            "page URLs should be *relative* to the content folder. Here is the page URL: {}".format(url_page))
    
def _prepare_toc(toc):
    """Prepare the TOC for processing."""
    # Drop toc items w/o links
    toc = [ii for ii in toc if ii.get('url', None) is not None]
    # Un-nest the TOC so it's a flat list
    new_toc = []
    for ii in toc:
        sections = ii.pop('sections', None)
        new_toc.append(ii)
        if sections is None:
            continue
        for jj in sections:
            subsections = jj.pop('subsections', None)
            new_toc.append(jj)
            if subsections is None:
                continue
            for kk in subsections:
                new_toc.append(kk)
    return new_toc


def _prepare_url(url):
    """Prep the formatting for a url."""
    # Strip suffixes and prefixes of the URL
    if not url.startswith('/'):
        url = '/' + url

    # Standardize the quotes character
    url = url.replace('"', "'")
    return url


def _clean_notebook_cells(path_ntbk):
    """Clean up cell text of an nbformat NotebookNode."""
    ntbk = nbf.read(path_ntbk, nbf.NO_CONVERT)
    # Remove '#' from the end of markdown headers
    for cell in ntbk.cells:
        if cell.cell_type == "markdown":
            cell_lines = cell.source.split('\n')
            for ii, line in enumerate(cell_lines):
                if line.startswith('#'):
                    cell_lines[ii] = line.rstrip('#').rstrip()
            cell.source = '\n'.join(cell_lines)
    nbf.write(ntbk, path_ntbk)


def _error(msg):
    msg = '\n\n==========\n{}\n==========\n'.format(msg)
    raise ValueError(msg)

