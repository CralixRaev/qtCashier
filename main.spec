# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

a = Analysis(['main.py', 'resources_rc.py'],
             pathex=[],
             binaries=[],
             datas=[('app_modules', 'app_modules'), ('config.json', '.'), ('plugins', 'plugins'),
                    ('db_new.sqlite', '.'), ('ui', 'ui')],
             hiddenimports=['importlib', 'dataclasses', 'sqlite3', 'PIL.Image',
                            'importlib.resources', 'docxtpl'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='qtcashier',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None, icon='./ui/icons/window-icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='qtcashier',)
