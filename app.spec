
import os
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT

# Define paths for Tesseract-OCR and FFmpeg
tesseract_path = "Tesseract-OCR"
ffmpeg_path = "ffmpeg-v1/bin/ffmpeg.exe"
tesseract_data_path = os.path.join(tesseract_path, "tessdata")  # Include Tesseract data files if needed

# Collect necessary data files and directories
datas = [
    (tesseract_path, "Tesseract-OCR"),  # Ensure this directory is correct
    (ffmpeg_path, "ffmpeg-v1/bin/ffmpeg.exe"),  # Ensure FFmpeg path is correct
    (tesseract_data_path, "Tesseract-OCR/tessdata")  # Ensure this directory is correct
]

a = Analysis(
    ['app.py'],
    pathex=[os.path.abspath('.')],  # Ensure it includes the working directory
    binaries=[],
    datas=datas,  # Include Tesseract-OCR and FFmpeg
    hiddenimports=[],
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
    name='app',
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
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)
