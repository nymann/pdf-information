import pytest

from pdf_information import Encrypted
from pdf_information import PDFInfo
from tests.data import clean
from tests.data import owner_encrypted

test_cases = [
    (
        clean,
        PDFInfo(
            user_properties=False,
            suspects=False,
            java_script=False,
            optimized=False,
            page_rot=0,
            pdf_version="1.5",
            title=None,
            subject=None,
            keywords=None,
            author=None,
            creator="LaTeX via pandoc",
            producer="pdfTeX-1.40.24",
            creation_date="Sat Aug 27 21:28:45 2022 CEST",
            mod_date="Sat Aug 27 21:28:45 2022 CEST",
            custom_metadata=True,
            metadata_stream=False,
            tagged=False,
            form="none",
            pages=1,
            encrypted=None,
            page_size="612 x 792 pts (letter)",
            file_size="53029 bytes",
        ),
    ),
    (
        owner_encrypted,
        PDFInfo(
            user_properties=False,
            suspects=False,
            java_script=False,
            optimized=False,
            page_rot=0,
            pdf_version="1.5",
            title=None,
            subject=None,
            keywords=None,
            author=None,
            creator="LaTeX via pandoc",
            producer="pdfTeX-1.40.24",
            creation_date="Sat Aug 27 21:28:45 2022 CEST",
            mod_date="Sat Aug 27 21:28:45 2022 CEST",
            custom_metadata=True,
            metadata_stream=False,
            tagged=False,
            form="none",
            pages=1,
            encrypted=Encrypted(
                print=True,
                copy=True,
                change=True,
                add_notes=True,
                algorithm="RC4",
            ),
            page_size="612 x 792 pts (letter)",
            file_size="53428 bytes",
        ),
    ),
]


@pytest.mark.parametrize("cmd_output,expected", test_cases)
def test_pdf_info(cmd_output: bytes, expected: PDFInfo):
    assert expected == PDFInfo.from_cmd_output(cmd_output=cmd_output)
