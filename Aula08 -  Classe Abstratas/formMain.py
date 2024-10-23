from Form import Form
from FormCarro import FormCarro
from FormMoto import FormMoto

import sys
from PyQt5.QtWidgets import QApplication

app = QApplication( sys.argv )

telaCarro = FormCarro()
telaCarro.show()

telaMoto = FormMoto()
telaMoto.show()

sys.exit(app.exec_())