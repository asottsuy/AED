from Form import Form
from FormCarro import FormCarro

import sys
from PyQt5.QtWidgets import QApplication

app = QApplication( sys.argv )

telaCarro = FormCarro()
telaCarro.show()

sys.exit(app.exec_())