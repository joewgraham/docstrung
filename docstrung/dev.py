"""
docstrung dev
"""

import docstrung

exclude=['netpyne.conversion.neuromlFormat.NetPyNEBuilder', 'netpyne.conversion.neuromlFormat.importNeuroML2']

docstrung.archive.restore_original('/Users/graham/Applications/python_modules/netpyne/netpyne_predocstrung')

netpyne_docstrung = np = docstrung.docstrung.Docstrung('netpyne', exclude=exclude)


for item in np.all_docstrungs:
    print()
    print()
    print()
    print()
    print('=====================================================')
    print(item.report)
    print('=====================================================')
    print()
    print()
    print()
    print()

import netpyne