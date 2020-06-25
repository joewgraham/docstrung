import os
import shutil
from docstrung import get
from datetime import datetime

from . import get



def archive_package(package_name, archive_dir='auto', overwrite=False):
    """
    Archives the package directory.
    """

    print()
    print('docstrung.archive.archive_package')
    print('---------------------------------')

    date = datetime.today().strftime('%Y%m%d')

    package_dir = get.get_package_location(package_name)

    if archive_dir == 'auto':
        archive_dir = os.path.join(os.path.dirname(package_dir), package_name + '_' + date)
    elif archive_dir == 'docstrung':
        archive_dir = os.path.join(os.getcwd(), package_name + '_docstrung')

    file_index = 0
    while os.path.isdir(archive_dir):
        if overwrite:
            shutil.rmtree(archive_dir)
            print('Overwriting existing dir:', archive_dir)
        else:
            file_index += 1
            archive_dir += '_' + str(file_index)
    
    if not os.path.isdir(archive_dir):
        shutil.copytree(package_dir, archive_dir)
        print('Copied:', package_dir)
        print('    To:', archive_dir)
    else:
        print('Warning: Not overwriting existing dir:', archive_dir)

    print('---------------------------------')
    print()

    return archive_dir, package_dir



def restore_original(archive_dir, package_dir=None):
    """Deletes the current package directory and replaces it with an archived copy.
    """

    print()
    print('docstrung.archive.restore_original')
    print('----------------------------------')

    if os.path.isdir('docstrung_temp'):
        shutil.rmtree('docstrung_temp')

    print('Copying archive from:', archive_dir)
    shutil.copytree(archive_dir, 'docstrung_temp')
    
    #print('Removing package directory')
    if package_dir is None:
        
        package_parent, archive_name = os.path.split(archive_dir)
        package_name = os.path.split(os.path.dirname(archive_dir))[-1]
        package_dir = os.path.join(package_parent, package_name)

    else:
        package_dir = get.get_package_location(package_name)
        
    shutil.rmtree(package_dir)
    
    print('Restoring archive to:', package_dir)
    shutil.copytree('docstrung_temp', package_dir)
    shutil.rmtree('docstrung_temp')

    print('----------------------------------')
    print()


