# -*- mode: python -*-
a = Analysis(['app.py'],
             hiddenimports=None,
             hookspath=['pkg/hooks'],
             runtime_hooks=None,
             excludes=['PyQt4'])
for d in a.datas:
  if 'pyconfig' in d[0]:
    a.datas.remove(d)
    break
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [('res/logo.png', 'smartva/res/logo.png', 'DATA')],
          [('res/favicon.ico', 'smartva/res/favicon.ico', 'DATA')],
          [('res/about.html', 'smartva/res/about.html', 'DATA')],
          [('res/documentation.html', 'smartva/res/documentation.html', 'DATA')],
          [('res/documentation.fld/filelist.xml', 'smartva/res/documentation.fld/filelist.xml','DATA')],
          [('res/documentation.fld/colorschememapping.xml', 'smartva/res/documentation.fld/colorschememapping.xml','DATA')],
          [('res/documentation.fld/themedata.thmx', 'smartva/res/documentation.fld/themedata.thmx','DATA')],
          [('res/documentation.fld/item0001.xml', 'smartva/res/documentation.fld/item0001.xml','DATA')],
          [('res/documentation.fld/props002.xml', 'smartva/res/documentation.fld/props002.xml','DATA')],
          [('res/documentation.fld/image001.png', 'smartva/res/documentation.fld/image001.png', 'DATA')],
          [('res/documentation.fld/image002.png', 'smartva/res/documentation.fld/image002.png', 'DATA')],
          [('res/documentation.fld/image003.png', 'smartva/res/documentation.fld/image003.png', 'DATA')],
          [('res/documentation.fld/image004.png', 'smartva/res/documentation.fld/image004.png', 'DATA')],
          [('res/documentation.fld/image005.png', 'smartva/res/documentation.fld/image005.png', 'DATA')],
          [('res/documentation.fld/image006.png', 'smartva/res/documentation.fld/image006.png', 'DATA')],
          [('res/documentation.fld/image007.png', 'smartva/res/documentation.fld/image007.png', 'DATA')],
          [('res/documentation.fld/image008.png', 'smartva/res/documentation.fld/image008.png', 'DATA')],
          [('res/documentation.fld/image009.png', 'smartva/res/documentation.fld/image009.png', 'DATA')],
          [('res/documentation.fld/image010.png', 'smartva/res/documentation.fld/image010.png', 'DATA')],
          [('res/documentation.fld/image011.png', 'smartva/res/documentation.fld/image011.png', 'DATA')],
          [('res/documentation.fld/image012.png', 'smartva/res/documentation.fld/image012.png', 'DATA')],
          [('res/documentation.fld/image013.png', 'smartva/res/documentation.fld/image013.png', 'DATA')],
          [('res/documentation.fld/image014.png', 'smartva/res/documentation.fld/image014.png', 'DATA')],
          [('res/documentation.fld/image015.png', 'smartva/res/documentation.fld/image015.png', 'DATA')],
          [('res/documentation.fld/image016.png', 'smartva/res/documentation.fld/image016.png', 'DATA')],
          [('res/SmartVA Analyze Output Interpretation Sheet.docx', 'smartva/res/SmartVA Analyze Output Interpretation Sheet.docx', 'DATA')],
          [('data/tariffs-adult.csv', 'smartva/data/tariffs-adult.csv', 'DATA')],
          [('data/tariffs-child.csv', 'smartva/data/tariffs-child.csv', 'DATA')],
          [('data/tariffs-neonate.csv', 'smartva/data/tariffs-neonate.csv', 'DATA')],
          [('data/validated-adult.csv', 'smartva/data/validated-adult.csv', 'DATA')],
          [('data/validated-child.csv', 'smartva/data/validated-child.csv', 'DATA')],
          [('data/validated-neonate.csv', 'smartva/data/validated-neonate.csv', 'DATA')],
          [('data/chinese.json', 'smartva/data/chinese.json', 'DATA')],
          [('data/spanish.json', 'smartva/data/spanish.json', 'DATA')],
          [('data/adult_undetermined_weights.csv', 'smartva/data/adult_undetermined_weights.csv', 'DATA')],
          [('data/child_undetermined_weights.csv', 'smartva/data/child_undetermined_weights.csv', 'DATA')],
          [('data/neonate_undetermined_weights.csv', 'smartva/data/neonate_undetermined_weights.csv', 'DATA')],
          name='SmartVA-Analyze.exe',
          debug=False,
          strip=None,
          upx=False,
          console=False,
          icon='pkg/icon.ico')
