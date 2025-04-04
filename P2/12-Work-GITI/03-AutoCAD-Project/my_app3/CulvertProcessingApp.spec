# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['CulvertProcessingApp.py'],
    pathex=[],
    binaries=[('C:\\Python Interpreters\\in_main\\Lib\\site-packages\\pyautocad', 'pyautocad')],
    datas=[('data/*.csv', 'data')],
    hiddenimports=['pyautocad', 'comtypes', 'comtypes.stream', 'pandas', 'numpy', 'math', 'tqdm', 'pythoncom', 'time', 'os'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CulvertProcessingApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assests\\logo-color.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CulvertProcessingApp',
)
