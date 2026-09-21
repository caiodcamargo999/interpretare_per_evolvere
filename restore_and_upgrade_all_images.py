import os, shutil, glob
from PIL import Image

src_dir = 'assets interpretar para evoluir/images'
dst_dir = 'images'

# 1. Restore all original photographic and graphic assets
# (e.g. 76ec044f smiling mother, ef51b634 boy thumbs up, mFPujI8456037 fanned sheets, bca575f3 platform, all bonus cards, all testimonials)
preserved_files = [
    'dppDQD5163414',
    'WReKdb5163414',
    'd597bf16-8a79-4749-bdf1-bbe4b3dea8ea-misc-src'
]

for src_path in glob.glob(f'{src_dir}/*'):
    fname = os.path.basename(src_path)
    # Check if it's one of the preserved custom hero/stack files
    is_preserved = any(fname.startswith(p) for p in preserved_files)
    if not is_preserved:
        dst_path = os.path.join(dst_dir, fname)
        shutil.copy2(src_path, dst_path)
        print(f'Restored original high-res asset: {fname}')

print('All authentic high-res assets restored successfully!')
