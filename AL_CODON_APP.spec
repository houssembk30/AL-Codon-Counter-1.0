# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['interface_AL_Counter.py'],
    pathex=['AL-Codon-Counter-1.0'],
    binaries=[],
    datas=[('JPG_PNG IMAGES', 'JPG_PNG IMAGES'),
        ('features', 'features')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AL CODON Version 1.0',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='JPG_PNG IMAGES\logo_ICON.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AL CODON Version 1.0 '
)
