"""Maintain the legacy eula.txt URL as a notice, never a custom ASC agreement.

Select Apple's Standard EULA in App Store Connect. Do not paste this notice
or the supplementary terms page into its custom-EULA field.
"""
from pathlib import Path

NOTICE = """HEXIS — END USER LICENCE
Updated 14 September 2026

Hexis uses Apple's Standard End User License Agreement:
https://www.apple.com/legal/internet-services/itunes/dev/stdeula/

Supplementary Terms of Use and subscription information:
https://tally484.github.io/tally-legal/terms.html

Privacy Policy:
https://tally484.github.io/tally-legal/privacy.html

This notice is not a custom EULA and does not replace or amend Apple's
Standard EULA. Martin Elenjikkal remains the application provider.
Support: martyelenjikkal@gmail.com
"""

if __name__ == "__main__":
    Path(__file__).with_name("eula.txt").write_text(NOTICE, encoding="utf-8")
    print("Updated standard-EULA notice; do not use the ASC custom-EULA field.")
