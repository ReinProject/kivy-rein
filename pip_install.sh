cat requirements.txt | while read PACKAGE; do pip install "$PACKAGE"; done
